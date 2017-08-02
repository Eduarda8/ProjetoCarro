from carro import carro
from hibrido import hibrido

def main():

   c1 = carro("colorido", "ferrari", 1999)
   c1.acelerar()
   c1.freiar()

   print(c1)

   h1 = hibrido("vermelho", "fox", 1970)
   h1.acelerar()
   h1.freiar()
   h1.carregandoBateria()

   print(h1)

if __name__=="__main__":
    main()
