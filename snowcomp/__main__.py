from git import Repo
import xml.etree.ElementTree as ET
import os, json

def get_config():
    with open('conf.json', 'r') as conf_file:
        conf_json = conf_file.read()
        json_conf = json.loads(conf_json)
    return json_conf['username'], json_conf['password'], json_conf['git_repo_link'], json_conf['latest_branch'], json_conf['old_branch'], json_conf['clone_dir'], json_conf['instance_of_old_app'], json_conf['ignore_deletions']

def read_file(file_path):
    root = ET.parse(file_path).getroot()
    class_sys_id_dict = {}
    for x in root:
        if x.find('sys_id') != None:
            if not (str(x.tag) in class_sys_id_dict):
                class_sys_id_dict[str(x.tag)] = [x.find('sys_id').text]
            else:
                class_sys_id_dict[str(x.tag)].append(x.find('sys_id').text)
    return class_sys_id_dict

def get_class_sys_id_dict(update_dir):
    class_sys_id_dict = {}

    for each_file in os.listdir(update_dir):
        temp_dict = read_file(os.path.join(update_dir, each_file))
        for class_name in temp_dict.keys():
            if not (class_name in class_sys_id_dict):
                class_sys_id_dict[class_name] = temp_dict[class_name]
            else:
                class_sys_id_dict[class_name] += temp_dict[class_name]

    return class_sys_id_dict

def exists_in_other_dict(class_name, file_name, all_files):
    return (class_name in all_files) and (file_name in all_files[class_name])

def is_ignored(class_name, ignored):
    return class_name in ignored

if __name__ == '__main__':
    try:
        username, password, repo_link, latest_branch, old_branch, clone_path, instance, ignore_deletions = get_config()
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
                if not exists_in_other_dict(a_class, a_file, latest_files) and not is_ignored(a_class, ignore_deletions):
                    deleted_files += f'https://{instance}.service-now.com/{a_class}.do?sys_id={a_file}\n'

        with open ('Deleted Files.txt', 'w+') as file:
            file.write(deleted_files)
    except Exception as ex:
        print (ex)