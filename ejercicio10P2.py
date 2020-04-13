str = ['im1','im2','im3']
cont=0




for i in str:
  print('ingrese una coordenada')
  caracter= input()

  if cont==0 :
	  str[cont] = i+" "+ caracter

  
	#coord = input()
  else : 	
    while(-1 !=(str[cont-1].find(caracter))):
      print('coord repetida')
      caracter= input()	
  str[cont] = i+" "+ caracter
  cont = cont + 1
      
    	
		
print(str)	
