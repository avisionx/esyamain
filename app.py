from flask import Flask, render_template, abort, jsonify
from blogData import blogJson
from hackData import hackJson
from cseData import cseJson
from eceData import eceJson
from nontechData import nontechJson
from workshopData import workshopJson
from talkData import talkJson
from festSponsors import festSponsors
from mediaPartData import mediaPartJson

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/privacy-policy")
def policy():
    return render_template('policy.html')

@app.route("/blogs/")
def blogs():
    return render_template('blogs.html', blogs = blogJson)

@app.route("/blog/<int:idB>")
def blog(idB):
    idAvailable = []
    for i in range(len(blogJson)):
        idAvailable.append(blogJson[i]['id'])
    if not(idB in idAvailable):
        abort(404)
    else:
        return render_template('blogpost.html', blog=blogJson[idB - 1])

@app.route("/events/")
def events():
    return render_template('events.html')

@app.route("/workshops/")
def workshops():
    return render_template('workshops.html', workshops=workshopJson)


@app.route("/workshop/<int:idE>")
def workshop(idE):
    idAvailable = []
    for i in range(len(workshopJson)):
        idAvailable.append(workshopJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('workshoppage.html', eventTypeLink="/workshops/", event=workshopJson[idE - 1])

@app.route("/talks/")
def talks():
    return render_template('talks.html', talks=talkJson)


@app.route("/talk/<int:idE>")
def talk(idE):
    idAvailable = []
    for i in range(len(talkJson)):
        idAvailable.append(talkJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('talkpage.html', eventTypeLink="/talks/", event=talkJson[idE - 1])

@app.route("/register/")
def register():
    return render_template('register.html')

@app.route("/event/hackathons/<int:idE>")
def hackathonEvent(idE):
    idAvailable = []
    for i in range(len(hackJson)):
        idAvailable.append(hackJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('eventpage.html', eventTypeLink="/events/#hackathons", event=hackJson[idE - 1])

@app.route("/event/cse/<int:idE>")
def cseEvent(idE):
    idAvailable = []
    for i in range(len(cseJson)):
        idAvailable.append(cseJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('eventpage.html', eventTypeLink="/events/#cse", event=cseJson[idE - 1])

@app.route("/event/ece/<int:idE>")
def eceEvent(idE):
    idAvailable = []
    for i in range(len(eceJson)):
        idAvailable.append(eceJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('eventpage.html', eventTypeLink="/events/#ece", event=eceJson[idE - 1])

@app.route("/event/nontech/<int:idE>")
def nontechEvent(idE):
    idAvailable = []
    for i in range(len(nontechJson)):
        idAvailable.append(nontechJson[i]['id'])
    if not(idE in idAvailable):
        abort(404)
    return render_template('eventpage.html', eventTypeLink="/events/#nontech", event=nontechJson[idE - 1])

@app.route("/api/event/<eventName>")
def eventDataApi(eventName):
    if(eventName == "hackathons"):
        return jsonify(hackJson)
    elif(eventName == "cse"):
        return jsonify(cseJson)
    elif(eventName == "ece"):
        return jsonify(eceJson)
    elif(eventName == "nontech"):
        return jsonify(nontechJson)
    return "404"

@app.route("/sponsors/")
def sponsors():
    return render_template('sponsors.html', sponsors=festSponsors, mediaSponsors=mediaPartJson)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8082)
