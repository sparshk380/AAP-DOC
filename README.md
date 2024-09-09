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

