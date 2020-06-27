#imports
from pynput.keyboard import Key, Controller
import time
import random
from multiprocessing import Process
import sys
from threading import Thread

keyboard = Controller()#defining keyboard

def enter():#making an enter definition
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def text(n=''):#shortcut for keyboard.type
    keyboard.type(n)

class Money():#money
    def pls_beg():
        counter=0#counts how many times we have looped thru
        time.sleep(random.choice([1 , 1.25, 1.5, 1.75 ]))
        while True:
            text('pls beg')
            enter()
            if counter==3:#checks if we have looped thru 3 times
                time.sleep(.5)
                text('pls dep all')#deposits all the money 
                enter()#enters
                counter=0#resets the counter
            else:
                counter += 1
            time.sleep(random.choice([40,40.2, 40.25, 40.1 , 40.3, 40.35, 40.32, 40.42, 40.35,41.2]))

    def postmeme():
        counter=0
        time.sleep(1+random.choice([1 , 1.25, 1.5, 1.75 ]))
        while True:
            text('pls postmeme')
            enter()
            time.sleep(random.choice([1 , 1.25, 1.5, 1.75 ]))
            text(random.choice(['n','e','r','d']))
            enter()
            if counter==25:
                time.sleep(.25)
                text('pls withdraw 1500')
                enter()
                time.sleep(.25)
                text('pls buy laptop')
                enter()
                counter=0
            else:
                counter += 1
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6]))

    def fishing():
        counter=0
        time.sleep(random.choice([1 , 1.25, 1.5, 1.75 ])+4)
        while True:
            text('pls fish')
            enter()
            if counter == 6:
                time.sleep(.15)
                text('pls sell fish all')
                enter()
            elif counter == 45:
                time.sleep(.15)
                text('pls wihtdraw 15000')
                enter()
                counter = 0
            else:
                counter+=1
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])*10 )
    
    def hunting():
        counter=0
        time.sleep(random.choice([1 , 1.25, 1.5, 1.75 ])+6)
        while True:
            text('pls hunt')
            enter()
            if counter == 60:
                text('pls withdraw 15000')
                enter()
                time.sleep(.15)
                text('pls buy rifle')
                enter()
                counter=0
            else:
                counter+=1
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])*6)

if __name__ == "__main__":#we use this to run the script
    Thread(target = Money.postmeme).start()
    Thread(target = Money.pls_beg).start()
    #Thread(target=Money.fishing).start() #take out # infornt of the code IF YOU HAVE FISHING ROD
    #Thread(target = Money.hunting).start() #take out # infornt of the code IF YOU HAVE HUNTING RIFLE
