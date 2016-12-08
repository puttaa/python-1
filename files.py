import os

for files in os.walk('..'):
	for ff in files:
		if isinstance(ff, list):
			for f in ff:
				print (f)
				print (os.path.abspath(f))

#('..', ['Docker', 'Python', 'Unix'], [])
#('../Docker', ['mydockerbuild', 'nginx'], ['index.html'])
#('../Docker/mydockerbuild', [], ['Dockerfile'])
#('../Docker/nginx', [], ['Dockerfile'])
#('../Python', [], ['files.py', 'python.py', 'python2.py'])
#('../Unix', [], ['file_permissions.sh', 'test.txt'])

