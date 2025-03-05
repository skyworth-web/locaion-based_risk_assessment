import googlemaps
import os

GMAPS_API_KEY = os.getenv("GMAPS_API_KEY")  # Store API Key in environment variables
gmaps = googlemaps.Client(key=GMAPS_API_KEY)

def get_location_image(address):
    """Fetches Google Maps static image and geolocation data"""
    geocode_result = gmaps.geocode(address)
    if not geocode_result:
        return None

    location = geocode_result[0]['geometry']['location']
    lat, lng = location['lat'], location['lng']

    image_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=15&size=600x300&maptype=roadmap&markers=color:red%7C{lat},{lng}&key={GMAPS_API_KEY}"
    
    return {"lat": lat, "lng": lng, "image_url": image_url}
