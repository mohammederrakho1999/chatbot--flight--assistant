from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import AirlineScraper as scraper
import Pickle as pickle
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import pandas as pd
import numpy as np
import time
import nltk


lookup = [] #contains city names
extract = [] # list of targeted cities



class WebServerHandler(BaseHTTPRequestHandler):


	def Do_Get(self):
		self.send_response(300)
		self.send_header("content-type","text/plain")
		self.end_headers()
		query = urlparse(self.path).query
		message = query.split("=")[1]
		intent = model.predict([message])[0]

		if intent == "atis_flight":
			# performing named entity recognition
			tokens = nltk.word_tokenize(message)
			msg_components = nltk.pos_tag(tokens)
			for entity in msg_components:
				if entity[-1] == "NN" and name[0].lower() in lookup:
					extract.append(name[0])












	
	
		