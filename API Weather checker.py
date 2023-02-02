import requests
import os
from datetime import datetime

#Api section.............................................................................................................
os.environ['apikey']='86b3dff0144c07ef56d8faf422fd4b60' #creating or storing values in os environment on the program...dynamically....

env=os.getenv('apikey')#now calling or getting env data on the program....
#alternative of above environment calling os.environ.get()
#another method to call envirn first save in comp users environment variable the call same as the above...

location=input("Enter any city or country name: ")


Main_Api_source_lk='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+env
api_lki=requests.get(Main_Api_source_lk)
api_legacy=api_lki.json()

if api_legacy['cod']=='404':
    print("invalid city: {}, vmro plz check urs city name".format (location))


else:
    temprt_city=((api_legacy['main']['temp'])-273.15)#we use main then temp its means from main get temp valu and subtracted 273.15 the raw is comming in 'kelvin' but after subtraction it will converted into 'celcius'
    weather_des=api_legacy['weather'][0]['description']#same as above from weather goto 1st element and fetch the value of weather..
    hmdt=api_legacy['main']['humidity']#same as above...
    wndspd=api_legacy['wind']['speed']#same as above ...
    dateetime=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    #formating wheater info......................................................................
    print('***............................................................................................................................***')
    print('weather stats for - {} || {}'.format(location.upper(),dateetime))
    print('***............................................................................................................................***')
    print('current temp is :{:.2f} deg C*'.format(temprt_city))
    print('current weather is : ',weather_des)
    print('current humidity : ',hmdt,'%')
    ext=input("Enter to exit.")


    

