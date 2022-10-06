from flask import Flask, render_template, request
from my_tools import Analytics 

app = Flask(__name__)
stats = Analytics('analytics.db')

@app.get('/')
def greeting():
    """
    Index page.
    """
    stats.analyse(request)
    print(type(request.endpoint))
    print(type(request.user_agent))
    return render_template('greeting.html')

@app.get('/home')
def home():
    """
    Main page.
    """
    stats.analyse(request)
    return render_template('home.html')

@app.get('/bio')
def bio():
    """
    About myself page.
    """
    stats.analyse(request)
    return render_template('bio.html')

@app.get('/contato.html')
def contato():
    """
    This is the contact page.
    """
    stats.analyse(request)
    return render_template('contato.html')

@app.get('/jobs')
def jobs():
    """
    Portfolio page.
    """
    stats.analyse(request)
    return render_template('jobs.html')

@app.get('/resume')
def resume():
    """
    Displays resume page.
    """
    stats.analyse(request)
    return render_template('resume.html')

@app.get('/analytics')
def analytics():
    """
    return analytics
    """
    return stats.analytics()

@app.get('/current')
def current():
    """
    returns todays' analytical records
    """
    return stats.current()

@app.get('/errorlog')
def errorlog():
    """
    returns the error_log.txt file
    """
    with open('error_log.txt', 'r+') as file:
        return file.read()
    return 'Something went wrong'


if __name__ == "__main__":
    app.run(debug=True)
