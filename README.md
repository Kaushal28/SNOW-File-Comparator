# SNOW-File-Comparator
Compares files from different branches and spits out deleted files

# How to install?
Run following command in terminal to install SNOW Comparator (snowcomp) module:

<pre>pip install snowcomp</pre>

# How to use?
Create a configuration file (`conf.json`) having information related branches to compare, Git repository etc.

<pre>{
    "username": "[your_username]",
    "password": "[your_password]",
    "git_repo_link": "[link_of_git_repo]",
    "old_branch": "master",
    "latest_branch": "develop",
    "clone_dir": "test_clone",
    "instance_of_old_app": "[venXXXXX]",
    "ignore_deletions": ["sys_dictionary", "sys_documentation", "ua_table_licensing_config", "wf_workflow_version", 
                        "wf_activity", "wf_condition", "sys_variable_value", "wf_transition", "wf_estimated_runtime_config"]
}</pre>

You can add more classes in `delete_not_allowed` key. Currently only the files from above classes will be displayed if they are deleted from the new application.

Now run following command in the directory where above `config.json` is saved.

<pre>python -m snowcomp</pre>

This will create a file named `Deleted Files.txt` having links to deleted files.

## Note
Supports Python 3.x
