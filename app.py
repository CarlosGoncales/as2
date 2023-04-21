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
        	"""<h2> Calculadora do Dobro!!! </h2>"""
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

@app.route("/<string:script>")
def run(script):
    script=request.args.get("script", "")
    return (
	"""<h2> Run! 🕸 </h2>"""
	"""<form action="" method="get">
                <input type="text" name="script">
                <input type="submit" value="Run">
            </form>"""
    + '<a id="script">' + script + '</a>'
) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
     #app.run(host="0.0.0.0", port=8080, debug=False)
