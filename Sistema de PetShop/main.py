import os

from flask import Flask, flash, redirect, render_template, request, url_for

from repositories.dados import Servicos_Disponiveis
from services.petshop_service import (
    cadastrar_cliente_com_pet,
    clientes_com_pets,
    obter_resumo,
)


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "petshop-dev-key")


@app.get("/")
def homepage():
    return render_template(
        "index.html",
        resumo=obter_resumo(),
        clientes=clientes_com_pets(),
        servicos=Servicos_Disponiveis,
    )


@app.post("/cadastros")
def cadastrar():
    try:
        cadastrar_cliente_com_pet(
            nome=request.form.get("nome", ""),
            documento=request.form.get("documento", ""),
            telefone=request.form.get("telefone", ""),
            endereco=request.form.get("endereco", ""),
            nome_pet=request.form.get("nome_pet", ""),
            tipo_pet=request.form.get("tipo_pet", ""),
            servico_id=request.form.get("servico_id", ""),
        )
        flash("Cliente e pet cadastrados com sucesso.", "success")
    except ValueError as erro:
        flash(str(erro), "error")

    return redirect(url_for("homepage"))


if __name__ == "__main__":
    app.run(debug=True)
