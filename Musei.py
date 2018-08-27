#-*- coding: utf-8 -*-
#importo le librerie
from settings import token, start_msg
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
import json
import os
import requests
import sys
import telepot

# State for user
user_state = {}
#data = json.load(open("Musei.json"))

#with open("output.json", "w") as outfile:
   # json.dump(data, outfile)

#TOKEN = '694050542:AAHeatUTS24sA3RowYyh9QtOAmK5WT07CYs'
#definizione della funzione on_chat_message
def on_chat_message(msg):

	content_type, chat_type, chat_id = telepot.glance(msg)
	name = msg["from"]["first_name"]
    	txt = msg['text']

	# Check user state
    	try:
        	user_state[chat_id] = user_state[chat_id]
    	except:
        	user_state[chat_id] = 0
	# start command
    	if 'text' in msg and msg['text'] == '/start':
		bot.sendMessage(chat_id, 'ciao {}'.format(name))

    	elif 'text' in msg and msg['text'] == '/cerca':
        	msg = "clicca o digita la localita marchigiana" 
        	markup = ReplyKeyboardMarkup(keyboard=[["PesaroUrbino", "Ancona"], ["AscoliPiceno", ""], ["Macerata"]])
        	bot.sendMessage(chat_id, msg, reply_markup=markup)
       		user_state[chat_id] = 1

    	elif 'text' in msg and msg['text'] == '/help':
		bot.sendMessage(chat_id, 'ciao {}, usa sono /cerca per trovate i musei nella città'.format(name))
		bot.sendMessage(chat_id, msg)

    	elif user_state[chat_id] == 1:

    		if content_type == 'text':
	    		try:	
				r = requests.get(
                			url='http://api.openweathermap.org/data/2.5/weather?q='+str(msg['text'])
					+',Italy&appid=22722fe37a60c60a10e9336d1216c371')
                		json_data = r.json()
		
				#estraggo i dati JSON
				description = json_data ["weather"][0]["description"]
				main = json_data ["weather"][0]["main"] 
                		temp = json_data ["main"]["temp"] 
				temp_min = json_data["main"]["temp_min"]
				temp_max = json_data["main"]["temp_max"] 	        
				pressure = json_data ["main"]["pressure"] 	        
                		humidity = json_data ["main"]["humidity"]
				wind = json_data ["wind"]["speed"]
				lon = json_data ["coord"]["lon"]
				lat = json_data ["coord"]["lat"]
		
				bot.sendMessage(chat_id, "Principale: {}.\nDescrizione: {}.\n".
						         format(main,description), reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
				
				
				bot.sendMessage(chat_id, "Temperatura: {} C°.\nTemperatura minima: {} C°.\nTemperatura massima: {} C°.\n". 
							 format((temp-273.15),(temp_min-273.15),(temp_max-273.15))+ 
							 "Pressione: {} hpa.\nUmidità: {} %.\nVelocità vento: {} m/s.\n". 
							 format(pressure,humidity,wind),
							 reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
			        bot.sendMessage(chat_id, "Viene mostrata la posizione geografica della città.\n")
				bot.sendLocation(chat_id, lat,lon)

                		user_state[chat_id] = 0
				
	    		except:
	
				bot.sendMessage(chat_id, "Errore API", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
		else:
			bot.sendMessage(chat_id, "Digita /info per visualizzare i comandi.\n ")

# Main
print("Avvio Meteo_bot!")

# Start working
try:
	bot = telepot.Bot(token)
    	bot.message_loop(on_chat_message)
    	while(1):
        	sleep(10)
finally:
	print("Esci")
