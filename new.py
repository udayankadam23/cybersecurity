import phonenumbers
from phonenumbers import geocoder
import folium
import re

phone_num_patt = r"^[189][0-9]{7}"
num = input("Enter phone number: ")
check_num = phonenumbers.parse(num)
num_loc = geocoder.description_for_number(check_num, "en")
print("Country Name: " + num_loc)


from phonenumbers import carrier
isp = phonenumbers.parse(num)
print("Service provider name: " + carrier.name_for_number(isp, "en"))