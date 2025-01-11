import random


def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    return random.choice(palabras)

def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')\n
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    lista = []
    letras_probadas_normalizadas = {normalizar_letra(l) for l in letras_probadas}

    for l in palabra:
        if normalizar_letra(l) in letras_probadas_normalizadas:
            lista.append(l)  # Mostrar la letra original con tilde
        else:
            lista.append('_')
    
    return ' '.join(lista)


def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    abecedario = set("abcdefghijklmnopqrstuvwxyz")
    while True:
        l = input("Introduzca la siguiente letra: ").lower()
        if len(l) == 1 and l in abecedario and l not in letras_probadas:
            return l
        elif l in letras_probadas:
            print("Esa letra ya fue probada. Intente con otra.")
        else:
            print("Entrada no válida. Introduzca una sola letra del abecedario.")

def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    letra_normalizada = normalizar_letra(letra)
    palabra_normalizada = ''.join(normalizar_letra(l) for l in palabra_secreta)

    if letra_normalizada in palabra_normalizada:
        print("¡Bien hecho! Esa letra está en la palabra.")
        return True
    else:
        print("Lo siento, esa letra no está en la palabra.")
        return False

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    for l in palabra_secreta:
        if l not in letras_probadas:
            return False
    return True

def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    enmascarar_palabra(palabra_secreta, letras_probadas)
    l = pedir_letra(letras_probadas)
    letras_probadas.add(l)
    return comprobar_letra(palabra_secreta, l)

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("Bienvenido ✌️", end="\n\n\n\n")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = set()
    intentos_fallidos = 0
    
    while intentos_fallidos < max_intentos:
        print(f"Progreso || {enmascarar_palabra(palabra_secreta, letras_probadas)}", end="\n\n\n\n")
        
        resultado = ejecutar_turno(palabra_secreta, letras_probadas)
        
        if not resultado:
            intentos_fallidos += 1
        
        print(f"\nIntentos restantes: {max_intentos - intentos_fallidos}", end="\n\n\n\n")

        if comprobar_palabra_completa(palabra_secreta, letras_probadas):
            break
        
    if comprobar_palabra_completa(palabra_secreta, letras_probadas):
        print("🎉🎉🎉🎉🎉🎉🎉🎉")
    else:
        print("💀💀💀💀💀💀💀💀")

def normalizar_letra(letra):
    equivalencias = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'
    }
    
    return equivalencias.get(letra, letra)
    

# Iniciar el juego
if __name__ == "__main__":
    #palabras = cargar_palabras("data/palabras_ahorcado.txt")
    palabras = cargar_palabras("data/palabras_ahorcado_conTildes.txt")
    jugar(6, palabras)