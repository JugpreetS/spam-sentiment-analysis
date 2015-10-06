__author__ = 'jugpreet'

import sys
import math

def main(argv):
    inputFileLoc = argv[0]
    testFileLoc = argv[1]
    #actualFileLoc = argv[2]

    #build model dictionary
    inputFile = open(inputFileLoc, "r")

    type = ""
    modelDictionary = {}
    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()
        type = words[0].split(":")[0]
        break

    if type=="negReviews" or type=="posReviews" or type=="uniqueReviewWords":
        #print("Reviews model")
        #sentimentClassification(inputFileLoc, testFileLoc, actualFileLoc)
        sentimentClassification(inputFileLoc, testFileLoc)
    elif type=="hamEmails" or type=="spamEmails" or type=="uniqueEmailWords":
        #print("Email model")
        #hamSpamClassification(inputFileLoc, testFileLoc, actualFileLoc)
        hamSpamClassification(inputFileLoc, testFileLoc)


#def sentimentClassification(inputFileLoc, testFileLoc, actualFileLoc):
def sentimentClassification(inputFileLoc, testFileLoc):
    inputFile = open(inputFileLoc, "r")
    modelDictionary = {}

    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()
        val=""
        for word in words:

            items = word.split(":")
            if items[0]=="posReviews":
                modelDictionary["POSITIVE"] = {}
                val = "POSITIVE"
            elif items[0] =="negReviews":
                modelDictionary["NEGATIVE"] = {}
                val = "NEGATIVE"
            elif items[0] == "uniqueReviewWords":
                modelDictionary["WORDCOUNT"] = {}
                val = "WORDCOUNT"

            modelDictionary[val][items[0]] = items[1]

    #classifySentiment(modelDictionary, testFileLoc, actualFileLoc)
    classifySentiment(modelDictionary, testFileLoc)


#def hamSpamClassification(inputFileLoc, testFileLoc, actualFileLoc):
def hamSpamClassification(inputFileLoc, testFileLoc):
    inputFile = open(inputFileLoc, "r")
    modelDictionary = {}

    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()
        val=""
        for word in words:
            items = word.split(":")
            if items[0]=="hamEmails":
                modelDictionary["HAM"] = {}
                val = "HAM"
            elif items[0] =="spamEmails":
                modelDictionary["SPAM"] = {}
                val = "SPAM"
            elif items[0] == "uniqueEmailWords":
                modelDictionary["WORDCOUNT"] = {}
                val = "WORDCOUNT"

            modelDictionary[val][items[0]] = items[1]

    #classifySpam(modelDictionary, testFileLoc, actualFileLoc)
    classifySpam(modelDictionary, testFileLoc)


#def classifySentiment(modelDictionary, testFileLoc, actualFileLoc):
def classifySentiment(modelDictionary, testFileLoc):

    testFile = open(testFileLoc, "r")
    #actualFile = open(actualFileLoc, "r")

    vocabularySize = modelDictionary["WORDCOUNT"]["uniqueReviewWords"]
    positiveReviews = modelDictionary["POSITIVE"]["posReviews"]
    negativeReviews = modelDictionary["NEGATIVE"]["negReviews"]
    posWordCount = modelDictionary["POSITIVE"]["posWordCount"]
    negWordCount = modelDictionary["NEGATIVE"]["negWordCount"]

    #print("vocab size "+str(vocabularySize))
    #print("positiveReviews "+str(positiveReviews))
    #print("negativeReviews "+str(negativeReviews))
    #print("posWordCount "+str(posWordCount))
    #print("negWordCount "+str(negWordCount))

    probPositiveLog = math.log(int(positiveReviews)/(int(positiveReviews)+int(negativeReviews)))
    probNegativeLog = math.log(int(negativeReviews)/(int(positiveReviews)+int(negativeReviews)))


    testCount = 0
    #actualCount = 0
    #actualDictionary = {}
    #actualPositive = 0
    #actualNegative = 0
    for line in testFile:
        testCount=testCount+1
    #for line in actualFile:
    #    actualCount=actualCount+1
    #    line = str(line).strip()
    #    if line=="POSITIVE":
    #        actualPositive = actualPositive+1
    #   elif line=="NEGATIVE":
    #        actualNegative =actualNegative+1

    #    actualDictionary[actualCount] = line

    #calculate probability of POSITIVE review
    #predictedDictionary = {}
    count=0
    #outputFile = open("sentiment.nb.out", "w")

    testFile = open(testFileLoc, "r")
    for line in testFile:
        posProbLog = 0
        negProbLog = 0
        #count=count+1
        line = str(line).strip()
        words =str(line).split()
        for word in words:
            item = str(word).split(":")
            feature = str(item[0])
            freq = str(item[1])
            #POSITIVE
            if feature in modelDictionary["POSITIVE"]:
                posOccurrencesInTrainingSet = modelDictionary["POSITIVE"][feature]
            else:
                posOccurrencesInTrainingSet = 1
            posProbLog = posProbLog + math.log((int(posOccurrencesInTrainingSet) + 1)/(int(posWordCount)+int(vocabularySize)))

            #NEGATIVE
            if feature in modelDictionary["NEGATIVE"]:
                negOccurrencesInTrainingSet = modelDictionary["NEGATIVE"][feature]
            else:
                negOccurrencesInTrainingSet = 1
            negProbLog = negProbLog + math.log((int(negOccurrencesInTrainingSet) + 1)/(int(negWordCount)+int(vocabularySize)))

        posProbLog = posProbLog + probPositiveLog
        negProbLog = negProbLog + probNegativeLog
        finalClass = "POSITIVE"
        if posProbLog > negProbLog:
            finalClass = "POSITIVE"
        else:
            finalClass = "NEGATIVE"

        #predictedDictionary[count] = finalClass
        #outputFile.write(str(finalClass))
        #outputFile.write("\n")
        #print(finalClass)
        sys.stdout.write(finalClass)
        sys.stdout.write("\n")


    #calulate precision and recall for POSITIVE and NEGATIVE
    #correctPositive = 0
    #correctNegative = 0
    #totalPositive = 0
    #totalNegative = 0

    #for index in range (1, count+1):
    #    if predictedDictionary[index]=="POSITIVE":
    #        totalPositive = totalPositive +1
    #        if actualDictionary[index]=="POSITIVE":
    #            correctPositive = correctPositive+1
    #    elif predictedDictionary[index]=="NEGATIVE":
    #        totalNegative = totalNegative+1
    #        if actualDictionary[index]=="NEGATIVE":
    #            correctNegative = correctNegative +1


    #print(str(totalPositive))
    #print(str(totalNegative))
    #print(str(correctPositive))
    #print(str(correctNegative))

    #posPrecision = correctPositive/totalPositive
    #negPrecision = correctNegative/totalNegative

    #posRecall = correctPositive/actualPositive
    #negRecall = correctNegative/actualNegative

    #posF1 = posPrecision*posRecall*2/(posPrecision+posRecall)

    #negF1 = negPrecision*negRecall*2/(negPrecision+negRecall)
    #print("F1 Positive: " + str(posF1))

    #print("Precision Positive: "+str(posPrecision))
    #print("Recall Positive: "+str(posRecall))
    #print("F1 Negative: "+ str(negF1))
    #print("Precision Negative: "+str(negPrecision))
    #print("Recall Negative: "+str(negRecall))


#def classifySpam(modelDictionary, testFileLoc, actualFileLoc):
def classifySpam(modelDictionary, testFileLoc):
    testFile = open(testFileLoc, "r")
    #actualFile = open(actualFileLoc, "r")

    vocabularySize = modelDictionary["WORDCOUNT"]["uniqueEmailWords"]
    hamEmails = modelDictionary["HAM"]["hamEmails"]
    spamEmails = modelDictionary["SPAM"]["spamEmails"]
    hamWordCount = modelDictionary["HAM"]["hamWordCount"]
    spamWordCount = modelDictionary["SPAM"]["spamWordCount"]

    #print("vocab size "+str(vocabularySize))
    #print("hamEmails "+str(hamEmails))
    #print("spamEmails "+str(spamEmails))
    #print("hamWordCount "+str(hamWordCount))
    #print("spamWordCount "+str(spamWordCount))

    probHamLog = math.log(int(hamEmails)/(int(hamEmails)+int(spamEmails)))
    probSpamLog = math.log(int(spamEmails)/(int(hamEmails)+int(spamEmails)))


    testCount = 0
    actualCount = 0
    actualDictionary = {}
    actualHam = 0
    actualSpam = 0
    for line in testFile:
        testCount=testCount+1
    #for line in actualFile:
    #    actualCount=actualCount+1
    #    line = str(line).strip()
    #    if line=="HAM":
    #        actualHam = actualHam+1
    #    elif line=="SPAM":
    #        actualSpam =actualSpam+1

    #    actualDictionary[actualCount] = line

    #calculate probability of POSITIVE review
    #predictedDictionary = {}
    count=0

    #outputFile = open("spam.nb.out", "w")

    testFile = open(testFileLoc, "r")
    for line in testFile:
        hamProbLog = 0
        spamProbLog = 0
        #count=count+1
        line = str(line).strip()
        words =str(line).split()
        for word in words:
            item = str(word).split(":")
            feature = str(item[0])
            freq = str(item[1])
            #HAM
            if feature in modelDictionary["HAM"]:
                hamOccurrencesInTrainingSet = modelDictionary["HAM"][feature]
            else:
                hamOccurrencesInTrainingSet = 1
            hamProbLog = hamProbLog + math.log((int(hamOccurrencesInTrainingSet) + 1)/(int(hamWordCount)+int(vocabularySize)))

            #SPAM
            if feature in modelDictionary["SPAM"]:
                spamOccurrencesInTrainingSet = modelDictionary["SPAM"][feature]
            else:
                spamOccurrencesInTrainingSet = 1
            spamProbLog = spamProbLog + math.log((int(spamOccurrencesInTrainingSet) + 1)/(int(spamWordCount)+int(vocabularySize)))

        hamProbLog = hamProbLog + probHamLog
        spamProbLog = spamProbLog + probSpamLog
        finalClass = "HAM"
        if hamProbLog > spamProbLog:
            finalClass = "HAM"
        else:
            finalClass = "SPAM"

        #predictedDictionary[count] = finalClass
        #outputFile.write(str(finalClass))
        #outputFile.write("\n")
        #print(finalClass)
        sys.stdout.write(finalClass)
        sys.stdout.write("\n")


    #calulate precision and recall for HAM and SPAM
    #correctHam = 0
    #correctSpam = 0
    #totalHam = 0
    #totalSpam = 0

    #for index in range (1, count+1):
    #    if predictedDictionary[index]=="HAM":
    #        totalHam = totalHam +1
    #        if actualDictionary[index]=="HAM":
    #            correctHam = correctHam+1
    #       totalSpam = totalSpam+1
    #        if actualDictionary[index]=="SPAM":
    #            correctSpam = correctSpam +1


    #print(str(totalHam))
    #print(str(totalSpam))
    #print(str(correctHam))
    #print(str(correctSpam))

    #hamPrecision = correctHam/totalHam
    #spamPrecision = correctSpam/totalSpam

    #hamRecall = correctHam/actualHam
    #spamRecall = correctSpam/actualSpam

    #hamF1 = hamPrecision*hamRecall*2/(hamPrecision+hamRecall)

    #spamF1 = spamPrecision*spamRecall*2/(spamPrecision+spamRecall)
    #print("F1 Ham: " + str(hamF1))

    #print("Precision Ham: "+str(hamPrecision))
    #print("Recall Ham: "+str(hamRecall))
    #print("F1 Spam: "+ str(spamF1))
    #print("Precision Spam: "+str(spamPrecision))
    #print("Recall Spam: "+str(spamRecall))


if __name__=="__main__" : main(sys.argv[1:])