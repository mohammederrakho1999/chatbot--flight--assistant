# this function simplifie city names taped by the user
import numpy as np
import pandas as pd


cities = {"casablanca":"CMN",
          "agadir":"AGA",
          "marrakech":"RAK",
          "rabat":"RBA",
          "tangier":"TNG",
          "paris":"CDG",
          "nice":"NCE",
          "lyon":"LYS",
          "marseille":"MRS",
          "Atlanta":"ATL",
          "Los Angeles":"LAX",
          "O'Hare":"ORD",
          "Dallas":"DFW",
          "denver":"DEN",
          "san francisco":"SFO",
          "seattle":"SEA",
          "McCarran":"LAS",
          "Aberdeen":"ABZ",
          "London":"LCY",
          "Manchester":"MAN",
          "Mildenhall":"MHZ",
          "Newbury":"EWY",
          "Nottingham":"NQT",
          "Oban":"OBN",
          "Glasgow":"GLA",
          "Hamburg":"HAM",
          "Hannover":"HAJ",
          "Baden-Baden":"FKB",
          "berlin":"SXF",
          "Munich":"MUC"}



def CityFrom(CityNameFrom):

	for city in cities:
		if city == CityNameFrom.lower():
			CodeFrom = cities[city]

	return CodeFrom


def CityTo(CityNameTo):

	for city in cities:
		if city == CityNameTo.lower():
			CodeTo = cities[city]

	return CodeTo




