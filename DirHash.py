import hashlib
import os
import sys
import glob

MD5hashes = []
SHAhashes = []
filenames = []

def createHash(path):

	sha = hashlib.sha512()
	md5 = hashlib.md5()
	with open(path, 'rb') as p:
		while True:
			picdata = p.read(65536)
			if not picdata:
				break
			sha.update(picdata)
			md5.update(picdata)
	print("Path: " + path)
	print("MD5: " + md5.hexdigest())
	print("SHA-512: " + sha.hexdigest())
	MD5hashes.append(md5.hexdigest())
	SHAhashes.append(sha.hexdigest())

def main():
	print("Starting DirHash")
	print("You will find the results in the current working directory in results.csv.")
	for filename in glob.glob(os.path.join(sys.argv[1],'*')):
		filenames.append(filename)
		createHash(filename)
	if os.path.exists('results.csv'):
		os.remove('results.csv')
	with open('results.csv','w') as f:
		f.write("Unique Identifier,Filename,MD5,SHA-512\n")
		for x in range(0,len(filenames)):
			if x <=9:
				f.write("000"+str(x)+"," +filenames[x]+","+MD5hashes[x]+","+SHAhashes[x]+"\n")
			elif x>9 and x<=99:
				f.write("00"+str(x)+"," +filenames[x]+","+MD5hashes[x]+","+SHAhashes[x]+"\n")
			elif x>99 and x<=999:
				f.write("0"+str(x)+"," +filenames[x]+","+MD5hashes[x]+","+SHAhashes[x]+"\n")
			elif x>99 and x<=9999:
				f.write(str(x)+"," +filenames[x]+","+MD5hashes[x]+","+SHAhashes[x]+"\n")
			else:
				print("File Limit of 9999 reached")
		print("Finished")
		f.close()
		
main()