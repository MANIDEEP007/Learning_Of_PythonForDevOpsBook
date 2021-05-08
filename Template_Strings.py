from string import Template

#Create Template String - Used for Internalization
greet = Template("$Hello World")

#Substitute Hello with Hola - Spanish
print(greet.substitute(Hello="Hola"))

#Substitute Hello with Hola - French
print(greet.substitute(Hello="Bonjour"))

#Substitute Hello with Ola - Portugese
print(greet.substitute(Hello="Ola"))

'''
Output:
~~~~~~~~~

Hola World
Bonjour World
Ola World
'''
