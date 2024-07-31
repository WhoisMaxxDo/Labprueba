
lst = []

def verificacion_operacion():
    # esta funcion va a verificar que numeros va a utilizar para realizar la operacion correspondiente que el ususario asigne
    print("1-suma")
    print("2-resta")
    print("3-division")
    print("4-multiplicacion")
    opcion = int(input("digite la operacion que desea realizar: "))
    num1 = int(input("digite el numero 1: "))
    num2 = int(input("digite el numero 2: "))
    if opcion == 1:
        resultado = num1 + num2
        print(resultado)
    elif opcion == 2:
        resultado = num1 - num2
        print(resultado)
    elif opcion == 3:
        resultado = num1 / num2
        print(resultado)
    elif opcion == 4:
        resultado = num1 * num2
        print(resultado)

def contador_objetos():
    # aqui se utiliza el sum para sumar la lista el "/" para dividirla en el len o sea la cantidad de objetos que tenga la lista
    total_lst = sum(lst)/len(lst)
    print(total_lst)


def suma_de_lista():
    while True:
        try:
            # aqui vamos a crear un recorrido para saber cuantos elementos desea agregrar a la lista
            recorrido = 1
            cantidad = int(input("cuantos elementos va a agregar a la lista?: "))
            for _ in range(cantidad):
                digito = int(input(f"{recorrido}-que numero desea agregar?: "))
                # con esto agregamos todo lo que se ponga en la variable "digito" en la lista lst
                lst.append(digito)
                recorrido += 1
            print(lst)
            opcion = input("desea saber el promedio de la lista o salir? prom/salir: ").lower()
            if opcion == "prom":
                # aqui se llama la funcion que va a sacar el promedio de la lista
                contador_objetos()
                break
            else:
                break
        except ValueError:
            print("digite numeros o una opcion valida")




def principal():
    while True:
        opcion = input("desea realizar una operacion, o añadir objetos a una lista o salir?: operacion/lista/salir: ").lower()
        if opcion == "operacion":
            # aqui se llama la funcion que va a realizar las operaciones
            verificacion_operacion()
        elif opcion == "lista":
            suma_de_lista()
        else:
            break




principal()



