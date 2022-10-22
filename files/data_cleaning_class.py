
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))
from string import digits
import re
import string





class data_cleaning:
  

  def __init__(self,X):

    
    self.X=X

  def main(self):
    self.X = self.X.apply(lambda x : x.lower())
    self.X = self.X.apply(lambda x : self.remove_stopwords(x))
    self.X =  self.X.apply(lambda x : self.remove_emoji(x))
    self.X =  self.X.apply(lambda x : self.remove_punct(x))
    self.X =  self.X.apply(lambda x : self.number_removal(x))
    return self.X

    
    

  # Removing the stopwords from text
  def remove_stopwords(self,text):
      final_text = []
      for i in text.split():
          if i.strip().lower() not in stop:
              final_text.append(i.strip())
      return " ".join(final_text)


  # Removing emojis

  def remove_emoji(self,text):
      emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
      return emoji_pattern.sub(r'', text)



  # Removing punctuations


  def remove_punct(self,text):
      table=str.maketrans('','',string.punctuation)
      return text.translate(table)

  # Removing numbers


  def number_removal(self,text):
      remove_digits = str.maketrans('', '', digits)
      return text.translate(remove_digits)