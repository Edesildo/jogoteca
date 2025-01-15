from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GOD', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combat', 'Luta', 'PS2')
jogo4 = Jogo('Lol', 'Moba', 'PC')
lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)
app.secret_key = 'ed'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo-jogo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'teste123' in request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f"{session['usuario_logado']} logado com sucesso!")
        return redirect('/')
    else:
        flash('Usuário não logado com sucesso!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
