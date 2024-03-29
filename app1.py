"""Simple routing calculator."""

from flask import Flask
app = Flask("hello")


@app.route("/")
def index():
    """Gives user info how to use."""
    return "<h1>Use this calculator by typing the /add/*number*/*number in to the URL</h1>"


@app.route("/add/<float:number_1>/<float:number_2>")
def add(number_1, number_2):
    """Returns added value."""
    tulos = number_1 + number_2
    return "<h1> {}".format(number_1) + " +" + " {}".format(number_2) + " = " + "{}".format(tulos) + "</h1>"


@app.route("/sub/<float:number_1>/<float:number_2>")
def minus(number_1, number_2):
    """Returns subtracted value."""
    tulos = number_2 - number_1
    return "<h1> {}".format(number_2) + " -" + " {}".format(number_1) + " = " + "{}".format(tulos) + "</h1>"


@app.route("/mul/<float:number_1>/<float:number_2>")
def mult(number_1, number_2):
    """Returns multiplied value."""
    tulos = number_1 * number_2
    return "<h1> {}".format(number_1) + " *" + " {}".format(number_2) + " = " + "{}".format(tulos) + "</h1>"


@app.route("/div/<float:number_1>/<float:number_2>")
def div(number_1, number_2):
    """Returns divided value."""
    if number_2 == 0.0:
        return "<h1> {}".format(number_1) + " /" + " {}".format(number_2) + " = " + "NaN" + "</h1>"
    tulos = number_1 / number_2
    return "<h1> {}".format(number_1) + " /" + " {}".format(number_2) + " = " + "{}".format(tulos) + "</h1>"
