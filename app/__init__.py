from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/login")
    def login():
        return render_template('login.html')

    @app.route("/register")
    def register():
        return render_template('register.html')

    @app.route("/about")
    def about():
        return render_template('about.html')

    @app.route("/blog")
    def blog():
        return render_template('blog.html')

    return app