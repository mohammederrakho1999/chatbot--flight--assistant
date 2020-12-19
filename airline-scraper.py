from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


cityFrom = "CMN"
cityTo = "PAR"
new = []

url = "https://www.vol-direct.fr/vols/resultats/"+cityFrom+"-"+cityTo+"/2020-12-24/00/0/1-0-0?sid=FFR9_5fde6029314d3&source=c2VhcmNoLWZvcm18"
PATH_chrome_driver = "C:/Users/info/Desktop/seleniumtools/chromedriver"


chromeOptions = Options() 
chromeOptions.add_argument("--incongnito")

driver = webdriver.Chrome(executable_path = PATH_chrome_driver, options = chromeOptions)
driver.set_window_size(1120, 1000)
driver.get(url)

flights = driver.find_elements_by_class_name("flights-itinerary-default") 

while len(new) < 5: # maximun five flight to be returned

	for flight in flights:
		try:
			FlightTime = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-origin-departure"]').text
			FlightArrivalTime = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-destination-arrival"]').text
			duration = driver.find_element_by_xpath('.//section//span[@class="flights-itinerary-duration"]').text
			price = driver.find_element_by_xpath('.//span[@class="flights-itinerary-oneway-price flights-itinerary-oneway-price-length-5"]').text
			Type = driver.find_element_by_xpath('.//span[@class="flights-itinerary-duration-stops"]').text
			site = driver.find_element_by_xpath('.//span[@class="first-offer-price"]').text
		except:
			pass

		new.append({"flighttime":FlightTime,
		            "flightArrivalTime":FlightArrivalTime,
		            "duration":duration,
		            "price":price,
		            "Type":Type,
	                "site":site})


print(new)




