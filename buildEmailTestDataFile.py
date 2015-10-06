__author__ = 'jugpreet'
#prepare the final test data for Spam analysis based on
#email in the spam_or_ham_test folder

import glob


def main():
    print("build file")

    vocabDictionary = {}
    inputFile = open("enron.vocab", "r", encoding="latin1")
    count =0
    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()
        for word in words:
            vocabDictionary[word] = count
            count = count+1
    print("built vocab")

    outputFile = open("spam_test.feat","w", encoding="latin1")
    fileCount=0

    directory = "spam_or_ham_test/"
    fileNames = glob.glob(directory+"/*.txt")
    fileCount=0
    for fileCount in range(1, 11513):
        if int(fileCount) <= 9:
            file = "0000"+str(fileCount)+".txt"
        elif int(fileCount) <=99:
            file = "000"+str(fileCount)+".txt"
        elif int(fileCount) <=999:
            file = "00"+str(fileCount)+".txt"
        elif int(fileCount) <= 9999:
            file = "0"+str(fileCount)+".txt"
        else:
            file = str(fileCount)+".txt"

        fileLoc = directory+file
        buildFile = {}
        inputFile = open(fileLoc, "r", encoding="latin1")
        for line in inputFile:
            line = str(line).strip()
            words = str(line).split()
            for word in words:
                temp = vocabDictionary[word]
                temp = int(temp)

                if temp not in buildFile.keys():
                   buildFile[temp] = 1
                else:
                   buildFile[temp] = int(buildFile[temp])+1

        statement=""
        for key in sorted(buildFile):
            statement+= str(key)+":"+str(buildFile[key])+" "
        outputFile.write(statement)
        outputFile.write("\n")


if __name__ == '__main__':main()