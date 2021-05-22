#Author : Manideep Paduchuri
'''
About pathlib
--------------------
An Pythob built-in module
Used to represent file systems
Used to perform IO operations
'''
import pathlib

#Create a pathlib object
path_obj = pathlib.Path("sample.txt")

#Read entire text file content as a string
print(path_obj.read_text())

#Create a pathlib object
path_obj = pathlib.Path("Sample.pdf")

#Reading other files using pathlib
print(path_obj.read_bytes())
