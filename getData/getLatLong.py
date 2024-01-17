from geopy.geocoders import Nominatim


def getLatLong(country):
    geolocator = Nominatim(user_agent="FilmMetric")
    location = geolocator.geocode(country)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"Could not find coordinates for {country}")
        return None
