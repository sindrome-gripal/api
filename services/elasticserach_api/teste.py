# from elasticsearch import Elasticsearch
# from ipdb import set_trace


# ELASTIC_PWD = "Za4qNXdyQNSa9YaA"
# ELASTIC_USER = "user-public-notificacoes"


# # Found in the 'Manage Deployment' page
# CLOUD_ID = "Bl_bPjCNSQGexVuot8nokg"

# ada = [{
#     'host': 'elasticsearch-saps.saude.gov.br', 
#     'port': 443, 
#     'use_ssl': True, 
#     'scheme': 'http', 
#     'http_auth': 'user-public-notificacoes:Za4qNXdyQNSa9YaA'
# }]
# HOST = 'https://' + ELASTIC_USER + ':' + ELASTIC_PWD + '@elasticsearch-saps.saude.gov.br:443'

# index = 'user-public-notificacoes:Za4qNXdyQNSa9YaA'
# # Create the client instance
# client = Elasticsearch(
#     hosts=[HOST],
#     basic_auth=(ELASTIC_USER, ELASTIC_PWD)
# )

# set_trace()

# # Successful response!
# client.info()


# '''
# body={"query": {"match_all": {}}}


# '{\n 
#     "name" : "elasticsearch-master-0",\n  
#     "cluster_name" : "elasticsearch",\n  
#     "cluster_uuid" : "Bl_bPjCNSQGexVuot8nokg",\n  
#     "version" : {\n    
#         "number" : "7.16.2",\n    
#         "build_flavor" : "default",\n    
#         "build_type" : "docker",\n    
#         "build_hash" : "2b937c44140b6559905130a8650c64dbd0879cfb",\n    
#         "build_date" : "2021-12-18T19:42:46.604893745Z",\n   
#         "build_snapshot" : false,\n    
#         "lucene_version" : "8.10.1",\n    
#         "minimum_wire_compatibility_version" : "6.8.0",\n   
#         "minimum_index_compatibility_version" : "6.0.0-beta1"\n  
#     },\n  
#     "tagline" : "You Know, for Search"\n}\n'
# '''