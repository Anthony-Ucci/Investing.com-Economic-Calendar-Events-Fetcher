from bs4 import BeautifulSoup

class HTMLParser:
    def parse_html(self, html_data):
        soup = BeautifulSoup(html_data, 'lxml')
        events = []
        for row in soup.find_all("tr", class_="js-event-item"):
            event_data = {
                "date": row.get("data-event-datetime", "N/A"),
                "time": row.find("td", class_="js-time").text.strip(),
                "country": row.find("span", class_="ceFlags").get("title", "N/A"),
                "importance": len(row.find_all("i", class_="grayFullBullishIcon")),
                "event_title": row.find("td", class_="event").a.text.strip() if row.find("td", class_="event").a else "N/A",
                "actual": row.find("td", class_="act").text.strip(),
                "forecast": row.find("td", class_="fore").text.strip(),
                "previous": row.find("td", class_="prev").text.strip()
            }
            events.append(event_data)
        return events
