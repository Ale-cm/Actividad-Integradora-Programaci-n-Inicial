

def list():
    """ Devuelve una lista de 5 numeros enteros que ingresa el usuario """
    lista_cantidad = 5
    lista=[]
    for k in range(lista_cantidad):
        numero = verifica_entero()
        lista.append(numero)
   # print(lista)
    return lista

def verifica_entero():
    """ Solicita un valor entero y lo devuelve.
        Si el valor ingresado no es entero,cambia el mensaje de ingreso y da 5 intentos para ingresarlo
        correctamente, y de no ser así, lanza una excepción. """
    intentos = 0
    while intentos < 5:
        mensaje= "Ingrese un número entero : "
        error_mensaje= "Solo ingrese numeros enteros!!! : "
        if(intentos==1): mensaje=error_mensaje  
        valor = input(mensaje)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            intentos += 1
    raise ValueError("Valor incorrecto ingresado en 5 intentos")

    #me sumo al proyecto integrador, creo una rama y hago un push
    #creo un comentario nuevo desde de mi rama de funciones "rama de funciones rodrigo perez :)"

