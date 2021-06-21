#Author : Manideep Paduchuri

'''Demo for Hierarchial Parsers''''

import argparse

#Main Parser
parser =  argparse.ArgumentParser(description="Demo for hierarchical Parsers")

#Creating sub parser object
subparsers = parser.add_subparsers(dest='func')

#Sub Parser 1
greet_parser = subparsers.add_parser('greet')

#Argument for First Sub Parser
greet_parser.add_argument("name",help="Enter Name")

#Sub Parser 2
ops_parser = subparsers.add_parser("operation")

#Args for Second Sub Parser
ops_parser.add_argument("command",choices=['add','subtract'])
ops_parser.add_argument("First_Num")
ops_parser.add_argument("Second_Num")

args = parser.parse_args()

#python main.py greet Manideep --> Bonjour Manideep
if args.func  == "greet":
  print("Bonjour " + args.name+ "!!")

#python main.py operation add 1 2 --> 3
elif args.func == "operation":
  if args.command == "add":
    print(int(args.First_Num) + int(args.Second_Num))
#python main.py operation subtract 93 26 --> 67
  elif args.command == "subtract":
    print(int(args.First_Num) - int(args.Second_Num))
