import argparse
from helpers.request_manager import RequestManager
from helpers.html_cleaner import HTMLCleaner
from helpers.html_parser import HTMLParser

def main(args):
    request_manager = RequestManager()
    cleaner = HTMLCleaner()
    parser = HTMLParser()

    params = {
        "country[]": args.countries,
        "category[]": args.categories,
        "importance[]": args.importance,
        "dateFrom": args.date_from,
        "dateTo": args.date_to,
        "timeZone": args.timeZone,
        "timeFilter": args.timeFilter,
        "currentTab": args.currentTab,
        "limit_from": args.limit_from,
    }

    html_response = request_manager.post_request(params)
    if html_response:
        clean_html = cleaner.clean_html(html_response)
        events = parser.parse_html(clean_html)
        for event in events:
            print(event)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Send POST request to Investing.com and extract economic events data.")
    arg_parser.add_argument("--countries", nargs='+', type=int, required=True)
    arg_parser.add_argument("--categories", nargs='+', type=str, required=False)
    arg_parser.add_argument("--importance", nargs='+', type=int, required=False)
    arg_parser.add_argument("--date_from", type=str, required=True)
    arg_parser.add_argument("--date_to", type=str, required=True)
    arg_parser.add_argument("--timeZone", type=int, required=True)
    arg_parser.add_argument("--timeFilter", type=str, required=True)
    arg_parser.add_argument("--currentTab", type=str, required=True)
    arg_parser.add_argument("--limit_from", type=int, required=True)
    args = arg_parser.parse_args()
    
    main(args)
