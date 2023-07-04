from kubernetes import client, config
import sys
import os

config.load_incluster_config()

with open(sys.argv[1]) as f:
    data = f.read()

api_instance = client.CoreV1Api()
cmap = client.V1ConfigMap()
cmap.data = {}
cmap.data["http-snippet"] = data

api_instance.patch_namespaced_config_map(namespace=os.environ.get("CONFIGMAPNAMESPACE"),name=os.environ.get("CONFIGMAPNAME"), body=cmap)
