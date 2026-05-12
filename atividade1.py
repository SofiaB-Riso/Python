'''
Crie uma aplicação Flask que contenha uma rota específica responsável por explicar o conceito de decorator em Python.
Requisitos
Crie uma rota acessível por meio do caminho: /decorator
Ao acessar essa rota no navegador, deve ser exibido um texto explicando:
O que é um decorator em Python
Para que ele serve
Como ele é utilizado no Flask (exemplo: @app.route)
'''

from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/')
def oi():
    return 'Acesse uma rota por meio do caminho: /decorator'
@app.route('/decorator') 
def decorator():
    return '"/" Isso é o decorator, ele é usado para mapear a função abaixo para a rota específica de um servidor web (como no Flask ou FastAPI). Basicamente, ele "avisa" ao framework que, sempre que alguém acessar aquele endereço no navegador, a função logo abaixo deve ser executada para entregar a resposta.'

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

