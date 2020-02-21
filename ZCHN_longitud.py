'''Zariel Carmelo Hernandez Neri N° 1218100436 GDS0152'''
class long: 
  def longitud(self):
    letra=input("Ingrese una palabra: ")
    num=letra.lower()
    num=num[0].upper()+num[1:]
    numletra=0
    for i in letra:
      numletra+=1
    print('Su palabra ' , num , 'tiene',numletra,'letras')

  

cadena=long()
cadena.longitud()
