from flask import render_template
from app import app

# Chapter 2
@app.route('/program')
def program():
    return render_template('program.html', title='program')
