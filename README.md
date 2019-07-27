# SNOW-File-Comparator
Compares files from different branches and spits out deleted files

# How to install?
Run following command in terminal to install SNOW Comparator (snowcomp) module:

<pre>pip install snowcomp</pre>

# How to use?
Create a configuration file (`config.json`) having information related branches to compare, Git repository etc.

<pre>{
    "username": "[your_git_username]",
    "password": "[your_git_password]",
    "git_repo_link": "[link_of_get_repository]",
    "old_branch": "master",
    "latest_branch": "develop",
    "clone_dir": "test_clone",
    "instance_of_old_app": "[optional_name_of_instance_of_old_app_like_venXXXXX]",
    "delete_not_allowed": ["sys_db_object", "sys_ui_page", "sysauto_script", "sys_script", "sys_script_include", "sys_ui_action", "sysevent_register" , "sysevent_script_action", "sys_script_client", "sys_user_role", "sys_security_acl", "ecc_agent_script_include"]
}</pre>

You can add more classes in `delete_not_allowed` key. Currently only the files from above classes will be displayed if they are deleted from the new application.

Now run following command in the directory where above `config.json` is saved.

<pre>python -m snowcomp</pre>

This will create a file named `Deleted Files.txt` having links to deleted files.

## Note

Supports Python 3.x
