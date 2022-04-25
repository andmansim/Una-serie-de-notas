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
