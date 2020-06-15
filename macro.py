from pynput.keyboard import Key, Controller #imports pynput, keyboard and controller
import random #imports random for random numbers, so dank memer doesnt detect the macro.
import time #imports time
from multiprocessing import Process
import sys
from threading import Thread

#declares golobal variable
keyboard = Controller()

nerd = ['n','e','r','d']
#random time generators
class random_genrator:
    random_number_depall = random.choice([2 , 2.25, 2.5, 2.75 ])
    number_1sec = random.choice([1 , 1.25, 1.5, 1.75 ])
    number_3sec = number_1sec = random.choice([3 , 3.25, 3.5, 3.75 ])
    random_number_plsbeg = random.choice([40,40.2, 40.25, 40.1 , 40.3, 40.35, 40.32, 40.42, 40.35,41.2])
    random_number_plsfish =  random.choice([45.21, 45.1, 45.23, 45.24, 45.45, 45.6])
    random_nerd_picker = random.choice(['n','e','r','d'])
    random_number_postmeme =  random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])
    random_sell_time =  random.choice([30.21, 30.1, 30.23, 30.24, 30.45, 30.6])
    random_selltime1 =  random.choice([20.21, 20.1, 20.23, 20.24, 20.45, 20.6])
    random_buytime =  random.choice([32.21, 32.1, 32.23, 32.24, 32.45, 32.6])
    random_laptop_buyer = random.choice([60.21*60, 60.1*60, 60.23*60, 60.24*60, 60.45*60, 60.6*60])
    nerd_randomselector = random.choice(nerd)

class nerdnibba():
    def nibba():
        while True:
            lol = random.choice(nerd)
            time.sleep(.5)
            keyboard.type(lol)

def pls_beg():
    while True:
        time.sleep(random_genrator.number_1sec+8)
        keyboard.type('pls beg ') #type pls beg
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)#simulates the press of the enter key
        time.sleep(random_genrator.random_number_plsbeg) #waits 40 - 42.5

def postmeme():
    time.sleep(.5)
    while True:
        lol = random.choice(nerd)
        keyboard.type('pls postmeme')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_genrator.number_1sec)
        keyboard.type(lol)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_genrator.random_number_postmeme)

def hunt():
    while True:
        time.sleep(random_genrator.random_number_depall*8)
        keyboard.type('pls hunt')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_genrator.random_number_postmeme*5)



def fishing():
    while True:
        time.sleep(random_genrator.number_1sec*5)
        keyboard.type('pls fish')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_genrator.random_number_plsfish*10)

def laptopbuyer():
    while True:
        time.sleep(random_genrator.random_buytime*30)
        keyboard.type('pls withdraw 1500')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_genrator.number_1sec)
        keyboard.type('pls buy laptop')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

class inventory_sell:
    def sell_pill():
        while True:
            time.sleep(random_genrator.random_sell_time * 60)
            keyboard.type('pls sell chillpill all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_fish():
        while True:
            time.sleep(random_genrator.random_sell_time * 27)
            keyboard.type('pls sell fish all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


    def sell_bread():
        while True:
            time.sleep(random_genrator.random_selltime1 * 23)
            keyboard.type('pls sell bread all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_candy():
        while True:
            time.sleep(random_genrator.random_selltime1 * 30)
            keyboard.type('pls sell candy all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_alcohol():
        while True:
            time.sleep(random_genrator.random_selltime1 * 45)
            keyboard.type('pls sell alcohol all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_cookie():
        while True:
            time.sleep(random_genrator.random_selltime1 * 25)
            keyboard.type('pls sell cookie all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_rabbit():
        while True:
            time.sleep(random_genrator.random_selltime1 * 65)
            keyboard.type('pls sell rabbit all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_duck():
        while True:
            time.sleep(random_genrator.random_selltime1 * 55)
            keyboard.type('pls sell duck all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_skunk():
        while True:
            time.sleep(random_genrator.random_selltime1 * 35)
            keyboard.type('pls sell skunk all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_boar():
        while True:
            time.sleep(random_genrator.random_selltime1 * 69)
            keyboard.type('pls sell boar all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def sell_deer():
        while True:
            time.sleep(random_genrator.random_selltime1 * 23)
            keyboard.type('pls sell deer all')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def dep_all():
        while True:
            time.sleep(random_genrator.random_buytime+2.5)
            keyboard.type('pls dep all') #types dep all to dep to bank
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
#boar, skunk, duck, rabbit, deer

if __name__ == '__main__':
    Thread(target = postmeme).start()
    Thread(target = pls_beg).start()
    Thread(target = laptopbuyer).start()
    #Thread(target = fishing).start()
    Thread(target = inventory_sell.sell_pill).start()
    Thread(target = inventory_sell.sell_bread).start()
    Thread(target = inventory_sell.sell_alcohol).start()
    Thread(target = inventory_sell.sell_cookie).start()
    Thread(target = inventory_sell.sell_rabbit).start()
    Thread(target = inventory_sell.sell_boar).start()
    Thread(target = inventory_sell.sell_skunk).start()
    Thread(target = inventory_sell.sell_duck).start()
    #Thread(target = hunt).start()
    #Thread(target = inventory_sell.sell_fish).start()
    Thread(target = inventory_sell.dep_all).start()
    Thread(target = inventory_sell.sell_deer).start()