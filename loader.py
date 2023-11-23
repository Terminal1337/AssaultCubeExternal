from pymem import *
from pymem.process import *
from colorama import Fore
import os
import pyfiglet
pm = pymem.Pymem('ac_client.exe')
ac_module = module_from_name(pm.process_handle,'ac_client.exe').lpBaseOfDll
def getptr(base,offsets):
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr+i)
        
    return addr + offsets[-1]

def health():
    while True:
        pm.write_int(getptr(ac_module+ 0x00183828,[0x8,0x9F8,0x30,0x98,0x9D8]),100)

def ammo():
    pm.write_int(getptr(ac_module+ 0x001A3344,[0x4,0x64,0x98,0x30,0x68,0x7E0]),val)

def Unlimited_ammo():
    while True:
        pm.write_int(getptr(ac_module+ 0x001A3344,[0x4,0x64,0x98,0x30,0x68,0x7E0]),9999)


print(Fore.LIGHTCYAN_EX+pyfiglet.figlet_format("AssasultTrainer")+Fore.RESET)
os.system('title Assault Cube Trainer Beta v0.1 [Main-Menu] Support : Terminal')
print(Fore.LIGHTMAGENTA_EX+'[1] Change Ammo Count'+Fore.RESET)
print(Fore.LIGHTMAGENTA_EX+'[2] Unlimited Health '+Fore.RESET)
print(Fore.LIGHTMAGENTA_EX+'[3] Unlimited Ammo \n'+Fore.RESET)
val_in = int(input(Fore.LIGHTBLUE_EX+"Option [>] "+Fore.RESET))
if val_in == 1:
    val = int(input(Fore.LIGHTBLUE_EX+'Enter the ammo count [>] '+Fore.RESET))
    print(Fore.GREEN+"Cheat Activated Successfully!!"+Fore.RESET)
    ammo()
    
if val_in == 2:
    print(Fore.GREEN+"Cheat Activated Successfully!!"+Fore.RESET)
    health()
    
if val_in == 3:
    print(Fore.GREEN+"Cheat Activated Successfully!!"+Fore.RESET)
    Unlimited_ammo()


