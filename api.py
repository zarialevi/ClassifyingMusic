import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests
import json
import pprint

import pandas as pd
pd.set_option('display.max_columns', 999)
pd.set_option('display.max_rows', 90)

import re



client_credentials_manager = SpotifyClientCredentials(client_id='472d9fe420af4222b7afdd11b9578446', client_secret='518bc9207d064855be7f6300ca080c76')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_auth():
    CLIENT_ID ='472d9fe420af4222b7afdd11b9578446'
    CLIENT_SECRET = '518bc9207d064855be7f6300ca080c76'

    credentials = SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET)

    token = credentials.get_access_token()
    return "Bearer " + token


def get_tracks_from_playlist(lst):
    df_list=[]
    for playlist in lst:
        r = requests.get(
        f"https://api.spotify.com/v1/playlists/{playlist}/tracks",
        headers={ "Accept": "application/json", "Content-Type": "application/json", "Authorization": get_auth()})
        dat =r.json()
        
        data = dat['items']
        tracks_list=[]
                
        for i in range(0,len(data)):
            if data[i]['track'] == None:
                continue
            else:
                tracks_list.append({
                    "track_name" : data[i]['track']['name'], 
                    "artist" : data[i]['track']['artists'][0]['name'],
                    "album" : data[i]['track']['album']['name'], 
                    "release_date" : data[i]['track']['album']['release_date'],
                    "explicit" : data[i]['track']['explicit'], 
                    "track_id" : data[i]['track']['id'],
                    "track_uri" : data[i]['track']['uri']
                })
        
        df_list.append(pd.DataFrame(tracks_list))
        
    tracks_df = pd.concat(df_list)
    tracks_df = tracks_df.reset_index()
    tracks_df.drop('index', axis = 1, inplace=True)
    return tracks_df

def get_playlists():
    r = requests.get("https://api.spotify.com/v1/users/loliblews/playlists",
                     headers={ "Accept": "application/json", "Content-Type": "application/json", "Authorization": get_auth()})
    data =r.json()

    playlists = []

    for x,y in enumerate(data['items']):
        playlists.append(data['items'][x]['id'])
        
    return playlists


def get_feats(df):

    feats = []

    for x in df.index:
        dat = sp.audio_features(tracks = df.track_id[x])
        data = dat[0]
        
        if data == None:
            continue
        else:
            feats.append({
                'danceability' : data['danceability'],
                'energy' : data['energy'],
                'key': data['key'],
                'loudness': data['loudness'],
                'mode': data['mode'],
                'speechiness': data['speechiness'],
                'acousticness': data['acousticness'],
                'instrumentalness': data['instrumentalness'],
                'liveness': data['liveness'],
                'valence': data['valence'],
                'tempo': data['tempo'],
                'type': 'audio_features',
                'id': data['id'],
                'uri': data['uri'],
                'track_href': data['track_href'],
                'analysis_url': data['analysis_url'],
                'duration_ms': data['duration_ms'],
                'time_signature': data['time_signature']
                    })
        
    df = pd.DataFrame(feats)
    
    return df

def get_artists_uri(lst):
    
    artists_edit = []

    for artist in lst:
            artists_edit.append(re.sub('\s+', '%20', artist))
        
    full = []

    for artist in artists_edit:
        r = requests.get(f"https://api.spotify.com/v1/search?q={artist}&type=artist",
                         headers={ "Accept": "application/json", "Content-Type": "application/json", "Authorization": 
                                  get_auth()})
        data =r.json()

        full.append(data)
    
    success = []

    
    for x in range(len(lst)):
        if (len(full[x]['artists']['items']) > 0):
            success.append({
                'name': full[x]['artists']['items'][0]['name'], 
                'uri': full[x]['artists']['items'][0]['uri']})
    
    for x in range(len(success)):
        success[x]['uri'] = success[x]['uri'][-22:] 
        
    df = pd.DataFrame(success)
    return df