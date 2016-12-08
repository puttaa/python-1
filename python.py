import os
import glob

print ("ALWAL")
print (glob.glob("/Users/puttaa*"))
print '*'*30
print (glob.glob("*"))
print '*'*30
print (os.listdir("/Users/puttaa"))
print '*'*30

relevant_path = "/Users/puttaa"
included_extenstions = ['jpg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir(relevant_path)
	if any(fn.endswith(ext) for ext in included_extenstions)]

