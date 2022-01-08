#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, time, signal, random

def DummyShot():
    print(f"bank!\n\033[0;31m{GetPath()}\033[0;0m")
    time.sleep(2)
    exit(0)

def Shot():
    '''To use the real shot decomment the next line and comment the DummyShot function call'''
    #os.remove(GetPath()) #The real shot, don't decomment
    DummyShot()

def def_handler(sig, frame):
    print("\n\n\033[0;33m[!]\033[0;0m You think you're so funny(?, so fuck off!\n")
    Shot()

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def GetPath():
    return ("C:\Windows\System32" if sys.platform == 'win32' else   "/")
    
def Again():
    n = input("Another attempt? [y|n]:  ")
    if n.lower() == 'y':
        print("Let's try again...")
        time.sleep(1)
        return True
    elif n.lower() == 'n':
        print("bye")
        time.sleep(1)
        return False
    else:
        print("Wrong Answare")
        print("Let's try again...")
        time.sleep(1)
        return True

def Main(var):
    if not var:
        print("Coward")
        exit(1)
    if random.randint(0,6) == 1:
        Shot()
    else:
        print("click")
        time.sleep(1.5)
        return Main(Again())

if __name__ =="__main__":
    Main(True)