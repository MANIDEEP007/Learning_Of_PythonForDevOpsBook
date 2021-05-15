#Author : Manideep Paduchuri

'''
About cryptography
-------------------
Python 3rd party library
To install it use pip install cryptography
Used in encryption and decryption of messages
This code - Demonstrates Symmetric Encryption
'''

from cryptography.fernet import Fernet

#Generating random key to be used for Fernet(Implementation of AES) algorithm
key = Fernet.generate_key()

#Create object of Fernet object with key generated in above step
fernet_obj = Fernet(key)

#Sample message
message = b"Hello World!!"

#Encrypt message
encrypted_msg = fernet_obj.encrypt(message)

#Print Encrypted message
print(encrypted_msg)

#Decrypt message
original_msg = fernet_obj.decrypt(encrypted_msg)

#Print Original message decrypted using Fernet algorithm
print(original_msg)
