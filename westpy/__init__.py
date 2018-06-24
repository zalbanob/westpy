from __future__ import print_function

from westpy.units import * 
from westpy.utils import * 
from westpy.atom import * 
from westpy.geometry import * 
from westpy.groundState import * 

__version__ = '3.1.0'

def header() :
   """Prints welcome header."""
   import datetime
   print(" ")
   print(" _    _ _____ _____ _____            ")
   print("| |  | |  ___/  ___|_   _|           ")
   print("| |  | | |__ \ `--.  | |_ __  _   _  ")
   print("| |/\| |  __| `--. \ | | '_ \| | | | ")
   print("\  /\  / |___/\__/ / | | |_) | |_| | ")
   print(" \/  \/\____/\____/  \_/ .__/ \__, | ")
   print("                       | |     __/ | ")
   print("                       |_|    |___/  ")
   print(" ")
   print("WEST version     : ",__version__)
   print("Today            : ", datetime.datetime.today())

header()
