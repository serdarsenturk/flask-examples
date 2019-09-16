from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact')
def contactGet():
    return render_template('contact_get.html')

@app.route('/contact', methods = ['POST'])
def conctactPost():
    email = request.form.get('email')
    message = request.form.get('message')
    
    return render_template("contact_post.html", email = email, message = message)