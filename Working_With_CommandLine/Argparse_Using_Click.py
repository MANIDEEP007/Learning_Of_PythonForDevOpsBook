#Author : Manideep Paduchuri
import click

'''
About click Module
--------------------------
Third party Python library
Easy to design command line interface
'''

#Main Group
@click.group(help = "Custom Command Line interface")
def custom_cli():
  pass

#Sub group1 of main group
@click.group(help="Greeting Related commands")
def greeting():
  pass

#Sub group2 of main group
@click.group(help="Operation Related commands")
def operation():
  pass

#Add greeting and operation group to custom_cli
custom_cli.add_command(greeting)
custom_cli.add_command(operation)

#Add greet command to greeting group
@greeting.command(help="Pass Name as argument")
#Add option to greet command
@click.option("--option", default="English")
#Add argument to greet command
@click.argument('name')
def greet(option,name):
  if option == "Spain":
    print("Hola " + name)
  else:
    print("Hello " + name)

#Add perform command to operation group
@operation.command(help="Pass 2 numbers as arguments")
#Add option to perform command
@click.option("--arith", default="add")
#Add argument to perform command
@click.argument('first_num')
@click.argument('second_num')
def perform(arith,first_num,second_num):
  if arith == "sub":
    print(int(first_num) - int(second_num))
  else:
    print(int(first_num) + int(second_num))

#Create object for main group
custom_cli()

#python main.py greeting greet Manideep --> Hello Manideep
#python main.py greeting greet --option Spain  Manideep --> Hola Manideep
#python main.py operation perform 1 2 --> 3
#python main.py operation perform --arith sub 3 2 --> 1
