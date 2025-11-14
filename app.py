from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

contador = 0

@app.route('/guardar', methods=['POST'])
def guardarestado ():
    global contador
    contador +=1
    
    print(f"Contador: {contador}")
    
    return '', 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)


