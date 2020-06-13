<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Codigo de RL</title>
    <link rel="stylesheet" type="text/css" href="assets/css/EnlighterJS.min.css" />	
	<script type="text/javascript" src="assets/js/MooTools.min.js"></script>	
    <script type="text/javascript" src="assets/js/EnlighterJS.min.js"></script>
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/example.css">  
</head>
<body>
	<div class="container">
		<div class="page-header">
            <h1 align="center">REGRESIÓN LINEAL EN PYTHON </h1>
            <h3 align="center" class="text-muted">Para predecir el valor del peso mexicano</h3>
		</div>
		<div id="content">
	<script >
		window.addEvent('domready', function(){
			EnlighterJS.Util.Init('pre', 'code.special', {

				infoButton: false,
				windowButton: true,
				rawButton: true,
				// special hover class
				hover: 'myHoverClass',
				
				// default language
				language: 'html',
				
				// default theme
				theme: 'classic',
				
				// toolbar labels
				toolbar: {
					rawTitle: 'RAW Code',
					windowTitle: 'New Window',
					infoTitle: 'RL CODE'
				}
			});
		});
	</script>
<pre data-enlighter-language="python" data-enlighter-highlight="5">
"""
Created on Fri May 29 02:18:32 2020

@author: Eliot
"""
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import ctypes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from tkinter import*

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

ventana=Tk()
ventana.title("REGRESION LINEAL de 'Peso vs Dolar'")
ventana.geometry("1368x768+0+0")
ventana.config(bg = 'lightgreen')

#cargamos los datos del csv
data = pd.read_csv("datos_.csv")
#veamos cuantas dimensiones y registros contiene
print(data.shape)

print(data.head())
print(data.describe())

# RECORTAR los datos en la zona donde se concentran más los puntos
# esto es en el eje X: entre 0 y 5139
# y en el eje Y: entre 0 y 30 
#(30 es el maximo donde se entrar todos los datos, cambiar si se desea una busqueda más reducida)
filtered_data = data[(data['Periodo'] <= 5149) & (data['Monto'] <= 30.00)]
 
colores=['green','blue']
tamanios=[3,2]
 
f1 = filtered_data['Periodo'].values
f2 = filtered_data['Monto'].values
 
# Vamos a pintar en colores los puntos por debajo y por encima del promedio del valor del peso
asignar=[]
for index, row in filtered_data.iterrows():
    if(row['Monto']>13.39):
        asignar.append(colores[0])
    else:
        asignar.append(colores[1])
    
plt.scatter(f1, f2, c=asignar, s=tamanios[0])

# Asignamos nuestra variable de entrada X para entrenamiento y las etiquetas Y.
dataX =filtered_data[["Periodo"]]
X_train = np.array(dataX)
y_train = filtered_data['Monto'].values
 
# Creamos el objeto de Regresión Linear
regr = linear_model.LinearRegression()
 
# Entrenamos nuestro modelo
regr.fit(X_train, y_train)
 
# Hacemos las predicciones que en definitiva una línea (en este caso, al ser 2D)
y_pred = regr.predict(X_train)
 
# Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
print('Coefficients: \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('Independent term: \n', regr.intercept_)
# Error Cuadrado Medio
print("Mean squared error: %.4f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Variance score: %.4f' % r2_score(y_train, y_pred))

#Funcion ver notas
def Notas():
    messagebox.showwarning("NOTAS","\n***Periodo***\n(1/5149)= 1 dia\n(Desde 03/01/2000 Hasta 12/06/2020)\n\n***Ecuacion:****\ny = 0.0021x + 7.8731\nR² = 0.8203\n\n***Promedio:***\n$13.39\n\n***Colores:***\n-Azul: Valor < al promedio\n-Verde: Valor >= al promedio\n")

#Función para ver predicción
def Prediction():
    messagebox.showinfo("PREDICCION ","PREDICCION:\nEl valor del peso mexicano frente al dolar\ndentro de cinco anos (13/06/2025) sera de: $22.85949654")

#Función Lineal.
def f(x):
    return regr.coef_*x+7.8731
x = range(0, 6000)

plt.plot(x, [f(i) for i in x])

#Establecemos el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Especificamos los limites de los ejes.
plt.xlim(0, 5160)
plt.ylim(0, 40)

#PARA GUARDAR LA IMAGEN DE LA GRAFICA
plt.title('REGRESION LINEAL')
plt.xlabel('Periodo')
plt.ylabel('Precio del Peso Mexicano')
plt.savefig("rlineal.png")

#Vamos a comprobar:
# Quiero predecir cuánto valdrá el peso mexicano en cinco años
# según nuestro modelo, hacemos:
Prediccion_a_5años=regr.predict([[6975]])
#INGRESE EL NUMERO 6975 PORQUE actualmente son 5149 datos hasta el 12/06/2020
#Si multiplicamos 365*5 nos da el numero para ingresar en la prediccion
print(Prediccion_a_5años)

#PARA MOSTRAR LA GRAFICA EN TKINTER
img_gra=PhotoImage(file="rlineal.png")
######IMPORTANTE#########
#COMENTAR LINEA INFERIOR SI HAY ERROR, CORRER EL ARCHIVO. DESPUES QUITAR EL '#' Y CORRER DE NUEVO
boton=Button (ventana,image=img_gra).place(x=100,y=10)
boton_predicion=Button (ventana,text="PREDICCIÓN",command=Prediction).place(x=780,y=670)
boton_notas=Button (ventana,text="NOTAS",command=Notas).place(x=530,y=670)

#PARA SOLO MOSTRAR EN EL PANEL DE 'GRAFICOS'
plt.show()
ventana.mainloop()

</pre>
	</div>
    <br>
    <a href="index.php" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Regresar</a>
    <br>
    <br>
    <br>
    </div>
</body>
</html>