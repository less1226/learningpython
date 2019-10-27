#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def ls(inputStr=''):
    current_path = os.getcwd()
    print('Current path is %s' % current_path)
    commands=inputStr.split(' ')
    all_list = os.listdir()
    for command in commands:
        if not command == '-a':
            all_list = [l for l in all_list if not l.startswith('.')]
        if command == '-r':
            all_list.reverse()

    for l in all_list:
        print(l)

if __name__ == "__main__":
    commands = input('Please input ls command:')
    ls(commands)