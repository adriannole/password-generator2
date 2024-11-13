from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/')
def index():
    password = generate_password()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
