import PySimpleGUI as sg
import random
sg.ChangeLookAndFeel('Dark RED')
sg.ChangeLookAndFeel('Dark RED')
#initial_tablero=[[BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10, [BLANK,] *10]
#blank = {'letra':'', 'imagen': os.path.join(PATH, 'blank.png')}
blank = {'letra':'', 'imagen': r'blank.png'}
a={'letra':'A','imagen': r'a.png'} #(r'img.png')
b={'letra':'A','imagen': r'b.png'}
c={'letra':'A','imagen': r'c.png'}
d={'letra':'A','imagen': r'd.png'}

e={'letra':'A','imagen': r'e.png'}
f={'letra':'A','imagen': r'f.png'}
g={'letra':'A','imagen': r'g.png'}

#b={'letra': 'B', 'imagen' : os.path_join(PATH, 'a.png')}
# b={'letra':'A','imagen': os.path.join(PATH,'a.png')}
# b={'letra':'B','imagen': os.path.join(PATH,'a.png')}
# c={'letra':'C','imagen': os.path.join(PATH,'a.png')}
# d={'letra':'D','imagen': os.path.join(PATH,'a.png')}
color_button=('white','white')
images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g}

initial_atril=[]
images_keys= list(images.keys())
images_keys.remove('BLANK')
print(images_keys)

for i in range(0,7):
	initial_atril.append(random.choice(images_keys))
print(initial_atril)

def render_square(image, key):
	return sg.RButton('',image_filename=image, size=(2,2), pad=(3,3),key=key,button_color=color_button)
	
tablero=[]
for i in range(10):  ### tablero botones
	row=[]
	for j in range(10):
		piece_image = images['BLANK']
		row.append(render_square(piece_image['imagen'],key = (i,j)))	
	tablero.append(row)
	
	
#print(tablero)	
	
## botones del atril

atril = []
for i in range(7):
	row = []
	piece_image = images[initial_atril[i]]
	row.append(render_square(piece_image['imagen'],key = i))
	atril.append(row)###	
	
#print(atril)	
	
board_tab=[[sg.Button('CHECK')],[sg.Column(atril), sg.Column(tablero)],[sg.Button('COMENZAR'),sg.Button('EXIT'),sg.Button('PASAR')]]
window = sg.Window('ScrabbleAr',default_button_element_size=(10,2), auto_size_buttons=False).Layout(board_tab)
#indow = sg.Window('tablero', layout, default_button_element_size=(5,2), auto_size_buttons=False)

event, value = window.Read()


