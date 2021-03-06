
# This is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get ("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=05F2915A-32F2-4E75-B7C5-F43A9D874994")


	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error ..."

	if api [0]['Category']['Name'] == "Good": 
		category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
		category_colour = "good"
	elif api [0]['Category']['Name'] == "Moderate":
		category_description = "(51 to 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
		category_colour = "moderate"
	elif api [0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
		category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public is not likely to be affected." 
		category_colour = "usg"
	elif api [0]['Category']['Name'] == "Unhealthy": 
		category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
		category_colour = "unhealthy"
	elif api [0]['Category']['Name'] == "Very Unhealthy": 
		category_description = "(201-300) Health alert: everyone may experience more serious health effects."
		category_colour = "veryunhealthy"
	elif api [0]['Category']['Name'] == "Hazardous": 
		category_description = "(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
	 	#category_colour = "hazardous"

	return render(request, 'home.html',{
		'api': api,
		'category_description': category_description,
		'category_colour': category_colour})

def about(request):
	return render(request, 'about.html',{})

