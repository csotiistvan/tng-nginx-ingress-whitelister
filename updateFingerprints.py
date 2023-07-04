from kubernetes import client, config
import sys

config.load_incluster_config()

with open(sys.argv[1]) as f:
    data = f.read()

api_instance = client.CoreV1Api()
cmap = client.V1ConfigMap()
cmap.data = {}
cmap.data["http-snippet"] = data

api_instance.patch_namespaced_config_map(namespace="kube-system",name="addon-http-application-routing-nginx-configuration", body=cmap)
