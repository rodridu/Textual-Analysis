import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
model = tf.keras.models.load_model('saved_model')

# Check its architecture

tokenizer = Tokenizer()
test_word ="good"
tw = tokenizer.texts_to_sequences([test_word])
tw = pad_sequences(tw,maxlen=200)

prediction = int(model.predict(tw).round().item())

print(prediction)

model.save('ModelTry.h5')