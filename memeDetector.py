import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json
import json




def textEncoder(text, mapper):
    words = kpt.text_to_word_sequence(text)
    temp = []
    for word in words:
        if word in mapper:
            temp.append(mapper[word])
    return temp

if __name__ == "__main__":
    tok = Tokenizer(num_words=2500)
    cats = ['Meme','News Title']
    
    #read in saved map
    with open('data_map.json','r') as m:
        mapper = json.load(m)

    f1 = open('newsMeme.json','r')
    model = f1.read()
    f1.close()
    
    model = model_from_json(model)
    model.load_weights('newsMeme.h5')

    while True:
        i = raw_input('Enter Phrase: ')
        
        if len(i) == 0:
            break; 
    

        a = textEncoder(i,mapper)
        b = tok.sequences_to_matrix([a], mode='binary')

        result = model.predict(b)
        

        print("%s:%f%%" % (cats[np.argmax(result)], result[0][np.argmax(result)] * 100))


