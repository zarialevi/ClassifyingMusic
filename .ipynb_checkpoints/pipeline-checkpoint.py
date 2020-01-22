from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn import tree
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, f1_score, roc_curve, auc, accuracy_score, roc_auc_score
from xgboost.sklearn import XGBClassifier

from yellowbrick.classifier import ROCAUC
from yellowbrick.datasets import load_game

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 999)
pd.set_option('display.max_rows', 90)


pipe_lr_1 = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=5)),
                    ('log', OneVsRestClassifier(LogisticRegression(random_state=123, solver='saga')))])
    
pipe_lr_2 = Pipeline([('scl', StandardScaler()),
                ('pca', PCA(n_components=5)),
                ('log', OneVsRestClassifier(LogisticRegression(random_state=123, multi_class='multinomial', class_weight='balanced')))])

pipe_dt = Pipeline([('scl', StandardScaler()),
                ('tree', tree.DecisionTreeClassifier(random_state=123))])    
    
pipe_bt = Pipeline([('scl', StandardScaler()),
                    ('bt', BaggingClassifier(tree.DecisionTreeClassifier(random_state = 123), random_state=123))])
    
pipe_knn = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=5)),
                    ('knn', KNeighborsClassifier())])
    
pipe_bo = Pipeline([('scl', StandardScaler()),
                    ('boo', AdaBoostClassifier(tree.DecisionTreeClassifier(random_state=123),random_state=123))])

pipe_xg = Pipeline([('scl', StandardScaler()),
                    ('xgb', XGBClassifier(random_state=123))])
    
pipe_gb = Pipeline([('scl', StandardScaler()),
                    ('gb', GradientBoostingClassifier(random_state=123))])


param_grid_lr_1 = {'log__estimator__penalty':['elasticnet'],
                'log__estimator__max_iter':[100,200,300,400,500],
                 'log__estimator__l1_ratio':[0.2,0.4,0.6,0.8]
                 }

param_grid_lr_2 = {'log__estimator__penalty':['l2'],
                 'log__estimator__solver':['newton-cg','sag','lbfgs'],
                 'log__estimator__max_iter':[75,100,125,150]
                 }

param_grid_dt = {'tree__max_features':[6,8,10],
                 'tree__min_samples_leaf':[5,10,15],
                 'tree__max_depth':[3,4,5,6,7,8,9]  
             }    

param_grid_bt = {'bt__base_estimator__max_features':[6,8,10],
                 'bt__base_estimator__min_samples_leaf':[5,7,9],
                 'bt__base_estimator__max_depth':[10,11,12,13,14],
                 'bt__n_estimators':[10,12,14,16]
             }

param_grid_knn = {'knn__n_neighbors':[5,10,15,20],
                  'knn__leaf_size':[40,50,60,70],
                  'knn__algorithm':['auto', 'ball_tree', 'kd_tree','brute']
                    }


param_grid_bo = {'boo__learning_rate':[0.2,0.4,0.6],
                 'boo__n_estimators':[5,10,15],
                 'boo__base_estimator__max_features':[6,8,10],
                 'boo__base_estimator__min_samples_leaf':[5,7,9],
                 'boo__base_estimator__max_depth':[10,11,12,13,14],
                 'boo__n_estimators':[10,12,14,16]
             }

param_grid_xg = {'xgb__booster':['gbtree', 'gblinear','dart'],
                 'xgb__learning_rate':[0.1,0.2,0.3,0.4,0.5],
                 'xgb__max_depth':[10,15,20],
                 'xgb__subsample':[.25,.5,.75]
                }

param_grid_gb = {'gb__n_estimators':[100,200,300,400],
                 'gb__learning_rate':[0.01,0.05,0.1],
                 'gb__max_depth':[3,5,7,9]
                }


def base_model(X_train, y_train,X_test, y_test):
    model = LogisticRegression(multi_class='auto',solver='lbfgs')
    visualizer = ROCAUC(model, classes=['dancehall','reggae','soca'])

    visualizer.fit(X_train, y_train)
    visualizer.score(X_test, y_test)
    visualizer.show() 

def fit_pipe(pipes, X_train, y_train):
    for pip in pipes:
        pip.fit(X_train, y_train)
        pipe = pip.best_estimator_
        

        # # Compare accuracies
    for idx, val in enumerate(pipes):
         print('%s pipeline test accuracy: %.4f' % (pipe_dict[idx], val.score(X_test, y_test)))
            
    return pipes

def best_pipe(pipes, pipe_dict):
    # Identify the most accurate model on test data
    best_acc = 0.0
    best_clf = 0
    best_pipe = ''
    for idx, val in enumerate(pipes):
        if val.score(X_test, y_test) > best_acc:
            best_acc = val.score(X_test, y_test)
            best_pipe = val
            best_clf = idx

    # Save pipeline to file
    joblib.dump(best_pipe, 'best_pipeline.pkl', compress=1)
    print('Saved %s pipeline to file' % pipe_dict[best_clf])
    
    return best_pipe

def best_model(model):
    visualizer = ROCAUC(model, classes=['reggae','soca','dancehall'])
    visualizer.fit(X_train, y_train)
    visualizer.score(X_test, y_test)
    visualizer.show() 


def full_pipeline(X_train, y_train, X_test, y_test):
    
    gs_lr_1 = GridSearchCV(pipe_lr_1, param_grid_lr_1, cv=5)

    gs_lr_2 = GridSearchCV(pipe_lr_2, param_grid_lr_2, cv=5)

    gs_dt = GridSearchCV(pipe_dt, param_grid_dt, cv=5)

    gs_bt = GridSearchCV(pipe_bt, param_grid_bt, cv=5)

    gs_knn = GridSearchCV(pipe_knn, param_grid_knn, cv=5)

    gs_bo = GridSearchCV(pipe_bo, param_grid_bo, cv=5)

    gs_xg = GridSearchCV(pipe_xg, param_grid_xg, cv=5)

    gs_gb = GridSearchCV(pipe_gb, param_grid_gb, cv=5)
    
    pipes = [gs_lr_1, gs_lr_2, gs_dt, gs_bt, gs_knn, gs_bo, gs_xg, gs_gb]
    
    fit_pipe(pipes, X_train, y_train)

    pipe_dict = {0: 'Log Reg Elastic', 1: 'Log Reg Laso', 2: 'Decision Tree', 3: 'Bagged Tree', 4: 'K Nearest',
                5: 'AdaBoost', 6: 'XGBoost', 7: 'Grad Boost'}
    
    best_pipe = best_pipe(pipes, pipe_dict)
    
    best_model(best_pipe)