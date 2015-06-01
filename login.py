from bottle import Bottle, get, post, request, run, template, response, redirect, static_file # or route

apps = Bottle()

@apps.get('/login')  # or @route('/login')
def login():
    return template("login")
    # return '''
    #     <form action="/login" method="post">
    #         Username: <input name="username" type="text" />
    #         Password: <input name="password" type="password" />
    #         <input value="Login" type="submit" />
    #     </form>
    # '''

@apps.post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return redirect('http://gitserver.com/')
        # return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(name,passwd):
    return True

#Twitter Bootstrap Static Files

@apps.route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')

@apps.route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')

@apps.route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./css')

run(app=apps, host='localhost', port=8080, debug=True, reloader=True)