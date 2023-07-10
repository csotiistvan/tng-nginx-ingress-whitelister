import os
import glob
import base64
from kubernetes import client, config

config.load_incluster_config()

bundle_namespace = os.environ.get("BUNDLE_NAMESPACE")
bundle_name=os.environ.get("BUNDLE_NAME")

api_instance = client.CoreV1Api()
api_instance.delete_namespaced_secret(namespace=bundle_namespace,name=bundle_name)
