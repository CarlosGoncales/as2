from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    valor = request.args.get("valor", "")
    if valor:
        resultado = operacao(valor)
    else:
        resultado = ""

    return (
        	"""<h2> Calculadora do Dobro!! </h2>"""
		"""<br>"""
		"""<form action="" method="get">
                <input type="text" name="valor">
                <input type="submit" value="Resultado">
            </form>"""
        + "Ultimo Valor digitado: "+valor+ '</br>'+
        "Dobro: " + '<a id="resultado">' +resultado+ '</a>'

    )
 
@app.route("/<int:valor>")
def operacao(valor):
    """Efetuado o dobro do numero"""
    resultado = float(valor) * 2
    return str(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
     #app.run(host="0.0.0.0", port=8080, debug=False)
