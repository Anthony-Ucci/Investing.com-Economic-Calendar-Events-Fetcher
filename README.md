# Investing.com-Economic-Calendar-Events-Extractor
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
python main.py --countries 5 --timeZone 8 --importance 2 3 --timeFilter timeRemain --currentTab today --limit_from 0
```


## Arguments
```bash
--countries : IDs des pays (ex : 5 pour les États-Unis)
--timeZone : ID du fuseau horaire (ex : 8 pour GMT-5)
--importance : Niveau d importance des nouvelles (ex : 2, 3)
--timeFilter : Filtre de temps (ex : timeRemain)
--currentTab : Onglet actuel (ex : today)
--limit_from : Indice de départ pour limiter les résultats (ex : 0)
