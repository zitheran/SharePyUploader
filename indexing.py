class Indexing:
    def createKeywords(self, folderPath, file):
        file_name_list = file.split('-')
        no_extintion = file_name_list[-1].split('.')        
        file_name_list[-1] = no_extintion[0]  
        keywordList = file_name_list[0:len(file_name_list)]   

        return keywordList

    #reads the index file and creates a list
    def readIndex(self, file, folderPath):                
        with open(f'{folderPath}\\{file}', 'r') as f:
            file_content = f.read()
            indexList = file_content.split(',')
            
            return indexList