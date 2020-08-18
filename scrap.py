from bs4 import BeautifulSoup
import requests
import pandas as pd

# Se indica la url a la que se quiere hacer scraping
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'

# Descargamos el html de la pagina
page = requests.get(url)

# Vamos a accesder al contenido de la pagina e indicar que se interprete como html
soup = BeautifulSoup (page.content, 'html.parser')


# Equipos
# Que nos encuentre todas las etiquetas tipo span, con clase = 'nombre-equipo'
# Se referencia a la clase de html con 'class_' para que no se interprete como el creador de clases de python
eq = soup.find_all('span', class_='nombre-equipo')

# De los datos extraidos de la web en los elementos indicados solo necesitamos el texto, para esto vamos a realiar un for y extraer el texto y agregarlo a una lista llamada 'equipos'

equipos = list()

# Como en la página hay mas elementos con la etiqueta nombre-equipo al imprimir la lista se repiten los elementos, por esto se realiza un contador hasta 20 para que se tomen los primeros 20 elementos.

count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1

print(equipos, len(equipos))

# Puntos
# Que nos encuentre todas las etiquetas tipo span, con clase = 'destacado'
# Se referencia a la clase de html con 'class_' para que no se interprete como el creador de clases de python

pt = soup.find_all('td', class_='destacado')

# De los datos extraidos de la web en los elementos indicados solo necesitamos el texto, para esto vamos a realiar un for y extraer el texto y agregarlo a una lista llamada 'equipos'

puntos = list()

# Como en la página hay mas elementos con la etiqueta destacado al imprimir la lista se repiten los elementos, por esto se realiza un contador hasta 20 para que se tomen los primeros 20 elementos.

count = 0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1

print(puntos, len(puntos))


# Ahora vamos a incluir la información que se extrae en un dataFrame usando la libreria pandas

df = pd.DataFrame({'Nombre': equipos, 'Puntos': puntos}, index =  list(range(1, 21)))

print (df)

# Exporto el dataFrame a un archivo plano

df.to_csv('Classificación.csv', index=False)

