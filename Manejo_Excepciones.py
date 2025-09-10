#  Manejo de Excepciones

#zero_division_error.py
# Ejemplo de manejo de la excepción ZeroDivisionError

num1 = input("Introduce el primer numero distinto de cero")
num2 = input("Introduce el segundo numero distinto de cero")

def dividir(num1, num2):
    try:
        resultado = float(num1) / float(num2)
        
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
    else:
        print("La division se ha realizado correctamente.")
        return resultado
resultado = dividir(num1, num2)
print("Resultado:", resultado)
   
#--------------------------------------------------------------------#

# listas, string y numeros
# Ejemplo de manejo de la excepción TypeError

lista = [23,45,65,3,6,2,9]
nombre = "Juan"

def sumar(lista, nombre):
    try :
        resultado = lista + nombre
        return resultado
    except TypeError:
        print("Error: No se puede sumar una lista con un string.")
sumar(lista, nombre)
resultado = sumar(lista, nombre)
print("Resultado:", resultado)

#--------------------------------------------------------------------#
# Ejemplo de manejo de la excepción keyerror
datos_personales = {
    "nombre": "Erica",
    "edad": 39,
    "DNI": "12345678",
    "ciudad": "Buenos Aires",
    "profesion": "Instrumentadora",
    "hobby": "Viajar",
    "pais": "Argentina",
    "idioma": "Español"
}
def obtener_dato(diccionario, apellido):
    try:
        return diccionario[apellido]
    except KeyError:
        print(f"Error: La clave '{apellido}' no existe en el diccionario.")
dato = obtener_dato(datos_personales, "apellido")
print("Dato obtenido:", dato)

#--------------------------------------------------------------------#
# Abrir archivos inexistentes
# Ejemplo de manejo de la excepción FileNotFoundError

def leer_archivo():
    try:
        # Intento abrir el archivo en modo lectura
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)

    except FileNotFoundError:
        # Si no existe, muestro mensaje y lo creo
        print("Error: El archivo 'datos.txt' no existe. Creándolo ahora...")
        with open("datos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Creando archivo\n")
        print("El archivo 'datos.txt' ha sido creado correctamente.")

# Llamo a la función
leer_archivo()
#--------------------------------------------------------------------#

#ZeroDivisionError y ValueError
def dividir_numeros():
    try:
        numero1 = float(input("Introduce el primer numero: "))
        numero2 = float(input("Introduce el segundo numero: "))
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Debes introducir un numero valido.")
    else:
        print("El resultado de la division es:", resultado)
dividir_numeros()
#--------------------------------------------------------------------#
        

