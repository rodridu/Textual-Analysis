import pandas as pd
import re
import gensim
from nltk.tokenize.treebank import TreebankWordDetokenizer

import time

dataset = pd.read_csv("C:/Users/xl/Desktop/sentiment/DataFinal.csv")

def depure_data(data):
    
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    data = url_pattern.sub(r'', data)

    data = re.sub('\S*@\S*\s?', '', data)

    data = re.sub('\s+', ' ', data)

    data = re.sub("\'", "", data)
        
    return data

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence),deacc=True))

def detokenize(text):
    return TreebankWordDetokenizer().detokenize(text)



lexion_df = pd.read_excel('C:/Users/xl/Desktop/sentiment/NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx')
#lexion_df.info()

#English sentiment dictionary
english_dic = lexion_df[['English (en)','Positive','Negative','Anger','Anticipation','Disgust','Fear','Joy','Sadness','Surprise','Trust']]
Positive = []
Negative = []
Anger = []
Anticipation = []
Disgust = []
Fear = []
Joy = []
Sadness = []
Surprise = []
Trust = []
for idx, row in english_dic.iterrows():
    if row ['Positive']==1:
        Positive.append(row['English (en)'])
    if row ['Negative']==1:
        Negative.append(row['English (en)'])
    if row ['Anger']==1:
        Anger.append(row['English (en)'])
    if row ['Anticipation']==1:
        Anticipation.append(row['English (en)'])
    if row ['Disgust']==1:
        Disgust.append(row['English (en)'])
    if row ['Fear']==1:
        Fear.append(row['English (en)'])
    if row ['Joy']==1:
        Joy.append(row['English (en)'])
    if row ['Sadness']==1:
        Sadness.append(row['English (en)'])
    if row ['Surprise']==1:
        Surprise.append(row['English (en)'])
    if row ['Trust']==1:
        Trust.append(row['English (en)'])



def SentimentAnalysis(text):
    positive, negative, anger, anticipation, disgust, fear, joy, sadness, surprise, trust =[0 for i in range(10)]
    wordlist = text
    wordset=wordlist.split()
    for word in  wordset:
        freq = wordlist.count(word)
        if word in Positive:
            positive+=freq
        if word in Negative:
            negative+=freq
        if word in Anger:
            anger+=freq
        if word in Anticipation:
            anticipation+=freq
        if word in Disgust:
            disgust+=freq
        if word in Fear:
            fear+=freq
        if word in Joy:
            joy+=freq
        if word in Sadness:
            sadness+=freq
        if word in Surprise:
            surprise+=freq
        if word in Trust:
            trust+=freq

    emotion_info ={
        'positive': positive,
        'negative': negative,
        'anger': anger,
        'anticipation': anticipation,
        'disgust': disgust,
        'fear':fear,
        'joy':joy,
        'sadness':sadness,
        'surprise':surprise,
        'trust':trust,
        'length':len(wordlist)}
    
    score_list = list(emotion_info.values())
    return score_list

temp = []
#Splitting pd.Series to list
data_to_list = dataset['D.content'].values.tolist()
for i in range(len(data_to_list)):
    temp.append(depure_data(data_to_list[i]))
data_words = list(sent_to_words(temp))
data = []
for i in range(len(data_words)):
    data.append(detokenize(data_words[i]))
senti_array=[]
for i in range(0,len(data)):
    text = data[i]
    senti_array.append(SentimentAnalysis(text))
    print(i)
        
name = ['positive', 'negative', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust', 'length']
senresult = pd.DataFrame(columns=name, data=senti_array)
output = pd.concat([dataset,senresult],axis=1)
output.to_csv("C:/Users/xl/Desktop/sentiment/sentiment_output.csv",index=False)
