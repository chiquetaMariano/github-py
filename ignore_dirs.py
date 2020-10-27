import urllib.request
import json

def download_file(file_url, file_name):
	file_data = urllib.request.urlopen(file_url).read()
		
	# saves data to file
	file_stream = open(file_name, 'wb')
	file_stream.write(file_data)
	file_stream.close()
	return None

def download(url):
	data = urllib.request.urlopen(url).read()

	# total number of elements in a folder
	total = len(json.loads(data))

	for res in range(total):
		# gets resource parameters
		res_name = json.loads(data)[res]['name']
		res_type = json.loads(data)[res]['type']

		# checks for resource type
		if res_type == 'dir':
			print('ignoring dir ' + res_name)
		else:
			file_url = json.loads(data)[res]['download_url']
			download_file(file_url, res_name)