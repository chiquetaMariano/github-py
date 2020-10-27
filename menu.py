import url_builder as builder
import ignore_dirs
import verbose

print('Enter Github repo's path url: ')
url = input()

request_url = builder.build_url(url)

print('\nSelect an option\n1. Normal download\n2. Recursive download\n3. Ignore dir \n4. Verbose mode')
option = input()
if option == '1':
	print('you selected ND')
elif option == '2':
	print('you selected RD')
elif option == '3':
	# print('you selected ID')
	ignore_dirs.download(request_url)
elif option == '4':
	# print('you selected VM')
	verbose.download(request_url)