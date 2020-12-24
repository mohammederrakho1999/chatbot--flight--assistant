from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import vol_scraper as scraper
import pickle
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import TextSimplifier as Tx
import pandas as pd
import numpy as np
import time
import nltk
from datetime import datetime
import requests
from spacy.lang.en import English
import nltk
import logging


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



lookup = ["casablanca","paris"] #contains city names
extract = [] # list of targeted cities
date = datetime.today().strftime("%Y-%m-%d")
parser = English()





class WebServerHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("content-type","text/plain")
		self.end_headers()
		message = urlparse(self.path).query.split("=")[1].replace("%20"," ")
		intent = model.predict([message])[0]
		if intent == "atis_flight":
			tokens = nltk.word_tokenize(message)
			msg_components = nltk.pos_tag(tokens)
			for entity in msg_components:
				if entity[-1] == "NN" and entity[0].lower() in lookup:
					extract.append(entity[0].lower())
					CodeFrom = Tx.CityFrom(extract[0])
			CodeTo = Tx.CityTo(extract[0])
			flight_info = scraper.AirlineScraper(CodeFrom, CodeTo, date)
			print(flight_info)
			reply = 'Your Agenda:<br>'
			reply = {
			"summury":"schedule",
			"start":{
		         "intent":intent,
		         "data":flight_info["FlightTime"][0],
		         },
		         "end":{
		         "congrats":"hello world",
		         "timezone":"casablanca",
		         }
		         }
		reply += '<br>' + '/' + ' ' + date + ' ' + reply['data']
		self.wfile.write({"intent": intent,"reply":reply})

	def log_message(self, format, *args):
		return






			# extraction just the info nedeed.
	#def do_Post(self):
		#content_length = int(self.end_headers['content_length'])
		#post_data = self.rfile.read(content_length)

			
			#response = requests.post(url, data = flight_info)
			#print(response.text)




def tokenize(text):
    tokens = parser(text)
    new = []
    for token in tokens:
    	new.append(token.lemma_.lower().strip())
    return new

if __name__ == "__main__":


	print("unpickling the model ......")
	with open("classifier1.pkl","rb") as f:
		model = pickle.load(f)

	print("loading english parser")
	parser = English()

	try:
		server = HTTPServer(("localhost", 8080), WebServerHandler)
		print("python server is running on port 8080")
		server.serve_forever()
	except KeyboardInterrupt:
		print("shutting the server")
		server.socket.close()




















	
	
		