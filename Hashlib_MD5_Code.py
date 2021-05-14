#Author : Manideep Paduchuri
'''
About hashlib
-----------------
An Python built-in module
Supports variuous hash & message digest algorithms
'''
import hashlib

#Sample Message
message = "Hello World!! Welcome to Programming"

#Turn message into binary string if its a string
bmessage = message.encode()

#Create Hash object of MD5 algorithm
hash_obj = hashlib.md5()

#Add digest to message
hash_obj.update(bmessage)

#Print digest to be used
print(hash_obj.digest())
