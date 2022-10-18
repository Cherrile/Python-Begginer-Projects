import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW + "Hi My name is Tina Masha" +
      Fore.YELLOW + Back.Blue + ", I am your Machine Learning Instructor")
print(Back.CYAN + "Hi my name is Tina Masha")
print(Fore.RED+Back.GREEN + " Hi My name is Tina Masha")


# wont work for windows operating systems
