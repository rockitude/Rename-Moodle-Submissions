#!/usr/bin/env python

import os
import sys
from zipfile import ZipFile
import shutil
# import webbrowser

# argument 1 - location of files to be renamed
# argument 2 - assignment title

# set location of files to be renamed
filePath = sys.argv[1]
# set assignment name
assignmentName = sys.argv[2]

def delEmptyHtml(filename):
	# if this is an html file, detect whether it contains a URL
	if "html" in filename:
		htmlPath = os.path.join(filePath, filename)
		contents = open(htmlPath, 'r').read()
		if "http" not in contents:
			os.remove(htmlPath)

def renameFile(filename):
	# set starting current file name
	lastFile = None;

	# if the file isn't hidden and has an underscore (from Moodle)
	if (not filename.startswith(".")) and ("_" in filename):
		# determine file extension
		if "." in filename:
			fileExtension = filename[filename.index(".") + 1:]
		if fileExtension:
			# build new file name if there's an extension
			newFileName = filename[:filename.index("_")] + " - " + assignmentName + "." + fileExtension
		else:
			# build new folder name
			newFileName = filename[:filename.index("_")] + " - " + assignmentName
		# check if the current file name is the same as the last one
		if lastFile is newFileName:
			newFileName = ' '.join(newFileName, 2)
		# remember the current file name
			lastFile = newFileName
		# change file or folder's name
		oldPath = os.path.join(filePath, filename)
		newPath = os.path.join(filePath, newFileName)
		# print("Renaming " + oldPath + " to " + newPath)
		os.rename(oldPath, newPath)

fileList = os.listdir(filePath)

for filename in fileList:
	delEmptyHtml(filename)

fileList = os.listdir(filePath) # make new file list; some files were likely deleted

for filename in fileList:
	renameFile(filename)

	# if this is a zip file, figure out how to open it and rename the result
	# if "zip" in filename:
	# 	# store path to zip
	# 	zipPath = os.path.join(filePath, filename)