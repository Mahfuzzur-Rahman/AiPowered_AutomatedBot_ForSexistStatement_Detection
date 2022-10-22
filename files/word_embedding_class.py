import numpy as np
import nltk
from sklearn import metrics
nltk.download('stopwords')
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))

from tqdm import tqdm
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

class word_embedding_GloVe:

 


  def __init__(self,X):

    self.X=X

    

  def create_corpus(self,X):
    corpus=[]
    for sentence in tqdm(X):
        words=[word.lower() for word in word_tokenize(sentence) if((word.isalpha()==1) & (word not in stop))]
        corpus.append(words)
    return corpus

  


  def GloVe(self , corpus):


    embedding_dict={}

    with open('F:\study\Data Science\Projects\sexist_comment\glove_text\glove.6B.100d.txt','r', encoding="utf8") as f:
      for line in f:
          values=line.split()
          word=values[0]
          vectors=np.asarray(values[1:],'float32')
          embedding_dict[word]=vectors
    f.close()

    MAX_LEN=200
    tokenizer_obj=Tokenizer()
    tokenizer_obj.fit_on_texts(corpus)
    sequences=tokenizer_obj.texts_to_sequences(corpus)

    sentence_pad=pad_sequences(sequences,maxlen=MAX_LEN,truncating='post',padding='post')

    word_index=tokenizer_obj.word_index
    print('Number of unique words:',len(word_index))


    num_words=len(word_index)+1
    embedding_matrix=np.zeros((num_words,100))

    for word,i in tqdm(word_index.items()):
      if i > num_words:
          continue
      
      emb_vec=embedding_dict.get(word)
      if emb_vec is not None:
          embedding_matrix[i]=emb_vec



    return sentence_pad, embedding_matrix , num_words



  

  def main(self):

      corp = self.create_corpus(self.X)

      padded, matrix , num = self.GloVe (corp)

      

      return padded , matrix, num


  


              

  
  