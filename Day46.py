from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geopiExercises")

place=input("Enter City Name:")
location = geolocator.geocode(place)
print(location)
