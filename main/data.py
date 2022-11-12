# import urllib,urllib2


"""This Programs Fetch The Address"""

from googlemaps import *


address='Mahatma Gandhi Rd, Shivaji Nagar, Bangalore, KA 560001'

add=GoogleMaps().address_to_latlng(address)
print(add)