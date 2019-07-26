from git import Repo
import os, json, re

def get_config():
    with open('conf.json', 'r') as conf_file:
        conf_json = conf_file.read()
        json_conf = json.loads(conf_json)
    return json_conf['username'], json_conf['password'], json_conf['git_repo_link'], json_conf['latest_branch'], json_conf['old_branch'], json_conf['clone_dir'], json_conf['instance_of_old_app'], json_conf['delete_not_allowed']

def read_file(file_path):
    with open(file_path, 'r') as a_file:
        raw_file = a_file.read()
        sys_id = re.search(r'<sys_id>([a-f0-9]{32})<\/sys_id>', raw_file).groups()[0]
        sys_class = re.search(r'<sys_class_name>(.*?)</sys_class_name>', raw_file).groups()[0]
    return sys_id, sys_class

def get_class_sys_id_dict(update_dir):
    class_sys_id_dict = {}

    for each_file in os.listdir(update_dir):
        sys_id, sys_class = read_file(os.path.join(update_dir, each_file))
        if not (sys_class in class_sys_id_dict):
            class_sys_id_dict[sys_class] = [sys_id]
        else:
            class_sys_id_dict[sys_class].append(sys_id)

    return class_sys_id_dict

def exists_in_other_dict(class_name, file_name, all_files):
    return file_name in all_files[class_name]

def is_delete_allowed(class_name, delete_not_allowed):
    return not (class_name in delete_not_allowed)

if __name__ == '__main__':
    instance = '<your_instance>'
    username, password, repo_link, latest_branch, old_branch, clone_path, instance, delete_not_allowed = get_config()
    update_dir = os.path.join(clone_path, 'update')
    repository = Repo.clone_from(f'{repo_link[:8]}{username}:{password}@{repo_link[8:]}', clone_path)
    repository.git.checkout(latest_branch)
    latest_files = get_class_sys_id_dict(update_dir)
    repository.git.checkout(old_branch)
    old_files = get_class_sys_id_dict(update_dir)

    #Find difference
    deleted_files = ''
    for a_class in old_files.keys():
        for a_file in old_files[a_class]:
            if not exists_in_other_dict(a_class, a_file, latest_files) and not is_delete_allowed(a_class, delete_not_allowed):
                deleted_files += f'https://{instance}.service-now.com/{a_class}.do?sys_id={a_file}\n'

    with open ('Deleted Files.txt', 'w+') as file:
        file.write(deleted_files)