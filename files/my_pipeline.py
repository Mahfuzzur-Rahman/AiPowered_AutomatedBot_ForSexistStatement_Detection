import data_cleaning_class
import word_embedding_class



class pipe_line:

    def __init__(self, df_col) :

        self.df_col = df_col

        

    def main(self):

        cleaned_data_instance = data_cleaning_class.data_cleaning(self.df_col)

        cleaned_data = cleaned_data_instance.main()

        embedding_instance = word_embedding_class.word_embedding_GloVe(cleaned_data)

        padded_sequence , embedded_matrix , unique_numbers = embedding_instance.main()

        

        return padded_sequence,  embedded_matrix, unique_numbers








    
