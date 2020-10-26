# github API format
# https://api.github.com/repos/:owner/:repo/contents/:path

import urllib.request
import json

data = urllib.request.urlopen('https://api.github.com/repositories/3873687/contents/pcv_book').read()

# total number of elements in a folder
total = len(json.loads(data))

for res in range(total):
	# gets files parameters
	file_name = json.loads(data)[res]['name']

	print('You are going to download file ', file_name, '. Proceed?[Y/n] (press enter to skip all)')
	ans = input()
	if ans == 'Y' or ans == 'y':
		file_url = json.loads(data)[res]['download_url']
		file_data = urllib.request.urlopen(file_url).read()

		# saves data to file
		file_stream = open(file_name, 'wb')
		file_stream.write(file_data)
		file_stream.close()
	elif ans == '':
		break