
 #Description : Il s'agit d'une virtuelle assistante qui obtient la date d'aujourd'hui  et retourne la salutation ainsi que donne l'info sur une personnage à partir de wikipedia
	and return info on a person

#imprter les biblioteques

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar 
import random 
import wikipedia
from playsound import playsound

#ignorer les messages de warning
warnings.filterwarnings('ignore')

#Enregistrer  l'audio and et le retourner comme un string
def record_audio():
	#Enregistrer l'audio
	r=sr.Recognizer()
	#Commencer l'enregistrement avec un mcrophone
	with sr.Microphone() as source:
		print('Yo what up?')
		audio =r.listen(source)

	#La recognition de Google
	data = ''
	try :
		data = r.recognize_google(audio)
		print('You said :'+data)
	except sr.UnknownValueError:
		print('Google speech Reconition cound not understand this crap, unkown error')
	except sr.RequestError as e:
		print('Request from Google speech recognition service error '+e)

	return data	


#record_audio(commande)


#La fonction de réponse de VA 

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


# La fonction pour la réveiller

def wakeWord(text):
	 WAKE_WORDS=['yo computer','ok computer']#Liste pour réveiller 
	 text=text.lower()   #convertir en miniscule
	 #Vérifier si les commandes/text de l'utilisateur  contient a wake phrase
	 for  phrase in WAKE_WORDS:
	 	if phrase in text :
	 		return True
	 #Si les wake word(mots pour réveiller) n'est pas trouvé dans le text dans la boucle donc on retourne False
	 return False

	 #Fonction pour obtenir la date
def getDate():
	now=datetime.datetime.now()
	my_date=datetime.datetime.today()
	weekday=calendar.day_name[my_date.weekday()]
	monthNum=now.month
	dayNum=now.day


	 # liste des mois


	month_names=['January','February','Mars','April','May','June','July','August','September','October','November','December']
	 # Liste des nombres ordinal 
	ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
	return 'Today is ' +weekday+' '+month_names[monthNum-1]+' the '+ordinalNumbers[dayNum-1] +  '.'




# la fonction print(getDate())

#La fonction qui retourne une salutation aléatoire

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


	#checker pour le mot/phrase
	if(wakeWord(text)==True):
		#checker pour une salutation
		response=response+greeting(text)
		#check to see if he wants date
		if('date' in text):
			get_date=getDate()
			response=response+' '+get_date
		#checker pour voir  si l'utiisateur utilise 'who is'
		if('who is'in text):
			person=getPerson(text)
			wiki=wikipedia.summary(person,sentence=2)
			response=response+' '+wiki

		#L'assistante répond avec l'audio de la prochaine réponse
		AssistantResponse(response)






























	#for a in command :
	#	a.sr=translate(a).txt




#day=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#month=['January','February','Mars','April','May','June','July','August','September','October','November','December']
#year=[]
