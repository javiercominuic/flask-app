from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenidos amigos!'

@app.route('/about')
def about():
    return 'Acerca de esta página'

@app.route('/contact')
def contact():
    return 'Concatatnos'

@app.route('/hobbies')
def hobbies():
    return 'Mis hobbies son programar y leer'

@app.route('/audit')
def hobbies():
    return 'Auditoria anual'

if __name__ == '__main__':
    app.run(debug=True)
