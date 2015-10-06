__author__ = 'jugpreet'
#contruct the labeled data for Spam analysis.
#it uses the enron.vocab and email present in folders
#enron(1,2,4,5)
import glob


def main():

    vocabDictionary = {}
    inputFile = open("enron.vocab", "r", encoding="latin1")
    #outputFileTest = open("testVocabFile", "w")
    count =0
    for line in inputFile:
        line = str(line).strip()
        words = str(line).split()
        for word in words:
            vocabDictionary[word] = count
            count = count+1
    print("built vocab")


    dictionaryUnique = {}
    uniqueItems=0;

    #build ham data
    list = ["enron1","enron2", "enron4", "enron5"]
    #list = ["enron11"]
    outputFile = open("labeledEmail.feat","w", encoding="latin1")
    fileCount=0
    for directory in list:
        fileNames = glob.glob(directory+"/ham/*.txt")
        fileCount=0
        for file in fileNames:
            fileCount = fileCount+1
            buildFile = {}
            inputFile = open(file, "r", encoding="latin1")
            for line in inputFile:
                line = str(line).strip()
                words = str(line).split()
                for word in words:
                    temp = vocabDictionary[word]
                    temp = int(temp)

                    if temp not in dictionaryUnique.keys():
                        dictionaryUnique[temp] = 1
                        uniqueItems=uniqueItems+1

                    if temp not in buildFile.keys():
                       buildFile[temp] = 1
                    else:
                       buildFile[temp] = int(buildFile[temp])+1

            statement = "HAM "
            #buildFile = sorted(buildFile)
            for key in sorted(buildFile):
                statement+= str(key)+":"+str(buildFile[key])+" "
            outputFile.write(statement)
            outputFile.write("\n")

        print("HAM file in "+ str(directory) + " "+ str(fileCount))

    #build spam data
    fileCount=0
    for directory in list:
        fileNames = glob.glob(directory+"/spam/*.txt")
        fileCount=0
        for file in fileNames:
            fileCount = fileCount+1
            buildFile = {}
            inputFile = open(file, "r", encoding="latin1")
            for line in inputFile:
                words = str(line).split()
                for word in words:
                    temp = vocabDictionary[word]
                    temp = int(temp)

                    if temp not in dictionaryUnique.keys():
                        dictionaryUnique[temp] = 1
                        uniqueItems=uniqueItems+1
                    
                    if temp not in buildFile.keys():
                       buildFile[temp] = 1
                    else:
                       buildFile[temp] = int(buildFile[temp])+1


            statement = "SPAM "
            #buildFile = sorted(buildFile)
            for key in sorted(buildFile):
                statement+= str(key)+":"+str(buildFile[key])+" "
            outputFile.write(statement)
            outputFile.write("\n")

        print("SPAM file in "+ str(directory) + " "+ str(fileCount))

    print("Unique items: "+str(uniqueItems))


if __name__=="__main__" : main()