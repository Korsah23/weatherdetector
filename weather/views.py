from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=396daa3fbf3dfd0a272f4c42b1c8a31a').read()
        json_list = json.loads(res)

        list = {
            "country_code": str(json_list['sys']["country"]),
            "coordinates" : str(json_list['coord']['lon']) + "" + str(json_list['coord']['lat']),
            "temp" : str(json_list['main']['temp']) + 'k',
            "pressure": str(json_list['main']['pressure']),
            "humidity": str(json_list['main']['humidity']),

        }
        city = city.capitalize()

    else:
        city = " "
        list = { }

    return render(request,'index.html', {'list':list, 'city':city})





    