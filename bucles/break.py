def run():
    menu = """
    
    B I E N VE N I D O  A  A P R E N D E R  A  S U M A R   Y   R E S T A R  C O N   M A M A.
    
    Para Sumar, escribe 1...
    Para Restar, escribe 2...

    Elije una opción:
    
    """
    opcion = int(input(menu))

    while opcion != 1 and opcion != 2:
        print('\nIngresa una opcion correcta, por favor\n')
        opcion = int(input(menu))
        continue
    numero1 = int(input('\nEscribe el primer numero: '))
    numero2 = int(input('\nEscribe el segundo numero: '))
    if opcion == 1:
        operacion(numero1, numero2, '+', 'suma')
    elif opcion == 2:
        while numero1 < numero2:
            print('\nLo siento, no puedes restar por ahora, el primer numero debe ser mas grande. Vuelve a intentarlo')
            numero1 = int(input('\nEscribe el primer numero: '))
            numero2 = int(input('\nEscribe el segundo numero: '))
            continue
        operacion(numero1, numero2, '-', 'resta')
    else:
        print('\nIngresa la opcion correcta por favor')


def operacion(numero1, numero2, simbolo, opcion):
    contador = 1
    while contador <= numero1:
        print('\n🎃\n')
        contador += 1
    print('\n{}\n'.format(simbolo))
    contador = 1
    while contador <= numero2:
        print('\n🎃\n')
        contador += 1

    if simbolo == '+':
        result = numero1 + numero2
    elif simbolo == '-':
        result = numero1 - numero2

    numero = int(input('\nEscribe el resultado de la {}: '.format(opcion)))
    while(numero != result):
        numero = int(
            input('\nEscribe el resultado correcto de la {}: '.format(opcion)))
        continue
    print('\n Es correcto el resultado de la {} es {}. Felicitaciones amigo, estoy orgulloso de ti'.format(
        opcion, result))


if __name__ == '__main__':
    run()
