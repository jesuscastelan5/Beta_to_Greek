def getSuppLangs():
    """Reads csv file will all supported languages."""
    oldDir = os.getcwd()
    os.chdir('./Prompts') # to access csv
    SuppLangs = read_csv('Supported Languages.csv', header='infer')
    os.chdir(oldDir) # returns to old directory
    return SuppLangs

def overwriteLang (suffix, Prompts):
    """Changes the user language set in UserPref.txt."""
    thispath = './Prompts/Prompts_' + suffix + '.txt'
    if not os.path.exists(thispath):
        return 6
    elif not os.path.exists("UserPref.txt"):
        return 7
    else:
        UserPref = open ("UserPref.txt","w")
        UserPref.write('Language:'+suffix)
        UserPref.close()
        return 0

def getCurrLang():
    """Gets the user language currently set from UserPref.txt."""
    UserPref = open ("UserPref.txt","r")
    UserPref.seek(0,0) # moves cursor to top of program
    UserPrefLang = UserPref.readline(); UserPrefLang = UserPrefLang.split(":")[1]
    UserPref.close()
    return UserPrefLang
    
def getPrompts(promptFile):
    """Reads prompts file and converts the dataframe into a Python dictionary."""
    Prompts = dict()
    promptdf = read_csv (promptFile, sep = ':', header = None, names = ['col1', 'col2'])
    for key in promptdf.loc[:,'col1']:
        Prompts.update ({key : promptdf[promptdf['col1'] == key].iloc[0]['col2'] })
    return Prompts
    
    
def getUserPref():
    """Obtains user language currently set from getCurrLang()
    and finds the txt prompts file."""
    UserPrefLang = getCurrLang()
    oldDir = os.getcwd()
    os.chdir('./Prompts') # to access prompts
    promptFile = 'Prompts_' + UserPrefLang + '.txt'
    if not os.path.exists(promptFile):
        LSF.Error61(UserPrefLang)
        return DataFrame()
    else:
        Prompts = read_csv (promptFile, sep = ":", header = None, names = ["Prompt Name", "Prompts"])
    os.chdir(oldDir) # returns to old directory
    return Prompts

import os
from pandas import read_csv
from pandas import DataFrame
import LangSetFrontend as LSF
