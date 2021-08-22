import phonenumbers
from phonenumbers import geocoder, carrier, timezone
check_length = int(13)

n = str(input("Enter the Number to search with '+' and country code: "))
temp = n.replace(" ", "")  #omiting spaces from number
#data validation
while True:
    if len(temp)==check_length:
        break
        
    else:
        print("Invalid number check and try again")

check = temp
search_number = phonenumbers.parse(check)

print("The Region of the Number is")
print(geocoder.description_for_number(search_number, "en"))
print("------------------------------------")
print("The ISP of"+ check +"is")
print(carrier.name_for_number(search_number, "en"))
print("------------------------------------")
print("The zonal time is")
print(timezone.time_zones_for_number(search_number))
