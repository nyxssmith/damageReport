import requests
from lxml import html
import time

address = "https://www.reddit.com/r/all/"

def checkValidLink(link):#checks if the link will work or not, so we can use this to remove bad links from lists and make sure the program wont error
	try:
		page = requests.get(link).text#we get the webpage
		#print(link,"is valid")
		return True
	except:
		#print(link,"is not valid")
		return False


def openPage(address):
	
	if(not checkValidLink):
		return 0,0,[],null,null
	page = requests.get(address).text#we get the webpage
	doc = html.fromstring(page)#doc convets the page to strings
	pageLines = page.split("\n")#my method of making a list of lines in the html
	linesWithLinks = []
	numberOfLines = 0
	linkCount=1
	toFind = "a href"#this makes a list of all lines of html that contain links
	for line in pageLines:
		if(line.find(toFind)!=-1):
			#print("contains a link")
			linesWithLinks.append(line)
			linkCount+=1
		numberOfLines+=1

	return linkCount,numberOfLines,linesWithLinks,doc,page

def findLinkTo(to,linksList,doc):#takes linesWithLinks and doc at end
	i=0
	for linkline in linksList:
		link = doc.cssselect("a")[i]
		i+=1
		if(link.text_content()==to):
				return linkline,link

def listLinksTo(to,linksList,doc):#takes linesWithLinks and doc at end
	listOfFinishedLinks = []
	for line in linksList:
		#print(line)
		if to in line:
			listOfFinishedLinks.append(getUrlFromLink(line))
	return listOfFinishedLinks#returns a list that has links to the 'to' search term
			
		
def getUrlFromLink(rawLinkLine):#gets the hmtl file from the line with the link in html
	string = rawLinkLine#make my typing easyer
	i=0
	j=0
	try:
		for char in string:
			if(string[i]=='<' and string[i+1]=='a'):
				string = string[i+9:]#cuts off the firts part upto the name of the hml
				
				#now to cut off the end part
				
			i+=1
	except:
		pass#this makes it not throw out of bounds exepction, and ignores it because we are hunting for something in the middle
	#now to remove the rest past .html
	try:
		for char in string:
			if(string[j]=='.' and string[j+1]=='h' and string[j+2]=='t' and string[j+3]=='m' and string[j+4]=='l'):
				string = string[:j+5]#cuts off the rest past hmtl
				#print(string)
			j+=1
	except:
		pass#this makes it not throw out of bounds exepction, and ignores it because we are hunting for something in the middle
	return string

def toFullLink(inputList):
	outputList = []
	for item in inputList:
		item=addressBase+item
		outputList.append(item)
	return outputList

def removeInvalidLinks(inputList):
	outputList = []
	for item in inputList:
		if(checkValidLink(item)):
			outputList.append(item)
	return outputList

def addToSet(inputSet,inputList):
	for item in inputList:
		inputSet.add(item)

def elementsMustHave(inputSet,mustHave,outputSet):
	for item in inputSet:
		if(item.find(mustHave)!=-1):
			outputSet.add(item)

def outputToText(inputSet,name):
	with open(name,"w") as N:
		for item in inputSet:
			N.write(item+"\n")

def outputToWeb(inputSet,name):
	with open(name,"w") as N:
		N.write("<html> \n <body> \n")
		for item in inputSet:
			N.write("<a href="+item+">"+item+"</a> <br>\n")

#program starts here

startTime = time.time()

linkCountM, numberOfLinesM, linesWithLinksM, docM, pageM = openPage(address)

pageM =pageM.lower()
print(numberOfLinesM)
print(type(pageM))



print(time.time()-startTime,"seconds to run")

