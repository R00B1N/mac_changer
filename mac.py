#!/usr/bin/env python
#
# Basic mac changer.
# Coded By Blackster. Copiright all rights reserved.

#importamos los modulos necesarios.
from colorama import Fore, init
import subprocess
import random
import time
import os
init()

banner = """
 /$$      /$$  /$$$$$$   /$$$$$$
| $$$    /$$$ /$$__  $$ /$$__  $$
| $$$$  /$$$$| $$  \ $$| $$  \__/
| $$ $$/$$ $$| $$$$$$$$| $$
| $$  $$$| $$| $$__  $$| $$
| $$\  $ | $$| $$  | $$| $$    $$
| $$ \/  | $$| $$  | $$|  $$$$$$/
|__/     |__/|__/  |__/ \______/

    By Blackster
"""

#creamos la clase para nuestro programa.
class Generador:
    def __init__(self):
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        n0,n1,n2,n3,n4,n5 = random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)
        self.num_gen = (self.numbers[n0],self.numbers[n1],self.numbers[n2],self.numbers[n3],self.numbers[n4],self.numbers[n5])
        l0,l1,l2,l3,l4,l5 = random.randint(0, 6),random.randint(0, 6),random.randint(0, 6),random.randint(0, 6),random.randint(0, 6),random.randint(0, 6)
        self.let_gen = (self.letters[l0],self.letters[l1],self.letters[l2],self.letters[l3],self.letters[l4],self.letters[l5])
        self.waiting = "Generando MAC..."
        self.i = 0
        while self.i <= 3:
            time.sleep(1)
            print(self.waiting)
            self.i += 1
            if self.i == 3:
                break
        print(Fore.GREEN)
        self.convert1 = ("Direccion MAC Generada: {}{}:{}{}:{}{}:{}{}:{}{}:{}{}".format(self.numbers[n0],self.numbers[n1],self.numbers[n2],self.numbers[n3],self.letters[l0],self.numbers[n4],self.letters[l1],self.letters[l2],self.numbers[n5],self.numbers[n3],self.numbers[n2],self.letters[l3]))
        print(self.convert1)
        input("\nCopie esta MAC para guardarla y cambiar su MAC (opcional. puede establecerla a su gusto.)")
        pass

#creamos nuestra clase para setear nuestra mac o cambiarla.
class Changer:
    def __init__(self):
        pass

    def down_set(self):
        print(Fore.YELLOW)
        ask_by = int(raw_input("Escoge el tipo de interfaz que deseas cambiar: \n1-eth0.\n2-wlan0.\n3-Introducir manualmente.\n >>> "))
        if ask_by==1:
            interface = "eth0"
            subprocess.call("sudo ifconfig {} down".format(interface), shell=True)
            mac = raw_input("Introduce tu MAC nueva aqui >> ")
            print("Cambiando MAC...")
            time.sleep(3)
            subprocess.call("sudo ifconfig eth0 hw ether {}".format(mac), shell=True)
            subprocess.call("sudo ifconfig eth0 up", shell=True)
            print(Fore.MAGENTA)
            print("Su direccion MAC en la interfaz eth0 ha sido cambiada a --> {}".format(mac))
            raw_input("\nPresione enter...")
            pass
        elif ask_by==2:
            interface = "wlan0"
            subprocess.call("sudo ifconfig {} down".format(interface), shell=True)
            mac = raw_input("Introduce tu MAC nueva aqui >> ")
            print("Cambiando MAC...")
            time.sleep(3)
            subprocess.call("sudo ifconfig wlan0 hw ether {}".format(mac), shell=True)
            subprocess.call("sudo ifconfig wlan0 up", shell=True)
            print(Fore.MAGENTA)
            print("Su direccion MAC en la interfaz wlan0 ha sido cambiada a --> {}".format(mac))
            input("\nPresione enter...")
            pass
        else:
            if ask_by==3:
                interface = raw_input("Introduce tu interfaz aqui (ejemplo: eth0): ")
                subprocess.call("sudo ifconfig {} down".format(interface), shell=True)
                mac = raw_input("Introduce tu MAC nueva aqui >> ")
                try:
                    print("Cambiando MAC...")
                    time.sleep(3)
                    subprocess.call("sudo ifconfig {} hw ether {}".format(interface, mac), shell=True)
                    subprocess.call("sudo ifconfig {} up".format(interface), shell=True)
                    print(Fore.MAGENTA)
                    print("Su direccion MAC en la interfaz {} ha sido cambiada a --> {}".format(interface, mac))
                    raw_input("\nPresione enter...")
                    pass
                except:
                    print("Se ha producido un error al intentar cambiar su direccion MAC")




def Menu():
    os.system('clear')
    print(Fore.GREEN)
    print(banner)
    print("Script que genera direcciones y cambia tu direccion MAC.")
    menu = """
///////  Menu ///////
1->> Generador de MAC.
2->> Cambiar Direccion MAC.

99->> Salir.
    """
    print(Fore.CYAN)
    print(menu)

if __name__=="__main__":
    os.system('sudo mac.py')
    while True:
        Menu()
        ask = int(raw_input("Escoge una opcion >>> "))
        if ask==1:
            generar = Generador()
        elif ask==2:
            chng = Changer()
            chng.down_set()
        else:
            if ask==99:
                print("See you...")
                break
