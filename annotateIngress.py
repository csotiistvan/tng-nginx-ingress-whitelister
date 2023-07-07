from kubernetes import client, config
import sys
import os

ingress_namespace = os.environ.get("INGRESS_NAMESPACE")
ingress_name=os.environ.get("INGRESS_NAME")

api_instance = client.NetworkingV1Api()
ingress = api_instance.read_namespaced_ingress(name=ingress_name,namespace=ingress_namespace)
print(ingress)
