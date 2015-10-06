__author__ = 'jugpreet'
#convert the output of megam to proper format for comparison

import sys

def main(argv):
    inputFile = open(argv[0], "r")
    outputFile = open("sentiment.megam.out", "w")

    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()

        val = int(words[0])
        if val == 1:
            outputFile.write("POSITIVE")
            outputFile.write("\n")
        else:
            outputFile.write("NEGATIVE")
            outputFile.write("\n")





if __name__ == '__main__':main(sys.argv[1:])