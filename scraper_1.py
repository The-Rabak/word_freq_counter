import urllib.request as request
import re
from collections import Counter
from get_input_args import ParseArguments


def get_parsed_args():
    argumentsParser = ParseArguments()

    argumentsParser.add_input_args("--url", str, 'https://finance.yahoo.com/topic/stock-market-news',
                               'input web page to get most common words from')

    argumentsParser.add_input_args("--count", int, 10,
                               'most common word count to be returned')
                               
    return argumentsParser.get_parsed_args()

args = get_parsed_args()
url, word_count = str(args.url), int(args.count)
#word_pattern = re.compile(r"\w+")
url_pattern = re.compile(r"^(https?)(:\/\/)(www)?\.?[\w@:%._\+~#=\-]{1,256}?\.[\w+\.]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&=]*)")
matches = url_pattern.match(url)

if not matches:
    print(f"url entered: {url} is invalid, please try again with a valid url")
    exit(401)

words_counter = Counter()

with request.urlopen(url) as f:
    while lines := f.read(500):
        words = Counter(lines.lower().split())
        words_counter = words_counter + words
       
n_most_common_words = [key.decode("utf-8") for key, val in words_counter.most_common(word_count)]
print(n_most_common_words)

