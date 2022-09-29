from flask import Flask, render_template


app = Flask(__name__)

@app.get('/')
def greeting():
    """
    Index page.
    """
    return render_template('greeting.html')

@app.get('/home')
def home():
    """
    Main page.
    """
    return render_template('home.html')

@app.get('/bio')
def bio():
    """
    About myself page.
    """
    return render_template('bio.html')

@app.get('/contato.html')
def contato():
    """
    This is the contact page.
    """
    return render_template('contato.html')

@app.get('/jobs')
def jobs():
    """
    Portfolio page.
    """
    return render_template('jobs.html')

@app.get('/resume')
def resume():
    """
    Displays resume page.
    """
    return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True)
