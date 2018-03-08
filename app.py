from loginform import LoginForm
from flask import Flask, request, render_template
import pyrebase


app = Flask(__name__)

config = {
  "apiKey": "AIzaSyBarjxK5kmEF7tnZIO9tpIF4t9FzBnsfjk",
  "authDomain": "bhive-5f732.firebaseapp.com",
  "databaseURL": "https://bhive-5f732.firebaseio.com",
  "storageBucket": "bhive-5f732",
  "serviceAccount": "377032490280"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database(app)


@app.route('/')
def index():
    return render_template('user.html')


class User(UserMixin):
    def __init__(self, email, id, active=True):
        self.email = email
        self.id = id
        self.active = active

    def is_active(self):
        return self.active


@login_manager.user_loader
def load_user(user_id):
    usr = db.child("users").order_by_child("id").equal_to(user_id).get()
    return User(usr['email'], usr['id'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = auth.sign_in_with_email_and_password(form.email.data,     form.password.data)
            login_user(load_user(user['localId']))

            return redirect(url_for('a-login-restricted-page'))

    return render_template('login-form.html', form=form)


@app.route('/hives')
def hives():
    return render_template("hives.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "Your probably using GET"


@app.route('/signup')
def login():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
