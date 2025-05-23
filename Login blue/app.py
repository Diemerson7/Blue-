from flask import Flask, render_template, request, session, url_for, redirect, flash

import database

app = Flask(__name__)
app.secret_key = "chave_muito_segura"

@app.route('/') # Rota para a página inicial
def index():
    return render_template('index.html')



@app.route('/login', methods=["GET", "POST"]) # Rota para a página de login
def login():
    if request.method == "POST":
        form = request.form
        if database.fazer_login(form) == True:
            session['email'] = form['email']    # Armazena o email do usuário na sessão
            return redirect(url_for('home')) 
        else:
            return "Ocorreu um erro ao fazer login"
    else:
        return render_template('login.html')


@app.route('/cadastro', methods=["GET", "POST"]) # Rota para a página de login
def cadastro():
    if request.method == "POST":
        form = request.form
        
        if database.criar_usuarios(form) == True:
            return redirect('/login')
        else:
            return "Ocorreu um erro ao cadastrar o usuário"
    else:
            return render_template('cadastro.html')
    

# @app.route('/home', methods=["GET", "POST"])
# def home():
#     produtos = database.selecionar_produtos(session['email'])
#     return render_template('home.html', produtos = produtos)





if __name__ == '__main__':
    app.run(debug=True)