#Author : Manideep Paduchuri
'''
PyYaml is 3rd party library
USe pip install PyYaml to install the library
Used to read and write YAML files
YAML files used in network configuration
One use case is using YAML file for software configuration automation
'''

import yaml

#Create a file obj
file_obj = open("employee.yaml")

#Pass object to YAML load function - Converts YAML content to dict
employee_data = yaml.safe_load(file_obj)

#Read the content of the YAML file & Print specific details
print(employee_data['Name'])

#Modifying data
employee_data['Name'] = 'Rajesh'

#Create a file object for new YAML file
mod_file_obj = open("employee_modified.yaml","w")

#Use Sagfe Dump to store modified content(dictionary) to new YAML file
#Use sort_keys as False to prevent sorting of keys
yaml.safe_dump(employee_data, mod_file_obj,sort_keys=False)
