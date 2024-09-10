# Red Hat Ansible Automation Platform (AAP) Documentation

# Architecture of Ansible Automation Platform:


The Red Hat Ansible Automation Platform reference architecture provides an example setup of a standard deployment of Ansible Automation Platform using automation mesh on Red Hat Enterprise Linux. The deployment shown takes advantage of the following key components to provide a simple, secure and flexible method of handling your automation workloads, a central location for content collections, and automated resolution of IT requests.

  -  Automation controller: 
Provides the control plane for automation through its UI, Restful API, RBAC workflows and CI/CD integrations.

  - Automation mesh:
Is an overlay network that provides the ability to ease the distribution of work across a large and dispersed collection of workers through nodes that establish peer-to-peer connections with each other using existing networks.

  - Private automation hub:
Provides automation developers the ability to collaborate and publish their own automation content and streamline delivery of Ansible code within their organization.

The architecture for this example consists of the following:

  * A two node automation controller cluster
  * An optional hop node to connect automation controller to execution nodes
  * A two node automation hub cluster
  * A single PostgreSQL database connected to the automation controller and automation hub
  * Two execution nodes per automation controller cluster

  ![Screenshots](<AAP ARCH DIAGRAM.png>)


# Architecture of Event Driven Ansible (EDA):


Event-Driven Ansible processes events 
containing discrete intelligence about 
conditions in your IT environment, 
determines the appropriate response 
to the event, then executes automated 
actions to address or remediate the 
event. These 3 components are the 
building blocks of Event-Driven Ansible: 
event sources, rules, and actions.

There are three major building blocks in the Event-Driven Ansible model, sources, rules and actions that play key roles in completing the workflow described above:

* Sources - They are third party vendor tools that provide the events. They define and identify where events occur, then pass them to Event-Driven Ansible.  Current source support includes Prometheus, Sensu, Red Hat solutions, webhooks and Kafka, as well as custom "bring your own" sources.
* Rules- They document your desired handling of the event via Ansible Rulebooks. They use familiar YAML-like structures and follow an "if this then that" model.  Ansible Rulebooks may call Ansible Playbooks or have direct module execution functions.
* Actions are the result of executing the Ansible Rulebook's instructions when the event occurs.

![Screenshots](<EDA ARCH.png>)



# Inventory Section:

Inventory Section allows you to create inventory for the nodes you want your ansible playbooks to run on.
Now you can either create a simple static inventory, a smart inventory or a constructed inventory.

![Screenshots](<Inventory - 1.png>)

## Inventory:

An inventory is a collection of hosts managed by the controller.

![Screenshots](<Inventory - 2.png>)

1. Name: Enter a name appropriate for this inventory.

2. Description: Enter an arbitrary description as appropriate (optional).

3. Organization: Required. Choose among the available organizations.

4. Instance Groups: Click the search button to open a separate window. Choose the instance group(s) for this inventory to run on. If the list is extensive, use the search to narrow the options. You may select multiple instance groups and sort them in the order you want them ran.

5. Labels - Optional labels that describe this inventory, such as 'dev' or 'test'. Labels can be used to group and filter inventories and completed jobs.

6. Options - If enabled, the inventory will prevent adding any organization instance groups to the list of preferred instances groups to run associated job templates on. Note: If this setting is enabled and you provided an empty list, the global instance groups will be applied.

7. Variables: Variable definitions and values to be applied to all hosts in this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

## Smart Inventory:

A Smart Inventory is a collection of hosts defined by a stored search that can be viewed like a standard inventory and made to be easily used with job runs. Organization administrators have admin permission to inventories in their organization and can create a Smart Inventories. A Smart Inventory is identified by KIND=smart. You can define a Smart Inventory using the same method being used with Search. InventorySource is directly associated with an Inventory.

![Screenshots](<Inventory - 3.png>)

1. Smart host filter - Smart host filters in Ansible Automation Platform allow you to dynamically create subsets of your inventory based on specific criteria, enabling targeted automation and simplified management of complex infrastructures.

2. Instance Groups - Instance groups in Ansible Automation Platform, when creating a smart inventory, determine which execution nodes will run jobs using that inventory, allowing for targeted job execution and load balancing across specific sets of AAP nodes.

3. Variables - Variables Variable definitions and values to be applied to all hosts in this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

## Constructed Inventory

As a platform user, this feature allows creation of a new inventory (called a constructed inventory) from a list of input inventories. The constructed inventory contains copies of hosts and groups in its input inventories, allowing jobs to target groups of servers across multiple inventories. Groups and hostvars can be added to the inventory content, and hosts can be filtered to limit the size of the constructed inventory. Constructed inventories address some limitations of the Smart Inventories host filtering model and makes use of the Ansible core constructed inventory model.

The key factors that distinguish a constructed inventory from a Smart Inventory are:

  * the normal Ansible hostvars namespace is available

  * they provide groups

Smart inventories take a host_filter as input and create a resultant inventory with hosts from inventories in its organization. Constructed inventories take source_vars and limit as inputs and transform its input_inventories into a new inventory, complete with groups. Groups (existing or constructed) can then be referenced in the limit field to reduce the number of hosts produced.

![Screenshots](<Inventory - 4.png>)

1. Input Inventories - This is where you will list existing inventories that the constructed inventory will get inventory content (hosts, groups, etc.) from

2. Cached timeout (seconds): (Only applicable to constructed inventories) Optionally set the length of time you want the cache plugin data to timeout.

3. Verbosity -  Control the level of output Ansible produces as the playbook executes related to inventory sources associated with constructed inventories. Choose the verbosity from Normal to various Verbose or Debug settings. This only appears in the “details” report view. Verbose logging includes the output of all commands. Debug logging is exceedingly verbose and includes information on SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.

4. Limit - Restricts the number of returned hosts for the inventory source associated with the constructed inventory. You can paste a group name into the limit field to only include hosts in that group. 

5. Source Vars:

    * Source vars for constructed inventories creates groups, specifically under the groups key of the data. It accepts Jinja2 template syntax, renders it for every host, makes a True/False evaluation, and includes the host in the group (from key of the entry) if the result is True. This is particularly useful because you can paste that group name into the limit field to only include hosts in that group. 
    Example:  If your source inventory has a variable called "os_type" for each host, you could use this to create new groups in your constructed inventory: 

    ```
      plugin: constructed
      strict: False
      groups:
        windows: os_type == 'Windows'
        linux: os_type == 'Linux'
    ```
    * This would create two new groups, "windows" and "linux", based on the value of the "os_type" source var.
    The power of constructed inventories lies in their ability to use these source vars to create more flexible and dynamic inventory structures without modifying the original inventory source.

### Projects Section:

- A Project is a logical collection of Ansible playbooks.

- You can manage playbooks and playbook directories by either placing them manually under the Project Base Path on your server, or by placing your playbooks into a source code management (SCM) system supported by automation controller, including Git, Subversion, and Red Hat Insights. To create a Red Hat Insights project, refer to Setting up Insights Remediations.

![Screenshots](<Project Section 1.png>)

1. Name: Name of the project as per your requirements

2. Description - (Optional) Details about what you want to do with this project.

3. Organization -  A project must have at least one organization. Pick one organization now to create the project, and then after the project is created you can add additional organizations.

4. Execution Environment (optional) - Enter the name of the execution environment or search from a list of existing ones to run this project

5. Source Control Type - Select from the drop-down menu list an SCM type associated with this project. The options in the subsequent section become available depend on the type you choose.

   - Manual - Create one or more directories to store playbooks under the Project Base Path (for example, /var/lib/awx/projects/).

     * Create or copy playbook files into the playbook directory.

     * Ensure that the playbook directory and files are owned by the same UNIX user and group that the automation controller service runs as.

     * Ensure the permissions are appropriate for the playbook directories and files

   - Git or Subversion - Select the appropriate option (Git) from the SCM Type drop-down menu list.

     ![Screenshot](<Project Section 2.png>)

     * Source Control URL - Add the SCM git URL from GitHub or GitLab

     * Source Control Branch/Tag/Commit - Optionally enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout. Some commit hashes and refs may not be available unless you also provide a custom refspec in the next field. If left blank, the default is HEAD which is the last checked out Branch/Tag/Commit for this project.

     * Source Control Refspec - SCM Refspec - This field is an option specific to git source control and only advanced users familiar and comfortable with git should specify which references to download from the remote repository.

     * Source Control Credential - If authentication is required, select the appropriate source control credential

     * Options - In the SCM Update Options, optionally select the launch behavior, if applicable.

       * Clean - Removes any local modifications prior to performing an update.

       * Delete - Deletes the local repository in its entirety prior to performing an update. Depending on the size of the repository this may significantly increase the amount of time required to complete an update.

       * Track submodules - Tracks the latest commit.

       * Update Revision on Launch - Updates the revision of the project to the current revision in the remote source control, as well as cache the roles directory from Galaxy or Collections. Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. Also, to avoid job overflows if jobs are spawned faster than the project can sync, selecting this allows you to configure a Cache Timeout to cache prior project syncs for a certain number of seconds.

       * Allow Branch Override - Allows a job template or an inventory source that uses this project to launch with a specified SCM branch or revision other than that of the project’s.

    - Red Hat Insights - 
      ![Screenshot](<Workflow job template 4.png>)

      * Insights Credentials - Red Hat Insights requires a credential for authentication. Select from the Credential field the appropriate credential for use with Insights.

      * Options -In the SCM Update Options, optionally select the launch behavior, if applicable.
          * Clean - Removes any local modifications prior to performing an update.

          * Delete - Deletes the local repository in its entirety prior to performing an update. Depending on the size of the repository this may significantly increase the amount of time required to complete an update.

          * Update Revision on Launch - Updates the revision of the project to the current revision in the remote source control, as well as cache the roles directory from Galaxy or Collections. Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. Also, to avoid job overflows if jobs are spawned faster than the project can sync, selecting this allows you to configure a Cache Timeout to cache prior project syncs for a certain number of seconds.
    
    - Remote Archive - Playbooks using a remote archive allow projects to be provided based on a build process that produces a versioned artifact, or release, containing all the requirements for that project in a single archive.
      ![Screenshot](<Workflow job template 5.png>)

      * SCM URL - requires a URL to a remote archive, such as a GitHub Release or a build artifact stored in Artifactory and unpacks it into the project path for use

      * SCM Credential - If authentication is required, select the appropriate SCM credential

      * Options - In the SCM Update Options, optionally select the launch behavior, if applicable.

        * Clean - Removes any local modifications prior to performing an update.
        * Delete - Deletes the local repository in its entirety prior to performing an update. Depending on the size of the repository this may significantly increase the amount of time required to complete an update.
        * Update Revision on Launch - Not recommended, as this option updates the revision of the project to the current revision in the remote source control, as well as cache the roles directory from Galaxy or Collections.
        * Allow Branch Override - Not recommended, as this option allows a job template that uses this project to launch with a specified SCM branch or revision other than that of the project’s.

6. Content Signature Validation Credential - Enable content signing to verify that the content has remained secure when a project is synced. If the content has been tampered with, the job will not run.


# Resources:

### Templates Section:

In the templates section, you can create either job template or a workflow template.

- Job Template - In Ansible Automation Platform (AAP), a job template is used to define and manage the execution of Ansible playbooks by specifying the playbook to run, the inventory to use, and any associated variables or credentials.

- Workflow Template - a workflow template is used to orchestrate and manage complex automation tasks by defining a sequence of job templates and their dependencies, allowing for the execution of multiple playbooks in a specific order and with conditional logic.

![Screenshot](<Template 1 .png>)

### Job Template:

In the Job Template Section, you can specify the following parameters as:

![Screenshot](<Job template 1.png>)

1. Name: Refers to the name of the job template you want.

2. Description: You can provide the description of the job template.

3. Job Type: With job type you can either select Run and Check as the parameters.
    * Run - Execute the playbook when launched, running Ansible tasks on the selected hosts.
    * Check -   Perform a “dry run” of the playbook and report changes that would be made without actually making them. Tasks that do not support check mode will be skipped and will not report potential changes

![Screenshot](<Job template 2.png>)

4. Inventory - Select the inventory containing the hosts you want this job to manage.

5. Project - Select the project containing the playbook you want this job to execute.

6. Execution Environment - The execution environment refers to the container image, used for execution.

7. Playbook - This field allows you to select the playbook you want to execute from the source.

8. Credentials - This field allows you to select the credentials you require for your nodes, so that AAP can run the playbook on it.

![Screenshot](<Job template 3.png>)

9. Variables - You can pass extra command line variables to the playbook. This is the -e or --extra-vars command line parameter for ansible-playbook. Provide key/value pairs using either YAML or JSON.

10. Forks - The number of parallel or simultaneous processes to use while executing the playbook. A value of zero uses the Ansible default setting, which is 5 parallel processes unless overridden in /etc/ansible/ansible.cfg.

11. Limit -  A host pattern to further constrain the list of hosts managed or affected by the playbook. Multiple patterns can be separated by colons (“:”). As with core Ansible, “a:b” means “in group a or b”, “a:b:&c” means “in a or b but must be in c”, and “a:!b” means “in a, and definitely not in b”.

12. Verbosity - Control the level of output Ansible produces as the playbook executes. Choose the verbosity from Normal to various Verbose or Debug settings. This only appears in the “details” report view. Verbose logging includes the output of all commands. Debug logging is exceedingly verbose and includes information on SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.

13. Job Slicing - Specify the number of slices you want this job template to run. Each slice will run the same tasks against a portion of the inventory. For more information about job slices, see Job Slicing.

14. Timeout - Allows you to specify the length of time (in seconds) that the job may run before it is canceled. Some caveats for setting the timeout value:
    * There is a global timeout defined in the settings which defaults to 0, indicating no timeout.

    * A negative timeout (<0) on a job template is a true “no timeout” on the job.

    * A timeout of 0 on a job template defaults the job to the global timeout (which is no timeout by default).

    * A positive timeout sets the timeout for that job template.

15.  Show Changes - Allows you to see the changes made by Ansible tasks.

16. Job Tags - If you have a large playbook, it may be useful to run only specific parts of it instead of running the entire playbook. You can do this with Ansible tags. Using tags to execute or skip selected tasks is a two-step process:

    * Add tags to your tasks, either individually or with tag inheritance from a block, play, role, or import.

    * Select or skip tags when you run your playbook.

17. Skip Tags: Skip tags are useful when you have a large playbook, and you want to skip specific parts of a play or task. Use commas to separate multiple tags.

18. Options - Specify options for launching this template, if necessary.
    * Privilege Escalation - If checked, you enable this playbook to run as an administrator. This is the equivalent of passing the --become option to the ansible-playbook command.

    * Provisioning Callbacks - Provisioning callbacks are a feature of Automation Controller that allow a host to initiate a playbook run against itself, rather than waiting for a user to launch a job to manage the host from the Automation Controller console

    * Enable Webhook- Turns on the ability to interface with a predefined SCM system web service that is used to launch a job template. Currently supported SCM systems are GitHub and GitLab.

  ![Screenshot](<Job template webhook.png>)
    
  If you enable webhooks, other fields display, prompting for additional information:
    Webhook Service: Select which service to listen for webhooks from

  Webhook URL: Automatically populated with the URL for the webhook service to POST requests to.

  Webhook Key: Generated shared secret to be used by the webhook service to sign payloads sent to automation controller. This must be configured in the settings on the webhook service in order for automation controller to accept webhooks from this service.

  Webhook Credential: Optionally, provide a GitHub or GitLab personal access token (PAT) as a credential to use to send status updates back to the webhook service. Before you can select it, the credential must exist. See Credential Types to create one.

* Concurrent Jobs - If checked, you are allowing jobs in the queue to run simultaneously if not dependent on one another. Check this box if you want to run job slices simultaneously. 

  * Enable Fact Storage: When checked, automation controller will store gathered facts for all hosts in an inventory related to the job running.

  * Prevent Instance Group Fallback: Check this option to allow only the instance groups listed in the Instance Groups field above to execute the job.


### Workflow Job Template:

![Screenshot](<Workflow job template 1.png>)

1. Name - Enter a name for a job

2. Description: Enter an arbitrary description as appropriate (Optional)

3. Organization: Choose the organization to be used with this template from the organizations available to the currently logged in user.

4. Inventory - Optionally choose the inventory to be used with this template from the inventories available to the currently logged in user.

5. Limit - A host pattern to further constrain the list of hosts managed or affected by the playbook. Multiple patterns can be separated by colons (:). As with core Ansible, a:b means “in group a or b”, a:b:&c means “in a or b but must be in c”, and a:!b means “in a, and definitely not in b”.

6. Source Control Branch - Select a branch for the workflow. This branch is applied to all workflow job template nodes that prompt for a branch.

7. Labels - Optional labels that describe this workflow job template, such as 'dev' or 'test'. Labels can be used to group and filter workflow job templates and completed jobs.

* Prompt on Launch - Yes. If selected, even if a default value is supplied, you will be prompted upon launch to supply additional labels if needed.

 * You will not be able to delete existing labels - clicking (x-circle) only removes the newly added labels, not existing default labels.

8. Variables - Pass extra command line variables to the playbook. This is the “-e” or “–extra-vars” command line parameter for ansible-playbook that is documented in the Ansible documentation at Passing Variables on the Command Line.

* Provide key/value pairs using either YAML or JSON. These variables have a maximum value of precedence and overrides other variables specified elsewhere. An example value might be:

```
  git_branch: production
  release_version: 1.5
```

9. Job Tags - Tags are useful when you have a large playbook, and you want to run a specific part of a play or task. Use commas to separate multiple tags

10. Skip Tags - Skip tags are useful when you have a large playbook, and you want to skip specific parts of a play or task. Use commas to separate multiple tags

11. Options - Specify options for launching this workflow job template, if necessary.

![Screenshot](<Workflow job template 2.png>)

 * Webhooks - If you enable webhooks, other fields display, prompting for additional information:
    * Webhook Service: Select which service to listen for webhooks from

    * Webhook URL: Automatically populated with the URL for the webhook service to POST requests to.

    * Webhook Credential: Optionally, provide a GitHub or GitLab personal access token (PAT) as a credential to use to send status updates back to the webhook service. Before you can select it, the credential must exist

* Enable Concurrent Jobs - Allow simultaneous runs of this workflow.



# Difference between Execution Environment and Instance Groups.

1. Execution Environment -

    * Definition -  Execution Environments are container images that package together Ansible, its dependencies, and any additional tools or libraries needed for a specific automation task.
   
    * Purpose: They provide a consistent and isolated environment for running Ansible playbooks and roles.

    * Dependency management: They encapsulate all necessary dependencies, making it easier to manage complex automation requirements.

2. Instance Groups -
   
   * Definition: Instance Groups are a way to organize and manage Ansible execution capacity within Ansible Automation Platform.

   * Purpose: They allow you to group together execution nodes (machines that run Ansible jobs) based on various criteria like location, purpose, or capabilities.

   * Scalability: Instance Groups help in scaling your automation by distributing jobs across multiple execution nodes.

     * Difference between Instance Group "Default" and "Control Plane"
       
        1. Default -
           
           * Purpose: The Default Instance Group is the primary group for running automation jobs in Ansible Automation Platform.
           * Job execution: Unless specified otherwise, all jobs will run in this group by default.
           * Scalability: It can contain multiple execution nodes to distribute the workload.
           * It has one node machine by default (in our case).
           * It can handle 56 forks meaning it can run 56 concurrent tasks in parallel

             ![Screenshots](<Default Instance Node.png>)

         2. Control Plane -

            * Definition: The control plane, often referred to as the "automation controller," is the central management component of Ansible Automation Platform.
            * Core functionality: It handles core platform functions such as job scheduling, inventory management, credential storage, and user interface.
            * Job coordination: The control plane coordinates job execution, but doesn't typically run the jobs itself.
            
             ![Screenshots](<Instance groups Controlplane.png>)


# Advantages of Red Hat Insights in Project Section.

Key benefits of Red Hat Insights in Ansible Automation Platform projects: 
 
   * Comprehensive monitoring:
Gain real-time insights into the health and status of your Ansible-managed systems within a project, including system configurations, performance metrics, and potential security vulnerabilities. 
 
  * Proactive issue detection:
Identify potential problems early through alerts and notifications, enabling timely remediation before issues escalate. 
 
  * Root cause analysis:
Leverage detailed reporting to pinpoint the root cause of issues within your projects, facilitating faster troubleshooting. 
 
  * Security assessment:
Identify security risks and vulnerabilities across your automated infrastructure, allowing you to prioritize security patches and remediation actions. 
 
   * Performance optimization:
Monitor performance metrics within a project to identify areas for improvement and optimize your automation workflows. 
 
 
   * Data-driven decision making:
Access detailed analytics to make informed decisions regarding future automation initiatives and project prioritization. 



# Job Slicing and how it works?

Job slicing in Ansible Automation Platform is a feature that lets you run a job across multiple hosts in a cluster: 
 
How it works: You add a job_slice_count field to a job template and specify how many jobs to slice the Ansible run into. The inventory is then split evenly across the slice jobs, and a workflow job is created. 
 
Benefits: Job slicing can reduce stress on nodes and improve performance. 
 
When to use it: For example, if you have 30 nodes in your inventory and create 3 slices, you'll have a workflow with three jobs, each running on 10 nodes in parallel. 
 


# Difference between AWX and Ansible Automation Platform

![Screenshot](<Difference AWX and AAP 1.png>)
![Screenshot](<Difference AWX and AAP 2.png>)
![Screenshot](<Difference AWX and AAP 3.png>)


# HOSTS Section under inventory:

Facts can be stored under the Inventory section, by enabling the facts_storage option in Ansible Automation Platform's Job template section.

The outputs of facts generated are different when gathering the facts through cli for the same host.

Benefits of fact caching:

  - Fact caching saves a significant amount of time over running fact gathering. If you have a playbook in a job that runs against a thousand hosts and forks, you could easily spend 10 minutes gathering facts across all of those hosts. But if you run a job on a regular basis, the first run of it caches these facts and the next run will just pull them from the database. This cuts the runtime of jobs against large inventories, including Smart Inventories, by an enormous magnitude.

Output of Facts gathered through the CLI: 


```
  ec2-1 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.31.21.236"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::8ff:cfff:fe4f:dcc9"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "08/24/2006",
        "ansible_bios_vendor": "Xen",
        "ansible_bios_version": "4.11.amazon",
        "ansible_board_asset_tag": "NA",
        "ansible_board_name": "NA",
        "ansible_board_serial": "NA",
        "ansible_board_vendor": "NA",
        "ansible_board_version": "NA",
        "ansible_chassis_asset_tag": "NA",
        "ansible_chassis_serial": "NA",
        "ansible_chassis_vendor": "Xen",
        "ansible_chassis_version": "NA",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-6.5.0-1022-aws",
            "console": "ttyS0",
            "nvme_core.io_timeout": "4294967295",
            "panic": "-1",
            "ro": true,
            "root": "PARTUUID=c3c83566-041b-448c-847a-c32f2ae31352"
        },
        "ansible_date_time": {
            "date": "2024-09-10",
            "day": "10",
            "epoch": "1725954148",
            "epoch_int": "1725954148",
            "hour": "07",
            "iso8601": "2024-09-10T07:42:28Z",
            "iso8601_basic": "20240910T074228839819",
            "iso8601_basic_short": "20240910T074228",
            "iso8601_micro": "2024-09-10T07:42:28.839819Z",
            "minute": "42",
            "month": "09",
            "second": "28",
            "time": "07:42:28",
            "tz": "UTC",
            "tz_dst": "UTC",
            "tz_offset": "+0000",
            "weekday": "Tuesday",
            "weekday_number": "2",
            "weeknumber": "37",
            "year": "2024"
        },
        "ansible_default_ipv4": {
            "address": "172.31.21.236",
            "alias": "eth0",
            "broadcast": "",
            "gateway": "172.31.16.1",
            "interface": "eth0",
            "macaddress": "0a:ff:cf:4f:dc:c9",
            "mtu": 9001,
            "netmask": "255.255.240.0",
            "network": "172.31.16.0",
            "prefix": "20",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_device_links": {
            "ids": {},
            "labels": {
                "xvda1": [
                    "cloudimg-rootfs"
                ],
                "xvda15": [
                    "UEFI"
                ]
            },
            "masters": {},
            "uuids": {
                "xvda1": [
                    "a7e321c6-fe24-4b08-b922-b296032b6eda"
                ],
                "xvda15": [
                    "E0C7-CA96"
                ]
            }
        },
        "ansible_devices": {
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "51688",
                "sectorsize": "512",
                "size": "25.24 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "113992",
                "sectorsize": "512",
                "size": "55.66 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "130960",
                "sectorsize": "512",
                "size": "63.95 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "178240",
                "sectorsize": "512",
                "size": "87.03 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "79520",
                "sectorsize": "512",
                "size": "38.83 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "178256",
                "sectorsize": "512",
                "size": "87.04 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "xvda": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {
                    "xvda1": {
                        "holders": [],
                        "links": {
                            "ids": [],
                            "labels": [
                                "cloudimg-rootfs"
                            ],
                            "masters": [],
                            "uuids": [
                                "a7e321c6-fe24-4b08-b922-b296032b6eda"
                            ]
                        },
                        "sectors": "16549855",
                        "sectorsize": 512,
                        "size": "7.89 GB",
                        "start": "227328",
                        "uuid": "a7e321c6-fe24-4b08-b922-b296032b6eda"
                    },
                    "xvda14": {
                        "holders": [],
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "sectors": "8192",
                        "sectorsize": 512,
                        "size": "4.00 MB",
                        "start": "2048",
                        "uuid": null
                    },
                    "xvda15": {
                        "holders": [],
                        "links": {
                            "ids": [],
                            "labels": [
                                "UEFI"
                            ],
                            "masters": [],
                            "uuids": [
                                "E0C7-CA96"
                            ]
                        },
                        "sectors": "217088",
                        "sectorsize": 512,
                        "size": "106.00 MB",
                        "start": "10240",
                        "uuid": "E0C7-CA96"
                    }
                },
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "16777216",
                "sectorsize": "512",
                "size": "8.00 GB",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            }
        },
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "22",
        "ansible_distribution_release": "jammy",
        "ansible_distribution_version": "22.04",
        "ansible_dns": {
            "nameservers": [
                "127.0.0.53"
            ],
            "options": {
                "edns0": true,
                "trust-ad": true
            },
            "search": [
                "ec2.internal"
            ]
        },
        "ansible_domain": "ec2.internal",
        "ansible_effective_group_id": 0,
        "ansible_effective_user_id": 0,
        "ansible_env": {
            "HOME": "/root",
            "LANG": "C.UTF-8",
            "LOGNAME": "root",
            "MAIL": "/var/mail/root",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin",
            "PWD": "/home/ubuntu",
            "SHELL": "/bin/bash",
            "SUDO_COMMAND": "/bin/sh -c echo BECOME-SUCCESS-pacledrthlgpssesjeuxyoatnudnhrlx ; /usr/bin/python3.10 /home/ubuntu/.ansible/tmp/ansible-tmp-1725954156.0794723-12158-122133518789224/AnsiballZ_setup.py",
            "SUDO_GID": "1000",
            "SUDO_UID": "1000",
            "SUDO_USER": "ubuntu",
            "TERM": "xterm-256color",
            "USER": "root"
        },
        "ansible_eth0": {
            "active": true,
            "device": "eth0",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "hsr_dup_offload": "off [fixed]",
                "hsr_fwd_offload": "off [fixed]",
                "hsr_tag_ins_offload": "off [fixed]",
                "hsr_tag_rm_offload": "off [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "macsec_hw_offload": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_gro_list": "off",
                "rx_udp_gro_forwarding": "off",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "off [fixed]",
                "tx_checksum_ipv4": "on [fixed]",
                "tx_checksum_ipv6": "on",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_list": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "on [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sctp_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_mangleid_segmentation": "off",
                "tx_tcp_segmentation": "on",
                "tx_tunnel_remcsum_segmentation": "off [fixed]",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "172.31.21.236",
                "broadcast": "",
                "netmask": "255.255.240.0",
                "network": "172.31.16.0",
                "prefix": "20"
            },
            "ipv6": [
                {
                    "address": "fe80::8ff:cfff:fe4f:dcc9",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "0a:ff:cf:4f:dc:c9",
            "mtu": 9001,
            "pciid": "vif-0",
            "promisc": false,
            "timestamping": [],
            "type": "ether"
        },
        "ansible_fibre_channel_wwn": [],
        "ansible_fips": false,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "ip-172-31-21-236.ec2.internal",
        "ansible_hostname": "ip-172-31-21-236",
        "ansible_hostnqn": "",
        "ansible_interfaces": [
            "lo",
            "eth0"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "",
        "ansible_kernel": "6.5.0-1022-aws",
        "ansible_kernel_version": "#22~22.04.1-Ubuntu SMP Fri Jun 14 16:31:00 UTC 2024",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "hsr_dup_offload": "off [fixed]",
                "hsr_fwd_offload": "off [fixed]",
                "hsr_tag_ins_offload": "off [fixed]",
                "hsr_tag_rm_offload": "off [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "macsec_hw_offload": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_gro_list": "off",
                "rx_udp_gro_forwarding": "off",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_list": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_tunnel_remcsum_segmentation": "off [fixed]",
                "tx_udp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "on [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0",
                "prefix": "8"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "timestamping": [],
            "type": "loopback"
        },
        "ansible_loadavg": {
            "15m": 0.0,
            "1m": 0.0,
            "5m": 0.0
        },
        "ansible_local": {},
        "ansible_locally_reachable_ips": {
            "ipv4": [
                "127.0.0.0/8",
                "127.0.0.1",
                "172.31.21.236"
            ],
            "ipv6": [
                "::1",
                "fe80::8ff:cfff:fe4f:dcc9"
            ]
        },
        "ansible_lsb": {
            "codename": "jammy",
            "description": "Ubuntu 22.04.4 LTS",
            "id": "Ubuntu",
            "major_release": "22",
            "release": "22.04"
        },
        "ansible_lvm": {
            "lvs": {},
            "pvs": {},
            "vgs": {}
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "db97c915c7ca435680c25c11180fd55b",
        "ansible_memfree_mb": 233,
        "ansible_memory_mb": {
            "nocache": {
                "free": 695,
                "used": 254
            },
            "real": {
                "free": 233,
                "total": 949,
                "used": 716
            },
            "swap": {
                "cached": 0,
                "free": 0,
                "total": 0,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 949,
        "ansible_mounts": [
            {
                "block_available": 1342980,
                "block_size": 4096,
                "block_total": 1985394,
                "block_used": 642414,
                "device": "/dev/root",
                "dump": 0,
                "fstype": "ext4",
                "inode_available": 920618,
                "inode_total": 1032192,
                "inode_used": 111574,
                "mount": "/",
                "options": "rw,relatime,discard,errors=remount-ro",
                "passno": 0,
                "size_available": 5500846080,
                "size_total": 8132173824,
                "uuid": "a7e321c6-fe24-4b08-b922-b296032b6eda"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 202,
                "block_used": 202,
                "device": "/dev/loop0",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 16,
                "inode_used": 16,
                "mount": "/snap/amazon-ssm-agent/7993",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 26476544,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 446,
                "block_used": 446,
                "device": "/dev/loop1",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10944,
                "inode_used": 10944,
                "mount": "/snap/core18/2829",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 58458112,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 512,
                "block_used": 512,
                "device": "/dev/loop2",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 12057,
                "inode_used": 12057,
                "mount": "/snap/core20/2318",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 67108864,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 697,
                "block_used": 697,
                "device": "/dev/loop3",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 959,
                "inode_used": 959,
                "mount": "/snap/lxd/28373",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 91357184,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 311,
                "block_used": 311,
                "device": "/dev/loop4",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 651,
                "inode_used": 651,
                "mount": "/snap/snapd/21759",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 40763392,
                "uuid": "N/A"
            },
            {
                "block_available": 201292,
                "block_size": 512,
                "block_total": 213663,
                "block_used": 12371,
                "device": "/dev/xvda15",
                "dump": 0,
                "fstype": "vfat",
                "inode_available": 0,
                "inode_total": 0,
                "inode_used": 0,
                "mount": "/boot/efi",
                "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
                "passno": 0,
                "size_available": 103061504,
                "size_total": 109395456,
                "uuid": "E0C7-CA96"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 697,
                "block_used": 697,
                "device": "/dev/loop5",
                "dump": 0,
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 959,
                "inode_used": 959,
                "mount": "/snap/lxd/29351",
                "options": "ro,nodev,relatime,errors=continue,threads=single",
                "passno": 0,
                "size_available": 0,
                "size_total": 91357184,
                "uuid": "N/A"
            }
        ],
        "ansible_nodename": "ip-172-31-21-236",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_proc_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-6.5.0-1022-aws",
            "console": [
                "tty1",
                "ttyS0"
            ],
            "nvme_core.io_timeout": "4294967295",
            "panic": "-1",
            "ro": true,
            "root": "PARTUUID=c3c83566-041b-448c-847a-c32f2ae31352"
        },
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz"
        ],
        "ansible_processor_cores": 1,
        "ansible_processor_count": 1,
        "ansible_processor_nproc": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 1,
        "ansible_product_name": "HVM domU",
        "ansible_product_serial": "ec2c9fe0-5ebc-23e7-8b64-5e2333d48500",
        "ansible_product_uuid": "ec2c9fe0-5ebc-23e7-8b64-5e2333d48500",
        "ansible_product_version": "4.11.amazon",
        "ansible_python": {
            "executable": "/usr/bin/python3.10",
            "has_sslcontext": true,
            "type": "cpython",
            "version": {
                "major": 3,
                "micro": 12,
                "minor": 10,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                3,
                10,
                12,
                "final",
                0
            ]
        },
        "ansible_python_version": "3.10.12",
        "ansible_real_group_id": 0,
        "ansible_real_user_id": 0,
        "ansible_selinux": {
            "status": "disabled"
        },
        "ansible_selinux_python_present": true,
        "ansible_service_mgr": "systemd",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBATm0gryhcAglxZf3zMX2/sTXQneF/3iUzmbrddl0n9rxeTU12z20RynKw4Xf84qr+140lahQ5VEIID5nOCLVxM=",
        "ansible_ssh_host_key_ecdsa_public_keytype": "ecdsa-sha2-nistp256",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIHkGlIY2WLmKj3Ip7SpZonAL8EORW8QSp28rSzyLQUyK",
        "ansible_ssh_host_key_ed25519_public_keytype": "ssh-ed25519",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQDX1R3RhotmRwBe0pwVls7LAO4RJXEZAEe2M8ekX4Uyy5YkyQQnyUzcyKt3BTPFkzDcDy3sWDImogkqc4EmJe3JI24FM2ZaBpZiTNIilSN0SfX+Q2JSxFU9FjmiSriieTXHyzLgzlAhJVKSp6m9NyZ+ABEx1gD/iQaN26kYR/7RmlJko1GQdtGlz5bSNWcJXVJ9YZveoGA5qSKRTEv/AEFzbpZTmU9xWnIjS1xAHwFQJ8nraD+UW2Z/ITI1m1BIg10+g+EsE1aASCstj71Wq1TKqYfrOD68dnyc4cwVeCa3O2h9VvSFyjNRpyzncmkLiKRgA9pg234lAw5gKS/o0B1lM4r+cLY/aI318RbdxH1rHVwexR76kZqDxI3oQQUH6e7ucXPthl+3RDIT/3Ka2AXTUi5Sb4s5U+tpKkUQ8/vMl4swtHAvqgOc+SOT2D2qHcl8XckOpfNXVm6zt3S9B/CGydQrmlG4EV9ZBEuxt1UGZ0a2VlQfIQvr8x+FTCLEypE=",
        "ansible_ssh_host_key_rsa_public_keytype": "ssh-rsa",
        "ansible_swapfree_mb": 0,
        "ansible_swaptotal_mb": 0,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [],
        "ansible_system_capabilities_enforced": "False",
        "ansible_system_vendor": "Xen",
        "ansible_uptime_seconds": 180680,
        "ansible_user_dir": "/root",
        "ansible_user_gecos": "root",
        "ansible_user_gid": 0,
        "ansible_user_id": "root",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 0,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_tech_guest": [
            "xen"
        ],
        "ansible_virtualization_tech_host": [],
        "ansible_virtualization_type": "xen",
        "discovered_interpreter_python": "/usr/bin/python3.10",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false,
    "deprecations": []
}

```

Output of Facts Gathered through Automation platform:

```
  {
  "ansible_lo": {
    "mtu": 65536,
    "ipv4": {
      "prefix": "8",
      "address": "127.0.0.1",
      "netmask": "255.0.0.0",
      "network": "127.0.0.0",
      "broadcast": ""
    },
    "ipv6": [
      {
        "scope": "host",
        "prefix": "128",
        "address": "::1"
      }
    ],
    "type": "loopback",
    "active": true,
    "device": "lo",
    "promisc": false,
    "features": {
      "rx_all": "off [fixed]",
      "rx_fcs": "off [fixed]",
      "highdma": "on [fixed]",
      "fcoe_mtu": "off [fixed]",
      "loopback": "on [fixed]",
      "rx_gro_hw": "off [fixed]",
      "netns_local": "on [fixed]",
      "rx_gro_list": "off",
      "tx_gso_list": "on",
      "tx_lockless": "on [fixed]",
      "hw_tc_offload": "off [fixed]",
      "tls_hw_record": "off [fixed]",
      "tx_gso_robust": "off [fixed]",
      "esp_hw_offload": "off [fixed]",
      "l2_fwd_offload": "off [fixed]",
      "ntuple_filters": "off [fixed]",
      "rx_vlan_filter": "off [fixed]",
      "scatter_gather": "on",
      "tx_gso_partial": "off [fixed]",
      "hsr_dup_offload": "off [fixed]",
      "hsr_fwd_offload": "off [fixed]",
      "receive_hashing": "off [fixed]",
      "rx_checksumming": "on [fixed]",
      "rx_vlan_offload": "off [fixed]",
      "tx_checksumming": "on",
      "tx_nocache_copy": "off [fixed]",
      "tx_vlan_offload": "off [fixed]",
      "vlan_challenged": "on [fixed]",
      "tx_checksum_ipv4": "off [fixed]",
      "tx_checksum_ipv6": "off [fixed]",
      "tx_checksum_sctp": "on [fixed]",
      "macsec_hw_offload": "off [fixed]",
      "tls_hw_rx_offload": "off [fixed]",
      "tls_hw_tx_offload": "off [fixed]",
      "tx_scatter_gather": "on [fixed]",
      "hsr_tag_rm_offload": "off [fixed]",
      "hsr_tag_ins_offload": "off [fixed]",
      "rx_vlan_stag_filter": "off [fixed]",
      "tx_esp_segmentation": "off [fixed]",
      "tx_gre_segmentation": "off [fixed]",
      "tx_tcp_segmentation": "on",
      "tx_udp_segmentation": "on",
      "tx_checksum_fcoe_crc": "off [fixed]",
      "tx_fcoe_segmentation": "off [fixed]",
      "tx_sctp_segmentation": "on",
      "tx_tcp6_segmentation": "on",
      "large_receive_offload": "off [fixed]",
      "rx_udp_gro_forwarding": "off",
      "rx_vlan_stag_hw_parse": "off [fixed]",
      "esp_tx_csum_hw_offload": "off [fixed]",
      "tx_checksum_ip_generic": "on [fixed]",
      "tx_ipxip4_segmentation": "off [fixed]",
      "tx_ipxip6_segmentation": "off [fixed]",
      "tx_vlan_stag_hw_insert": "off [fixed]",
      "generic_receive_offload": "on",
      "tx_tcp_ecn_segmentation": "on",
      "tx_udp_tnl_segmentation": "off [fixed]",
      "tcp_segmentation_offload": "on",
      "tx_gre_csum_segmentation": "off [fixed]",
      "rx_udp_tunnel_port_offload": "off [fixed]",
      "tx_scatter_gather_fraglist": "on [fixed]",
      "generic_segmentation_offload": "on",
      "tx_tcp_mangleid_segmentation": "on",
      "tx_udp_tnl_csum_segmentation": "off [fixed]",
      "tx_tunnel_remcsum_segmentation": "off [fixed]"
    },
    "timestamping": [],
    "hw_timestamp_filters": []
  },
  "ansible_dns": {
    "search": [
      "ec2.internal"
    ],
    "options": {
      "edns0": true,
      "trust-ad": true
    },
    "nameservers": [
      "127.0.0.53"
    ]
  },
  "ansible_env": {
    "PWD": "/home/ubuntu",
    "HOME": "/root",
    "LANG": "C.UTF-8",
    "MAIL": "/var/mail/root",
    "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin",
    "TERM": "xterm",
    "USER": "root",
    "SHELL": "/bin/bash",
    "LOGNAME": "root",
    "LC_CTYPE": "C.UTF-8",
    "SUDO_GID": "1000",
    "SUDO_UID": "1000",
    "SUDO_USER": "ubuntu",
    "SUDO_COMMAND": "/bin/sh -c echo BECOME-SUCCESS-ohihaxlqmpbtspebmqhtwzdffwwkzkmu ; /usr/bin/python3 /home/ubuntu/.ansible/tmp/ansible-tmp-1725965317.607504-30-125288842431340/AnsiballZ_setup.py"
  },
  "ansible_lsb": {
    "id": "Ubuntu",
    "release": "22.04",
    "codename": "jammy",
    "description": "Ubuntu 22.04.4 LTS",
    "major_release": "22"
  },
  "ansible_lvm": {
    "lvs": {},
    "pvs": {},
    "vgs": {}
  },
  "ansible_eth0": {
    "mtu": 9001,
    "ipv4": {
      "prefix": "20",
      "address": "172.31.21.236",
      "netmask": "255.255.240.0",
      "network": "172.31.16.0",
      "broadcast": ""
    },
    "ipv6": [
      {
        "scope": "link",
        "prefix": "64",
        "address": "fe80::8ff:cfff:fe4f:dcc9"
      }
    ],
    "type": "ether",
    "pciid": "vif-0",
    "active": true,
    "device": "eth0",
    "promisc": false,
    "features": {
      "rx_all": "off [fixed]",
      "rx_fcs": "off [fixed]",
      "highdma": "off [fixed]",
      "fcoe_mtu": "off [fixed]",
      "loopback": "off [fixed]",
      "rx_gro_hw": "off [fixed]",
      "netns_local": "off [fixed]",
      "rx_gro_list": "off",
      "tx_gso_list": "off [fixed]",
      "tx_lockless": "off [fixed]",
      "hw_tc_offload": "off [fixed]",
      "tls_hw_record": "off [fixed]",
      "tx_gso_robust": "on [fixed]",
      "esp_hw_offload": "off [fixed]",
      "l2_fwd_offload": "off [fixed]",
      "ntuple_filters": "off [fixed]",
      "rx_vlan_filter": "off [fixed]",
      "scatter_gather": "on",
      "tx_gso_partial": "off [fixed]",
      "hsr_dup_offload": "off [fixed]",
      "hsr_fwd_offload": "off [fixed]",
      "receive_hashing": "off [fixed]",
      "rx_checksumming": "on [fixed]",
      "rx_vlan_offload": "off [fixed]",
      "tx_checksumming": "on",
      "tx_nocache_copy": "off",
      "tx_vlan_offload": "off [fixed]",
      "vlan_challenged": "off [fixed]",
      "tx_checksum_ipv4": "on [fixed]",
      "tx_checksum_ipv6": "on",
      "tx_checksum_sctp": "off [fixed]",
      "macsec_hw_offload": "off [fixed]",
      "tls_hw_rx_offload": "off [fixed]",
      "tls_hw_tx_offload": "off [fixed]",
      "tx_scatter_gather": "on",
      "hsr_tag_rm_offload": "off [fixed]",
      "hsr_tag_ins_offload": "off [fixed]",
      "rx_vlan_stag_filter": "off [fixed]",
      "tx_esp_segmentation": "off [fixed]",
      "tx_gre_segmentation": "off [fixed]",
      "tx_tcp_segmentation": "on",
      "tx_udp_segmentation": "off [fixed]",
      "tx_checksum_fcoe_crc": "off [fixed]",
      "tx_fcoe_segmentation": "off [fixed]",
      "tx_sctp_segmentation": "off [fixed]",
      "tx_tcp6_segmentation": "on",
      "large_receive_offload": "off [fixed]",
      "rx_udp_gro_forwarding": "off",
      "rx_vlan_stag_hw_parse": "off [fixed]",
      "esp_tx_csum_hw_offload": "off [fixed]",
      "tx_checksum_ip_generic": "off [fixed]",
      "tx_ipxip4_segmentation": "off [fixed]",
      "tx_ipxip6_segmentation": "off [fixed]",
      "tx_vlan_stag_hw_insert": "off [fixed]",
      "generic_receive_offload": "on",
      "tx_tcp_ecn_segmentation": "off [fixed]",
      "tx_udp_tnl_segmentation": "off [fixed]",
      "tcp_segmentation_offload": "on",
      "tx_gre_csum_segmentation": "off [fixed]",
      "rx_udp_tunnel_port_offload": "off [fixed]",
      "tx_scatter_gather_fraglist": "off [fixed]",
      "generic_segmentation_offload": "on",
      "tx_tcp_mangleid_segmentation": "off",
      "tx_udp_tnl_csum_segmentation": "off [fixed]",
      "tx_tunnel_remcsum_segmentation": "off [fixed]"
    },
    "macaddress": "0a:ff:cf:4f:dc:c9",
    "timestamping": [],
    "hw_timestamp_filters": []
  },
  "ansible_fips": false,
  "ansible_fqdn": "ip-172-31-21-236.ec2.internal",
  "module_setup": true,
  "ansible_local": {},
  "gather_subset": [
    "all"
  ],
  "ansible_domain": "ec2.internal",
  "ansible_kernel": "6.5.0-1022-aws",
  "ansible_mounts": [
    {
      "uuid": "a7e321c6-fe24-4b08-b922-b296032b6eda",
      "mount": "/",
      "device": "/dev/root",
      "fstype": "ext4",
      "options": "rw,relatime,discard,errors=remount-ro",
      "block_size": 4096,
      "block_used": 644540,
      "inode_used": 111574,
      "size_total": 8132173824,
      "block_total": 1985394,
      "inode_total": 1032192,
      "size_available": 5492137984,
      "block_available": 1340854,
      "inode_available": 920618
    },
    {
      "uuid": "N/A",
      "mount": "/snap/amazon-ssm-agent/7993",
      "device": "/dev/loop0",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 202,
      "inode_used": 16,
      "size_total": 26476544,
      "block_total": 202,
      "inode_total": 16,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    },
    {
      "uuid": "N/A",
      "mount": "/snap/core18/2829",
      "device": "/dev/loop1",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 446,
      "inode_used": 10944,
      "size_total": 58458112,
      "block_total": 446,
      "inode_total": 10944,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    },
    {
      "uuid": "N/A",
      "mount": "/snap/core20/2318",
      "device": "/dev/loop2",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 512,
      "inode_used": 12057,
      "size_total": 67108864,
      "block_total": 512,
      "inode_total": 12057,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    },
    {
      "uuid": "N/A",
      "mount": "/snap/lxd/28373",
      "device": "/dev/loop3",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 697,
      "inode_used": 959,
      "size_total": 91357184,
      "block_total": 697,
      "inode_total": 959,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    },
    {
      "uuid": "N/A",
      "mount": "/snap/snapd/21759",
      "device": "/dev/loop4",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 311,
      "inode_used": 651,
      "size_total": 40763392,
      "block_total": 311,
      "inode_total": 651,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    },
    {
      "uuid": "E0C7-CA96",
      "mount": "/boot/efi",
      "device": "/dev/xvda15",
      "fstype": "vfat",
      "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
      "block_size": 512,
      "block_used": 12371,
      "inode_used": 0,
      "size_total": 109395456,
      "block_total": 213663,
      "inode_total": 0,
      "size_available": 103061504,
      "block_available": 201292,
      "inode_available": 0
    },
    {
      "uuid": "N/A",
      "mount": "/snap/lxd/29351",
      "device": "/dev/loop5",
      "fstype": "squashfs",
      "options": "ro,nodev,relatime,errors=continue,threads=single",
      "block_size": 131072,
      "block_used": 697,
      "inode_used": 959,
      "size_total": 91357184,
      "block_total": 697,
      "inode_total": 959,
      "size_available": 0,
      "block_available": 0,
      "inode_available": 0
    }
  ],
  "ansible_python": {
    "type": "cpython",
    "version": {
      "major": 3,
      "micro": 12,
      "minor": 10,
      "serial": 0,
      "releaselevel": "final"
    },
    "executable": "/usr/bin/python3",
    "version_info": [
      3,
      10,
      12,
      "final",
      0
    ],
    "has_sslcontext": true
  },
  "ansible_system": "Linux",
  "ansible_cmdline": {
    "ro": true,
    "root": "PARTUUID=c3c83566-041b-448c-847a-c32f2ae31352",
    "panic": "-1",
    "console": "ttyS0",
    "BOOT_IMAGE": "/boot/vmlinuz-6.5.0-1022-aws",
    "nvme_core.io_timeout": "4294967295"
  },
  "ansible_devices": {
    "xvda": {
      "host": "",
      "size": "8.00 GB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "16777216",
      "virtual": 1,
      "removable": "0",
      "partitions": {
        "xvda1": {
          "size": "7.89 GB",
          "uuid": "a7e321c6-fe24-4b08-b922-b296032b6eda",
          "links": {
            "ids": [],
            "uuids": [
              "a7e321c6-fe24-4b08-b922-b296032b6eda"
            ],
            "labels": [
              "cloudimg-rootfs"
            ],
            "masters": []
          },
          "start": "227328",
          "holders": [],
          "sectors": "16549855",
          "sectorsize": 512
        },
        "xvda14": {
          "size": "4.00 MB",
          "uuid": null,
          "links": {
            "ids": [],
            "uuids": [],
            "labels": [],
            "masters": []
          },
          "start": "2048",
          "holders": [],
          "sectors": "8192",
          "sectorsize": 512
        },
        "xvda15": {
          "size": "106.00 MB",
          "uuid": "E0C7-CA96",
          "links": {
            "ids": [],
            "uuids": [
              "E0C7-CA96"
            ],
            "labels": [
              "UEFI"
            ],
            "masters": []
          },
          "start": "10240",
          "holders": [],
          "sectors": "217088",
          "sectorsize": 512
        }
      },
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "mq-deadline",
      "support_discard": "0",
      "sas_device_handle": null
    },
    "loop0": {
      "host": "",
      "size": "25.24 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "51688",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop1": {
      "host": "",
      "size": "55.66 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "113992",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop2": {
      "host": "",
      "size": "63.95 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "130960",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop3": {
      "host": "",
      "size": "87.03 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "178240",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop4": {
      "host": "",
      "size": "38.83 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "79520",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop5": {
      "host": "",
      "size": "87.04 MB",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "178256",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop6": {
      "host": "",
      "size": "0.00 Bytes",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "0",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "0",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "4096",
      "sas_device_handle": null
    },
    "loop7": {
      "host": "",
      "size": "0.00 Bytes",
      "links": {
        "ids": [],
        "uuids": [],
        "labels": [],
        "masters": []
      },
      "model": null,
      "vendor": null,
      "holders": [],
      "sectors": "0",
      "virtual": 1,
      "removable": "0",
      "partitions": {},
      "rotational": "1",
      "sectorsize": "512",
      "sas_address": null,
      "scheduler_mode": "none",
      "support_discard": "0",
      "sas_device_handle": null
    }
  },
  "ansible_hostnqn": "",
  "ansible_loadavg": {
    "1m": 0,
    "5m": 0,
    "15m": 0
  },
  "ansible_machine": "x86_64",
  "ansible_pkg_mgr": "apt",
  "ansible_selinux": {
    "status": "disabled"
  },
  "ansible_user_id": "root",
  "ansible_apparmor": {
    "status": "enabled"
  },
  "ansible_hostname": "ip-172-31-21-236",
  "ansible_nodename": "ip-172-31-21-236",
  "ansible_user_dir": "/root",
  "ansible_user_gid": 0,
  "ansible_user_uid": 0,
  "ansible_bios_date": "08/24/2006",
  "ansible_date_time": {
    "tz": "UTC",
    "day": "10",
    "date": "2024-09-10",
    "hour": "10",
    "time": "10:48:44",
    "year": "2024",
    "epoch": "1725965324",
    "month": "09",
    "minute": "48",
    "second": "44",
    "tz_dst": "UTC",
    "iso8601": "2024-09-10T10:48:44Z",
    "weekday": "Tuesday",
    "epoch_int": "1725965324",
    "tz_offset": "+0000",
    "weeknumber": "37",
    "iso8601_basic": "20240910T104844383745",
    "iso8601_micro": "2024-09-10T10:48:44.383745Z",
    "weekday_number": "2",
    "iso8601_basic_short": "20240910T104844"
  },
  "ansible_is_chroot": false,
  "ansible_iscsi_iqn": "",
  "ansible_memory_mb": {
    "real": {
      "free": 244,
      "used": 705,
      "total": 949
    },
    "swap": {
      "free": 0,
      "used": 0,
      "total": 0,
      "cached": 0
    },
    "nocache": {
      "free": 689,
      "used": 260
    }
  },
  "ansible_os_family": "Debian",
  "ansible_processor": [
    "0",
    "GenuineIntel",
    "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz"
  ],
  "ansible_board_name": "NA",
  "ansible_interfaces": [
    "lo",
    "eth0"
  ],
  "ansible_machine_id": "db97c915c7ca435680c25c11180fd55b",
  "ansible_memfree_mb": 244,
  "ansible_user_gecos": "root",
  "ansible_user_shell": "/bin/bash",
  "ansible_bios_vendor": "Xen",
  "ansible_form_factor": "Other",
  "ansible_memtotal_mb": 949,
  "ansible_service_mgr": "systemd",
  "ansible_swapfree_mb": 0,
  "ansible_architecture": "x86_64",
  "ansible_bios_version": "4.11.amazon",
  "ansible_board_serial": "NA",
  "ansible_board_vendor": "NA",
  "ansible_default_ipv4": {
    "mtu": 9001,
    "type": "ether",
    "alias": "eth0",
    "prefix": "20",
    "address": "172.31.21.236",
    "gateway": "172.31.16.1",
    "netmask": "255.255.240.0",
    "network": "172.31.16.0",
    "broadcast": "",
    "interface": "eth0",
    "macaddress": "0a:ff:cf:4f:dc:c9"
  },
  "ansible_default_ipv6": {},
  "ansible_device_links": {
    "ids": {},
    "uuids": {
      "xvda1": [
        "a7e321c6-fe24-4b08-b922-b296032b6eda"
      ],
      "xvda15": [
        "E0C7-CA96"
      ]
    },
    "labels": {
      "xvda1": [
        "cloudimg-rootfs"
      ],
      "xvda15": [
        "UEFI"
      ]
    },
    "masters": {}
  },
  "ansible_distribution": "Ubuntu",
  "ansible_proc_cmdline": {
    "ro": true,
    "root": "PARTUUID=c3c83566-041b-448c-847a-c32f2ae31352",
    "panic": "-1",
    "console": [
      "tty1",
      "ttyS0"
    ],
    "BOOT_IMAGE": "/boot/vmlinuz-6.5.0-1022-aws",
    "nvme_core.io_timeout": "4294967295"
  },
  "ansible_product_name": "HVM domU",
  "ansible_product_uuid": "ec2c9fe0-5ebc-23e7-8b64-5e2333d48500",
  "ansible_real_user_id": 0,
  "ansible_swaptotal_mb": 0,
  "ansible_board_version": "NA",
  "ansible_real_group_id": 0,
  "ansible_system_vendor": "Xen",
  "ansible_chassis_serial": "NA",
  "ansible_chassis_vendor": "Xen",
  "ansible_kernel_version": "#22~22.04.1-Ubuntu SMP Fri Jun 14 16:31:00 UTC 2024",
  "ansible_product_serial": "ec2c9fe0-5ebc-23e7-8b64-5e2333d48500",
  "ansible_python_version": "3.10.12",
  "ansible_uptime_seconds": 191855,
  "ansible_userspace_bits": "64",
  "_ansible_facts_gathered": true,
  "ansible_board_asset_tag": "NA",
  "ansible_chassis_version": "NA",
  "ansible_processor_cores": 1,
  "ansible_processor_count": 1,
  "ansible_processor_nproc": 1,
  "ansible_processor_vcpus": 1,
  "ansible_product_version": "4.11.amazon",
  "ansible_chassis_asset_tag": "NA",
  "ansible_effective_user_id": 0,
  "ansible_fibre_channel_wwn": [],
  "ansible_all_ipv4_addresses": [
    "172.31.21.236"
  ],
  "ansible_all_ipv6_addresses": [
    "fe80::8ff:cfff:fe4f:dcc9"
  ],
  "ansible_effective_group_id": 0,
  "ansible_system_capabilities": [],
  "ansible_virtualization_role": "guest",
  "ansible_virtualization_type": "xen",
  "ansible_distribution_release": "jammy",
  "ansible_distribution_version": "22.04",
  "ansible_locally_reachable_ips": {
    "ipv4": [
      "127.0.0.0/8",
      "127.0.0.1",
      "172.31.21.236"
    ],
    "ipv6": [
      "::1",
      "fe80::8ff:cfff:fe4f:dcc9"
    ]
  },
  "discovered_interpreter_python": "/usr/bin/python3",
  "ansible_distribution_file_path": "/etc/os-release",
  "ansible_selinux_python_present": true,
  "ansible_userspace_architecture": "x86_64",
  "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQDX1R3RhotmRwBe0pwVls7LAO4RJXEZAEe2M8ekX4Uyy5YkyQQnyUzcyKt3BTPFkzDcDy3sWDImogkqc4EmJe3JI24FM2ZaBpZiTNIilSN0SfX+Q2JSxFU9FjmiSriieTXHyzLgzlAhJVKSp6m9NyZ+ABEx1gD/iQaN26kYR/7RmlJko1GQdtGlz5bSNWcJXVJ9YZveoGA5qSKRTEv/AEFzbpZTmU9xWnIjS1xAHwFQJ8nraD+UW2Z/ITI1m1BIg10+g+EsE1aASCstj71Wq1TKqYfrOD68dnyc4cwVeCa3O2h9VvSFyjNRpyzncmkLiKRgA9pg234lAw5gKS/o0B1lM4r+cLY/aI318RbdxH1rHVwexR76kZqDxI3oQQUH6e7ucXPthl+3RDIT/3Ka2AXTUi5Sb4s5U+tpKkUQ8/vMl4swtHAvqgOc+SOT2D2qHcl8XckOpfNXVm6zt3S9B/CGydQrmlG4EV9ZBEuxt1UGZ0a2VlQfIQvr8x+FTCLEypE=",
  "ansible_distribution_file_parsed": true,
  "ansible_virtualization_tech_host": [],
  "ansible_distribution_file_variety": "Debian",
  "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBATm0gryhcAglxZf3zMX2/sTXQneF/3iUzmbrddl0n9rxeTU12z20RynKw4Xf84qr+140lahQ5VEIID5nOCLVxM=",
  "ansible_virtualization_tech_guest": [
    "xen"
  ],
  "ansible_distribution_major_version": "22",
  "ansible_processor_threads_per_core": 1,
  "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIHkGlIY2WLmKj3Ip7SpZonAL8EORW8QSp28rSzyLQUyK",
  "ansible_system_capabilities_enforced": "False",
  "ansible_ssh_host_key_rsa_public_keytype": "ssh-rsa",
  "ansible_ssh_host_key_ecdsa_public_keytype": "ecdsa-sha2-nistp256",
  "ansible_ssh_host_key_ed25519_public_keytype": "ssh-ed25519"
}

```

To Clear Facts you need to run clear_facts meta task

```
  - hosts: all
    gather_facts: false
    tasks:
      - name: Clear gathered facts from all currently targeted hosts
        meta: clear_facts
```


## Grouping of Hosts based on Keywords in Inventory section:

When you go to Inventories > AWS EC2 Region us-east-1 inventory (Dynamic) > Sources > AWS EC2 Sources, you can see Source Variables Section. In that field if I add these parameters.

![Screenshots](<Inventory - 5.png>)
```
regions:
  - us-east-1 
keyed_groups:
  - key: instance_type 
    prefix: type_
filters:
  instance-type: <--- Only looks for instances based on the type t2.micro
    - t2.micro
```

After Saving and syncing it, you can see the groups as: 

![Screenshots](<Inventory - 6.png>)

Note: In the screenshot aws_ec2 group is also present, because it was created using the aws_ec2 plugin automatically, when we select the source as AWS EC2 during the creation of Dynamic Inventory.


# What are Instance Groups and Container Groups under Instance Groups Section?

![Screenshots](<Instance Section.png>)

1. Container Group: 
   - Purpose - A ContainerGroup is a type of InstanceGroup that has an associated Credential that allows for connecting to an OpenShift cluster. 

   - Container groups act as a pool of resources within a virtual environment. You can create instance groups to point to an OpenShift container, which are job environments that are provisioned on-demand as a Pod that exists only for the duration of the playbook run. This is known as the ephemeral execution model and ensures a clean environment for every job run.
   
    ![Screenshots](<Instance Groups - CG SPECS.png>)

   - Name: Name you want to specify for the container groups
   - Credential - Credential to authenticate with Kubernetes or OpenShift. Must be of type "Kubernetes/OpenShift API Bearer Token". If left blank, the underlying Pod's service account will be used.
   - Max concurrent Jobs - Maximum number of jobs to run concurrently on this group. Zero means no limit will be enforced.
   - Max Forks - Maximum number of forks to allow across all jobs running concurrently on this group. Zero means no limit will be enforced.
   - Options- If you enable the customise pod specification, a custom pod spec field will open, and you can customise the pod specification. 

   
2. Instance Group:

   - Instance Groups - These are basically the virtual machine environments we configure to run the Jobs in Ansible Automation Platform.
   - Purpose - A group that contains instances for use in a clustered environment. An instance group provides the ability to group instances based on policy.

   - Instance groups can be assigned to one or more of the resources listed below.

      - Organizations

      - Inventories

      - Job Templates
 
 **Note - During the execution process, instance groups associated with Job Templates are checked before those associated with Inventories. Similarly, instance groups associated with Inventories are checked before those associated with Organizations. Thus, Instance Group assignments for the three resources form a hierarchy: Job Template > Inventory > Organization.

 ![Screenshots](<Instance Groups - IG SPECS.png>)

  - Name: Name must be unique and must not be named "controller".
  - Policy instance minimum - Enter the minimum number of instances to automatically assign to this group when new instances come online.
  - Policy instance percentage- Minimum percentage of all instances that will be automatically assigned to this group when new instances come online.
  - Max Concurrent jobs - Maximum number of jobs to run concurrently on this group. Zero means no limit will be enforced.
  - Max Forks - Maximum number of forks to allow across all jobs running concurrently on this group. Zero means no limit will be enforced.

# Instances Section - 

  - Purpose - Now to associate instances to an instance group, we configure that from the instances section.

![Screenshots](<Instances - 1.png>)

Currently we have a by default Instance - which is created as soon as we install ansible automation platform. 

![Screenshots](<Policy Type .png>)
When we click on it, it shows us the details like:

  - Policy Type - Auto, which means how the system manages and allocates resources for job allocation.

  - Instance Groups - The instances which are a part of this group.
