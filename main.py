import streamlit as st
import pickle 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer



def mail(input_data):

    with open("tf_model.sav", "rb") as f:
        vectorizer = pickle.load(f)

    with open("SVM_model.sav", "rb") as f:
        loaded_model = pickle.load(f)

    tansdata=vectorizer.transform([input_data])

    pred=loaded_model.predict(tansdata)

    print(pred)
    

    if (pred[0] == 0):
        return "This mail🎁 is legitimate"
    else:
        return "This is a phishing🤢 mail🎁"
    
def main():

    import streamlit as st


    st.markdown('<p style="font-size:24px; font-weight:bold;">Welcome to the Phishing Mail Prediction App</p>', unsafe_allow_html=True)


    st.write("This app predicts whether a mail🎁 is a phishing and legitimate")


    
    #getting the input data  from the user
    text= st.text_input("Enter Mail Message🎁: ")
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Mail Prediction'):
        diagnosis= mail(text)
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()

