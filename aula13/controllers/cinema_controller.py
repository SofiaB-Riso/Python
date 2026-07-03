from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for

from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")

@cinema_bp.route("/")
def index():
    return render_template("cinema/lista_sessoes.html", sessoes=Sessao.listar_com_detalhes())


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":

        data_hora_string = request.form.get("data_hora")
        data_hora_objeto = datetime.fromisoformat(data_hora_string) if data_hora_string else None


        sessao = Sessao(
            filme_id=request.form.get("filme_id"),
            sala_id=request.form.get("sala_id"),
            data_hora=data_hora_objeto,
            preco=request.form.get("preco")
            )
        
        db.session.add(sessao)
        db.session.commit()

        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
