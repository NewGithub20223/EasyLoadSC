# load 1: ...
# load 2: ⟹⟹⟹
# load 3: >>>

from sys import stdout
import time
import os

class loadbar:
    def load1(self):
        for i in range(5):
            print("please wait", end="")
            time.sleep(0)
            self.write("...")
            os.system("cls")
    def load2(self):
        for i in range(5):
            print("loading: ", end="")
            time.sleep(0)
            self.write("⟹⟹⟹")
            os.system("cls")
    def load3(self):
        for i in range(5):
            print("starting ", end="")
            time.sleep(0)
            self.write(">>>")
            os.system("cls")
    def write(self, a):
        for i in a:
            stdout.write(i)
            stdout.flush()
            time.sleep(0.5)
load = loadbar()
