__author__ = 'jugpreet'
#convert the Sentiments rating to POSITIVE/NEGATIVE


def main():

    inputFile = open("labeledBow.feat.fixed", "r")
    outputFile = open("labeledReviews.feat", "w")
    for line in inputFile:
        line = str(line).strip()
        items = line.split()
        type = items[0]
        if int(type)<=4:
            items[0] = "NEGATIVE"
        elif int(type)>=7:
            items[0] = "POSITIVE"

        statement = ""
        for item in items:
            statement = statement + item + " "
        outputFile.write(str(statement))
        outputFile.write("\n")


if __name__=="__main__" : main()
