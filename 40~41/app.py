from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import requests
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "minha_chave_secreta"

def get_db():
    conn = sqlite3.connect("tarefas.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conn = get_db()
        user = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user["senha"], senha):
            session["usuario_id"] = user["id"]
            return redirect(url_for("dashboard"))
        else:
            flash("Login inválido!")
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = generate_password_hash(request.form["senha"])

        conn = get_db()
        conn.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()

        flash("Usuário registrado com sucesso!")
        return redirect(url_for("login"))
    return render_template("registro.html")

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    usuario_id = session["usuario_id"]
    conn = get_db()
    tarefas = conn.execute("SELECT * FROM tarefas WHERE usuario_id = ?", (usuario_id,)).fetchall()
    conn.close()

    frase = requests.get("https://api.adviceslip.com/advice").json()["slip"]["advice"]

    return render_template("dashboard.html", tarefas=tarefas, frase=frase)

@app.route("/nova_tarefa", methods=["GET", "POST"])
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = "Pendente"
        usuario_id = session["usuario_id"]

        conn = get_db()
        conn.execute("INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)",
                     (titulo, descricao, status, usuario_id))
        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))
    return render_template("nova_tarefa.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = get_db()
    tarefa = conn.execute("SELECT * FROM tarefas WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]

        conn.execute("UPDATE tarefas SET titulo=?, descricao=?, status=? WHERE id=?",
                     (titulo, descricao, status, id))
        conn.commit()
        conn.close()
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("editar_tarefa.html", tarefa=tarefa)

@app.route("/excluir/<int:id>")
def excluir(id):
    conn = get_db()
    conn.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

