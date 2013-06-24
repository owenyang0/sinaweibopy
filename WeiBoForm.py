#coding=utf8
import wx
import os

from WeiboClass import WeiboControl




class MainWindow(wx.Frame):    
    def __init__(self, parent, title):
        self.dirname=''
        self.WeiboText = ''
        self.PicPath = ''  
        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        self.icon = wx.Icon('face.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.tbicon=wx.TaskBarIcon()  
        self.tbicon.SetIcon(self.icon,"wxPython Demo")  
        
        
        self.control_Text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control_Pic = wx.TextCtrl(self, style = wx.TE_READONLY | wx.TE_CHARWRAP )
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        
        
        # Setting up the menu.
        filemenu= wx.Menu()
        aboutmenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open Picture"," Open a file to edit")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        menuAbout= aboutmenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        
        
        #self.tbicon.CreatePopupMenu(menuOpen)
        

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&FILE") # Adding the "filemenu" to the MenuBar
        menuBar.Append(aboutmenu, "&OTHERS")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        self.btn_ChoosePic = wx.Button(self, -1, "&Choose Pic")
        self.btn_SendWeibo = wx.Button(self, -1, "&Send Weibo")
        
        self.sizer_hor = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_hor.Add(self.control_Pic, 1)
        self.sizer_hor.Add(self.btn_ChoosePic, 0)
        self.sizer_hor.Add(self.btn_SendWeibo, 0)
        
        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.btn_ChoosePic)
        self.Bind(wx.EVT_BUTTON, self.OnSend, self.btn_SendWeibo)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #self.Bind(wx.EVT_MENU, self.OnRightClk, id=self.ID_Hello)
        
        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control_Text, 1, wx.EXPAND)
        self.sizer.Add(self.sizer_hor, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.Center()
        #self.sizer.Fit(self)
        self.Show()

    def OnClose(self, event):
        self.tbicon.Destroy()
        self.Destroy()
    
    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, "A simple and easy APP to Update your status"
            "\nbuild 20130827 \nCOPYRIGHT @ YANG 2013", "WeiBo App", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.
        
    def OnRightClk(self, e):
        wx.MessageBox('t')
        event.Skip()

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a picture", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            file_path = os.path.join(self.dirname, self.filename)
            self.control_Pic.SetValue(file_path)
        dlg.Destroy()
    
    def OnSend(self, e):
        self.WeiboText = self.control_Text.Value
        self.PicPath = self.control_Pic.Value
        
        self.StatusBar.SetStatusText(u'正在发送微博，请稍候！')
        WeiboCtrl = WeiboControl(self.WeiboText, self.PicPath)
        return_status = WeiboCtrl.updateText(self)
        self.StatusBar.SetStatusText(return_status)

app = wx.App(False)
frame = MainWindow(None, "WeiBo App")
app.MainLoop()
