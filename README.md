# SNOW-File-Comparator
Compares files from different branches and spits out deleted files

# How to install?
Run following command in terminal to install SNOW Comparator (snowcomp) module:

<pre>pip install snowcomp</pre>

# How to use?
Create a configuration file (`conf.json`) having information related branches to compare, Git repository etc.

<pre>{
    "username": "<your_username>",
    "password": "<your_password>",
    "git_repo_link": "<link_of_git_repo>",
    "old_branch": "master",
    "latest_branch": "develop",
    "clone_dir": "test_clone",
    "instance_of_old_app": "<optional: venXXXXX>",
    "ignore_deletions":  ["sys_dictionary", "sys_documentation", "ua_table_licensing_config", "wf_workflow_version", 
                        "wf_activity", "wf_condition", "sys_variable_value", "wf_transition", "wf_estimated_runtime_config", 
                        "sys_scope_privilege", "sys_wizard_answer", "sys_ui_view", "sys_metadata_link", "sys_embedded_help_role"]
}</pre>

You can add more classes in `ignore_deletions` list. File deletions from this list will be ignored and won't be shown as deleted files (Will be considered valid deletions). 

Now run following command in the directory where above `conf.json` is saved.

<pre>python -m snowcomp</pre>

This will create a file named `Deleted Files.txt` having links to deleted files.

## Note
Supports Python 3.x
