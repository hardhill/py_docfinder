#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import re
import sys
import argparse



def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type',choices=['pdf', 'epub', 'djvu','txt','doc','rtf'], default='pdf')
    parser.add_argument('-p','--path',default='/home')

    return parser


parser = createParser()
names= parser.parse_args(sys.argv[1:])

extension = names.type
next = len(extension)*-1
path = names.path

dir = path

for root, dirs, files in os.walk(dir): # пройти по директории рекурсивно
    for name in files:
        fullname = os.path.join(root, name) # получаем полное имя файла
        subs = fullname[next:].lower()
        if subs==extension:
            print(fullname)
print('usage: docfinder -t [pdf] ')
print('where -t is parameter as type extansion file. Forexample "docfinder -t pdf" (without <\">)')
