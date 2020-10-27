import urllib.request
import json
import os

def download_file(file_url, file_path):
	file_data = urllib.request.urlopen(file_url).read()

	# saves data to file
	file_stream = open(file_path, 'wb')
	file_stream.write(file_data)
	file_stream.close()

def download(url):
	data = urllib.request.urlopen(url).read()

	# total number of elements in a folder
	total = len(json.loads(data))

	for res in range(total):
		# gets files parameters
		res_name = json.loads(data)[res]['name']
		res_type = json.loads(data)[res]['type']
		save_path = json.loads(data)[res]['path']

		print('You are going to download', save_path,'. Proceed?[Y/n] (press enter to finish)')
		ans = input()
		if ans == 'Y' or ans == 'y':
			if res_type == 'dir':
				download(url + '/' + res_name)
			else:
				# creates folder if not exists
				folder = save_path[:-1-len(res_name)]
				if not os.path.isdir(folder):
					os.makedirs(folder)

				file_url = json.loads(data)[res]['download_url']
				download_file(file_url, save_path)
		elif ans == '':
			break