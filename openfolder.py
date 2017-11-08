#!/bin/python
'''open given file's parent folder in nautilus '''

import os,sys

if len(sys.argv) < 2:
    exit()

''' get the parameter'''
strFile = str(sys.argv[1])
print ("strFile:", strFile)

'''get the absolute path'''
strPath = os.path.abspath(strFile)
print ("strPath:", strPath)

'''get the parent folder of the file'''
strFolder = os.path.dirname(strPath)
print ("strFolder:", strFolder)

'''open it in nautilus'''
os.system("nautilus " + strFolder)
