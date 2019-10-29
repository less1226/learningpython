#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def ls(inputStr=''):
    current_path = os.getcwd()
    print('Current path is %s' % current_path)
    #将所有命令转成list
    commands=inputStr.split()
    all_list = os.listdir()
    #处理-a命令，如果没有-a，需要隐藏.目录
    if '-a' not in commands:
        all_list = [l for l in all_list if not l.startswith('.')]
    else:
        commands.remove('-a')
    
    for command in commands:
        if command == '-r':
            all_list.reverse()
        if command == '-t':
            dictnory=[]
            for l in all_list:
                file_path = os.path.join(current_path,l)
                create_time = os.path.getctime(file_path)
                dictnory.append((l,create_time))
            all_list = process_tcommand(dictnory)

    #输出处理好的目录信息
    for l in all_list:
        print(l)

def process_tcommand(all_list_dict):
    all_list_dict.sort(key=lambda x:x[1], reverse = True)
    return [y[0] for y in all_list_dict]


if __name__ == "__main__":
    commands = input('Please input ls command:')
    ls(commands)