import wikipedia as wiki

topics = ["Central processing unit","IBM Personal Computer","IBM PC compatible","Microsoft Windows","Macintosh hardware","Operating system","Motherboard","Memory","Microsoft","Apple Inc.","Computer hardware","Software","Motorcycle","Car","Airplane","Ship","Engine","Fuel","Parachuting","Rocket","Submarine","Badminton","Volleyball","Baseball","Hockey","Cricket","Football","Table tennis","Carrom","Chess","Sport","Poker","Blackjack","Marketing","Accounting","Economics","Finance","Business","Discounts and allowances","Bank","Income","Sales"]
for topic in topics:
	a = wiki.page(topic)
	b =  a.content
	c = ""
	for i in b:
		if((i != '=')&(i!='\n')):
			c+=i
	c = c.encode('utf-8')
	topic += ".txt"
	f = open(topic,'w')
	f.write(c)
	f.close()
