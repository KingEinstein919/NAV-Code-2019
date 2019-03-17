import random
from flask import Flask
from string import Template

app = Flask(__name__)
app.config["DEBUG"] = True



def caller (wifi):
    dic={}
    if wifi == 0:
        dic = {"Casino":random.randrange(0, 100), "Bar":random.randrange(0, 100),"Pool":random.randrange(0, 100)}
    elif wifi == 1:
        dic = {"Bar":random.randrange(0, 100), "Pool":random.randrange(0, 100),"Theater":random.randrange(0, 100)}
    elif wifi == 2:
        dic = {"Pool":random.randrange(0, 100), "Theater":random.randrange(0, 100),"Library":random.randrange(0, 100)}

    return (dic)

amey_in = random.randrange(0,2)

ans = caller(amey_in)

loc = list(ans.keys())

per = list(ans.values())

loc1 = loc[0]
per1 = per[0]
loc2 = loc[1]
per2 = per[1]
loc3 = loc[2]
per3 = per[2]

TEMPLATE = Template('''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>title</title>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
	<script
	src="https://code.jquery.com/jquery-3.1.1.min.js"
	integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
	crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
</head>
<body>
<!-- First Location Tile -->
<div class="ui card">
  <div class="image">
    <img src="https://images.unsplash.com/photo-1517232115160-ff93364542dd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=966&q=80" alt="Casino Image">
  </div>
  <div class="content">
    <a class="header">{{loc1}}</a>
    <div class="meta">
      <span class="date">A place to have fun. Only restriction is that you have to be 21 or older.</span>
    </div>
  </div>
  <div class="extra content">
    <a>
      <i class="user icon"></i>
      Capacity
    </a>
  </div>
  <div class="ui bottom attached progress" data-percent="75" id="bar1">
    <div class="bar"></div>
  </div>
</div>
<script>
    $('#bar1').progress({
  percent: {{per1}}
});
</script>

<!-- Second Location Tile -->
<div class="ui card">
  <div class="image">
    <img src="https://images.unsplash.com/photo-1505236732171-72a5b19c4981?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80" alt="Pool Image">
  </div>
  <div class="content">
    <a class="header">{{loc2}}</a>
    <div class="meta">
      <span class="date">An Aquatic wonderland where  patrons old and young may have the time of their lives.</span>
    </div>
  </div>
  <div class="extra content">
    <a>
      <i class="user icon"></i>
      Capacity
    </a>
  </div>
  <div class="ui bottom attached progress" data-percent="75" id="bar2">
    <div class="bar"></div>
  </div>
</div>
<script>
    $('#bar2').progress({
  percent: {{per2}}
});
</script>


<!-- Third Location Tile -->
<div class="ui card">
  <div class="image">
    <img src="https://images.unsplash.com/photo-1503803548695-c2a7b4a5b875?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80" alt="Viewing Deck View">
  </div>
  <div class="content">
    <a class="header">{{loc3}}</a>
    <div class="meta">
      <span class="date">A peaceful part of the ship where patrons can enjoy the mesmerizing views that nature has to offer.</span>
    </div>
  </div>
  <div class="extra content">
    <a>
      <i class="user icon"></i>
      Capacity
    </a>
  </div>
  <div class="ui bottom attached progress" data-percent="75" id="bar3">
    <div class="bar"></div>
  </div>
</div>
<script>
    $('#bar3').progress({
  percent: {{per3}}
});
</script>
</body>
</html>

''')

@app.route('/<WEEFEE>')
def home(WEEFEE):
    return (TEMPLATE.substitute(wifi=WEEFEE))
app.run(use_reloader=True)
