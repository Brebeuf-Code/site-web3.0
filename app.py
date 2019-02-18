from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/qui')
def qui():
    return render_template("qui.html")


@app.route('/rencontres')
def rencontres():
    return render_template("rencontres.html")


@app.route('/ressources')
def ressources():
    return render_template("ressources.html")


@app.route('/competitions')
def competitions():
    return render_template("competitions.html")


@app.route('/projets')
def projets():
    return render_template("projets.html")

@app.route('/sociocode')
@app.route('/codesprint')
def codesprint():
        return render_template("codesprint.html")

@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
