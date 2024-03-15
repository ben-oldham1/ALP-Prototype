# IMPORTANT
# This is the code provided by Hisham, it is NOT yet integrated into the main project, 
# which means it will run its own server when you execute it.
# Don't run this code at the same time as main.py, or it will not work 


from flask import Flask, request, render_template_string
from openai import OpenAI

app = Flask(__name__)

# you need an API Key: create one for your account
client = OpenAI(api_key='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')

@app.route('/', methods=['GET'])
def home():
    # Render a simple form for code submission
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Code Efficiency Analyser</title>
        </head>
        <body>
            <h2>Submit your Python code for efficiency analysis:</h2>
            <form action="/analyze-code" method="post">
                <textarea name="code_snippet" rows="10" cols="50" placeholder="Enter your Python code here..."></textarea><br>
                <input type="submit" value="Analyse Code">
            </form>
        </body>
        </html>
    """)

@app.route('/analyze-code', methods=['POST'])
def analyze_code():
    code_snippet = request.form['code_snippet']

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
          "role": "system",
          "content": "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements." ## Change this to instructions/improvement/analysis, etc. 
        },
        {
          "role": "user",
          "content": code_snippet
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    # Extracting the analysis or suggestion provided by the model
    suggestion = response.choices[0].message['content'] if response.choices else "No suggestion could be generated."

    # Displaying the result
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Analysis Result</title>
        </head>
        <body>
            <h2>Efficiency Analysis and Suggestions:</h2>
            <p>{{ suggestion }}</p>
            <a href="/">Submit another code snippet</a>
        </body>
        </html>
    """, suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)
