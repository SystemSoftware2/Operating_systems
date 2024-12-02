from tqdm import tqdm
import keyboard
import os
import time

mylist = [1,2,3,4,5,6,7,8]

for i in tqdm(mylist):
    time.sleep(1)

os.system('cls')

def root():
    print('   $#                 #?')
    print('   ##                 ##')
    print('T - Terminal         I - Info')

    def terminal():
        os.system('cls')
        print('#Terminal##############')
        while True:
            d = input('Command (off - exit): ')

            if d != 'off':
                os.system(d)
            if d == 'off':
                os.system('cls')
                break
        root()

    def information():
        os.system('cls')
        print('#Info###############')
        print('PyOS 1.0.')
        print('Memory: 512KB')
        print('Q - Exit')

        keyboard.wait('Q')
        os.system('cls')
        root()
    
    while True:
        a = keyboard.read_key()
        if a == 't' or a == 'T':
            terminal()

        if a == 'i' or a == 'I':
            information()

root()