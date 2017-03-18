import os
import hashlib
import argparse
from termcolor import colored


def get_sizes_of_files(root_folder):

    sizes_of_files = {}
    for dir_name, subdir, file_list in os.walk(root_folder):
        for file in file_list:
            file_path = os.path.join(dir_name, file)
            file_size = os.path.getsize(file_path)
            if file_size in sizes_of_files:
                sizes_of_files[file_size].append(file_path)
            else:
                sizes_of_files[file_size] = [file_path]
    return sizes_of_files


def get_same_hash_files(same_size_list):

    same_hash_files = {}
    for file_path in same_size_list:
        file_hash = get_hash_file(file_path)
        if file_hash in same_hash_files:
            same_hash_files[file_hash].append(file_path)
        else:
            same_hash_files[file_hash] = [file_path]
    return same_hash_files


def get_hash_file(file_path, size_block=1024 * 1024):

    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as afile:
        chunk = afile.read(size_block)
        while len(chunk) > 0:
            hash_obj.update(chunk)
            chunk = afile.read(size_block)
    return hash_obj.hexdigest()


def get_dups_for_size(same_size_list):

    dups_for_size = []
    for file_hash, file_paths in get_same_hash_files(same_size_list).items():
        if len(file_paths) > 1:
            dups_for_size.append(file_paths)
    return dups_for_size


def get_dups(root_folder):

    dups = []
    for file_size, file_list in get_sizes_of_files(root_folder).items():
        if len(file_list) > 1:
            dups += get_dups_for_size(file_list)
    return dups


def print_dups(dups):

    if not dups:
        print('No duplicates found!')
    else:
        print("Following duplicates were found:\n")
        for dups_list in dups:
            print(colored(
                "\nDuplicates of {}:".format(
                    os.path.basename(
                        dups_list[0])), 'green'))
            for item in dups_list:
                print(item)


def load_dups():

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_folder')
    args = parser.parse_args()
    if os.path.exists(args.path_to_folder):
        return get_dups(args.path_to_folder)
    else:
        raise ValueError("Incorrect path")


if __name__ == '__main__':

    dups = load_dups()
    print_dups(dups)
