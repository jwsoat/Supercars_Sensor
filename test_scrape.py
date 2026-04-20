import urllib.request
import re

def fetch_html(url, output_file):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Saved HTML to {output_file}")
    except Exception as e:
        print("Error fetching", url, e)

fetch_html('https://www.supercars.com/standings', 'standings.html')
fetch_html('https://www.supercars.com/results', 'results.html')
