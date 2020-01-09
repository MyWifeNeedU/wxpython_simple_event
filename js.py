#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------
 
import wx
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title,
                          pos=(10, 10), size=(1800, 1000))

        # Create the menubar
        ###menuBar = wx.MenuBar()

        # and a menu 
        ###menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        ###menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        ###self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        ###menuBar.Append(menu, "&File")
        ###self.SetMenuBar(menuBar)

        ###self.CreateStatusBar()
        

        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        self.text1 = wx.StaticText(panel, -1, "Hello World!")
        self.text1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.text1.SetSize(self.text1.GetBestSize())
        ###btn = wx.Button(panel, -1, "Close")
        ###funbtn = wx.Button(panel, -1, "Just for fun...")

        # bind the button events to handlers
        ###self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, btn)
        ###self.Bind(wx.EVT_BUTTON, self.OnFunButton, funbtn)
        

        image = wx.Image('image.png', wx.BITMAP_TYPE_ANY)
        #image =  wx.EmptyImage(240,240)
        self.imageBitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(image))
        ###imageBitmap.Bind(wx.EVT_MOTION, self.OnMove)
        self.imageBitmap.Bind(wx.EVT_LEFT_DOWN, self.OnMove)


        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text1, 0, wx.ALL, 10)
        ###sizer.Add(btn, 0, wx.ALL, 10)
        ###sizer.Add(funbtn, 0, wx.ALL, 10)
        sizer.Add(self.imageBitmap, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        
        panel.Layout()
        self.text1.SetLabel("aaaa")
        
        
        self.driver = webdriver.PhantomJS("bin\\phantomjs.exe") # or add to your PATH
        self.driver.set_window_size(1024, 768) # optional
        self.driver.get('https://google.com/')
        #actions = ActionChains(self.driver)
        #actions.move_by_offset(567,264)
        #actions.click()
        #actions.perform()
        #time.sleep(10)
        self.driver.save_screenshot('screen.png') # save a screenshot to disk
        self.imageBitmap.SetBitmap(wx.Bitmap('screen.png'))
        ###sbtn = self.driver.find_element_by_css_selector('button.gbqfba')
        ###sbtn.click()
        

        
        #wx.Frame.SetTitle('yourtitle')
    def OnMove(self, event):
        x, y = event.GetPosition()
        #wx.Frame.SetTitle('yourtitle')
        self.text1.SetLabel(str(x)+","+str(y))
        ###self.driver.clickAt("/html/body",str(x)+","+str(y))
        actions = ActionChains(self.driver)
        actions.move_by_offset(x,y)
        actions.click()
        actions.perform()
        time.sleep(5)
        self.driver.save_screenshot('screen.png')
        self.imageBitmap.SetBitmap(wx.Bitmap('screen.png'))
        
        
    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        print ("See ya later!")
        self.Close()

    def OnFunButton(self, evt):
        """Event handler for the button click."""
        print ("Having fun yet?")


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Simple wxPython App")
        self.SetTopWindow(frame)

        print ("Print statements go to this stdout window by default.")

        frame.Show(True)
        return True
        
app = MyApp(redirect=True)
app.MainLoop()

