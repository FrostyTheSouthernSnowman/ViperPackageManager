#!/usr/bin/env python3

from pyfiglet import Figlet
from simple_chalk import chalk, cyan
import inquirer
from halo import Halo
import time

print("🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍")
f = Figlet(font='slant')
print(cyan(f.renderText('Viper Package Manager')))
print("🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍")
print("\n\n\n")
print("Thank you for install Viper Package Manager (VPM)")

addToPath = [
    inquirer.Text(
        'add to path', message="Would you like to add Viper Package Manager (VPM) to path? (y/n/q)"),
]
answer = inquirer.prompt(addToPath)
if answer['add to path'] == "y":
    with Halo(text='Loading', spinner='dots'):
        time.sleep(5)
    print("Viper Package Manager successfully installed! 🐍")
elif answer['add to path'] == "n":
    pass
elif answer['add to path'] == "q":
    quit()
