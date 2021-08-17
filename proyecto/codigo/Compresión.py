nombreArchivo = None
archivos = []
condicion = 'Yes'

def recibir(nombre):
    archivo = open(nombre, "r")
    lineas = archivo.readlines()
    return lineas

nombreArchivo = input('Escriba el nombre del archivo: ')
archivos.append(recibir(nombreArchivo))
condicion = input("""¿Desea agregar otro archivo?
Escriba "Yes" para agregar otro, de lo contrario escriba "No": """)

while condicion == 'Yes':
    nombreArchivo = input('Escriba el nombre del siguiente archivo: ')
    archivos.append(recibir(nombreArchivo))
    condicion = input("""¿Desea agregar otro archivo? 
    Escriba "Yes" para agregar otro, de lo contrario escriba "No": """)
print(archivos)