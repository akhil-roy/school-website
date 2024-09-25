import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/foundation')
def foundation():
    return render_template('foundation.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/gallery')
def gallery():

    image_names= os.listdir('static/images/gallery/others')
    acad_images= os.listdir('static/images/gallery/academics')
    even_images= os.listdir('static/images/gallery/events')
    infra_images= os.listdir('static/images/gallery/infrastructure')
    sport_images= os.listdir('static/images/gallery/sports')
    depart_images= os.listdir('static/images/gallery/departments')

    return render_template('gallery.html', image_names=image_names, acad_images=acad_images, even_images=even_images, infra_images=infra_images, sport_images=sport_images, depart_images=depart_images) 

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)
