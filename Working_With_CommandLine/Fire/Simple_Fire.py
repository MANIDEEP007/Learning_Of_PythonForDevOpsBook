#Author : Manideep Paduchuri\
import fire
'''
About fire
------------------------
Python 3rd Party module
Easy to design command line interface
Better than argparse and click modules
Automatically creates the documentation
'''

#Function to display message based on the option and name inputs
def greeting(option="English",name="User"):
  if  option == "Spain":
    print(f"Hola {name} !!" )
  else:
    print(f"Hello {name}!!")

#Creates interface for our greeting function
fire.Fire(greeting)

#python main.py --option Spain --name Manideep --> Hola Manideep !!
#python main.py --name Manideep --> Hello Manideep!!
