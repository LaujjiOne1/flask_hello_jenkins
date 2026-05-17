from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Mon application DevOps fonctionne sur le port 8081 et mise a jour !'

if __name__ == '__main__':
    # L'application écoute sur le port 9090 à l'intérieur du conteneur
    app.run(host='0.0.0.0', port=9090)