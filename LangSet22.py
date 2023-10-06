def getSuppLangs():
    """
    Reads csv file with all supported languages.
    
    Returns: SuppLangs (dataframe) SuppLangs
    """
    oldDir = os.getcwd()
    os.chdir('./Prompts') # to access csv
    SuppLangs = read_csv('Supported Languages.csv', header='infer')
    os.chdir(oldDir) # returns to old directory
    return SuppLangs

def overwriteLang (suffix):
    """
    Changes the user language set in UserPref.txt.
    
    Param: suffix (str) ISO 693-3 language code that the user chose
    
    Returns: (int) 0 if the suffix could be replaced, error code otherwise
    """
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
    """
    Gets the user language currently set from UserPref.txt.
    
    Returns: UserPrefLang (str) ISO 963-3 language code
    """
    UserPref = open ("UserPref.txt","r")
    UserPref.seek(0,0) # moves cursor to top of program
    UserPrefLang = UserPref.readline(); UserPrefLang = UserPrefLang.split(":")[1]
    UserPref.close()
    return UserPrefLang
    
def getPrompts(promptFile):
    """
    Reads prompts file and converts the dataframe into a Python dictionary.
    
    Param: promptFile (str) the name of the file that contains the prompts
        ([almost] everything that will be displayed to the user)

    Returns: Prompts (dict)
    """
    Prompts = dict()
    promptdf = read_csv (promptFile, sep = ':', header = None, names = ['col1', 'col2'])
    for key in promptdf.loc[:,'col1']:
        Prompts.update ({key : promptdf[promptdf['col1'] == key].iloc[0]['col2'] })
    return Prompts
    
    
def getUserPref():
    """
    Obtains user language currently set from getCurrLang()
    and finds the txt prompts file.
    
    Returns: Prompts (dict)
    """
    UserPrefLang = getCurrLang()
    oldDir = os.getcwd()
    os.chdir('./Prompts') # to access prompts
    promptFile = 'Prompts_' + UserPrefLang + '.txt'
    if not os.path.exists(promptFile):
        LSF.Error61(UserPrefLang)
        return DataFrame()
    else:
        Prompts = getPrompts(promptFile)
    os.chdir(oldDir) # returns to old directory
    return Prompts

import os
from pandas import read_csv
from pandas import DataFrame
import LangSetFrontend2 as LSF
