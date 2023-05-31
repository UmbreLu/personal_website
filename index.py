from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

category = {
    'apartamento': 'apartamentos',
    'casa': 'casas',
    'terreno': 'terrenos',
    'comercial': 'comerciais'
}

localizacao_form = [
    "Asa Sul",
    "Asa Norte",
    "Brasília, Distrito Federal",
    "Lago Sul",
    "Noroeste",
    "Lago Norte",
    "Octogonal",
    "Taguatinga",
    "Guará",
    "Sudoeste",
    "Park Way",
    "Sobradinho",
    "Cruzeiro",
    "Jardim Botânico",
    "Águas Claras",
    "Ceilandia",
    "Vila Planalto",
    "Setor Habitacional Tororo",
    "Setor de Mansões Dom Bosco",
    "Granja Do Torto, Brasília",
    "Vila Da Telebrasilia",
    "Zona Central de Brasília",
    "Park Sul",
    "Setor de Habitações Coletivas Norte",
    "Setor de Armazenagem e Abastecimento Norte",
    "Centro de Atividades do Lago Norte",
    "Taquari",
    "Jardins Mangueiral",
    "Quadra Mista Sudoeste",
    "Setor De Autarquias Sul",
    "Samambaia",
    "Mansões do Lago",
    "Setor De Clubes Esportivos Sul, Brasília",
    "Guará",
    "Paranoá",
    "SIG - Setor De Industria Graficas",
    "Planaltina",
    "Recanto das Emas",
    "Candangolândia",
    "Noroeste",
    "Zona Rural",
    "Setor Militar Urbano",
    "Itapoã",
    "Zona Industrial",
    "Arniqueiras, Águas Claras",
    "Areal, Águas Claras",
    "Zona Rural, Águas Claras"
]

localizacao_decoder = [
    "Asa Sul, Brasília",
    "Asa Norte, Brasília",
    "Brasília, Distrito Federal",
    "Lago Sul, Brasília",
    "Noroeste, Brasília",
    "Lago Norte, Brasília",
    "Octogonal, Brasília",
    "Taguatinga, Brasília",
    "Guará, Brasília",
    "Sudoeste, Brasília",
    "Park Way, Brasília",
    "Sobradinho, Brasília",
    "Cruzeiro, Brasília",
    "Setor Habitacional Jardim Botânico, Brasília",
    "Águas Claras",
    "Ceilandia, Brasília",
    "Vila Planalto, Brasília",
    "Setor Habitacional Tororo, Brasília",
    "Setor de Mansões Dom Bosco, Brasília",
    "Granja Do Torto, Brasília",
    "Vila Da Telebrasilia, Brasília",
    "Centro, Brasília",
    "Park Sul, Brasília",
    "Setor de Habitações Coletivas Norte, Brasília",
    "Setor de Armazenagem e Abastecimento Norte, Brasília",
    "Centro de Atividades, Brasília",
    "Taquari, Brasília",
    "Setor Habitacional Jardins Mangueiral, Brasília",
    "Quadra Mista Sudoeste, Brasília",
    "Setor De Autarquias Sul, Brasília",
    "Samambaia, Brasília",
    "Mansões do Lago, Brasília",
    "Setor De Clubes Esportivos Sul, Brasília",
    "Guará, Brasília, Brasília",
    "Paranoá, Brasília",
    "SIG - Setor De Industria Graficas, Brasília",
    "Planaltina, Brasília",
    "Recanto das Emas, Brasília",
    "Candangolândia, Brasília",
    "Noroeste, Brasília, Brasília",
    "Zona Rural, Brasília",
    "Setor Militar Urbano, Brasília",
    "Itapoã, Brasília",
    "Zona Industrial, Brasília",
    "Arniqueiras, Águas Claras",
    "Areal, Águas Claras",
    "Zona Rural, Águas Claras"
]

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
    post method
    """
    data_entry = pd.DataFrame(
    {'category': category[request.form["categoria"]],
     'neighborhood': localizacao_decoder[localizacao_form.index(request.form["localizacao"])],
     'footage': request.form["area-util"],
     'total_footage': request.form["area-total"],
     'bedrooms': request.form["quantidade-quartos"],
     'bathrooms': request.form["quantidade-banheiros"],
     'parking_space': request.form["quantidade-vagas"]
    }, index=[0])
    with app.open_instance_resource('realestate_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with app.open_instance_resource('OH_encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    unencoded_cols = ['category', 'neighborhood']
    OH_cols = pd.DataFrame(encoder.transform(data_entry[unencoded_cols]))
    OH_cols.index = data_entry.index
    OH_cols.columns = encoder.get_feature_names_out()
    encoded_entry = data_entry.drop(unencoded_cols, axis=1)
    encoded_entry = pd.concat([encoded_entry, OH_cols], axis=1)
    prediction = 'R$ {:,.2f}'.format(
        model.predict(encoded_entry)[0]).replace(
            ',', '_').replace('.', ',').replace('_','.')
    if request.args.get('lang'):
        lang = request.args.get('lang')
    return render_template(
        'real_estate.html',
        page='real_estate',
        lang=lang,
        prediction=prediction
        )

if __name__ == "__main__":
    app.run(debug=True)
