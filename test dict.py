def main(promptFile):
    SuppLangs = list()
    promptdf = read_csv (promptFile, header = "infer")
    
    for key in promptdf.loc[:,'ISO 639-3 Code']:
        SuppLangs.update (promptdf[promptdf['ISO 639-3 Code'] == key].iloc[0]['Native Name'])
    SuppLangs.keys()
    print(SuppLangs['title'])
    

def main1(promptFile):
    ISOCODES = list ()
    natName = list()
    langdf = read_csv (promptFile, header = "infer")

    for ISOCode in langdf.loc[:,'ISO 639-3 Code']:
        ISOCODES.append (ISOCode)
        natName.append(
            langdf[langdf['ISO 639-3 Code'] == ISOCode].iloc[0]['Native Name']
        )
    myList = [ISOCODES, natName]
    print(myList)
    print(myList[0])

def main2(promptFile):
    ISOCODES = list ()
    natName = list()
    with open(promptFile) as csv_file:
        csv_rows = csv.reader(csv_file, delimiter = ",")
        for row in csv_rows:
            ISOCODES.append (row[0])
            natName.append( row [1])
    myList = [ISOCODES, natName]
    print(myList)
    print(myList[0])


#from pandas import read_csv
import csv
main2('Supported Languages.csv')

# main('Supported Languages.csv')
myD = dict()
if len(myD) == 0:
    print ("Uh oh")
