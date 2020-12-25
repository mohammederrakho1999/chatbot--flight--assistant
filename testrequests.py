import requests
r = requests.get(url = "http://localhost:8080/?message=on%20april%20first%20i%20need%20a%20flight%20going%20from%20casablanca%20to%20paris")
print(r.text)


