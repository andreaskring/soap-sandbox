from zeep import Client


client = Client('http://alfresco.example.org/alfresco/cmisws/cmis?wsdl')

factory = client.type_factory('ns1')

sp = client.bind('NavigationService', 'NavigationServicePort')

