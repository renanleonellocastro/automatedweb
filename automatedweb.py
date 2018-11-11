#!/usr/bin/python

import mechanize
import pyquery
import urllib

class AutomatedWeb:

# Initialize the class with browser opening
#------------------------------------------------------------------------------------------------------------------
    def __init__(self, debug=None):
    
        self.m_browser = mechanize.Browser()
        self.m_currentPage = None
        self.m_currentPageData = None
        self.m_debug = debug

# Execute a GET command in a given URL (navigate to this url)
#------------------------------------------------------------------------------------------------------------------
    def executeGet(self, url):
        
        self.logDebug('Executando GET na url: %s'%(url)) 
        self.m_currentPage = self.m_browser.open(url)
        self.m_currentPageData = self.m_currentPage.read()

# Execute a POST command in a given URL and with a given dictionary ()
#------------------------------------------------------------------------------------------------------------------
    def executePost(self, url, data):
    
        self.logDebug('Executando POST na url: %s'%(url)) 
        encodedData = urllib.urlencode(data)   
        self.m_currentPage = self.m_browser.open(url, encodedData)
        self.m_currentPageData = self.m_currentPage.read()

# Return web page contents
#------------------------------------------------------------------------------------------------------------------
    def getCurrentPage(self):
    
        self.logDebug('Retornando pagina atual.') 
        return self.m_currentPageData

# Return specific html text
#------------------------------------------------------------------------------------------------------------------
    def getDataFromPage(self, jquerySelector, lineNumber=None):
    
        self.logDebug('Obtendo dados da pagina atual.') 
        pageData = self.m_currentPageData
        pageSelection = pyquery.PyQuery(pageData)
        data = None
    
        if lineNumber:
            data = pageSelection(jquerySelector).eq(lineNumber).text()
        else:
            data = pageSelection(jquerySelector).text()
    
        return data

# Generate debug log
#------------------------------------------------------------------------------------------------------------------
    def logDebug(self, string):
    
        if self.m_debug:
            print string

#------------------------------------------------------------------------------------------------------------------
