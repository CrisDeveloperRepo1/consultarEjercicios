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
	
## falta convertir a minuscula la respuesta , se me paso
# tengo un problema con el espacio que tienen las respuesta dentro de la lista , para que ande tuve que borrar el espacio que tenian cada respuesta , pense en usar lista.partition , pero eso me retornaria 3 tuplas ( no), tengo una para space , respuesta y la tercer tupla que me devolveria ????   , 
# solo me gustaria tener una opinion de este ejercicio :)
