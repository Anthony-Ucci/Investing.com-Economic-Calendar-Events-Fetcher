import requests

class RequestManager:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.investing.com/economic-calendar/",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.url = "https://www.investing.com/economic-calendar/Service/getCalendarFilteredData"

    def post_request(self, params):
        response = self.session.post(self.url, headers=self.headers, data=params)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Erreur : {response.status_code}")
            return None