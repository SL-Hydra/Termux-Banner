# Don't Copy This Tools
# If You Copy This Tool ,Your Phone will Hack By Me😈

import os ,shutil ,time ,sys
from time import sleep

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

os.system("clear")

logo = """\033[1;34m
                      █▀█ █░█░█ █▄░█ █▀▀ █▀█
                      █▄█ ▀▄▀▄▀ █░▀█ ██▄ █▀▄\n"""

logo1 = """\033[1;31m
  ███████╗██╗         ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗
  ██╔════╝██║         ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
  ███████╗██║         ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
  ╚════██║██║         ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
  ███████║███████╗    ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
  ╚══════╝╚══════╝    ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝\n"""

delay_print (logo)
delay_print (logo1)

time.sleep (1.0)

os.system ("clear")

logo2 = """\033[1;33m
              █▀▀█  █▀▀█  █▄  █  █▄  █  █▀▀▀  █▀▀█
              █▀▀▄  █▄▄█  █ █ █  █ █ █  █▀▀▀  █▄▄▀
              █▄▄█  █  █  █  ▀█  █  ▀█  █▄▄▄  █  █\n"""

logo3 = """\033[1;32m
               ████████╗░█████╗░░█████╗░██╗░░░░░
               ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
               ░░░██║░░░██║░░██║██║░░██║██║░░░░░
               ░░░██║░░░██║░░██║██║░░██║██║░░░░░
               ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
               ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝\n"""

print (logo2)
time.sleep (1.0)
print (logo3)
time.sleep (1.0)

delay_print ("\033[1;36m		[+] Tool Created By SL Hydra😈\n")
time.sleep (1.0)
print ()

delay_print ("\033[1;33m           [01] Evil Eye Banner              \033[1;32m [+]Animation")
delay_print ("\033[1;33m	             [02] Neofetch Banner              \033[1;32m [+]Animation")
delay_print ("\033[1;33m              	   [03] Colourful Android Logo Banner\033[1;32m [+]Animation")
delay_print ("\033[1;33m  	  	           [04] Letter Banner                \033[1;32m [+]Animation")
delay_print ("\033[1;33m       	            [05] Colourful Letter Banner      \033[1;32m [+]Animation")
print ()

delay_print ("\033[1;33m           [06] UPDATE TOOL")
delay_print ("\033[1;33m                                                  [07] My Telegram Bot")
delay_print ("\033[1;33m                                              [00] Exit\n")


def evil():
	name = str(input("\033[1;33m [+] Enter Your Name : "))
	cs = str(input("\033[1;33m [+] Enter Your Cowsay Name : "))
	speed = str(input("\033[1;33m [+] Enter Speed [50-150] : "))
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = ("cowthink -f eyes "+cs+" |lolcat -a --speed="+speed)
	text2 = ("\nfiglet "+name+" |lolcat -a --speed="+speed)
	text3 = "\ncd"
	with open ("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)

def neo():
	name = str(input("\033[1;33m [+] Enter Your Name : "))
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = "\nneofetch"
	text2 = ("\nfiglet "+name+" |lolcat -a --speed=200")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text)
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)

def android():
	os.system("nano ban")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat ban |lolcat -a --speed=200"
	text3 = "\nneofetch"
	text4 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
		zsh.write(text4)

def only():
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = "\nneofetch"
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text)
		zsh.write(text1)
		zsh.write(text3)

def color():
	os.system("nano ban")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat ban |lolcat -a --speed=200"
	text3 = "\nneofetch |lolcat -a --speed=200"
	text4 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
		zsh.write(text4)

def letter():
	name = str(input("\033[1;33m [+] Enter Your Name : "))
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = ("\ntoilet "+name+" |lolcat -a --speed=200")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)

def letter_f():
	name = str(input("\033[1;33m [+] Enter Your Name : "))
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = ("\ntoilet -f mono12 -F gay "+name+" ")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)

def asici():
	os.system("nano asici")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat asici |lolcat -a --speed=200"
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)

def move_x():
	if os.path.exists("/data/data/com.termux/files/usr/etc/ban"):
		os.remove("/data/data/com.termux/files/usr/etc/ban")
	shutil.move("ban" ,"/data/data/com.termux/files/usr/etc")

def move_a():
	if os.path.exists("/data/data/com.termux/files/usr/etc/asici"):
		os.remove("/data/data/com.termux/files/usr/etc/asici")
	shutil.move("asici" ,"/data/data/com.termux/files/usr/etc")

def move_f():
	if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")

def move_z():
	if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
print ()
cho = int(input("\033[1;33m [+] Enter Your Choice : "))
print ()
if cho == 1 :
	evil()
	move_f()
	print ()
	print ("\033[1;32m [+] Processing....")
	time.sleep (2.0)
	print ()
	print ("\033[1;33m [+] Done")
	time.sleep (1.0)
	print ()
	print ("\033[1;34m [+] Please Restart Termux Or Get A New Session")
	print ()
elif cho == 2 :
	neo()
	move_f()
	print ()
	print ("\033[1;32m [+] Processing....")
	time.sleep (2.0)
	print ()
	print ("\033[1;33m [+] Done")
	time.sleep (1.0)
	print ()
	print ("\033[1;34m [+] Please Restart Termux Or Get A New Session")
	print ()
elif cho == 3 :
	color()
	move_x()
	move_z()
	print ()
	print ("\033[1;32m [+] Processing....")
	time.sleep (2.0)
	print ()
	print ("\033[1;33m [+] Done")
	time.sleep (1.0)
	print ()
	print ("\033[1;34m [+] Please Restart Termux Or Get A New Session")
	print ()
elif cho == 4 :
	letter()
	move_f()
	print ()
	print ("\033[1;32m [+] Processing....")
	time.sleep (2.0)
	print ()
	print ("\033[1;33m [+] Done")
	time.sleep (1.0)
	print ()
	print ("\033[1;34m [+] Please Restart Termux Or Get A New Session")
	print ()
elif cho == 5 :
	letter_f()
	move_f()
	print ()
	print ("\033[1;32m [+] Processing....")
	time.sleep (2.0)
	print ()
	print ("\033[1;33m [+] Done")
	time.sleep (1.0)
	print ()
	print ("\033[1;34m [+] Please Restart Termux Or Get A New Session")
	print ()
elif cho == 6 :
	print ()
	print ("\033[1;32m [+] UPDATING....")
	time.sleep (3.0)
	print ("\033[1;32m [+] Succesfully Updated The Tool🙈")
	time.sleep (2.0)
	os.system ("clear")
	os.system ("python Banner.py")
elif cho == 0 :
	print ("\033[1;32m [+] Thanks For Using...👋")
	time.sleep (1.0)
	exit ()
else :
	print ()
	print ("\033[1;32m [+] Your Choice Is Wrong😠")
	time.sleep (1.0)
	print ("\033[1;32m [+] Restarting....")
	time.sleep (2.0)
	os.system ("python Banner.py")
