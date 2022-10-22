
from keras.models import Sequential
from keras.layers import Embedding,LSTM,Dense,Bidirectional
from keras.initializers import Constant
from keras.layers import BatchNormalization,GlobalMaxPool1D,Dropout


class model_creation:

    def __init__(self, embedding_matrix , num_words):

        self.embedding_matrix = embedding_matrix
        self.num_words= num_words

    


    def model_create(self, embedding_matrix , num_words):

        model=Sequential()

        embedding=Embedding(num_words,100,embeddings_initializer=Constant(embedding_matrix),
                        input_length=200,trainable=False)

        model.add(embedding)

        model.add(Bidirectional(LSTM(128, return_sequences = True, recurrent_dropout=0.2)))
        model.add(GlobalMaxPool1D())
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(128, activation = "relu"))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation = "relu"))
        model.add(Dropout(0.5))
        model.add(Dense(2, activation = 'sigmoid'))
        model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        print(model.summary())
        return model



    def main(self):

        return self.model_create(self.embedding_matrix , self.num_words)
        