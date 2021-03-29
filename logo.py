from pyfiglet import *
from termcolor import colored
from random import randint



# font or style you can use
font = ['slant', "3-d", "3x5", "5lineoblique",
        "alphabet", "banner3-D", "doh", "isometric1", "letters",
        "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]


# Here is some valid colors that we can use to color our art
valid_color = ('red', 'green', 'yellow', 'blue', 'cyan', 'white')
msg = 'Z A F I'
color = 'cyan'



ascii_art = figlet_format(msg, font='3-d')

colored_ascii = colored(ascii_art, color)

print(colored_ascii,end=" ")