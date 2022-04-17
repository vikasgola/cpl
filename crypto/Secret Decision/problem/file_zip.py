import zipfile
import itertools
from itertools import permutations


# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'secret.zip'

file1 = open('players.txt','r')


numbers_set = '00000'

zip_file = zipfile.ZipFile(zipfilename)

for player in line:
	for c in itertools.product(numbers_set, repeat=4):
	    # Add the four numbers to the first half of the password.

		password = "player".strip()+''.join(c)
		# Try to extract the file.
		print("Trying: %s" % password)
		# If the file was extracted, you found the right password.
		if extractFile(zip_file, password):
		    print('*' * 20)
		    print('Password found: %s' % password)
		    print('Files extracted...')
		    exit(0)

# If no password was found by the end, let us know!
print('Password not found.')
