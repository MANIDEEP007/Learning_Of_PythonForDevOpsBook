#Author : Manideep Paduchuri
import fire
'''
About fire
------------------------
Python 3rd Party module
Easy to design command line interface
Better than argparse and click modules
Automatically creates the documentation
'''

#Function to display message based on the option and name inputs - greeting command
def greeting(option="English",name="User"):
  if  option == "Spain":
    print(f"Hola {name} !!" )
  else:
    print(f"Hello {name}!!")

#Function to add 2 numbers - add command
def add(num1,num2):
  print(int(num1) + int(num2))

#Creates interface for our functions as commands
fire.Fire()

#python main.py greeting --option Spain --name Manideep --> Hola Manideep !!
#python main.py add 1 2 --> 3
