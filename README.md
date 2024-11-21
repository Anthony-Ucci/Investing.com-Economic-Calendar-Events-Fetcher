# Investing.com-Economic-Calendar-Events-Fetcher
A Python tool for scraping and extracting economic event data from Investing.com. It automates data retrieval, cleaning, and parsing of key details like event timing, country, and significance—ideal for financial analysis.

## Prerequisites
- Python 3.8+
- Python libraries : `requests`, `bs4` (BeautifulSoup)


## Installation
To install the necessary dependencies, execute the following command:
```bash
pip install requests beautifulsoup4
```

## Utilisation
To use this script, you need to pass arguments via the command line. Here is an example command to run the script:
```bash 
python main.py --countries 5 --timeZone 8 --importance 3 --categories _employment _economicActivity --timeFilter timeRemain --currentTab custom --limit_from 0 --date_from 2024-01-01 --date_to 2024-05-31
```

## Arguments
- `--countries` : Country IDs (e.g., 5 for the United States)
- `--categories` : Categories of events to filter (e.g., _employment, _economicActivity)
- `--timeZone` : Time zone ID (e.g., 8 for GMT-5)
- `--importance` : Level of news importance (e.g., 2, 3)
- `--timeFilter` : Time filter (e.g., timeRemain)
- `--currentTab` : Current tab (e.g., today, custom)
- `--limit_from` : Start index to limit results (e.g., 0)
- `--date_from` : Start date in YYYY-MM-DD format (e.g., 2024-01-01)
- `--date_to` : End date in YYYY-MM-DD format (e.g., 2024-01-31)

