'''Zariel Carmelo Hernandez Neri N° 1218100436 GDS0152'''


class multiplicar:
    def tabla(self):
     
        for i in range (1,10):
            n = 10
            num = 1
            print(" ")
            while num <= n:
                z = num * i
                print("{} x {} = {}".format(i, num, z))
                num = num + 1
            
    
tabla=multiplicar()
tabla.tabla()
