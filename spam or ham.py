#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import pickle


# In[4]:


df= pd.read_csv("spam.csv", encoding="latin-1")
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
# Features and Labels
df['label'] = df['class'].map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label']


# In[5]:


# Extract Feature With CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X) # Fit the Data


# In[7]:


pickle.dump(cv, open('tranform.pkl', 'wb'))


# In[8]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB


# In[9]:


clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
filename = r'C:\Users\prash\Desktop\data\NLP-Deployment-Heroku-master\Email spam or Ham\nlp_model.pkl'
pickle.dump(clf, open(filename, 'wb'))


# In[ ]:




