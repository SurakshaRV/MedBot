#importing required modules
from flask import *
from chat import *
import nltk
import csv
import re
import random
from QuestionClassifier import *
import testing_for_generic
from fuzzywuzzy import fuzz
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from medicalBot import *
from Model import *
from medical_chat_test import *

#creating an instance of Flask class and takes current module name as arguement
app = Flask(__name__)
#initializing secret key for the session
app.secret_key = "super secret key"
f=''
filename=''

#bounding '/' url with upload function 
@app.route('/')  
def upload():
    #returning rendered test.html template
    return render_template("test.html")

#bounding '/home' url with success function 
@app.route('/home', methods = ["GET",'POST'])  
def success():
    global f,filename
    #checking if a file is selected to upload
    if request.method == 'POST':
        #getting the selected file
        f = request.files['file']
        #uploading the selected .jpg file.
        f.save(f.filename)
        #obtaining the name of the .jpg file uploaded
        fn=str(f)
        fn=fn[15:]
        filename=fn[:-17]
        print(filename)
        #classifying the image in the .jpg file.
        result = diseasePredictor(filename)
        #returning rendered home.html template
        return render_template("report.html", result = result)

#bounding '/report' url with upload function 
@app.route('/report')  
def home():
    #returning rendered home.html template
    return render_template("home.html")

#bounding '/get' url with get_bot_response function
@app.route("/get")
def get_bot_response():
    #getting the user query and converting it to lowercase
    userText = request.args.get('msg').lower()
    #removing the question mark at the end of query
    userText=userText.strip('?')
    #getting the query type using NaiveBaeyes classifier
    query_type=mainQuery(userText)
    #getting the chatbot response if query is a generic question
    if query_type=="generic":
        if str(genericResponse(userText)) !="None":
            return str(genericResponse(userText))
        else:
            return "Sorry. I did not understand..."
        
    #getting the chatbot response if query is a medical question
    elif query_type=="med":
        if str(response(userText)) !="None":
            return str(response(userText))
        else:
            return "Sorry. I did not understand. Can you please reframe your question!"
    else:
        return "Sorry.No idea..."
  
if __name__ == '__main__':
    #setting the debug mode to True
    app.debug = True
    #running the application
    app.run() 

