# help from mail.python.org/pipermail/python-list/2003-August/213591.html

MISTAKES = {'()', ')(', # multiple types of breath
            '/)', '/(', '\\)', '\\(', '=(', '=)', # accent before breath
            '|)', '|(', # iota before breath
            '|/', '|\\', '|=', # iota before accent
            '/\\', '/=', '\\/', '\\=', '=/', '=\\', # multiple types of accent
            '*)', '*(', '*/', '*\\', '*=', '*|', '*+', '*_', # incorr use of captital sign
            '+)', '+(', ')+', '+(', '+|', '+_', # incorr use of diaresis needs more
            # to be removed to be optional for non Attic dialects
            'U)', # capital upsilon with soft breath
            'e=', 'E=', 'o=', 'O=', # incorr use of =
            'e_','o_', # incorr use of macrons
            'e|', 'E|', 'i|', 'I|', 'o|', 'O|', 'u|', 'U|' # incorr use iota sub
            }
CAPS = {'*a':'A', '*b':'B', '*c':'C', '*d':'D', '*e':'E',
        '*f':'F', '*g':'G', '*h':'H', '*i':'I', '*k':'K',
        '*l':'L', '*m':'M', '*n':'N', '*o':'O', '*p':'P',
        '*q':'Q', '*r':'R', '*s':'S', '*t':'T', '*u':'U',
        '*v':'V', '*w':'W', '*x':'X', '*y':'Y', '*z':'Z'}

def CheckMistakes (string):
    """
    Checks for syntax mistakes like using two breath marks or
    two accent marks and also checks against Attic writing conventions
    such as no epsilon or omicron with a macron.
    """
    string += ' '
    len_str = len (string);
    for i in range(len_str):
        if string [i:i + 2] in MISTAKES:
            ErrMsg = Prompts['error1'] + '\n' \
            + string [i:i + 2] + Prompts['error2'] \
            + string [:i + 3] + Prompts['error3'] + '\n' \
            + Prompts['error4']
            return ErrMsg
        else:
            # if there is no mistake, do not return yet, keep going
            pass
    return ""

def InterpretNCheck(raw_string):
    """
    Checks for syntax errors and against Attic writing conventions
    using CheckMistakes(), and capitalizes vowels with a *,
    then it sends to BETA_TO_GREEK().
    """
    UserError = ""; len_str = len (raw_string);
    # checks for syntax mistakes
    UserError = CheckMistakes (raw_string)
    if UserError == "":
        # converts * + letter -> uppercase
        string = ''; i =0;
        while i < len_str:
            if raw_string [i:i + 2] in CAPS:
                string += CAPS [raw_string [i:i + 2]]; i += 2
            else:
                string += raw_string [i]; i +=1
        return BETA_TO_GREEK (string)
    wx.MessageBox (UserError, 'User Error',
            wx.OK | wx.ICON_WARNING)
    return ""
    
def main():
    appTitle = Prompts['title']
    myFrame = wx.Frame(None, title = appTitle, size=(550, 400))
    MainPanel = wx.Panel (myFrame)
    
    leftBarrier = 10 # left most of widgets
    upperBarrier = 10 # upper most of widgets
    xpadd = 10 # x axis padding btw widgets
    ypadd = 10 # y axis padding btw widgets
    
    
    def LangSettings(event):
        """
        Changes user language of interpreter.
        """
        LSF.changeLang(myFrame, Prompts)
        # #global LangMenuInUse
        # #if (LangMenuInUse):
        # #    warning = Prompts[Prompts['Prompt Name'] == 'interpretButton'].iloc[0]['Prompts']
        # #    messagebox.showwarning(myWin.title.get(),warning)
        # #else:
        # #    LangMenuInUse = True
        # #    changeLang(Prompts)
        # #    LangMenuInUse = False

    xcoor = leftBarrier
    ycoor = upperBarrier
    SettB = wx.Button (MainPanel, -1,
        Prompts['langButton'],
        pos = (xcoor,upperBarrier))
    SettB.Bind(wx.EVT_BUTTON, LangSettings)
    
    def HelpPage(event):
        """
        Gives users a quick guide to program.
        """
        helpPop = wx.Frame(myFrame, title = "help page", size = (500, 400))
        helpPopPanel = wx.Panel (helpPop)
        wx.StaticText(helpPopPanel, pos = (leftBarrier, upperBarrier),
            label = Prompts['helpMessage']).Wrap(500 - 30)
        helpPop.Show()

    ycoor += SettB.GetSize()[1] + ypadd
    HelpB = wx.Button(MainPanel, -1,
        Prompts['helpButton'],
        pos = (xcoor, ycoor))
    HelpB.Bind(wx.EVT_BUTTON, HelpPage)
    
    def AboutPage(event):
        """
        Tells users about program and creator.
        """
        aboutPop = wx.Frame(myFrame, title = "about page", size = (500, 400))
        aboutPopPanel = wx.Panel (aboutPop)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        text1 = wx.StaticText(aboutPopPanel,
            label = Prompts['aboutMessage'])
        lnk = hl.HyperLinkCtrl(aboutPopPanel, -1, "wxPython Main Page",
                                  URL="http://www.wxpython.org/")
        text2 = wx.StaticText(aboutPopPanel, label='Plain2')
        text_sizer.Add(text1, 0) # , wx.LEFT|wx.ALL, 5
        text_sizer.Add(lnk, 0) # , wx.ALL, 5 
        text_sizer.Add(text2, 0) # , wx.ALL, 5 
        aboutPopPanel.SetSizer(text_sizer)
        
        #wx.StaticText (aboutPopPanel, pos = (leftBarrier, upperBarrier),
        #    label = Prompts[Prompts['Prompt Name'] == 'aboutMessage'].iloc[0]['Prompts']).Wrap(500 - 30)
        aboutPop.Centre()
        aboutPop.Show()

    ycoor += HelpB.GetSize()[1] + ypadd
    AboutB = wx.Button(MainPanel, -1, 
        Prompts['aboutButton'],
        pos = (xcoor, ycoor))
    AboutB.Bind(wx.EVT_BUTTON, AboutPage)
    
    xcoor += HelpB.GetSize()[0] + xpadd
    myInput = wx.TextCtrl(MainPanel, size = (300, 100), pos = (xcoor,upperBarrier),  style = wx.TE_MULTILINE)
#   myInput.unbind('<Shift-Return>', None)
    ycoor = upperBarrier + myInput.GetSize()[1] + ypadd
    myResp = wx.TextCtrl(MainPanel, size = (300, 100), pos = (xcoor,ycoor),  style = wx.TE_MULTILINE)
    
    def doInterpret(event):
        """
        Clears output box, executes InterpretNCheck(), and returns Greek string.
        """
        myResp.SetValue("")
        Resp = myInput.GetValue()
        Resp = InterpretNCheck(Resp)
        myResp.SetValue(Resp)
    # def ShiftE(event):
        # """Executes doInterpret() when ENTER is ShiftEd."""
        # doInterpret(None)
    
    def ShiftE (event):
        # '<Shift-Return>'
        if (event.GetKeyCode() == wx.WXK_RETURN):
            print("It worked again!")

    xcoor += myInput.GetSize()[0] + xpadd
    InterpretB = wx.Button(MainPanel, -1,
       Prompts['interpretButton'], pos = (405, upperBarrier))
    InterpretB.Bind(wx.EVT_BUTTON, doInterpret)
    
    def AboutPageTab(event):
        keycode = event.GetKeyCode()
        print(keycode)
        if (keycode == wx.WXK_F1):
            print("It worked again!")
        event.Skip()
    
    # No need for this one: InterpretB.Bind('<KeyRelease-Return>', doInterpretsTab)
    # MainPanel.Bind(wx.EVT_KEY_DOWN, ShiftE)
    # MainPanel.Bind(wx.EVT_KEY_UP, AboutPageTab)
    
    myFrame.Show()
    myWin.MainLoop()


def main1():
    def ShiftE(event = None):
        """Executes doInterpret() when ENTER is ShiftEd."""
        doInterpret()

    #layout
    SettB.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    HelpB.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    AboutB.grid(row = 3, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    myInput.grid(row = 1, column = 9, rowspan = 3, columnspan = 4, padx = 10, pady = 10)
    myResp.grid(row = 5, column = 9, rowspan = 3, columnspan = 4, padx = 10, pady = 10)
    InterpretB.grid(row = 1, column = 40, rowspan = 1, columnspan = 1, padx = 10, pady = 10)


    myWin.mainloop()

def initiate():
    global myWin
    myWin = wx.App()
    if not (os.path.exists("UserPref.txt")):
        warning = "Make sure UserPref.txt is in " + os.getcwd() + " and that it contains 'Language:eng'"
        wx.MessageBox(warning, 'Betacode to Greek Text Interpreter',
            wx.OK | wx.ICON_ERROR)
        #wx.ICON_ERROR('Betacode to Greek Text Interpreter', warning)
    elif not (os.path.exists("./Prompts/Supported Languages.csv")):
        warning = 'Make sure "Supported Languages.csv" is in ' + os.getcwd() + "\Prompts"
        wx.MessageBox(warning, 'Betacode to Greek Text Interpreter',
            wx.OK | wx.ICON_ERROR)
        #wx.ICON_ERROR('Betacode to Greek Text Interpreter', warning)
    else:
        global Prompts
        Prompts = LS.getUserPref()
        if len(Prompts) == 0:
            return -1
        else:
            main()
    

import os
import wx
import wx.lib.agw.hyperlink as hl
from BETA_TO_GREEK import *
import LangSet22 as LS
import LangSetFrontend2 as LSF

# LangMenuInUse = False


initiate()


