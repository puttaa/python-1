#Writer: alwal putta

import os

for files in os.walk('.git'):
	for ff in files:
		if isinstance(ff, list):
			for f in ff:
#				print (f)
				print (os.path.abspath(f))
				full_file_name =  (os.path.abspath(f))
				print (os.system("cat $full_file_path"))

#('..', ['Docker', 'Python', 'Unix'], [])
#('../Docker', ['mydockerbuild', 'nginx'], ['index.html'])
#('../Docker/mydockerbuild', [], ['Dockerfile'])
#('../Docker/nginx', [], ['Dockerfile'])
#('../Python', [], ['files.py', 'python.py', 'python2.py'])
#('../Unix', [], ['file_permissions.sh', 'test.txt'])

