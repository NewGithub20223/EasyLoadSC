# EasyLoadSC

**i am asking nicely NO FORKING PLS**

**NOTE: ONLY WORKS IN WINDOWS**

welcome to my script in this script it makes 3 custom loading
now since this dosent have a PIP install yet you will have to 
install this manually


# installation
**WARNING: dont do load.write() its just a setting**

**installation:
download the zip file and extract it**

**put the EasyLoad.py to "%localappdata%\Programs\Python\Python311\Lib" (change 311 to your python version)**


# coding/examples
now for examples:

to start you must setup easyload 1st by doing this
```
load = loadbar()
```
then start your loading by this
```
load.load1()
```
output:
![image](https://github.com/NewGithub20223/EasyLoadSC/assets/121712055/c2564126-51e2-4f96-8990-70b1d867f695)

to use the other loadings its this
```
load.load1()
load.load2()
load.load3()
```

EXAMPLE CODE:
```
# import
import easyload
# setup load
load = loadbar()
# start the loading text
load.load1()
```

# loading texts

**load 1:**
![image](https://github.com/NewGithub20223/EasyLoadSC/assets/121712055/ad48d653-fc66-48c3-8226-1986426284a5)

**load 2:**
![image](https://github.com/NewGithub20223/EasyLoadSC/assets/121712055/9254ce77-aceb-4c20-9b3b-8810799e4199)

**load 3:**
![image](https://github.com/NewGithub20223/EasyLoadSC/assets/121712055/184cefda-79bb-4ca6-8494-6f99dde8651f)


# add more loading texts with or without coding


# with coding
how to add more loading text:

```
def load1():
```
then code your loading

under the ``def load01()``

next put your code inside the ``class loadbar``


# without coding

how to add more loading text **WITHOUT CODING**:

copy this code:
```
    def load1(self):
        for i in range(5):
            print("please wait", end="")
            time.sleep(0)
            self.write("...")
            os.system("cls")
```
ok now paste it in the script

then in the self.write("...")

change the "..." with your text

EXAMPLE:
```
class loadbar:
    def load1(self):
        for i in range(5):
            print("please wait", end="")
            time.sleep(0)
            self.write("...")
            os.system("cls")
    def write(self, a):
        for i in a:
            stdout.write(i)
            stdout.flush()
            time.sleep(0.5)
load = loadbar()
```
if you want to change how many times it repeats the "for i in range(5):" change the number 5 with any number (the number means how many times it repeats)


# changing the speed

in the ``def write(self, a)``
go to
```
time.sleep(0.5)
```
change the 0.5 to any number you want (the number means the speed (its seconds))
