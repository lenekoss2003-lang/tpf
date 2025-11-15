from flask import Flask, request, jsonify
from flask_cors import CORS
import sys


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

contador = 0

@app.route('/guardar', methods=['POST'])
def guardarestado ():
    global contador

    contador +=1
    
    print(f"Veces que se apreto el boton: {contador}")
    sys.stdout.flush()
    
    return '', 200

#esto lo habia armado para ver donde fallaba, lo dejo por si vuelve a no funcionar :)
@app.route('/cont', methods=['GET'])
def vercontador():
    return f"{contador}" 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)


