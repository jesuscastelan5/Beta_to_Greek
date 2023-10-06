def Error6(Prompts):
    wx.MessageBox(Prompts['error6'], 'Error 6',
        wx.OK | wx.ICON_ERROR)

def Error61(suffix):
    errorMsg = "It looks like " + suffix + " is not an accepted language."
    wx.MessageBox (errorMsg, 'Error 61', wx.OK | wx.ICON_ERROR)


def Error7(Prompts):
    errorMsg = Prompts['error7'] + os.getcwd()
    wx.MessageBox(errorMsg, 'Error 7', wx.OK | wx.ICON_ERROR)

def SuccChangeLang(Prompts):
    wx.MessageBox (Prompts['changeLangDone'],
        'Successfully Changed Language', wx.OK | wx.ICON_INFORMATION)

def changeLang (parentFrame, Prompts):
    """
    GUI to change user language.
    """
    
    def PressedOK(event):
        """
        Gives user last chance to not change user language.
        if user says 'yes', uses overwriteLang() to change language.
        """
        
        # not MessageBox
        AskBox = wx.MessageDialog (LangPop, Prompts['AskBeforeChange'],
        "Change Langs", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        
        # ShowModal()
        if AskBox.ShowModal() == wx.ID_YES:
            ind = dropMenu.GetSelection()
            langResult = LS.overwriteLang (SuppLangs['ISO 639-3 Code'].iloc[ind])
            if langResult == 6:
                Error6(Prompts)
            elif langResult == 7:
                Error7(Prompts)
            else:
                SuccChangeLang(Prompts)
        else:
            pass
        
    
    LangPop = wx.Frame(parentFrame, title = "Lang settings", size = (500, 400))
    LangPopPanel = wx.Panel (LangPop)
    wx.StaticText (LangPopPanel, label = Prompts['changeLangMessage'])
    
    SuppLangs = LS.getSuppLangs()
    langList = SuppLangs['ISO 639-3 Code'].values + " - " + SuppLangs['Native Name'].values
    dropMenu = wx.Choice (LangPopPanel, choices = langList, pos = (15, 30))
    
    try:
        currLangInd = SuppLangs.index(LS.getCurrLang())
    except:
        currLangInd = 0

    dropMenu.SetSelection(currLangInd)
    #dropMenu.Bind(wx.EVT_CHOICE, onSelect)
    
    ConfirmB = wx.Button (LangPopPanel, -1,
            Prompts['ConfirmLangSettButton'],
            pos = (150 ,30))
    ConfirmB.Bind(wx.EVT_BUTTON, PressedOK)
    
    
    LangPop.Show()


import os
import wx
import LangSet22 as LS