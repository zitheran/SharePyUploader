class Util:    
    def mergeDict(self, dict1, dict2):
        res = {**dict1, **dict2}
        return res

    def createDict(self, customeColumnList, keywordsList):
        res = dict(zip(customeColumnList, keywordsList))
        return res