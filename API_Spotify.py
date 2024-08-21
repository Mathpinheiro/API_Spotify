
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from collections import Counter

# Credenciamento do Spotify
client_id = ''
client_secret = ''

from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

client_id = SPOTIFY_CLIENT_ID
client_secret = SPOTIFY_CLIENT_SECRET


# Autenticação API do Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Lista dos artistas e IDs
artists_ids = {
    "Ed Sheeran": '6eUKZXaKkcviH0Ku9w2n3V',
    'Queen': "1dfeR4HaWDbWqFHLkxsg1d",
    'Ariana Grande': '66CXWjxzNUsdJxJ2JdwvnR',
    'Maroon 5': "04gDigrS5kc9YWfZHwBETP",
    "Imagine Dragons": '53XhwfbYqKCa1cC15pYq2q',
    "Eminem": "7dGJo4pcD2V6oG8kP0tJRR",
    "Lady Gaga": "1HY2Jd0NmPuamShAr6KMms",
    "Cold Play": "4gzpq5DPGxSnKTe4SA8HAU",
    "Beyonce": "6vWDO969PvNqNYHIOW5v0m",
    "Bruno Mars": "0du5cEVh5yTK9QJze8zA0C",
    "Rihanna": "5pKCCKE2ajJHZ9KAiaK11H",
    "Shakira": "0EmeFodog0BfCgMzAIvKQp",
    "Justin Bieber": "1uNFoZAHBGtllmzznpCI3s",
    "Demi Lovato": "6S2OmqARrzebs0tKUEyXyp",
    "Taylor Swift": "06HL4z0CvFAxyc27GXpf02"
}


artists_input = []
for artist_name, artist_id in artists_ids.items():
    artist_info = sp.artist(artist_id)
    artists_input.append({
        "name": artist_info['name'],
        "followers": artist_info['followers']['total'],
        "popularity": artist_info['popularity'],
        "genres": artist_info['genres']
    })


for artist in artists_input:
    print(artist)

# Filtrando os artistas e colocando em ordem
pop_artists = [artist for artist in artists_input if "pop" in artist['genres']]
pop_artists_sorted = sorted(pop_artists, key=lambda x: x['followers'], reverse=True)

# Contando os gêneros mais comuns
all_genres = [genre for artist in artists_input for genre in artist['genres']]
most_common_genres = Counter(all_genres).most_common(5)


print("Artistas do gênero 'pop' ordenados por número de seguidores:")

for artist in pop_artists_sorted:
    print(artist['name'], artist['followers'], artist['popularity'])

print("\n5 Gêneros mais comuns:")

for genre, count in most_common_genres:
    print(genre, count)

endpoint_url = "http://seu-endpoint.com/api"

data_to_send = {
    "pop_artists": pop_artists_sorted,
    "common_genres": most_common_genres
}

response = requests.post(endpoint_url, json=data_to_send)

if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print(f"Falha ao enviar dados: {response.status_code}")

   
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pop_artists=pop_artists_sorted, common_genres=most_common_genres)

if __name__ == '__main__':
    app.run(debug=True)

                      
#POST endereçamento da solução

post_url = "https://psel-solution-automation-cf-ubqz773kaq-uc.a.run.app?access_token=bC2lWA5c7mt1rSPR"

post_data = {
    "github_url": "https://github.com/Mathpinheiro/API_Spotify",
    "name": "Matheus Pinheiro de Souza",
    "pop_ranking": [
        {"artist_name": artist['name'], "followers": artist['followers']} for artist in pop_artists_sorted
    ],
    "genre_ranking": most_common_genres
}

response = requests.post(post_url, json=post_data)

if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print(f"Erro ao enviar dados: {response.status_code}")



                         


