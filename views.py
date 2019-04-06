from timezoneUtil import UtcContainer, DefinedZones, PrepareZoneContainers
from flask import render_template, Request, json, jsonify, request
from markdownUtil import MarkdownGenerator
from FlaskWebProject import app
from misaka import HtmlRenderer, HtmlTocRenderer
from flask_misaka import markdown


@app.route("/")
def index():
    return render_template("markdownNoTOC.html", md = MarkdownGenerator("mainpage.md"))

@app.route("/contact")
def contact():
    return render_template("markdownNoTOC.html", md = MarkdownGenerator("contact.md"))

@app.route("/flask")
def flask():
    return render_template("markdownNoTOC.html", md = MarkdownGenerator("flask.md"))

@app.route("/atn")
@app.route("/arethrunotifier")
@app.route("/twitch")
def twitch():
    return render_template("markdown.html", md = MarkdownGenerator("twitch.md"))

@app.route("/winscripts")
def winscripts():
    return render_template("markdown.html", md = MarkdownGenerator("winscripts.md"))

@app.route("/prorem")
@app.route("/projectremembrance")
def prorem():
    return render_template("markdown.html", md = MarkdownGenerator("prorem.md"))

# Time app

@app.route("/timezones/get", methods=["GET"])
def getTimes():
    returnDict = {}
    for i in range(-11, 12):
        currentObj = UtcContainer(i)
        returnDict[currentObj.utcCode] = currentObj.currentTime

    zonelist = DefinedZones
    for v in zonelist.itervalues():
        v.SetTime()
        returnDict[v.zoneId] = v.time

    return jsonify(returnDict)

@app.route("/time") 
def timeApp():
    return render_template("timeapp.html", timelist = PrepareZoneContainers())