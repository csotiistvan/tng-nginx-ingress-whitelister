from kubernetes import client, config

config.load_incluster_config()

api_instance = client.CoreV1Api()
cmap = client.V1ConfigMap()

cmap.data["allowSnippetAnnotations"] = "false"
cmap.data["enableSnippetDirectives"] = "false"
cmap.data["http-snippet"] = "test"

api_instance.patch_namespaced_config_map(namespace="kube-system",name="addon-http-application-routing-nginx-configuration", body=cmap)
