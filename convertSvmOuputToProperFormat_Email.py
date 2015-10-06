__author__ = 'jugpreet'
#convert the output of svm to proper format for comparison

import sys

def main(argv):

    inputFile = open(argv[0], "r")
    outputFile = open("actualClass.review.svm.file", "w")

    for line in inputFile:
        line = str(line).strip()
        val = float(line)
        if val < 0:
            outputFile.write("HAM")
            outputFile.write("\n")
        else:
            outputFile.write("SPAM")
            outputFile.write("\n")

if __name__ == '__main__':main(sys.argv[1:])