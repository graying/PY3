#!/bin/python
'''open given file's parent folder in nautilus '''

import os, sys, logging

if len(sys.argv) < 2:
    exit()

logging.basicConfig(filename='openfolder.log', filemode='w', level=logging.INFO)

''' get the parameter'''
strFile = str(sys.argv[1])
logging.info("strFile: " + strFile)

'''get the absolute path'''
strPath = os.path.abspath(strFile)
logging.info("strPath: " + strPath)

'''get the parent folder of the file'''
strFolder = os.path.dirname(strPath)
logging.info("strFolder: "+ strFolder)

'''open it in nautilus'''
os.system("nautilus " + strFolder)
