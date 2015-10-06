__author__ = 'jugpreet'
import math
import sys

def main(argv):
    inputFileLoc = argv[0]
    outputFileLoc = argv[1]
    inputFile = open(inputFileLoc, 'r')

    inputType = ""
    for line in inputFile:
        line=str(line).strip()
        items = line.split()
        inputType = items[0]
        break

    if inputType=="HAM" or inputType=="SPAM":
        print("Spam Analysis")
        hamSpamAnalysis(inputFileLoc, outputFileLoc)
    else:
        print("Sentiment Analysis")
        sentimentAnalysis(inputFileLoc, outputFileLoc)

def sentimentAnalysis(inputFileLoc, outputFileLoc):
    inputFile = open(inputFileLoc, "r")
    uniqueItems=0

    positiveReviews = 0
    negativeReviews = 0
    dictionary = {"POSITIVE" : {}, "NEGATIVE" : {}}
    dictionaryUnique = {}
    for line in inputFile:
        line = str(line).strip()
        items = line.split()
        noOfItems = len(items)
        type = items[0]
        if type=="NEGATIVE":
            negativeReviews = negativeReviews+1
            for index in range(1, noOfItems):
                item = items[index].split(":")
                key = int(item[0])
                value = int(item[1])
                if key in dictionary["NEGATIVE"]:
                    tempValue = dictionary["NEGATIVE"][key]
                    value = tempValue + value
                dictionary["NEGATIVE"][key] = value

        elif type=="POSITIVE":
            positiveReviews = positiveReviews+1
            for index in range(1, noOfItems):
                item = items[index].split(":")
                key = int(item[0])
                value = int(item[1])
                if key in dictionary["POSITIVE"]:
                    tempValue = dictionary["POSITIVE"][key]
                    value = tempValue + value
                dictionary["POSITIVE"][key] = value


    #count the total number of words for both POSITIVE and NEGATIVE
    wordCountPos = 0
    wordCountNeg = 0
    for i in dictionary.keys():
        for key in dictionary[i].keys():
            val = dictionary[i][key]
            if i == "POSITIVE":
                wordCountPos+=val
            elif i == "NEGATIVE":
                wordCountNeg+=val
            if key not in dictionaryUnique:
                dictionaryUnique[key] = 1
                uniqueItems=uniqueItems+1
            else:
                dictionaryUnique[key] = dictionaryUnique[key]+1
    print("Number of unique items: "+str(uniqueItems))

    #print("POSITIVE COUNT: "+str(wordCountPos))
    #print("NEGATIVE COUNT: "+str(wordCountNeg))
    #print("POSITIVE REVIEWS: "+str(positiveReviews))
    #print("NEGATIVE REVIEWS: "+str(negativeReviews))
    #print("TOTAL REVIEWS:" +str(positiveReviews+negativeReviews))

    print("Processing done, preparing model.")

    totalWordCount = 0
    with open(outputFileLoc, "w") as outputFile :
        for i in dictionary.keys():
            if i == "POSITIVE":
                totalWordCount = wordCountPos
                statement = "posReviews:"+str(positiveReviews)+" posWordCount:"+str(wordCountPos)+" "
            elif i == "NEGATIVE":
                totalWordCount = wordCountNeg
                statement="negReviews:"+str(negativeReviews)+" negWordCount:"+str(wordCountNeg)+" "

            for key in dictionary[i].keys():
                val = dictionary[i][key]
                #freq = math.log(val/totalWordCount)
                statement+= str(key)+":"+str(val)+" "

            outputFile.write(statement)
            outputFile.write("\n")
        total="uniqueReviewWords:"+str(uniqueItems)
        outputFile.write(total)
    print("Model prepared.")


def hamSpamAnalysis(inputFileLoc, outputFileLoc):
    inputFile = open(inputFileLoc, "r")
    uniqueItems=0

    hamEmails = 0
    spamEmails = 0
    dictionary = {"HAM" : {}, "SPAM" : {}}
    dictionaryUnique = {}
    for line in inputFile:
        line = str(line).strip()
        items = line.split()
        noOfItems = len(items)
        type = items[0]
        if type=="SPAM":
            spamEmails = spamEmails+1
            for index in range(1, noOfItems):
                item = items[index].split(":")
                key = int(item[0])
                value = int(item[1])
                if key in dictionary["SPAM"]:
                    tempValue = dictionary["SPAM"][key]
                    value = tempValue + value
                dictionary["SPAM"][key] = value

        elif type=="HAM":
            hamEmails = hamEmails+1
            for index in range(1, noOfItems):
                item = items[index].split(":")
                key = int(item[0])
                value = int(item[1])
                if key in dictionary["HAM"]:
                    tempValue = dictionary["HAM"][key]
                    value = tempValue + value
                dictionary["HAM"][key] = value


    #count the total number of words for both HAM and SPAM
    wordCountHam = 0
    wordCountSpam = 0
    for i in dictionary.keys():
        for key in dictionary[i].keys():
            val = dictionary[i][key]
            if i == "HAM":
                wordCountHam+=val
            elif i == "SPAM":
                wordCountSpam+=val
            if key not in dictionaryUnique:
                dictionaryUnique[key] = 1
                uniqueItems=uniqueItems+1
            else:
                dictionaryUnique[key] = dictionaryUnique[key]+1
    #print("Number of unique items: "+str(uniqueItems))

    #print("HAM COUNT: "+str(wordCountHam))
    #print("SPAM COUNT: "+str(wordCountSpam))
    #print("HAM EMAILS: "+str(hamEmails))
    #print("SPAM EMAILS: "+str(spamEmails))
    #print("Total Emails:" +str(hamEmails+spamEmails))
    print("Processing done, preparing model.")

    totalWordCount = 0
    with open(outputFileLoc, "w") as outputFile :
        for i in dictionary.keys():
            if i == "HAM":
                totalWordCount = wordCountHam
                statement = "hamEmails:"+str(hamEmails)+" hamWordCount:"+str(wordCountHam)+" "
            elif i == "SPAM":
                totalWordCount = wordCountSpam
                statement="spamEmails:"+str(spamEmails)+" spamWordCount:"+str(wordCountSpam)+" "

            for key in dictionary[i].keys():
                val = dictionary[i][key]
                statement+= str(key)+":"+str(val)+" "

            outputFile.write(statement)
            outputFile.write("\n")
        total="uniqueEmailWords:"+str(uniqueItems)
        outputFile.write(total)
    print("Model prepared.")

if __name__=="__main__" : main(sys.argv[1:])
