import urllib.request
import json

def download_file(file_url, file_name):
	file_data = urllib.request.urlopen(file_url).read()

	# saves data to file
	file_stream = open(file_name, 'wb')
	file_stream.write(file_data)
	file_stream.close()

def download(url):
	data = urllib.request.urlopen(url).read()

	# total number of elements in a folder
	total = len(json.loads(data))

	for res in range(total):
		# gets files parameters
		res_name = json.loads(data)[res]['name']

		print('You are going to download file ', res_name,'. Proceed?[Y/n] (press enter to skip all)')
		ans = input()
		if ans == 'Y' or ans == 'y':
			file_url = json.loads(data)[res]['download_url']
			download_file(file_url, res_name)

		elif ans == '':
			break