from elasticsearch import Elasticsearch
import os


def get_client():
    es_host_string = os.environ.get("ES_HOSTS", None)
    es_id = os.environ.get("ES_ID", None)
    es_apikey = os.environ.get("ES_APIKEY", None)
    if es_host_string is None:
        raise ValueError(
            "No environment variable called 'ES_HOSTS'. Unable to create an Elasticsearch client."
        )
    es_hosts = es_host_string.split(";")
    return Elasticsearch(
        es_hosts,
        api_key=(es_id, es_apikey)
    )