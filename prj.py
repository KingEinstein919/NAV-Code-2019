from random import randint
from flask import Flask
from jinja2 import Template

app = Flask(__name__)
app.config["DEBUG"] = True

def caller (wifi):
    places = []
    wifi = int(wifi)
    if wifi == 0:
        places = ["Casino", "Bar" ,"Pool"]
    elif wifi == 1:
        places = ["Bar","Pool","Theater"]
    elif wifi == 2:
        places = ["Pool", "Theater","Library"]
    elif wifi == 3:
        places = ["Pool", "Bunjee","Casino"]
    return (places)

with open('template.jinja2') as temp:
    template = Template(temp.read())
@app.route('/<val>')
def home(val):
    return template.render(places=caller(val))
app.run(use_reloader=True)
