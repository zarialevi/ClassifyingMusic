import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

labelencoder = LabelEncoder()

import api

def full_clean():
    df_r = pd.read_csv('data/more_reggae_done.csv')
    df_s = pd.read_csv('data/more_soca_done.csv')
    df_d = pd.read_csv('data/more_dance_done.csv')
    df_p = pd.read_csv('data/random_done.csv')
    df_f = pd.read_csv('data/full_working.csv') 
    df_m = pd.read_csv('data/fuller.csv')
    
    df_r['genre'] = 'reggae'
    df_s['genre'] = 'soca'
    df_d['genre'] = 'dancehall'
    df_p['genre'] = 'pop'
    
    df = pd.concat([df_r, df_s, df_d, df_p, df_f, df_m], sort=True)
    
    df.drop_duplicates(subset='track_id', keep='first', inplace=True)
    df.fillna(value=0, inplace=True)
    df.reset_index(inplace=True)
    
    return df
    
#     df.to_csv('data/working.csv', index=False)
    
    
def XySplit(df):
    y = df['genre']
    X = df.drop(columns=['genre','track_id'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state=123)
    
    return X_train, X_test, y_train, y_test  