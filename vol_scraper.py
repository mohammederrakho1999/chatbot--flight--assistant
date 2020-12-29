from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


PATH_chrome_driver = "C:/Users/info/Desktop/seleniumtools/chromedriver"

def AirlineScraper(CodeFrom, CodeTo, date):
	A, B, C, D, E  = ([] for i in range(5))

	dic = {"FlightTime":A,
            "FlightArrivalTime":B,
            "duration":C,
            "Type":D,
            "site":E}


	chromeOptions = Options() 
	chromeOptions.add_argument("--incongnito")

	driver = webdriver.Chrome(executable_path = PATH_chrome_driver, options = chromeOptions)
	driver.set_window_size(1120, 1000)

	url = "https://www.vol-direct.fr/vols/resultats/"+CodeFrom+"-"+CodeTo+"/"+date+"/00/0/1-0-0?sid=FFR5_5fe5edb07f660&source=c2VhcmNoLWZvcm18"
	driver.get(url)

	flights = driver.find_elements_by_class_name("flights-itinerary-default") 
	while len(dic["FlightTime"]) <=1:

		for flight in flights:

			try:
				FlightTime = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-origin-departure"]').text
				FlightArrivalTime = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-destination-arrival"]').text
				Duration = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-duration"]').text
				Type = driver.find_element_by_xpath('.//span[@class="flights-itinerary-duration-stops"]').text
				Site = driver.find_element_by_xpath('.//span[@class="first-offer-price"]').text
			except:
				pass

			A.append(FlightTime)
			B.append(FlightArrivalTime)
			C.append(Duration)
			D.append(Type)
			E.append(Site)

	return dic





