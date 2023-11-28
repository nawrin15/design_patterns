class JSONData:
    
    def readJSONData(self):
        pass
    
    
class JSONSoftware(JSONData):
    
    def readJSONData(self):
        print("UNDERSTAND ONLY JSON DATA")
    

class XMLData:
    
    def readXMLData(self):
        pass
    
class XMLSoftware(XMLData):
    
    def readXMLData(self):
        print("UNDERSTAND ONLY XML DATA")


class XMLToJSONDataAdapter(JSONData):
    
    def __init__(self, xmlData):
        self.xmlData = xmlData
        
    def readJSONData(self):
        self.xmlData.readXMLData()
        print("Convert here XML data to JSON data.") 
    

if __name__ == "__main__":
    xmlDataSoft = XMLSoftware()
    xmlAdapter = XMLToJSONDataAdapter(xmlDataSoft)
    xmlAdapter.readJSONData()