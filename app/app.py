from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

basedatos={
    'user': 'root',
    'password': '123',
    'host' : 'basedatos',
    'database' : 'clicks'
}

def conectar():
    return mysql.connector.connect(**basedatos)

@app.route('/guardar', methods=['POST'])
def guardarestado ():
    datos = request.get_json()
    estado = datos.get('oscuro')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO estado (estado) VALUES (%s)", (estado))
    conexion.commit()
    cursor.close()
    conexion.close()
    return 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)


