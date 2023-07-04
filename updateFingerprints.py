from kubernetes import client, config

cmap.metadata = client.V1ObjectMeta(name="test-config")
cmap.data = {}
cmap.data["http-snippet"] = "test"

api_instance.create_namespaced_config_map(namespace="kube-system", body=cmap)
