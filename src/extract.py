import requests

class Extract:
    def __init__(self):
        pass

    def extract_country(self, country):
        url = f"http://universities.hipolabs.com/search?country={country}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta erro se não for 200 OK
            universities = response.json()
            return universities
        except requests.exceptions.RequestException as e:
            print(f"Erro ao extrair dados: {e}")
            return []