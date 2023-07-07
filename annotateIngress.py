from kubernetes import client, config
import sys
import os

ingress_namespace = os.environ.get("INGRESS_NAMESPACE")
ingress_selector=os.environ.get("INGRESS_SELECTOR")

api_instance = client.NetworkingV1Api()
ingress = api_instance.read_namespaced_ingress(namespace=ingress_namespace)
print(ingress)
