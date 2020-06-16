# Les commentaires de ce code sont en anglais
 #Description : This is an VA that gets the date ,current  ,responds with a random greeting and return info on a person

#importing libraries

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar 
import random 
import wikipedia
from playsound import playsound

#ignore any warning message
warnings.filterwarnings('ignore')

#Record audio and return it as as a string
def record_audio():
	#Record the audio
	r=sr.Recognizer()
	#Starting the recording with microphone
	with sr.Microphone() as source:
		print('Yo what up?')
		audio =r.listen(source)

	#Google recognition
	data = ''
	try :
		data = r.recognize_google(audio)
		print('You said :'+data)
	except sr.UnknownValueError:
		print('Google speech Reconition cound not understand this crap, unkown error')
	except sr.RequestError as e:
		print('Request from Google speech recognition service error '+e)

	return data	


#record_audio(command)


#VA response function

def AssistantResponse(text):
	print(text)
	#Vonversion texte -speech
	myobj=gTTS(text= text, lang='en', slow=False)
	#Sauvegarder l'audio converti a un fichier
	myobj.save('assistant_response.mp3')
	#jouer le fichier converti
	os.system('start assistant_response.mp3')
	#playsound('assistant_response.mp3')

text ='This is a test'
AssistantResponse(text)


# Function for wake or phrase

def wakeWord(text):
	 WAKE_WORDS=['yo computer','ok computer']#Liste pour réveiller 
	 text=text.lower()   #convertir en miniscule
	 #Vérifier si les commandes/text de l'utilisateur  contient a wake phrase
	 for  phrase in WAKE_WORDS:
	 	if phrase in text :
	 		return True
	 #Si les wake word n'est pas trouvé dans le text dans la boucle donc on retourne False
	 return False

	 #Fonction pour obtenir la date
def getDate():
	now=datetime.datetime.now()
	my_date=datetime.datetime.today()
	weekday=calendar.day_name[my_date.weekday()]
	monthNum=now.month
	dayNum=now.day


	 # list of months


	month_names=['January','February','Mars','April','May','June','July','August','September','October','November','December']
	 #A List of ordinal numbers
	ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
	return 'Today is ' +weekday+' '+month_names[monthNum-1]+' the '+ordinalNumbers[dayNum-1] +  '.'




#print(getDate())

#Function to return a random greeting response

def greeting(text):
	Greeting_INPUT=['yo','hello','hey','hola','greetings','wassup']
	Greeting_RESPONSES=['howdy','whats good','hello','hey there']
	for word in text.split():
		if word.lower() in GREETING_INPUTS:
			return random.choice(Greeting_RESPONSES) +'.'
	return ''

def getPerson(text):
	wordList=text.split()
	for i in range(0,len(wordList)):
		if i+3<=len(wordList) -1 and wordList[i+1].lower() =='who' and wordList[i+1].lower()=='is':
			return wordList[i+2]+' '+wordList[i+3]


while True:
	text=record_audio()
	response=''


	#check for the word/phrase
	if(wakeWord(text)==True):
		#check for greeting
		response=response+greeting(text)
		#check to see if he wants date
		if('date' in text):
			get_date=getDate()
			response=response+' '+get_date
		#check to see if  user said 'who is'
		if('who is'in text):
			person=getPerson(text)
			wiki=wikipedia.summary(person,sentence=2)
			response=response+' '+wiki

		#Have the assistant respond back using audio and the next from response
		AssistantResponse(response)






























	#for a in command :
	#	a.sr=translate(a).txt




#day=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#month=['January','February','Mars','April','May','June','July','August','September','October','November','December']
#year=[]
