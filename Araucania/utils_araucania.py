import requests
import io
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
import pandas as pd

#Esta funcion retornara en un arreglo el texto de la pagina 0 del PDF
def get_info(fecha, url):
    print ("Obteniendo información del: " + fecha)
    page      = requests.get(url)                           #Obtenemos la respuesta del servidor
    f         = io.BytesIO(page.content)                    #Tenemos el pdf
    reader    = PdfFileReader(f)                            #leemos el pf 
    contenido = reader.getPage(0).extractText().split('\n') #Tenemos el pdf separado por salto de linea
    print (contenido)
    
    #Filtramos e iteramos los datos
    pos_ini   = contenido.index('Angol')
    pos_fin   = contenido.index('Total General')
    
    contenido = contenido[pos_ini:pos_fin]                  # Filtramos con los datos que queremos    
    contenido.remove("Chol")
    contenido.remove("-")
    contenido = ["Chol-Chol" if x=="Chol" else x for x in contenido] #Cambiamos el nombre de cholchol
    
    #Eliminamos los espacios en blanco
    contenido_filtrado = []
    for c in contenido:
        if c != " ":
            contenido_filtrado.append(c)
    
    return contenido_filtrado    



# Retornará si el elemento ingresado es una ciudad
def is_city(elemento):
    bandera  = False
    ciudades = ['Angol', 'Carahue', 'Chol-Chol', 'Collipulli', 'Cunco', 'Curacautín', 'Curarrehue', 'Ercilla', 'Freire', 'Galvarino', 'Gorbea', 'Lautaro', 'Loncoche', 'Lonquimay', 'Los Sauces', 'Lumaco',  'Melipeuco', 'Nueva Imperial', 'Padre Las Casas',  'Perquenco', 'Pitrufquén', 'Pucón', 'Renaico',  'Saavedra', 'Temuco', 'Teodoro Schmidt','Toltén', 'Traiguén',  'Victoria', 'Vilcún', 'Villarrica', 'Purén']
    if elemento in ciudades:
        bandera = True
    return bandera


#Retornará los datos acumulados de los casos por region
def get_data(elemento, f):
    datos = [f]
    anterior = '' 
    ciudad   = ''
    n = 0
    for e in elemento:
        if (is_city(e) == False):
            anterior += e
        else:
            if anterior != '':
                #print (ciudad + " : " + anterior)
                datos.append(int(anterior))
                anterior = ''
        
        if is_city(e):
            ciudad = e
        
        ## Eliminamos el error del ultimo elemento
        if n == len(elemento)-1:
            datos.append(int(anterior))
        n += 1    
  
    return datos

def get_citys(fecha, url):
    ciudades = ['Fecha']
    data     = get_info(fecha, url)
    for d in data:
        if is_city(d):
            ciudades.append(d)
    return ciudades

def prueba():
    print("hola")