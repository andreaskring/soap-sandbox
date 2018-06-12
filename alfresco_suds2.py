from suds.client import Client

client = Client('http://alfresco.example.org/alfresco/cmisws/cmis?wsdl')
# client = Client('http://alfresco.example.org/alfresco/cmisws/RepositoryService')

# cmt = client.factory.create('ns16:enumUsers')

r = client.service[6].getRepositories()
