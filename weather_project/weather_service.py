import requests
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def get_weather(city_name):
    api_key = '3b0b361a8592837f5f2913d96eb8064f'
    response = requests.get(url.format(city_name, api_key))
    data = response.json()
    return {
        'city': data['name'],  # or data.get('name)
        'weather': data.get('weather')[0].get('main'),
        'icon': data['weather'][0]['icon'],
        'temp': "{0:.2f}".format(data['main'].get('temp')-273)
    }