import packages.url_builder as builder
import packages.ignore_dirs as ignore_dirs
import packages.verbose as verbose
import packages.recursive as recursive

print('Enter Github repo\'s path url: ')
url = input()

request_url = builder.build_url(url)

print('\nSelect an option\n1. Recursive download\n2. Ignore dirs \n3. Verbose mode\n4. Exit')
option = input()
if option == '1':
	recursive.download(request_url)
elif option == '2':
	ignore_dirs.download(request_url)
elif option == '3':
	verbose.download(request_url)
elif option == '4':
	print('bye')
	exit()