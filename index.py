from flask import Flask, render_template, request
import requests
import json

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

@app.get('/real_estate')
def real_estate(lang='pt'):
    """
    Real estate project page
    """
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'real_estate.html',
        page='real_estate',
        lang=lang
        )

@app.post('/real_estate')
def real_estate_post(lang='pt'):
    """
    Real estate project page
    """
    if request.form.get('lang'):
        lang = request.form.get('lang')

    # URL of the API endpoint
    url = "http://umbrelu.pythonanywhere.com/real_estate_estimator"

    # Prepare the JSON payload
    if lang in ('pt', 'es'):
        payload = {
            "input_feature": {
                "categoria": request.form.get("categoria"),
                "localizacao": request.form.get("localizacao"),
                "area-util": request.form.get("area-util"),
                "area-total": request.form.get("area-total"),
                "quantidade-quartos": request.form.get("quantidade-quartos"),
                "quantidade-banheiros": request.form.get("quantidade-banheiros"),
                "quantidade-vagas": request.form.get("quantidade-vagas")
            },
            "parse": "brazil"
        }
    else:
        payload = {
            "input_feature": {
                "categoria": request.form.get("categoria"),
                "localizacao": request.form.get("localizacao"),
                "area-util": request.form.get("area-util"),
                "area-total": request.form.get("area-total"),
                "quantidade-quartos": request.form.get("quantidade-quartos"),
                "quantidade-banheiros": request.form.get("quantidade-banheiros"),
                "quantidade-vagas": request.form.get("quantidade-vagas")
            },
            "parse": "international"
        }

    # Convert payload to JSON string
    json_payload = json.dumps(payload)

    # Set the headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, data=json_payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return render_template(
            'real_estate.html',
            page='real_estate',
            lang=lang,
            prediction=response_data["prediction"],
            query=payload["input_feature"]
            )
    else:
        return render_template(
            'real_estate.html',
            page='real_estate',
            lang=lang,
            unsuccessful=True
            )

if __name__ == "__main__":
    app.run(debug=True)
