#Author : Manideep Paduchuri

'''
About subprocess module
----------------------
An Python built-in module
Used to spawn processes/pipes and process output
'''
import subprocess
process_obj = subprocess.run(
                  ["ls","-l"],
                  capture_output=True, #Store output
                  universal_newlines=True #For Formatting of \n to newlines
              )
print(process_obj.stdout) #Print stored success output of the executed command

process_obj = subprocess.run(
                  ["ls","-l","Random_File"],
                  capture_output=True, #Store output
                  universal_newlines=True, #For Formatting of \n to newlines
              )
print(process_obj.stderr) #Print stored error output of the executed command

try:
    process_obj = subprocess.run(
                  ["ls","-l","Random_File"],
                  capture_output=True, #Store output
                  universal_newlines=True, #For Formatting of \n to newlines
                  check=True #In case of failure, throws an exception
              )
    #In case of success print output
    print(process_obj.stdout) #Print stored output of the executed command
#Print Exception in case of any errors
except Exception as e:
    print(e)
