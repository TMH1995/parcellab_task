from parcellab import settings
import requests
from rest_framework import status

class TemperatureService:
    def fetchTemperature(self,city:str,zipCode:str)->str:
        try:
            response = requests.get(f'{settings.WEATHER_API_URL}', params={'city': city, 'postal_code': zipCode,'key':settings.WEATHER_API_KEY}, verify=True)
            content = response.json()
            if response.status_code != status.HTTP_200_OK:
                return {'error': 'Something went wrong'}
            data=content['data'][0]
            return float(data['app_temp'])
            
        except Exception as e:
            return {'error': str(e)}
