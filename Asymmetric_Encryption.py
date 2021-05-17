#Author : Manideep Paduchuri
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#Create Private Key - Provide exponent, Key Size, Backend object
private_key = rsa.generate_private_key(
               public_exponent = 65537, #Should be 3 or 65537
               key_size        = 4096,
               backend         = default_backend()
              )

#Create Public Key
public_key = private_key.public_key()

#Sample Message in Bytes
message = b"Hello World!! Welcome to Programming"

#Encrypt Message using Private Key & Optimal Asymmetric Encryption Padding
enc_msg = public_key.encrypt(
          message,
          padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
            )
          )

#Decrypt the message using corresponding public key of the private key used
dec_msg = private_key.decrypt(
          enc_msg,
          padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
            )
          )

print(dec_msg)# b'Hello World!! Welcome to Programming'
