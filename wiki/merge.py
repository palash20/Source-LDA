import glob 
files = []
for f in glob.glob("*.txt"):
	files.append(f)
mer = open("merge.txt",'a+')
for file in files:
	f = open(file,'r')
	mer.write(f.read())
	mer.write('\n')

mer.close()
