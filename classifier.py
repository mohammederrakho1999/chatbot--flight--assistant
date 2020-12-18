# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:43:08 2020

@author: mohammed errakho
"""
import numpy as np
import pandas as pd
from spacy.lang.en import English
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle

data = pd.read_csv("../input/atis-airlinetravelinformationsystem/atis_intents_train.csv").values
data_test = pd.read_csv("../input/atis-airlinetravelinformationsystem/atis_intents_test.csv").values

def load_atis_data():
    """
    load the data and split the target variable from the predictor
    """
    data = pd.read_csv("../input/atis-airlinetravelinformationsystem/atis_intents_train.csv")
    X = data[:,1]
    y = data[:,0]
    return X,y

def tokenize(text):
    """
    split the text into words and return an array
    """
    new = []
    tokens = parser(text)
    for token in tokens:
        new.append(token.lemma_.lower().strip())
    return new

def model():
    """
    construct a random forest classifier and return it
    """
    parser = English()
    vectorizer = CountVectorizer(tokenizer = tokenize, ngram_range = (1,1))
    X, y = load_atis_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    classifier = RandomForestClassifier(n_estimators = 100)
    model = Pipeline([("vectorizer", vectorizer),("classifier", classifier)])
    model.fit(X_train, y_train)

    return model

def validation(model, X_test, y_test):
    
    y_pred = model.predict(X_test)
    n_correct = 0
    
    for i in range(len(y_test)):
        if y_pred[i] == y_test[i]:
            n_correct += 1
            
    print("Predicted {0} correctly out of {1} training examples".format(n_correct, len(y_test)))
    
X_test, y_test = data_test[:,1], data_test[:,0]

if __name__ == "__main__":
    
    model = model()
    validation(model, X_test, y_test)
    
    print("pickling model .....")
    
    with open("classifier.pkl","wb") as f:
        pickle.dump(model, f)