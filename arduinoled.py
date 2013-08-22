# Código por Flaybson Diniz

from Tkinter import *
import Tkinter
from time import strftime
import serial

arduino = serial.Serial(port='/dev/ttyS0',baudrate=115200)

def ligarLed():
    arduino.write('1')
    print ('Led On')

def desligarLed():
    arduino.write('2')
    print ('Led Off')


tela = Tk()
container1= Frame(tela)
tela.title('Arduino LED')
tela.geometry('300x40+50+50')

ledOn = Button(container1,command=ligarLed)
ledOn['text']=('Ligar Led')
ledOn['fg']=('Green')
ledOn['bg']=('Black')
ledOn.pack(side=LEFT)

ledOff = Button(container1,command=desligarLed)
ledOff['text']=('Desligar Led')
ledOff['fg']=('Red')
ledOff['bg']=('Black')
ledOff.pack()




container1.pack()
tela.mainloop()
