import os
import hashlib
import argparse
from termcolor import colored


def dups_size(root_folder):

    dups_size = {}
    for dir_name, subdir, fileList in os.walk(root_folder):
        for file in fileList:
            file_path = os.path.join(dir_name, file)
            file_size = os.path.getsize(file_path)
            if file_size in dups_size:
                dups_size[file_size].append(file_path)
            else:
                dups_size[file_size] = [file_path]
    return dups_size


def dups_hash(same_size_list):

    dups_hash = {}
    for file_path in same_size_list:
        file_hash = hash_file(file_path)
        if file_hash in dups_hash:
            dups_hash[file_hash].append(file_path)
        else:
            dups_hash[file_hash] = [file_path]
    return dups_hash


def hash_file(file_path, size_block=1024*1024):

    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as afile:
        chunk = afile.read(size_block)
        while len(chunk) > 0:
            hash_obj.update(chunk)
            chunk = afile.read(size_block)
    return hash_obj.hexdigest()


def get_dups(root_folder):

    dups = []
    for file_size, file_list in dups_size(root_folder).items():
        if len(file_list) > 1:
            for file_hash, file_paths in dups_hash(file_list).items():
                if len(file_paths) > 1:
                    dups.append(file_paths)
    return dups


def print_dups():

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_folder')
    args = parser.parse_args()
    if os.path.exists(args.path_to_folder):
        dups = get_dups(args.path_to_folder)
        if len(dups) == 0:
            print('No duplicates found!')
        else:
            print("Following duplicates were found:\n")
            for dups_list in dups:
                print(colored(
                    "\nDuplicates of {}:".format(
                        os.path.basename(
                            dups_list[0])),'green'))
                for item in dups_list:
                    print(item)
    else:
        raise ValueError("Incorrect path")


if __name__ == '__main__':
    print_dups()
