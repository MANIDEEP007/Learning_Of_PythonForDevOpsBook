#Author : Manideep Paduchuri

'''
About os module
----------------------
An Python built-in module
Used in dealing with OS related aspects
'''

import os

#Get current working directory
print(os.getcwd())

#Change to another directory relative to current path
os.chdir("Sample")
print(os.getcwd()) #/home/runner/ColorfulArtisticBloatware/Sample

#Get the value of environment variable PATH
print(os.environ.get("PATH"))

#Set the new environment variable name to PADUCHURI MANIDEEP - Scope is limited to process spawned in this program
os.environ["name"] = "PADUCHURI MANIDEEP"
print(os.environ.get("name")) #PADUCHURI MANIDEEP
