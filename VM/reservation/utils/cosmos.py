import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
import azure.cosmos.errors as errors

import config as cfg


# Secret Useful bits
HOST = cfg.supersecret['uri']
PRIMARY_KEY = cfg.supersecret['pk']
DATABASE_ID = cfg.supersecret['db_name']
COLLECTION_ID = cfg.supersecret['cont_name']

database_link = 'dbs/' + DATABASE_ID
collection_link = database_link + '/colls/' + COLLECTION_ID
client = cosmos_client.CosmosClient(
    url_connection=HOST, auth={'masterKey': PRIMARY_KEY})

# Context Manager


class IDisposable(cosmos_client.CosmosClient):
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj  # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # Cleanup, cleanup, everybody do your share
        self.obj = None


class CollectionMgr:
    # Confirm Container exists
    @staticmethod
    def find_Container(client, id):
        print('1. Query Collection')

        collections = list(client.QueryContainers(
            database_link,
            {
                'query': 'SELECT * FROM r WHERE r.id=@id',
                'parameters': [
                    {'name': '@id', 'value': id}
                ]
            }
        ))

        if len(collections) > 0:
            print(f'Collection: {id} found')
        else:
            print(f'Collection: {id} NOT found')

    # Create Collection with default indexing
    @staticmethod
    def create_Container(client, id):
        try:
            client.CreateContainer(database_link, {'id': id})
            print(f'Collection: {id} created')

        except errors.HTTPFailure as e:
            if e.status_code == 409:
                print(f'A collection with id {id} exists')
            else:
                raise
    # Read Container

    @staticmethod
    def read_Container(client, id):
        print('\n Get Collection by id')
        try:
            collection_link = database_link + f'/colls/{id}'
            collection = client.ReadContainer(collection_link)
            print(
                f"Collection: {collection['id']} found, it's _self is {collection['_self']}")

        except errors.HTTPFailure as e:
            if e.status_code == 404:
                print(f'Collection: {id}, not a thing, try again')
            else:
                raise
    # See above error for why this is important

    @staticmethod
    def list_Containers(client):
        print('\n List all Colls in DB')

        print('Collections:')

        collections = list(client.ReadContainers(database_link))

        if not collections:
            return
        for collection in collections:
            print(collection['id'])
# Delete Container with id

    @staticmethod
    def delete_Container(client, id):
        print('Delete Collection')

        try:
            collection_link = database_link + f'/colls/{id}'
            client.DeleteContainer(collection_link)
            print(f"Collection: {id} deleted")
        except errors.HTTPFailure as e:
            if e.status_code == 404:
                print(f'Collection: {id}, not a thing, try again')
            else:
                raise


class DocumentMgr:
    @staticmethod
    def CreateDocs(client):
        print('\nCreating Documents\n')

    # client.CreateItem(collection_link, @TODO)

    @staticmethod
    def ReadOne(client, doc_id):
        print('\nReading document id\n')
        doc_link = collection_link + '/docs/' + doc_id
        response = client.ReadItem(doc_link)

        print(f'Document id:{doc_id}')
        print(f"Name: {response.get('given_name')} {response.get('last_name')}")
        print(f"{doc_id}, {response}")

    @staticmethod
    def ReadMany(client):
        print(f'Reading all documents in {COLLECTION_ID}')

        # maxItemCount is throttling db call to prevent 429 response
        documentlist = list(client.ReadItems(
            collection_link, {'maxItemCount': 10}))

        print(f'{len(documentlist)} Documents found')

        for doc in documentlist:
            print(f"Document id: {doc.get('id')}")
        return documentlist
