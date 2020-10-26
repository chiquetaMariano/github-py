
print('Enter Github file/directory url:')
url = input()
# TODO: check if is file or dir
print('Select an option\n1. Normal download\n2. Recursive download\n3. Ignore subdirs\n4. Verbose mode')
option = input()
if option == '1':
	print('you selected ND')
elif option == '2':
	print('you selected RD')
elif option == '3':
	print('you selected ID')
elif option == '4':
	print('you selected VM')