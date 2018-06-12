import requests
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

REPO_ID = 'b1f744ae-34c2-4ad3-b73d-c1f8ab5a8e2a'
ROOT_FOLDER_ID = 'workspace://SpacesStore/90e3ee82-c8dd-4eb6-8894-9802c24690e9'

session = requests.Session()
session.auth = HTTPBasicAuth('admin', 'admin')

client = Client(
    'http://alfresco.example.org/alfresco/cmisws/cmis?wsdl',
    transport=Transport(session=session)
)

factory = client.type_factory('ns2')

nav = client.bind('NavigationService', 'NavigationServicePort')
repo = client.bind('RepositoryService', 'RepositoryServicePort')

r = nav.getChildren(REPO_ID, ROOT_FOLDER_ID)
