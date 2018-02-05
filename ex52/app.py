#-*- coding: utf-8 -*-
from flask import Flask, session, request
from flask import url_for, redirect, render_template
import pickle
import new_map
import map

app = Flask(__name__)

games = [map, new_map]
map = None

	
#OLD LOGIN
#@app.route('/', methods=['GET', 'POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if request.form['username'] != 'PythonPro' or request.form['password'] != 'SuperSecret':
#            error = 'Wrong username or password. Please try again.'
#        else:
#            return redirect(url_for('index_get'))
#    return render_template('login.html', error=error)
#Login Page is opened as first page when going to your localhost on port 5001
#When login=correct you get redirected to the Homepage - localhost/home - if not, you have to try again
#Login Source: https://realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page/


@app.route('/', methods = ['GET'])
def verify_user():
    if 'user' in session:
        return redirect(url_for('index_get'))
    else:
        return redirect(url_for('login'))

#LOGIN
@app.route('/login', methods = ['GET'])
def login():
    if 'user' in session:
        return redirect(url_for('index_get'))
    else:
        return render_template('login.html')
        
@app.route('/login', methods = ['POST'])
def userdata():
    users = []
    username = request.form.get('username')
    password = request.form.get('password')
    with open('user_index.txt', 'r') as ui:
        users = pickle.loads(ui.read())
        print users
    try:
        users[username]
    except KeyError:
        return render-template('login.html', message = 'User does not exist.')
    else:
        if users[username]==password:
            session['user'] = username
            return redirect(url_for('index_get'))
        else:
            return render_template('login.html', message = 'Wrong Password.')
#compares users input to usernames and passwords in text file: user_index.txt


#REGISTRATION
@app.route('/registration', methods = ['GET'])
def register():
    return render_template('registration.html')

@app.route('/registration', methods = ['POST'])
def mk_newUser():
    user = request.form.get('username')
    password = request.form.get('password')
    
    data = {user:password}
    with open('user_index.txt', 'r+') as ui:
    	try:
    		users = pickle.loads(ui.read())
    		ui.seek(0) #moves pointer position to the beginning of txt
    		ui.truncate()
    	except:
    		users = {}
        users.update(data)
        pickle.dump(users,ui)
    return render_template('registration.html', message = "Registration was succesfull!")
#writes user input (password and username) to txt file 


#LOGOUT
@app.route('/logout', methods = ['GET'])
def logout():
    if 'user' in session:
    	del session['user']
    	return render_template('logout.html')


#GAME SELECTION
@app.route('/home', methods=['GET'])
def index_get():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def index_post():
    chosen_map = request.form.get('whichgame') 
    if chosen_map is None:
    	#that's the case when hacked
        return render_template('warning.html'), 400
    else:
        global map
        map = games[int(chosen_map)]
        session['scene'] = map.START.urlname
        return redirect(url_for('game_get'))
#on the homepage you are able to decide which game you'd like to play
#in the corresponding index.html, each game is ascribe a value
#depending on the game you choose the value is used here: (int(chosen_map)), to start the right game


#GAME START    
@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
    	if map is not None:
        	thescene = map.SCENES[session['scene']]
        	return render_template('show_scene.html', scene=thescene, background = map.BACKGROUND)
        else:
        	return render_template('no_session.html')   	
    else:
        #if user doesn't have a session it's because he did't enter the game at the beginning
        #as a consequence the game needs to redirect the user to the beginning:
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

#the last two blocks of code initiate the game chosen by the player
#depending on your choice, map.py or new_map.py - here both declared as map - and their respective scenes are executed

app.secret_key = '\xce\xd55\xb2\xd0j.z\x80\x16\xb3\x14\x86\x9d\xbd\xbf}g$Y\xacE\xf9\x1b'

if __name__ == "__main__":
    app.run(port=5001) #this app runs only on port 5001 of your localhost