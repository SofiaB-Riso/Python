from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def questao1():
    return render_template("q1.html", name="Sofia")

@app.route("/idade")
def questao2():
    return render_template("q2.html", name="Sofia", age="17")

@app.route("/dados")
def questao3():
    return render_template("q3.html", complet="Sofia Braga Riso", age="17", mail ="carochina224@gmailcom")

@app.route('/alunos')
def alunos():
    alunos = [{"nome": "Ana"}, {"nome": "Cicero"}, {"nome": "Sofia"}]
    return render_template('q4.html', alunos=alunos)

@app.route('/notas')
def notas():
    alunos = [{"nome": "Ana", "nota" : 6}, {"nome": "Cicero", "nota":8.5}, {"nome": "Sofia", "nota":9}]
    return render_template('q5.html', alunos=alunos)


if __name__ == "__main__":
    app.run(debug=True)
