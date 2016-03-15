import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def printMap(h_map):
    for key in h_map:
        print (key, ":", h_map[key])

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    sentiment(sent_file, tweet_file)

def sentiment(afile, tweets):
    afinnfile = afile
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
        print(score)
    outputfile = tweets
    sentimentMap = {}    
    for l in outputfile:
        count = 0
        eLine = json.loads(l)
        print eLine
	for word in eLine.text:
            sentimentMap[count] += scores[word]
        count += 1
    printMap(sentimentMap)

if __name__ == '__main__':
    main()
