#Author : Manideep Paduchuri

'''
About argparser module
----------------------
An Python built-in module
To parse and deal with command line arguments
'''

import argparse
#All arguments passed to Script are strings

#Create argument parser object
arg_paser = argparse.ArgumentParser(description='Demo for Learning')

#Argument not starting with -- are postional arguments
arg_paser.add_argument('First_Num',help="Input First Number")
arg_paser.add_argument('Second_Num',help="Input Second Number")

#Arguments starting with -- means its optional and should use short / long hand option to pass value
arg_paser.add_argument('--Third_Num','-t',help="Provide third number if needed")

#Parse the Arguments - Fails if mandate arguments are not provided
args = arg_paser.parse_args()

#Prints Arguments
print(args.First_Num)
print(args.Second_Num)

#If not provided, it prints None
print(args.Third_Num)

#Calculate the sum
if args.Third_Num == None:
  print(int(args.First_Num) + int(args.Second_Num))
else:
  print(int(args.First_Num) + int(args.Second_Num) + int(args.Third_Num))
