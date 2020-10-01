from util import Util


class AddMeta:
    # initiate the variables and call addMeta
    def __init__(self, site, fileName, folderPath, sharePointFolder, customeMetaDict):
        self.site = site
        self.fileName = fileName
        self.folderPath = folderPath
        self.sharePointFolder = sharePointFolder
        self.customeMetaDict = customeMetaDict
        self.addMeta()

    def addMeta(self):
        instanceOfDocumentLibrary = self.site.List(self.sharePointFolder)
        fields = ['Name', 'ID']
        query = {'Where': [('Contains', 'Name', self.fileName)]}
        GetData = instanceOfDocumentLibrary.GetListItems(fields=fields, query=query)
        getDataDict = GetData[-1] 
        util = Util()
        payload = util.mergeDict(getDataDict, self.customeMetaDict)            
        update_data = [payload]
        instanceOfDocumentLibrary.UpdateListItems(data=update_data,kind='Update')



