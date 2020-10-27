import urllib.parse as urlParser

def build_url(req_url):
	url = urlParser.urlparse(req_url)

	parameters = url.path.split('/')

	author = parameters[1]
	repo = parameters[2]
	path = parameters[-1]

	return 'https://api.github.com/repos/' + author + '/'+ repo +'/contents/' + path

# print(build_url('https://github.com/trenton3983/Programming_Computer_Vision_with_Python/tree/master/PCV'))