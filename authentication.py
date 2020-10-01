from shareplum import Site, Office365
from shareplum.site import Version


# create new class for login into sharepoint
class Auth:
    # initeate the varuables
    def __init__(self, username, password, siteURL, baseURL):
        self.username = username #username to include user@domain.com
        self.password = password #password for the user
        self.siteURL = siteURL #this is the url for the SharePoint site where the document library is located that you will be uploading to
        self.baseURL = baseURL #this is the url for you SharePoint, i.e. domain.sharepoint.com
        self.setUp()
    # build the sign dict
    def setUp(self):
        config = {
            'username': self.username,
            'password': self.password,
            'siteURL': self.siteURL,
            'baseURL': self.baseURL
        } 
        self.signIn(config)

    #Build the signin and execute the signin     
    def signIn(self, config):
        authcookie = Office365(config['baseURL'], username=config['username'], password=config['password']).GetCookies()
        self.site = Site(config['siteURL'],version=Version.v365,authcookie=authcookie)
        return self.site