#-*- coding: utf-8 -*-
from flask import Flask, session, request
from flask import url_for, redirect, render_template
import new_map
import map

app = Flask(__name__)

games = [map, new_map]
map = None

	

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'PythonPro' or request.form['password'] != 'SuperSecret':
            error = 'Wrong username or password. Please try again.'
        else:
            return redirect(url_for('index_get'))
    return render_template('login.html', error=error)
#https://realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page/


@app.route('/home', methods=['GET'])
def index_get():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def index_post():
    chosen_map = request.form.get('whichgame') 
    if chosen_map is None:
    	#when hacked
        return render_template('warning.html'), 400
    else:
        global map
        map = games[int(chosen_map)]
        session['scene'] = map.START.urlname
        return redirect(url_for('game_get')) #opens game_get


    
@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
    	if map is not None:
        	thescene = map.SCENES[session['scene']]
        	return render_template('show_scene.html', scene=thescene, background = map.BACKGROUND)
        else:
        	return render_template('cookie.html')   	
    else:
        #if user doesn't have a session it's because he did't enter the game at the beginning
        #the game needs to redirect the user to the beginning:
        return redirect(url_for("index_get"))


@app.route('/game', methods=['POST'])
def game_post():
	userinput = request.form.get('userinput')
	if 'scene' in session:
		if userinput is None:
			return redirect(url_for('game_get')) #opens game_get
		else:
			currentscene = map.SCENES[session['scene']]
			nextscene = currentscene.go(userinput)
			if nextscene is None:
				 return render_template('warning.html'), 400
			else:
				currentscene = map.SCENES[session['scene']]
            	nextscene = currentscene.go(userinput)
            	if nextscene is None:
                	return render_template('show_scene.html', scene=currentscene, background = map.BACKGROUND, unknown=1)
                else:
					session['scene'] = nextscene.urlname
					return render_template('show_scene.html', scene=nextscene, background = map.BACKGROUND)
	else:
		return redirect(url_for("index_get"))


app.secret_key = '\xce\xd55\xb2\xd0j.z\x80\x16\xb3\x14\x86\x9d\xbd\xbf}g$Y\xacE\xf9\x1b'

if __name__ == "__main__":
    app.run(port=5001)