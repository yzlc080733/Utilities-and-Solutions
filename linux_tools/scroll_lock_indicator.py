import os
import sys
import time
import psutil
import signal
import math

def set_led(value=0):
    if value == 1:
        os.system('xset led named "Scroll Lock"')
    else:
        os.system('xset -led named "Scroll Lock"')

def set_period(time_interval=0.07):
    set_led(1)
    time.sleep(time_interval)
    set_led(0)

def set_repeat(time_interval=0.07, number=1):
    for _ in range(number):
        set_led(1)
        time.sleep(time_interval)
        set_led(0)
        time.sleep(time_interval)



def sigint_handler(signum, frame):
    print('\033[91m\nEXIT\n\033[0m')
    set_led(0)
    sys.exit(0)

def get_freq(value):
    result = (-1) * math.log(value) / 1.6 + 2.95
    return result

signal.signal(signal.SIGINT, sigint_handler)

time_old = time.time()
cpu_value = 5
freq = get_freq(cpu_value)
while True:
    if time.time() - time_old > 2:
        # psutil.disk_io_counters(perdisk=False)
        cpu_value = psutil.cpu_percent()
        cpu_value = min(100, max(2, cpu_value))
        freq = get_freq(cpu_value)
        time_old = time.time()
        # print(cpu_value, freq, math.ceil(cpu_value/10))
    # set_period(0.07)
    set_repeat(0.08, math.ceil(cpu_value/10))
    time.sleep(freq)
    
