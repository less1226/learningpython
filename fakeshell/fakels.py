#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re


def ls(inputStr=''):
    current_path = os.getcwd()
    print('Current path is %s' % current_path)
    # 将所有命令转成list
    commands = inputStr.split()
    all_list = os.listdir()
    # 处理-a命令，如果没有-a，需要隐藏.目录
    if '-a' not in commands:
        all_list = [l for l in all_list if not l.startswith('.')]
    else:
        commands.remove('-a')

    for command in commands:
        if command == '-r':
            all_list.reverse()
        elif command == '-t':
            dictnory = []
            for l in all_list:
                file_path = os.path.join(current_path, l)
                create_time = os.path.getctime(file_path)
                dictnory.append((l, create_time))
            all_list = process_tcommand(dictnory)
        elif command == '-F':
            for index, value in enumerate(all_list):
                if os.path.isfile(value):
                    all_list[index] = value + '*'
                elif os.path.isdir(value):
                    all_list[index] = value + '/'
        elif command == '-R':
            path_dict = {}
            path_dict[current_path] = all_list
            process_Rcommand(all_list, path_dict)
        elif command == '-s':
            size_dict = {}
            for l in all_list:
                if os.path.isdir(l):
                    size_dict[l] = 0
                elif os.path.isfile(l):
                    size_dict[l] = os.path.getsize(l)
            size_list = sorted(size_dict.items(),
                            key=lambda x: x[1],
                            reverse=True)
        else:
            if os.path.isfile(command):
                all_list.clear()
                all_list.append(command)
            elif os.path.isdir(command):
                all_list.clear()
                all_list = os.listdir(command)
            elif '*' in command or '?' in command:
                r = command
                if command.startswith(r'*'):
                    r = r.replace(r'*', r'[0-9a-zA-Z]+')
                r = r.replace(r'*', r'[0-9a-zA-Z]*')
                r = r.replace(r'?', r'[0-9a-zA-Z]+')
                r = '^%s$' % r
                re_match = re.compile(r)
                temp_list = [x for x in all_list if re.match(r, x)]

                all_list.clear()
                for t in temp_list:
                    all_list.append(os.listdir(t))
                    all_list.append('\n')

    # 输出处理好的目录信息
    if '-R' in commands:
        for key, value in path_dict.items():
            print(key, end=':\n')
            for n in value:
                print(n)
            print('\n')
    elif '-s' in commands:
        print('total: %s' % (sum([i[1] for i in size_list])))
        for l in size_list:
            print('%s %s' % (l[1], l[0]), end='\n')
    else:
        for l in all_list:
            print(l)


def process_tcommand(all_list_dict):
    all_list_dict.sort(key=lambda x: x[1], reverse=True)
    return [y[0] for y in all_list_dict]


def process_Rcommand(r_all_list, process_dict):
    next_list = [l for l in r_all_list if os.path.isdir(l)]
    for n in next_list:
        process_dict[os.path.abspath(n)] = os.listdir(n)
        process_Rcommand(os.listdir(n), process_dict)
    return process_dict


if __name__ == "__main__":
    commands = input('Please input ls command:')
    ls(commands)