#!/usr/bin/python

import requests
import pyquery
import urllib3
import json

class AutomatedWeb:

# Initialize the class with browser opening
#------------------------------------------------------------------------------------------------------------------
    def __init__(self, simulatePage=None, debug=None):
    
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.m_browser = requests.Session()
        self.m_browser.trust_env = False
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
        self.m_currentPage = self.m_browser.get(url, verify=False)
        self.m_currentPageData = str(self.m_currentPage.content)

# Execute a POST command in a given URL and with a given dictionary
#------------------------------------------------------------------------------------------------------------------
    def executePost(self, url, data="", convertToJson=False, headers=None):
    
        if convertToJson:
            data = json.dumps(data)

        self.logDebug('Executando POST na url: %s'%(url))
        if (headers):
            self.m_currentPage = self.m_browser.post(url, data=data, headers=headers)
        else:
            self.m_currentPage = self.m_browser.post(url, data)
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
        print (self.m_currentPageData)

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

# Return specific html value
#------------------------------------------------------------------------------------------------------------------
    def getValueFromPage(self, jquerySelector, lineNumber=None):
    
        self.logDebug('Obtendo valores da pagina atual.') 
        pageData = self.m_currentPageData
        pageSelection = pyquery.PyQuery(pageData)
        data = None

        if lineNumber:
            data = pageSelection(jquerySelector).eq(lineNumber).val()
        else:
            data = pageSelection(jquerySelector).val()

        return data

# Return children values of a selection
#------------------------------------------------------------------------------------------------------------------
    def getOptionsValuesFromSelection(self, selectionId):
    
        self.logDebug('Obtendo as opcoes da selecao atual.') 
        pageData = self.m_currentPageData
        pageSelection = pyquery.PyQuery(pageData)
        options = pageSelection('#' + selectionId).children()
        option_values_list = []
        for option in options:
            option_values_list.append(pyquery.PyQuery(option).val())
        return option_values_list

# Return text from each element of a table
#------------------------------------------------------------------------------------------------------------------
    def getTextFromEachElementOfTable(self, tableId, position):
    
        self.logDebug('Obtendo o texto de cada item na tabela.') 
        items = []
        pageData = self.m_currentPageData
        pageSelection = pyquery.PyQuery(pageData)
        table = pageSelection('#' + tableId)
        try:
            rows = pyquery.PyQuery(table.children()[position])('tbody').children()
            for row in rows:
                col = []
                for item in pyquery.PyQuery(row).children():
                    col.append(pyquery.PyQuery(item).text())
                items.append(col)
            return items
        except:
            return []

# Generate debug log
#------------------------------------------------------------------------------------------------------------------
    def logDebug(self, string):
    
        if self.m_debug:
            print (string)

#------------------------------------------------------------------------------------------------------------------
