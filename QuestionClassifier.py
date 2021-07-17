from textblob.classifiers import NaiveBayesClassifier, DecisionTreeClassifier
import textblob
import pickle

def trainClassifier():
   generic_questions = ("Let's go","You never wanted to go out with 'me, did you?","Who knows?","What annoys you?",
                     "you've heard of him?","What were you doing?","Thank you anyway","No problem",
                     'She okay?',"Yes, I have a question.","What is your question?","What are your hobbies?",
                     "You know how sometimes you just become this 'persona'?  And you don't know how to quit?",
                     "what's up?",'sup people? I see the weather\'s getting better over there, Ben.',
                     "how are you doing?","Hi","Hello","Hey","How's you?","Have you heard the news?",
                     'i had the same problem your having so thats my i made my own.',"What is your favorite book?",
                     "good night","good morning","good afternoon","good evening","So what's your favorite color?",
                     'What good stuff?',"what's new?","How's life?","That is good to hear",
                     "I am doing well, how about you?","I am doing well, how about you?","I'm also good.",
                     "What are you then?",'What are you working on?',"Who are you?","What is it like?",
                     "How do you work?","Who is your appointment with?","What languages do you like to use?",
        )
   medical_questions = ('What are the symptoms of actinic keratoses?', 
                        'What are the preventive measures of actinic keratoses ?',
                        'What are the symptoms of basal cell carcinoma ?',
                        'What are the preventive measures of basal cell carcinoma ?',
                        'What are the symptoms of benign keratosis?',
                        'What are the preventive measures of dermatofibroma ?',
                        'What are the preventive measures of benign keratosis?',
                        'What are the symptoms of dermatofibroma ?',
                        'What are the symptoms of melanoma ?',
                        'What is actinic keratoses?',
                        'which areas does actinic keratoses appear?',
                        'what colour is actinic keratoses?',
                        'what are the remedies for actinic keratoses?',
                        'when to consult a doctor in case of actinic keratoses?',
                        'Does ititching happens in actinic keratoses?',
                        'What is basal cell carcinoma?',
                        'which areas does basal cell carcinoma appear?',
                        'what colour is basal cell carcinoma?',
                        'what are the remedies for basal cell carcinoma?',
                        'when to consult a doctor in case of basal cell carcinoma?',
                        'Does ititching happens in basal cell carcinoma?',
                        'What is benign keratosis?',
                        'which areas does benign keratosis appear?',
                        'what colour is benign keratosis?',
                        'what are the remedies for benign keratosis?',
                        'when to consult a doctor in case of benign keratosis?',
                        'Does ititching happens in benign keratosis?',
                        'What is dermatofibroma?',
                        'which areas does dermatofibroma appear?',
                        'What is the texture of dermatofibroma?',
                        'what colour is dermatofibroma?',
                        'what are the remedies for dermatofibroma?',
                        'when to consult a doctor in case of dermatofibroma?',
                        'Does ititching happens in dermatofibroma?',
                        'What is melanoma?',
                        'which areas does melanoma appear?',
                        'what colour is melanoma?',
                        'what are the remedies for melanoma?',
                        'when to consult a doctor in case of melanoma?',
                        'Does ititching happens in melanoma?',
                        'What is melanocytic nevi?',
                        'which areas does melanocytic nevi appear?',
                        'What is the texture of melanocytic nevi?',
                        'what colour is melanocytic nevi?',
                        'what are the remedies for melanocytic nevi?',
                        'when to consult a doctor in case of melanocytic nevi?',
                        'Does ititching happens in melanocytic nevi?',
                        'What is vascular lesions?',
                        'What is the texture of vascular lesions?',
                        'what colour is vascular lesions?',
                        'what are the remedies for vascular lesions?',
                        'when to consult a doctor in case of vascular lesions?',
                        'Does ititching happens in vascular lesions?',
                        'What are the preventive measures of melanoma ?',
                        'What are the symptoms of melanocytic nevi ?',
                        'What are the preventive measures of vascular lesions ?',
                        'What are the preventive measures of melanocytic nevi ?',
                        'What are the symptoms of vascular lesions ?')
    
   generic_questions = [(x, 'generic') for x in generic_questions]
   medical_questions = [(x, 'med') for x in medical_questions]

   training_set = []
   training_set.extend(generic_questions)
   training_set.extend(medical_questions)

   Qclassifier = NaiveBayesClassifier(training_set)
   save_classifier = open("F:/upload/uploads/chat_naivebayes2.pickle","wb")
   pickle.dump(Qclassifier, save_classifier)
   save_classifier.close()

def mainQuery(query):
   classifier_file=open("F:/upload/uploads/chat_naivebayes2.pickle","rb")
   Qclassifier=pickle.load(classifier_file)
   classifier_file.close()
   prob_dist = Qclassifier.prob_classify(query)
   if(prob_dist.max()=="med"):
       return "med"
   elif(prob_dist.max()=="generic"):
       return "generic"
   else:
       return None


      


   
