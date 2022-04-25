# Una-serie-de-notas

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Una-serie-de-notas.git)
https://github.com/andmansim/Una-serie-de-notas.git

En este repositorio voy a explicar como analizar datos estadísticamente.

# Explicar una serie de notas
En una clase hay 1000 estudiantes con unas series de notas de los exámenes que hicieron, esos exámenes son matemáticas, expresión escrita y comprensión lectora. Con todos estos datos los vamos a analizar estadísticamente, y se van a explicar cada paso y el porqué de ese procedimiento.

# Abrir y obtener datos del fichero CSV
Comenzamos por abrir el fichero .csv en el fichero main, que es un DataSet, lo cual lo sabemos por su gran cantidad de columnas y filas. Para abrirlo, primero necesitamos importar la librería pandas, que la importaremos como pd. 

```
import pandas as pd
``` 
La librería pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos. Sus usos principales son: definir nuevas estructuras de datos basadas en arrays(listas) de la librería NumPy, (que hablaremos más adelante), permite leer y escribir ficheros en formato CSV, Excel y bases de datos SQL, permite acceder a datos mediante sus índices o nombres de filas y columnas. También podemos reordenar, dividir y combinar datos, trabajar con series temporales y, por último, realiza operaciones de manera eficiente. 
Tras esta breve explicación de para que sirve esta librería, vamos a ver cómo podemos obtener y trabajar con los datos del DataSet. 
Primero debemos de leer el DataSet, para ello lo haremos de la siguiente manera:
```
df = pd.read_csv('StudentsPerformance.csv', delimiter= ',', encoding= 'UTF-8' )
``` 
Creamos una variable que va a ser a la que llamemos cuando queramos trabajar con este fichero CSV. Después ponemos la librería pandas, que hemos nombrado anteriormente como pd, y el .read_csv(‘StudentsPerformance.csv’, delimiter = ‘,’, encoding=’UTF-8’ ). El read_csv es para leer el fichero CSV. Luego ponemos su nombre para poder llamarlo, el delimiter nos indica cómo están separados los parámetros, en este caso será una coma y el enconding es para trasformar todo a UTF-8, para que Python sea capaz de leerlo.
Si lo ejecutamos obtenemos:
```
<<<
     gender race/ethnicity parental level of education  ... math score reading score  writing score
0    female        group B           bachelor's degree  ...         72            72             74
1    female        group C                some college  ...         69            90             88
2    female        group B             master's degree  ...         90            95             93
3      male        group A          associate's degree  ...         47            57             44
4      male        group C                some college  ...         76            78             75
..      ...            ...                         ...  ...        ...           ...            ...
995  female        group E             master's degree  ...         88            99             95
996    male        group C                 high school  ...         62            55             55
997  female        group C                 high school  ...         59            71             65
998  female        group D                some college  ...         68            78             77
999  female        group D                some college  ...         77            86             86
>>>
```
(Los tres puntos los pone para no mostrar todos los datos, dado que en este caso son demasiados para enseñarlos por pantalla)
Podemos observar que tenemos muchas columnas, con el género, grupo, curso, etc. Pero a nosotros nos interesa las notas de todo el centro para poder calcular los datos estadísticos. 
Crearemos una nueva variable df_new, con solo los datos importantes para la estadística:
```
df_new = pd.DataFrame({'math score': df['math score'], 'reading score': df['reading score'], 'writing score': df['writing score']})
``` 
Usaremos pandas para crear un Dataframe, que es muy útil para el manejo de datos en formato tabla. Para ello se lo debemos pasar los datos como un diccionario, indicando el nombre de las columnas, como 'math score'.
Obtenemos:
```
<<<
     math score  reading score  writing score
0            72             72             74
1            69             90             88
2            90             95             93
3            47             57             44
4            76             78             75
..          ...            ...            ...
995          88             99             95
996          62             55             55
997          59             71             65
998          68             78             77
999          77             86             86
>>>
```
# Análisis de datos
Tras esto, comenzaremos a analizar los datos estadísticamente, por ejemplo, de las notas de matemáticas, el math score. Para trabajar con ellas, crearemos una clase llamada JPEstadisticas, con el parámetro df_new[‘math score’], (sabemos que el df_new es el nombre del DataFrame que hemos creado previamente, y los corchetes con el math score, es para indicarle que nos vamos a centrar en la columna math score y que coja los datos de ahí, ignorando el resto del DataFrame. 
```
#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(df_new['math score'])
stats.analisisCaracteristica()
```
Antes de explicar stats.analisisCaracteristica(), vamos a empezar por el principio de la clase JMPEstadisticas.
El desarrollo de dicha clase se hará en el fichero clases.py. Comenzaremos escribiendo el nombre de la clase y su constructor.
```
class JMPEstadisticas:
    def __init__(self,caracteristica):
        self.caracteristica = caracteristica #columna notas
```
self.caracteristica va a ser el atributo que contenga a la columna df[‘math score’].

# Media aritmética
La media aritmética es el valor promedio de un conjunto de datos numéricos, en nuestro caso las notas de matemáticas, y se calcula sumando todos los conjuntos de valores y dividiéndolo entre el número total de valores.  
Pasos: 
1º Creamos un método llamado calculoMediaAritmetica, con el parámetro self. 
2º Establecemos una variable n que nos va a contar todos los datos que tenemos en nuestro DataFrame. Esto lo hará mediante la función .count()
3º Inicializamos las variables sumaValoresObservaciones y mediaAritmetica, las cuales las inicializaremos con un cero para llamarlas más adelante.
4º Creamos un bucle que nos vaya sumando cada fila de nuestra columna, es decir, que nos sume todas las notas que tenemos y nos guardará el valor final en la variable sumaValoresObservaciones.
5º Calculamos la media, que es la división de la suma de todas las notas, nuestros valores, y lo dividimos entre el número total de ellos. Lo guardamos en la variable mediaAritmetica.
6º El método nos devolverá el valor de la media.
```
def calculoMediaAritmetica(self):

        n = self.caracteristica.count() # 1000 datos para analizar
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica
```
# Mediana
La mediana es el valor que ocupa el lugar central de todos los datos cuando estos están ordenados de menor a mayor.
Pasos: 
1º Definimos el método calculoMediana y le pasamos el parámetro self.
2º Creamos la variable mediana, la igualamos a cero para usarla posteriormente, y la variable característica que se va a encargar de ordenar los valores de menor a mayor. Mediante la función .sort_values(), que además de ordenar los valores de la columna math score. También usaremos .resert_index(drop=True), para que nos resete los índices de cada valor.
Así es como se vería la variable característica:
<<<
0        0
1        8
2       18
3       19
4       22
      ...
995    100
996    100
997    100
998    100
999    100
>>>
3º Volvemos a contar los valores, dado que, al haber creado la variable n dentro del método de la media, no la reconoce. Por eso volvemos a hacer todo de nuevo.
4º Vamos a calcular la mediana, el problema de la mediana es que debemos de mirar si los datos son pares o impares. Porque si son pares, para calcular el dato de la posición central debemos dividir n/2, lo cual nos dará dos valores que están en dicha posición dependiendo de donde contemos. Así que debemos de hacer la media entre ellos, para calcularnos su valor. Pongamos un ejemplo sencillo, tenemos los siguientes valores:  1, 3, 5, 8, 2, 9. Los ordenamos de menos a mayor:  1, 2, 3, 5, 8, 9. Tenemos 6 datos, entonces el valor de la posición central será el que se encuentre en la posición 3 (6/2). Si empezamos a contar por la izquierda dará que el valor es 3, sin embargo, si empezamos por la derecha el valor será 5. Por ello, se realizará la media de ambos números, (3 + 5) / 2 = 4. Si n es impar tan solo sería hacer la división de n / 2. 
5º Vemos si el resto es igual a cero, para ver si es par o impar. 
6º Par: Establece el rango (la posición del valor central) y rangoPython (la posición del valor central en Python, es dicha posición, pero un número menos, dado que el índice de nuestros datos empieza en cero, no en uno). Y buscamos los valores que corresponden a esas posiciones en nuestra columna de notas. Después calculamos la mediana.
7º Impar: para que nos salga exacto a n le sumamos 1 y lo dividimos entre dos, hallando así la posición del valor central y calculamos como sería en Python, rangoPython.
8º Este método nos devuelve una lista con la mediana y el rango.
```
def calculoMediana(self):
        mediana = 0
        caracteristica = self.caracteristica.sort_values() #ordena valores
        caracteristica = caracteristica.reset_index(drop=True)
        n = self.caracteristica.count()
        par = False;
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2); 
            print("RANGO = "+str(rango))
            rangoPython = rango-1 
            valor1 = caracteristica[rangoPython] 
            valor2 = caracteristica[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = caracteristica[rangoPython]

        return [mediana, rango]
```


