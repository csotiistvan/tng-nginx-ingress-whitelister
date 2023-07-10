from kubernetes import client, config
import sys
import os

config.load_incluster_config()

config_namespace = os.environ.get("CONFIG_NAMESPACE")
config_name=os.environ.get("CONFIG_MAP")
config_seperator=os.environ.get("SEPERATOR")

if not config_namespace or not config_name:
    print("Config Namespace or Config Map not configured")
else: 
    api_instance = client.CoreV1Api()
    cmap = api_instance.read_namespaced_config_map(name=config_name, namespace=config_namespace)
    seperator = config_seperator
    if "http-snippet" in cmap.data:
        existingconfig = cmap.data["http-snippet"]
        map = existingconfig.split(seperator)
        if len(map) == 3:
          cmap.data["http-snippet"] = map[0].strip() + map[2].strip()

        httpSnippet = cmap.data["http-snippet"].strip()

        if httpSnippet == "":
            del cmap.data["http-snippet"]
     
    api_instance.replace_namespaced_config_map(namespace=config_namespace,name=config_name, body=cmap)
