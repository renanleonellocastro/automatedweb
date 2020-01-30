#!/usr/bin/python

import requests
import pyquery
import json

class AutomatedWeb:

# Initialize the class with browser opening
#------------------------------------------------------------------------------------------------------------------
    def __init__(self, simulatePage=None, debug=None):
    
        self.m_browser = requests.Session()
        self.m_currentPage = None
        self.m_currentPageData = None
        self.m_debug = debug
        self.m_simulatePage = simulatePage

        if self.m_simulatePage:
            f = open(self.m_simulatePage, "r")
            self.m_currentPageData = f.read()
            f.close()

# Execute a GET command in a given URL (navigate to this url)
#------------------------------------------------------------------------------------------------------------------
    def executeGet(self, url):
        
        self.logDebug('Executando GET na url: %s'%(url))
        self.m_currentPage = self.m_browser.get(url)
        self.m_currentPageData = str(self.m_currentPage.content)

# Execute a POST command in a given URL and with a given dictionary
#------------------------------------------------------------------------------------------------------------------
    def executePost(self, url, data, convertToJson=False):
    
        if convertToJson:
            data = json.dumps(data)

        self.logDebug('Executando POST na url: %s'%(url))
        self.m_currentPage = self.m_browser.post(url, data=data)
        self.m_currentPageData = str(self.m_currentPage.content)

# Return web page contents
#------------------------------------------------------------------------------------------------------------------
    def getCurrentPage(self):
    
        self.logDebug('Retornando pagina atual.') 
        return self.m_currentPageData

# Print web page contents
#------------------------------------------------------------------------------------------------------------------
    def printCurrentPage(self):
 
        self.logDebug('Imprimindo pagina atual.')
        print self.m_currentPageData

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
