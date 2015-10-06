__author__ = 'jugpreet'
#prepare the 75/25 split of the labeled data and construct
#train, test and the actual class(ouput) files.

import sys
import random

def main(argv):
    print("main")
    inputFileLoc = argv[0]
    trainingDataFileLoc = argv[1]
    testDataFileLoc = argv[2]
    actualClassFileLoc  =argv[3]

    inputFile = open(inputFileLoc, "r")
    trainingFile = open(trainingDataFileLoc, "w")
    testdataFile = open(testDataFileLoc, "w")
    actualClassFile = open(actualClassFileLoc, "w")

    totalLines = 0
    for line in inputFile:
        totalLines = totalLines+1

    print("total lines: "+str(totalLines))

    select = int(totalLines/4)*3 #the amount of test data
    print(select)
    randomDataIndexes = random.sample(range(1,totalLines), select)
    count = 0

    inputFile = open(inputFileLoc, "r")
    for line in inputFile:

        count=count+1
        line = str(line).strip()
        words = str(line).split()

        #build a test data file and a corresponding output file that has the class line by line
        if count in randomDataIndexes:
            type = words[0] #this goes in the actualClassFile

            words[0] = ""
            statement = ""
            for word in words:
                statement = statement + word + " "
            testdataFile.write(statement)
            testdataFile.write("\n")

            actualClassFile.write(type)
            actualClassFile.write("\n")

        #build training data
        else:
            trainingFile.write(line)
            trainingFile.write("\n")


if __name__ == '__main__': main(sys.argv[1:])
