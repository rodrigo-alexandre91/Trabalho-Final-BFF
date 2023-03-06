from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
apiKey = 'a52d564a84702ae0175b97bb00f173af';

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github')
def github():
    if 'usuario' in request.args and request.args.get('usuario') != '':
        usuario = request.args.get('usuario')
        respGit = requests.get('https://api.github.com/users/' + usuario)
        jsonGit = respGit.json()
        if 'message' in jsonGit:
            return jsonify({'message':'Usuario não localizado'}), 404
        resp = {
            'nome': jsonGit.get('name'),
            'usuario': jsonGit.get('login'),
            'bio': jsonGit.get('bio'),
            'local': jsonGit.get('location'),
            'foto': jsonGit.get('avatar_url'),
        }
        return jsonify(resp), 200
    
    return jsonify({'message':'Bad request'}), 400

@app.route('/searchfilme')
def searchfilme():
    if 'filme' in request.args and request.args.get('filme') != '':
        filme = request.args.get('filme')

        urlSearch = 'https://api.themoviedb.org/3/search/movie?api_key=a52d564a84702ae0175b97bb00f173af&query=' + filme
        respSearch = requests.get(urlSearch)
        jsonSearch = respSearch.json()
        if jsonSearch.get('total_results') == 0:
            return jsonify({'message':'Nenhum filme localizado'}), 404      
        
        urlSimilar = 'https://api.themoviedb.org/3/movie/' + str(jsonSearch.get('results')[0].get('id')) + '/similar?api_key=a52d564a84702ae0175b97bb00f173af&language=en-US&page=1'
        respSimilar = requests.get(urlSimilar)
        jsonSimilar = respSimilar.json()

        resp = {
            'titulo': jsonSearch.get('results')[0].get('original_title'),
            'data': jsonSearch.get('results')[0].get('release_date'),
            'foto': 'https://image.tmdb.org/t/p/w500' + jsonSearch.get('results')[0].get('poster_path'),
            'nota': jsonSearch.get('results')[0].get('vote_average'),
            'descricao': jsonSearch.get('results')[0].get('overview'),
            'similar': [
                {
                    'titulo': jsonSimilar.get('results')[0].get('original_title'),
                    'foto': 'https://image.tmdb.org/t/p/w500' + jsonSimilar.get('results')[0].get('poster_path'),
                },
                {
                    'titulo': jsonSimilar.get('results')[1].get('original_title'),
                    'foto': 'https://image.tmdb.org/t/p/w500' + jsonSimilar.get('results')[1].get('poster_path'),
                },
                {
                    'titulo': jsonSimilar.get('results')[2].get('original_title'),
                    'foto': 'https://image.tmdb.org/t/p/w500' + jsonSimilar.get('results')[2].get('poster_path'),
                },
            ]
        }
        return jsonify(resp), 200
    return jsonify({'message':'Bad request'}), 400

@app.route('/jinja')
def jinja():
    respFilme = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=a52d564a84702ae0175b97bb00f173af&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate')
    jsonFilme = respFilme.json()

    filmes = []
    if jsonFilme.get('results') is None:
        return render_template('gitJinja.html', erro = 'Falha ao buscar na api')
    for i in range(18):
        filmes.append({
            'titulo': jsonFilme.get('results')[i].get('original_title'),
            'foto': 'https://image.tmdb.org/t/p/w500' + jsonFilme.get('results')[i].get('poster_path'),
        })

    return render_template('gitJinja.html', filmes = filmes)

app.run(debug=True)