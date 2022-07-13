from flask import render_template
from . import bp as app

@app.route("/blog")
def blog():
    return render_template('blog.html')