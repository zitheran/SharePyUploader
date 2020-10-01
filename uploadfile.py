class Upload:
    # initiate the variables and call filePayload
    def __init__(self, site, filePath, fileName, sharePointFolder):
        self.site = site
        self.filePath = filePath
        self.fileName = fileName
        self.sharePointFolder = sharePointFolder
        self.filePayload()
        
    #Build the file payload
    def filePayload(self):
        folder = self.site.Folder(self.sharePointFolder)
        with open(f'{self.filePath}\\{self.fileName}', 'rb') as f:
            file_content = f.read()

        folder.upload_file(file_content, self.fileName)

