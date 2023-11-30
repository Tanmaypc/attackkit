#!/usr/bin/env python3

import functionsall
import sys

## main menu 

print("""

BANNER : **************************
         *******  WELCOME  ********
         $$$$   TO WIRELESS  $$$$$$
         $$  PROBE AND ATTACKIT $$$
         $$$$$$$$$$$$$$$$$$$$$$$$$$
      

MAIN MENU -> 
      
      Type the letter for selectin the option 

      1) I (for SSID sniffing)
      2) H (for Acess point )
      3) Y (for deauth-attack )
      4) L (You get 1000 rs )
      5) E (to exit the tool (pls dont!))

"""
)

inputletter = input("Choose what you wanna do: ") 

if(inputletter.lower()=='i'):
    functionsall.ssidsniff()

if(inputletter.lower()=='h'):
    functionsall.acesspnt()

if(inputletter.lower()=='y'):
    functionsall.deautattack()

if(inputletter.lower()=='l'):
    print("HaH ! you thought !")

#have to make an exit function now -> 

if(inputletter.lower()=='e'):
    sys.exit()




