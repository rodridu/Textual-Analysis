import tensorflow.python.training.saver

self = 'DataFinal1.csv'
import numpy as np
import pandas as pd
df = pd.read_csv(self)
sentiment_label = df.N_or_P.factorize()
#print(sentiment_label)
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
df = df.content.values
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df)
encoded_docs = tokenizer.texts_to_sequences(df)
vocab_size = len(tokenizer.word_index) + 1
padded_sequence = pad_sequences(encoded_docs,)

#print(padded_sequence[0])





from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, SpatialDropout1D
from keras.layers import Embedding
embedding_vector_length = 500
model = Sequential()
model.add(Embedding(vocab_size, embedding_vector_length))
model.add(SpatialDropout1D(0.25))
model.add(LSTM(10, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
#print(model.summary())


history = model.fit(padded_sequence,
                    sentiment_label[0],
                    validation_split=.2,
                    epochs=5,
                    batch_size=50)







model.save('saved_model')