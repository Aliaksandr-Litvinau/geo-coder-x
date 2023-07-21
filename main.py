import os

import requests


def geocode_address(api_key, address):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            results = data['results']
            if results:
                location = results[0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                return latitude, longitude
            else:
                print('No results found.')
        else:
            print('Error:', data['status'])
    except requests.exceptions.RequestException as e:
        print('Error:', e)

    return None, None


def main():
    api_key = os.environ.get('API_KEY')
    address = input('Введите адрес для геокодирования: ')

    latitude, longitude = geocode_address(api_key, address)
    if latitude is not None and longitude is not None:
        print(f'Широта: {latitude}, Долгота: {longitude}')
    else:
        print('Не удалось получить данные о местоположении.')


if __name__ == '__main__':
    main()
