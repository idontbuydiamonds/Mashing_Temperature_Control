
"""

This Software is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation.

Created on Sat Nov 16 16:37:58 2019

@author: Igor Arantes
e-mail igor.l.arantes@gmail.com
"""




import pyfirmata
import time


board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
temp_input = board.get_pin('a:0:i')
boiler=board.get_pin('d:13:o')
mixer=board.get_pin('d:12:o')

while True:
    try:
        temp_raw = temp_input.read()
        temp_in= float(temp_raw)*(5)/0.01
        print(str(temp_in) + " ºC")
        f=open('temp.temp', 'w')
        f.write(str(temp_in))
        f.close()
        s=open('sets.temp', 'r')
        sets=s.readlines()
        s.close()      
        if sets[0]=="ON\n":
           boiler.write(1)
        else:
            boiler.write(0)
        if sets[1]=="ON":
           mixer.write(1)
        else:
            mixer.write(0)
            
        
        
        time.sleep(1)
    except:
        print("Erro de comunicação")
        time.sleep(1)
        pass
    