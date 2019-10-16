import requests, json

class WeatherData():
    
    def __init__(self):
        self.info = {}
        self.key = '4e2cd17eb05943aa8192f7ccabec1a22'

    def getWeather(self, coord):
        if coord in self.info:
            return self.info[coord]
        else:
            return self.callAPI(coord)

    def callAPI(self, coord):
        try:
            lat = coord[0]
            lon = coord[1]
            url = 'http://api.weatherbit.io/v2.0/forecast/daily?days=2&units=I&lat={}&lon={}&key={}'.format(lat, lon, self.key)
            response = requests.get(url).json()
            today = response['data'][0]
            tomorrow = response['data'][1]
            data = {
                'today_temp': today['temp'],
                'tomorrow_temp': tomorrow['temp'],
                'precip': today['pop'],
                'condition': today['weather']['code'],
                'iCode': today['weather']['icon']
            }
            self.info[coord] = data
            return data
        except:
            print(response)
            return