"""
Codigo muestra del funcionamiento para el encendido del PC-bre 2023
"""

#Librerias ocupadas
from smbus import SMBus
import os

#Lista de identificadores de arduinos
addrs = [0x09,0x08,0x0A,0x0B]

#Lista de estados de leds
estados = [False,False,False,False]

#Cadena de encendido *CONDICIONAL DE ENCENDIDO*
encendido = "Estrella"

#Cadena de inicio de programa *CONDICIONAL DE INICIO*
apagado = "Inicio"

"""
Se crea el objeto bus de la clase SMBus, enfocandola en el Bus 1, 
ya que a diferencia del 1, el 0 es usado internamente por el rasberry
"""
bus = SMBus(1) 

#Tokens esperados, buscados en cyberseguridad
tokenList = ["1","2","3","4"]

#Ejemplo de funcionalidad
#Menu de Opciones
def menu():
    print("------PCBRE------")
    print("Bienvenido a la prubea de funcionalidad!")
    print("1. Arduino #1")
    print("2. Arduino #2")
    print("3. Arduino #3")
    print("4. Arduino #4")
    print("5. Salir #4\n")

#Funcion que solicita y valida el token
def solicitarToken(addrs,token, n):
    os.system("clear")
    sk = input(f"\n\nIngresa la clave para el arduino {addrs}: ")
    if sk == token:
        bus.write_byte(addrs,1)
        estados[n] = True
        input("Toque una tecla para continuar...")
    else:
        print("Incorrecto!")
        input("Toque una tecla para continuar...")

def main():
    #bus.write_byte(0x08,0)

    for add in addrs:
        bus.write_byte(add,0)
    bus.write_i2c_block_data(0x08,0,[ord(c) for c in apagado])

    while True:
        os.system("clear")
        print(f"{estados}\n")
        menu()
        op = int(input("Ingrese el número del arduino: "))
        match op:
            case 1:
                solicitarToken(addrs[0],tokenList[0],0)
            case 2:
                solicitarToken(addrs[1],tokenList[1],1)
            case 3:
                solicitarToken(addrs[2],tokenList[2],2)
            case 4:
                solicitarToken(addrs[3],tokenList[3],3)
            case 5:
                break
            case _:
                print("No es una opcion, ingresa una nueva")
                input("Toque una tecla para continuar...")
        if estados[0] and estados[1] and estados[2] and estados[3]:
            bus.write_i2c_block_data(0x08,0,[ord(c) for c in encendido])

        
    

if __name__ == "__main__":
    main()


