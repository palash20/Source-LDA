import string

stop = open("words.txt",'r').read()
# stop = f.read()
f2 = open("merge2.txt",'a+')

for line in open("final.txt",'r').readlines():
	c = ""
	line=line.translate(None, string.punctuation)
	line=line.lower()
	l = line.strip().split(' ')

	for word in l:
		if word not in stop:
			c+=word + " "
	#print c
	f2.write(c)
	f2.write('\n')

f2.close()
