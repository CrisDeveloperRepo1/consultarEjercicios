import random
lista=[['Buenos Aires limita con Santiago del Estero','no'],['Jujuy limita con Bolivia','si'],['San Juan limita con Misiones','no']]

while lista !=[] :

	x=random.randrange(len(lista))

		
		
	print(lista[x][0])
	respuesta=input('ingrese respuesta : ')
	print('analizando')
	if (lista[x][1])== respuesta :
		print('respuesta correcta')
	else :
		print('respuesta incorrecta')	
	del lista[x]
	print('')
	
## falta convertir a minuscula la respuesta
