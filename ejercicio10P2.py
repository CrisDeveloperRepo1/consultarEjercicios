str = ['im1','im2','im3']
cont=0
for i in str:
  print('ingrese')
  caracter= input()

  if cont==0 :
	  str[cont] = i+" "+ caracter
  
  elif cont>1 and cont<=len(str)-1:
	  while(-1 !=(str[cont-1].find(caracter)))or (-1 !=(str[cont-2].find(caracter))) :
		  print('ingrese otra coord repetida')
		  caracter=input()	
  else : 	
    while(-1 !=(str[cont-1].find(caracter))):
      print('ingrese otra coord repetida')
      caracter= input()	
  str[cont] = i+" "+ caracter
  
  cont = cont+1    
    	
		
print(str)		 
		

##### no me convence como quedo apesar de que hace lo que pide el ejercicio , me gustaria tener una solucion mucho mas simple y no  usar tres condicionales 	
######	
