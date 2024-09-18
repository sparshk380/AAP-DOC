#!/bin/bash

# Define the key file path
KEY_FILE="$HOME/.ssh/id_rsa"

# Generate the SSH key pair
ssh-keygen -t rsa -b 4096 -f "$KEY_FILE" -N ""

# Ensure the .ssh directory and authorized_keys file exist
mkdir -p "$HOME/.ssh"
touch "$HOME/.ssh/authorized_keys"

# Append the public key to the authorized_keys file
cat "$KEY_FILE.pub" >> "$HOME/.ssh/authorized_keys"

# Append the public key to the known_hosts file
# Note: known_hosts is usually for storing host keys, not user keys. This is unconventional.
# You may want to use it for a different purpose or ensure this fits your use case.
cat "$KEY_FILE.pub" >> "$HOME/.ssh/known_hosts"

# Set proper permissions
chmod 700 "$HOME/.ssh"
chmod 600 "$HOME/.ssh/authorized_keys"
chmod 600 "$HOME/.ssh/known_hosts"  # Ensure known_hosts has the correct permissions

echo "SSH key generated, added to authorized_keys, and appended to known_hosts."
