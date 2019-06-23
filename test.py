#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/12 19:31
# @Author : LiFH
# @Site : 
# @File : test.py
# @Software: PyCharm Community Edition
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

filename = 'labels_1.txt'
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split(',')
        print line[0],line[1],line[2]
        # filename = u'{0}/{1}/{2}.jpg'.format(line[0].decode('ascii'),line[1].decode('ascii'), line[2].decode('ascii'))
        filename = u'{0}/{0}/{0}.jpg'.format(line[3])
        print filename