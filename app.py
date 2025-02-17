from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para manejar sesiones

# Usuarios de ejemplo (en un caso real, usa una base de datos)
users = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

@app.route('/')
def home():
    if 'username' in session:
        return f'Bienvenido, {session["username"]}! <a href="/logout">Cerrar sesión</a>'
    return 'Por favor <a href="/login">inicia sesión</a>.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username  # Guardar el usuario en la sesión
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el usuario de la sesión
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)