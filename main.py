from youtube_search import YoutubeSearch
import argparse, sys

parser = argparse.ArgumentParser(description='Search YouTube and get a single link as the output.')

parser.add_argument('query', metavar='Q', nargs='+', help="query to search for")
parser.add_argument("--index", "-i", help="out of results, use INDEX instead of 1st result", type=int, default=1)

args = parser.parse_args()

result = YoutubeSearch(' '.join(args.query), max_results=10).to_dict()

if not result:
	print('No results found', file=sys.stderr)
	exit()

url_suffix = result[args.index - 1]['url_suffix']
print('https://www.youtube.com%s' % (url_suffix))