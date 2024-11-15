import re

class HTMLCleaner:
    @staticmethod
    def clean_html(raw_html):
        cleaned_html = re.sub(r'\\/', '/', raw_html)
        cleaned_html = re.sub(r'\\', '', cleaned_html)
        cleaned_html = re.sub(r'&lt;\/', '</', cleaned_html)
        cleaned_html = re.sub(r'&lt;', '<', cleaned_html)
        cleaned_html = re.sub(r'&gt;', '>', cleaned_html)
        cleaned_html = re.sub(r'"', '"', cleaned_html)
        return cleaned_html
