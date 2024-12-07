from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenidos a mi aplicación Flask!.'

@app.route('/about')
def about():
    return 'Acerca de esta página'

@app.route('/contact')
def contact():
    return 'Contáctanos en flask@example.com'

@app.route('/hobbies')
def hobbies():
    return 'Mis hobbies son programar y leer'


if __name__ == '__main__':
    app.run(debug=True)
