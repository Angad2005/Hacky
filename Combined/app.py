from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure random key

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Since we removed sessions, we'll need to check credentials on each request
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if not user or not check_password_hash(user.password, password):
                flash('Please login first.', 'error')
                return redirect(url_for('login'))
        else:
            flash('Please login first.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return render_template("signup.html")
            
        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'error')
            return render_template("signup.html")
            
        hashed_password = generate_password_hash(password)
        new_user = User(firstname=firstname, lastname=lastname, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route("/logout")
def logout():
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route("/self_guide", methods=['GET', 'POST'])

def self_guide():
    return render_template("self_guide.html")

@app.route("/books")
def books():
    return render_template("book.html")
@app.route("/games")
def games():
    return render_template("gamesindex.html")

@app.route("/games1")
def games1():
    return render_template("click10shells.html")

@app.route("/games2")
def games2():
    return render_template("locksmithPuzzle.html")

@app.route("/games3")
def games3():
    return render_template("pathfinderquest.html")

@app.route("/games4")
def games4():
    return render_template("ritualreset.html")

@app.route("/games5")
def games5():
    return render_template("symmetrysketch.html")

@app.route("/games6")
def games6():
    return render_template("threadtheneedle.html")

@app.route("/musicplayer", methods=['GET', 'POST'])

def music_player():
    return render_template("Playlist_English.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)