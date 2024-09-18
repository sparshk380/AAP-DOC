import requests

# Constants
API_TOKEN = ''
DROPLET_NAME = 'ansible-automation-platform-tf'
INVENTORY_FILE_PATH = '/root/ansible-automation-platform-setup-bundle-2.4-1-x86_64/inventory'
HOSTS_FILE_PATH = '/etc/hosts'

def get_droplet_id(api_token, droplet_name):
    url = 'https://api.digitalocean.com/v2/droplets'
    headers = {'Authorization': f'Bearer {api_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        droplets = data['droplets']
        for droplet in droplets:
            if droplet['name'] == droplet_name:
                return droplet['id']
        print(f'Droplet with name {droplet_name} not found.')
        return None
    else:
        print(f'Error fetching droplets info: {response.status_code} - {response.text}')
        return None

def get_droplet_ip(api_token, droplet_id):
    url = f'https://api.digitalocean.com/v2/droplets/{droplet_id}'
    headers = {'Authorization': f'Bearer {api_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        ip_address = data['droplet']['networks']['v4'][0]['ip_address']
        return ip_address
    else:
        print(f'Error fetching droplet info: {response.status_code} - {response.text}')
        return None

def update_inventory_file(file_path, new_ip):
    # Read the inventory file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    line_replaced = False

    # Go through each line and replace the desired one
    for line in lines:
        if line.startswith('automationplatform.zapto.org'):
            # Replace the line with the droplet's IP and ansible_collection
            new_lines.append(f'{new_ip} ansible_collection=local\n')
            line_replaced = True
        else:
            new_lines.append(line)

    if not line_replaced:
        print(f'Error: "automationplatform.zapto.org ansible_collection=local" not found in {file_path}')
    else:
        # Write the updated lines back to the inventory file
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

        print(f'Updated "automationplatform.zapto.org" with droplet IP {new_ip} in {file_path}.')

def update_hosts_file(new_ip, hosts_file_path):
    search_line = "127.0.0.1 localhost4.localdomain4 localhost4"

    with open(hosts_file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    line_found = False

    for line in lines:
        new_lines.append(line)
        if line.strip() == search_line:
            # Insert the new droplet IP directly after the specified line
            new_lines.append(f'{new_ip}\n')
            line_found = True

    if not line_found:
        print(f'Error: "{search_line}" not found in {hosts_file_path}')

    # Write the changes back to the file
    with open(hosts_file_path, 'w') as file:
        file.writelines(new_lines)

    if line_found:
        print(f'Added public IP {new_ip} to {hosts_file_path}.')

def main():
    droplet_id = get_droplet_id(API_TOKEN, DROPLET_NAME)
    if droplet_id:
        ip_address = get_droplet_ip(API_TOKEN, droplet_id)
        if ip_address:
            update_inventory_file(INVENTORY_FILE_PATH, ip_address)
            print('Inventory file updated successfully.')
            update_hosts_file(ip_address, HOSTS_FILE_PATH)
            print('Hosts file updated successfully.')

if __name__ == '__main__':
    main()