from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3
import json

def get_opensearch_client(host, region):
    """
    Initialize the OpenSearch client with AWS V4 signing.
    
    Parameters:
        host (str): The cluster endpoint.
        region (str): The AWS region.
    
    Returns:
        OpenSearch: An OpenSearch client object.
    """
    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, region)

    client = OpenSearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    return client

def create_index(client, index_name, index_body):
    """
    Create an index with specified settings.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index to be created.
        index_body (dict): Body of the index settings.
    
    Returns:
        dict: Response from the create index request.
    """
    response = client.indices.create(index=index_name, body=index_body)
    print('\nCreating index:')
    print(response)
    return response

def add_document(client, index_name, document, doc_id):
    """
    Add a document to the specified index.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index where the document will be added.
        document (dict): The document to be added.
        doc_id (str): ID of the document.
    
    Returns:
        dict: Response from the add document request.
    """
    response = client.index(index=index_name, body=document, id=doc_id, refresh=True)
    print('\nAdding document:')
    print(response)
    return response

def search_index(client, index_name, query):
    """
    Search for documents in the specified index.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index to search.
        query (dict): Search query.
    
    Returns:
        dict: Response from the search request.
    """
    response = client.search(body=query, index=index_name)
    print('\nSearch results:')
    print(response)
    return response

def delete_document(client, index_name, doc_id):
    """
    Delete a document from the specified index.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index from which the document will be deleted.
        doc_id (str): ID of the document to be deleted.
    
    Returns:
        dict: Response from the delete document request.
    """
    response = client.delete(index=index_name, id=doc_id)
    print('\nDeleting document:')
    print(response)
    return response

def delete_index(client, index_name):
    """
    Delete the specified index.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index to be deleted.
    
    Returns:
        dict: Response from the delete index request.
    """
    response = client.indices.delete(index=index_name)
    print('\nDeleting index:')
    print(response)
    return response

def upload_json(client, index_name, file_path):
    """
    Upload a JSON file to the specified index in bulk.
    
    Parameters:
        client (OpenSearch): An OpenSearch client object.
        index_name (str): Name of the index to upload the JSON data.
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Response from the bulk upload request.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    
    response = client.bulk(body=data, index=index_name, refresh=True)
    print('\nBulk upload response:')
    print(response)
    return response

if __name__ == "__main__":
    # Define the host and region
    host = 'search-demo-opensearch-hdla32lwzinmlgpiwrsudigknm.us-east-1.es.amazonaws.com'
    region = 'us-east-1'

    # Initialize the OpenSearch client
    client = get_opensearch_client(host, region)

    # Define the index name and search query
    index_name = 'movies'
    q = 'tim'
    query = {
        'size': 5,
        'query': {
            'multi_match': {
                'query': q,
                'fields': ['title^2', 'director']
            }
        }
    }

    # Search the index
    search_index(client, index_name, query)

    # Define the new index name and settings
    new_index_name = 'test'
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1
            }
        }
    }
    
    # Create the new index
    create_index(client, new_index_name, index_body)

    # Define the document to be added
    document = {
        'title': 'Moneyball',
        'director': 'Bennett Miller',
        'year': '2011'
    }
    doc_id = '1'

    # Add the document to the index
    add_document(client, new_index_name, document, doc_id)
    print("="*20)
    # Search the index for the newly added document
    search_index(client, new_index_name, query)
    print("="*20)
    # Delete the document from the index
    delete_document(client, new_index_name, doc_id)
    print("="*20)
    # Delete the index
    delete_index(client, new_index_name)
    print("="*20)
    # # Define the file path to the JSON file for bulk upload
    file_path = 'bulk_movies.json'

    # Upload the JSON file to the index
    upload_json(client, new_index_name, file_path)
