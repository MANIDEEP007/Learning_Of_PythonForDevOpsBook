#Author : Manideep Paduchuri
import fire

#Class to group Arithmetic Operations commands
class Arith:
  def add(self,num1,num2):
    print(int(num1) + int(num2))
  def sub(self,num1,num2):
    print(int(num1) - int(num2))
  def mul(self,num1,num2):
    print(int(num1) * int(num2))
  def div(self,num1,num2):
    print(int(num1) // int(num2))

#Class to group greeting related commands
class greet:
  def english(self,name):
    print(f"Hello {name}")
  def spain(self,name):
    print(f"Hola {name}")
  def french(self,name):
    print(f"Bonjour {name}")

#Create Command line interface from Classes
fire.Fire()
#python main.py Arith add 1 2 --> 3
#python main.py Arith mul 62 2 --> 124
#python main.py greet english Manideep --> Hello Manideep
#python main.py greet english Manideep --> Bonjour Manideep
