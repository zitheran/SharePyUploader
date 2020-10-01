from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path

from authentication import Auth
from uploadfile import Upload
from addmeta import AddMeta
from indexing import Indexing
from util import Util


def main():
    parser = ArgumentParser(description = 'Process the arguments')
    parser.add_argument('-ConfigFile', help='Enter the config file name', type=str)
    args = parser.parse_args()

    config = ConfigParser()
    config.read(args.ConfigFile)


    userName = config['DEFAULT']['username']
    password = config['DEFAULT']['password']
    siteName = config['sharepoint']['sitename']
    baseURL = config['sharepoint']['baseurl']
    siteURL = config['sharepoint']['siteurl']

    folderPath = config['fileinfo']['folderpath']
    fileExtention = config['fileinfo']['fileextention']
    indexExtention = config['fileinfo']['indexextention']
    sharePointFolder = config['sharepoint']['sharepointfolder']
    sharePointCustomeColumnList = ['Dealer Name', 'Date Signed']
    hasIndex = config['fileinfo'].getboolean('hasindex')

    sourceFolder = Path(folderPath)
    util = Util()
    indexing = Indexing()

    # returns True if there are files in the dealer_folder
    non_empty_dirs = bool({str(p.parent) for p in sourceFolder.rglob(f'*.{fileExtention}') if p.is_file()})
    if non_empty_dirs:
        #login into sharepoint site
        login = Auth(userName, password, siteURL, baseURL)
        #iterate  over files in the source folder
        files = [p for p in sourceFolder.iterdir() if p.is_file()]
        #if the source folder contains an index file
        if hasIndex:
            for file in files:
                # Find all files in folder
                match_file_name = file.match(f'*.{indexExtention}')
                if match_file_name:
                    indexRead = indexing.readIndex(file.name, folderPath)
                    
                    Upload(login.site, folderPath, indexRead[-1], sharePointFolder)

                    customeMetaDict = util.createDict(sharePointCustomeColumnList, indexRead[0:-1])

                    AddMeta(login.site, indexRead[-1], folderPath, sharePointFolder, customeMetaDict)
                else:
                    pass
        else:
            for file in files:
                # Find all files in folder
                match_file_name = file.match(f'*.{fileExtention}')
                if match_file_name:
                    upload = Upload(login.site, folderPath, file.name, sharePointFolder)

                    keywords = indexing.createKeywords(folderPath, file.name)

                    customeMetaDict = util.createDict(sharePointCustomeColumnList, keywords)

                    AddMeta(login.site, file.name, folderPath, sharePointFolder, customeMetaDict)
    else:
        print('Looks like the folder is equal to your heart')

if __name__ == '__main__':
    main()