__author__ = 'jugpreet'
#prepare Sentiment and Spam test and training data for Svm

import sys

def main(argv):

    #labeledEmailFile = open("labeledEmail.feat", "r")
    labeledEmailFile = open(argv[0], "r")
    labeledEmailSvmFile = open("labeledEmail.svm.file", "w")

    #labeledReviewsFile = open("labeledReviews.feat", "r")
    labeledReviewsFile = open(argv[1], "r")
    labeledReviewsSvmFile = open("labeledReview.svm.file", "w")

    #testEmailFile = open("spam_test.feat", "r")
    testEmailFile = open(argv[2], "r")
    testEmailSvmFile = open("spam_test.svm.file", "w")

    #testReviewsFile = open("sentiment_test.feat.fixed", "r")
    testReviewsFile = open(argv[3], "r")
    testReviewsSvmFile = open("sentiment_test.svm.file", "w")

    #prepare labeled email file for SVM
    for line in labeledEmailFile:
        line = str(line).strip()
        words = str(line).split()
        type = words[0]
        if str(type) == "SPAM":
            words[0] = str(1)
        elif str(type)=="HAM":
            words[0] = str(-1)

        statement = str(words[0]) +" "
        for index in range(1, len(words)):
            items = str(words[index]).split(":")
            statement = statement + str((int(items[0])+1))+":"+items[1] + " "
        labeledEmailSvmFile.write(str(statement))
        labeledEmailSvmFile.write("\n")

    #prepare labeled reviews file for SVM
    for line in labeledReviewsFile:
        line = str(line).strip()
        words = str(line).split()
        type = words[0]
        if str(type) == "POSITIVE":
            words[0] = str(1)
        elif str(type)=="NEGATIVE":
            words[0] = str(-1)

        statement = str(words[0])+" "
        for index in range(1, len(words)):
            items = str(words[index]).split(":")
            statement = statement + str((int(items[0])+1))+":"+items[1] + " "
        labeledReviewsSvmFile.write(str(statement))
        labeledReviewsSvmFile.write("\n")


    #prepare test email file for SVM
    for line in testEmailFile:
        line = str(line).strip()
        words = str(line).split()

        statement = "1 "
        for index in range(0, len(words)):
            items = str(words[index]).split(":")
            statement = statement + str((int(items[0])+1))+":"+items[1] + " "

        testEmailSvmFile.write(str(statement))
        testEmailSvmFile.write("\n")

    #prepare test review file for SVM
    for line in testReviewsFile:
        line = str(line).strip()
        words = str(line).split()

        statement = "1 "
        for index in range(0, len(words)):
            items = str(words[index]).split(":")
            statement = statement + str((int(items[0])+1))+":"+items[1] + " "

        testReviewsSvmFile.write(str(statement))
        testReviewsSvmFile.write("\n")

if __name__ == '__main__':main(sys.argv[1:])
