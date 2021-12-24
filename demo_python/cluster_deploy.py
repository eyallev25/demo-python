import requests
import json
from elasticsearch import Elasticsearch
from kobura.elasticsearch.es_handler import ElasticsearchHandler

# es = Elasticsearch([{"host": "localhost", "port": 9200}])
# es.index(
#     index="access_e2etenant",
#     id="3daa2ecf-58d7-49b2-b03f-6a8ceae155bd",
#     body={
#         "cluster_id": "cluster-29c6ae",
#         "owner_uid": 243095136,
#         "container_uid": 3000000001,
#         "asset_uid": 1000000000000000003,
#         "access": "not_blocked",
#         "process_name": "a3ViZS1wcm94eQ==",
#         "timestamp": "2021-12-23T11:59:24.215668",
#         "count": 1,
#         "record_type": "INODE_ACCESS",
#         "batch_id": "17dee7e1-762a-449c-b551-6e88b6ae2739",
#         "container": {
#             "name": "kube-proxy",
#             "image": "602401143452.dkr.ecr.us-west-2.amazonaws.com/eks/kube-proxy:v1.18.8-eksbuild.1",
#         },
#         "owner": {
#             "name": "kube-proxy",
#             "namespace": "kube-system",
#             "kind": "DaemonSet",
#         },
#         "asset": {
#             "type": "S_IFREG",
#             "asset_type": "volume",
#             "asset_name": "lib-modules",
#             "sub_type": "kubernetes.io/host-path",
#             "extra_data": None,
#         },
#         "is_directory": False,
#         "requested_access_mask": "MAY_EXEC|MAY_NOT_BLOCK",
#         "decoded_process_name": "kube-proxy",
#         "source_key": "/e2etenant/2021/12/23/11/con-data-access-stream-11-2021-12-23-11-59-26-d2b075d0-ffce-34c2-bf20-ce889b6bbe12",
#         "group_hash": "a40f0cbfb3c3f156d9b6d63c6d7da361d05d232de6fc592899c429a75cbe9f58",
#     },
# )
# r = requests.get(
#     "http://localhost:9200/access_e2etenant/_doc/3daa2ecf-58d7-49b2-b03f-6a8ceae155bd"
# )

# elastic_client: Elasticsearch = ElasticsearchHandler.initialize_handler().client()
# resp = elastic_client.search(index="access_e2etenant", query={"match_all": {}})
# for hit in resp["hits"]["hits"]:
#     print(hit["_source"])


# print(r.status_code)
# print(json.loads(r.content))


class ClusterDeploy:
    def show():
        print("ClusterDeploy")
