import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

pagina = "index"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
# Função de criação de conexão com o banco de dados



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


#obtendo apenas um post

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM empresa WHERE id = ?',
                        (post_id,)).fetchone()


    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/empresa/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)



#=====================================================================

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM empresa').fetchall()
    conn.close()
    pagina = index
    return render_template('index.html', posts=posts)




#criando um post

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        telecom = request.form['telecom']

        if not nome:
            flash('é necessario o nome da Empresa!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO empresa (nome, telecom) VALUES (?, ?)',
                         (nome, telecom))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


#Editar

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        nome = request.form['nome']
        telecom = request.form['telecom']

        if not nome:
            flash('É necessario colocar o nome da instituição')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE empresa SET nome = ?, telecom = ?'
                         ' WHERE id = ?',
                         (nome, telecom, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


#index2





@app.route('/index2')
def index2():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM escola').fetchall()
    pagina = "pagina"
    conn.close()
    pagina = index2
    return render_template('index2.html', posts=posts)





@app.route('/create2', methods=('GET', 'POST'))
def create2():
    if request.method == 'POST':
        nome = request.form['nome']
        grau = request.form['grau']
        horario = request.form['horario']

        if not nome:
            flash(' é necessario o nome da Escola!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO escola (nome, grau, horario) VALUES (?, ?, ?)',
                         (nome, grau, horario))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('createEscola.html')

#obtendo apenas um post

def get_post2(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM escola WHERE id = ?',
                        (post_id,)).fetchone()


    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/escola/<int:post_id>')
def post2(post_id):
    post = get_post2(post_id)
    return render_template('post2.html', post=post)