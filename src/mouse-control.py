import serial
from pynput.mouse import Controller
from time import time

ser = serial.Serial("COM4", 9600, timeout=0.05)
mouse = Controller()

anterior = 1280
last_move_time = 0
move_interval = 0.03  # 30ms

while True:
    if ser.in_waiting:
        read = ser.readline().decode('ascii').strip()
        if read:
            try:
                x = int(read.split()[0])
                current_time = time()
                if x != anterior and current_time - last_move_time >= move_interval:
                    mouse.position = (x, 540)  # Define diretamente a posição do mouse
                    last_move_time = current_time
                anterior = x
            except (ValueError, IndexError):
                pass


