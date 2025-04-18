import streamlit as st 
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Download the punkt tokenizer models
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
   

def Transform_text(text):
  #convert all text in lowercasepip install scikit-learn

  text = text.lower()

  #perform tokenizATION (WE CAN   done in two way using nltk libariy or using python built in fucntion split() let's use the libarary for more accuracy.)
  text = nltk.word_tokenize(text)

  # Removing special character.
  tem = []  #to store words temporaily

  for i in text:
    if i.isalnum():
      tem.append(i)

  # update text and clear tem nltk.download('punkt_tab')
  text = tem[:]
  tem.clear()

#  Removing stopwords and puntuation.
  from string import punctuation
  stopwords = nltk.corpus.stopwords.words('english')
  for i in text:
    if i not in stopwords and i not in punctuation:
      tem.append(i)

# update again
  text = tem[:]
  tem.clear()

# Perform steming
   
  from nltk.stem import PorterStemmer
  ps = PorterStemmer()
  for i in text:
    tem.append(ps.stem(i))

  #update again
  text = tem[:]
  tem.clear()

   

# REtrun transform text
  return " ".join(text)


# Title 
st.title("Email/SMS Detection")

# Import req things 
tfidf = pickle.load(open('Vectorizer.pkl', 'rb'))
model = pickle.load(open('Model.pkl', 'rb'))

# get msg to check 
input_sms = st.text_area("Enter the message...")

# if user press on button then then perform the reaming step 
if st.button("Predict"):


    # Preporcess 
    transform_sms = Transform_text(input_sms)
    # Vectorize     
    Vector_input = tfidf.transform([transform_sms])

    # Predict 
    result = model.predict(Vector_input)[0]

    # Display 

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
