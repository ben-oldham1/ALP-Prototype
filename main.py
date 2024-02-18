from flask import Flask, render_template
 
# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)
 
# Decorator which tells the application which URL should call the associated function
@app.route('/')
def index():
    return '<h1>Visit <a href="/home">/home</a> page to get started</h1>';
    
@app.route('/login')
def login():
    return render_template('pages/login.html');
 
@app.route('/home')
def home():
    return render_template('pages/home.html');

@app.route('/moduleview')
def moduleView():
    return render_template('pages/moduleView.html');

@app.route('/lessonview')
def lessonView():
    return render_template('pages/lessonView.html');

# Main driver function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)