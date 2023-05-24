from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def greeting():
    """
    Index page.
    """
    return render_template('greeting.html')

@app.get('/home')
def home(lang='pt'):
    """
    Main page.
    """
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'home.html',
        page='home',
        lang=lang
        )

@app.get('/bio')
def bio(lang='pt'):
    """
    About myself page.
    """
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'bio.html',
        page='bio',
        lang=lang
    )

@app.get('/jobs')
def jobs(lang='pt'):
    """
    Portfolio page.
    """
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'jobs.html',
        page='jobs',
        lang=lang
        )

@app.get('/resume')
def resume(lang='pt'):
    """
    Displays resume page.
    """
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'resume.html',
        page='resume',
        lang=lang
        )


if __name__ == "__main__":
    app.run(debug=True)
