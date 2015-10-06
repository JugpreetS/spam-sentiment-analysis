__author__ = 'jugpreet'
#compare the predicted class with actual class, used for both
#svm and megam with minor changes during the runs.

import sys

def main(argv):
    actualFile = open(argv[0], "r")
    predictedFile = open(argv[1], "r")

    actualDictionary = {}
    actualHam = 0
    actualSpam = 0
    actualCount = 0
    for line in actualFile:
        actualCount=actualCount+1
        line = str(line).strip()
        if line=="POSITIVE":
            actualHam = actualHam+1
        elif line=="NEGATIVE":
            actualSpam =actualSpam+1

        actualDictionary[actualCount] = line


    predictedDictionary = {}
    predictedCount = 0

    for line in predictedFile:
        line = str(line).strip()
        predictedCount = predictedCount+1
        #if line=="HAM":
        #   predictedHam = predictedHam+1
        #elif line=="SPAM":
        #    predictedSpam =predictedSpam+1
        predictedDictionary[predictedCount] = line

    correctHam = 0
    correctSpam = 0
    predictedHam = 0
    predictedSpam = 0

    for index in range (1, predictedCount+1):
        if predictedDictionary[index]=="POSITIVE":
            predictedHam = predictedHam +1
            if actualDictionary[index]=="POSITIVE":
                correctHam = correctHam+1
        elif predictedDictionary[index]=="NEGATIVE":
            predictedSpam = predictedSpam+1
            if actualDictionary[index]=="NEGATIVE":
                correctSpam = correctSpam +1


    hamPrecision = correctHam/predictedHam
    spamPrecision = correctSpam/predictedSpam

    hamRecall = correctHam/actualHam
    spamRecall = correctSpam/actualSpam

    hamF1 = hamPrecision*hamRecall*2/(hamPrecision+hamRecall)

    spamF1 = spamPrecision*spamRecall*2/(spamPrecision+spamRecall)

    print("F1 POSITIVE: " + str(hamF1))
    print("Precision POSITIVE: "+str(hamPrecision))
    print("Recall POSITIVE: "+str(hamRecall))
    print("F1 NEGATIVE: "+ str(spamF1))
    print("Precision NEGATIVE: "+str(spamPrecision))
    print("Recall NEGATIVE: "+str(spamRecall))


if __name__ == '__main__':main(sys.argv[1:])
