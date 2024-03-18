from flask import Flask, render_template, request, jsonify
import chatbot_api
 
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

# API route to provide AI chatbot functionality
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']

    # Send user_message to the chatbot and get the response
    # Replace this with actual code to interact with your chosen chatbot framework or service

    chatbot_response = chatbot_api.query(user_message)

    return jsonify({'response': chatbot_response})

# Main driver function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)