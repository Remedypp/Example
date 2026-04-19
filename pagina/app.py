# 0. ANTES DE EMPEZAR, INSTALAR EN LA TERMINAL:
# pip install flask mysql-connector-python

from flask import Flask, render_template
import mysql.connector # 1. IMPORTAR LIBRERÍA DE MYSQL

app = Flask(__name__)

@app.route('/')
def home():
    # 2. CONECTAR A MYSQL Y PEDIR UN DATO
    # (Esto asume que tienes XAMPP encendido con una base de datos)
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mi_base_de_datos" # Pon aquí tu base de datos
        )
        cursor = conexion.cursor()
        
        # Le pedimos a MySQL que nos traiga un mensaje
        cursor.execute("SELECT mensaje FROM mi_tabla LIMIT 1")
        dato_mysql = cursor.fetchone()[0] # Extraemos el texto exacto
        
        conexion.close() # Cerramos la conexión para no gastar memoria
        
    except Exception as e:
        # Si no tienes MySQL encendido ahora mismo, mostrará esto para no explotar:
        dato_mysql = "¡Error! No me pude conectar a MySQL. Asegúrate de encender XAMPP/WAMP."

    # 3. UNIR TODO (MYSQL -> PYTHON -> HTML):
    # El dato que sacamos de MySQL (o el error) se lo enviamos al archivo index.html
    return render_template('index.html', texto_desde_python=dato_mysql)

if __name__ == '__main__':
    app.run(debug=True)
