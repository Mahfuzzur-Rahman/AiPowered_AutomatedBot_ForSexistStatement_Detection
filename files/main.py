#Import important library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
import model_class
import my_pipeline

## Rading dataset

df= pd.read_excel('F:\study\Data Science\Projects\sexist_comment\Data\ISEP Sexist Data labeling.xlsx')



def pipeline_completion(input_col):

    input_pl = my_pipeline.pipe_line(input_col)


    train , m , n  = input_pl.main()

    return train , m ,n


train , embedded_matrix, unique_numbers = pipeline_completion(df['Sentences'])
model_instance = model_class.model_creation(embedded_matrix , unique_numbers)
model = model_instance.main()

X_train,X_test,y_train,y_test=train_test_split(train,df['Label'].values,test_size=0.2)

history = model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=20,batch_size=64)

loss, accuracy = model.evaluate(X_test, y_test)
print('Loss:', loss)
print('Accuracy:', accuracy)

model.save("model.h5")
trained_model = load_model("model.h5")




def app_AI (df):

    train , embedded_matrix, unique_numbers = pipeline_completion(df)

    print("Input trainned seq : ", train)

    result = trained_model.predict(train)

    return result


def main_bot(msg):

    data_col = [{'Sentences' : msg}]
    input_dataframe = pd.DataFrame(data_col)
    predicted_result = app_AI (input_dataframe['Sentences'])
    main_result = np.argmax(predicted_result, axis=1)
    print(main_result[0])
    
    reply= "Safe"

    if main_result[0] == 1 :
            
        reply= "Warning"
        
    return reply



# data_col = [{'Sentences' : str(input("Input Sentence: "))}]

# input_dataframe = pd.DataFrame(data_col)

# print(input_dataframe['Sentences'][0])

# predicted_result = app_AI (input_dataframe['Sentences'])

# print("predicted Result: ", predicted_result)

# print(np.argmax(predicted_result, axis=1)) 














