import PySimpleGUI as sg
from random import randint
from string import ascii_uppercase as up
from random import choice
# letrasRandom = lambda : [choice(up) for i in range(6)]
# a=letrasRandom()

# button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
color_button=('white','green')
# tam_button = 5,2
# tam_button1 = 7,2
# MAX_ROWS = MAX_COL = 15
image=r'b.png'
# # cambie la key a i + j, solo para que no sea una tupla
layout =  [
           #[sg.Button('',image_filename=image,size=(0,1), pad=(0,0))]]
           [sg.Button('',image_filename=image),sg.Button('',image_filename=image,button_color=color_button)]]
           #[sg.Button('comenzar')]]
#sg.RButton('',image_filename=image, size=(1,1), pad=(0,0),key=key)
window = sg.Window('tablero', layout, default_button_element_size=(1,2), auto_size_buttons=False)

event, values = window.read()
