'''
Data de entrega: 09:50
Atividade Prática (Passo a Passo)
Esta atividade foca na montagem da estrutura física do projeto.
Criação do Ambiente:
Crie uma pasta chamada Aula3.
Crie a venv
Dentro da pasta Aula3, abra o terminal e instale o Flask: pip install flask.
Criação do Servidor:
Crie o arquivo app.py e cole o código de exemplo acima.

Criação do Front-end:
Crie uma pasta chamada templates.
Dentro de templates, crie um arquivo home.html.
Escreva qualquer mensagem no HTML (Ex: <h1>Bem-vindo ao meu primeiro site em Flask!</h1>).

Teste de Execução:

Rode o comando: python app.py.

Abra o navegador em: http://127.0.0.1:5000.

Desafio de Fixação:
Tente renomear a pasta templates para meus_arquivos e veja o erro que aparece no navegador. Depois, volte para o nome correto. Isso ajuda a memorizar a importância da convenção.

Antes de entregar rode no terminal python -m black caminhodoarquivo.py
'''
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def ola():
    return 'Preparado?? ao lado de \sobre na url digite \ e seu nome!!'

@app.route('/sobre/<nome>')
def sobre(nome):
    return  f'Oiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii {nome}'
@app.route('/') 

def decorator():
    return

if __name__ == '__main__':
    app.run(debug=True) 