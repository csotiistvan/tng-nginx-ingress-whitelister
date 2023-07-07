from kubernetes import client, config
import sys
import os

config.load_incluster_config()

ingress_namespace = os.environ.get("INGRESS_NAMESPACE")
ingress_name=os.environ.get("INGRESS_NAME")
bundle_namespace = os.environ.get("BUNDLE_NAMESPACE")
bundle_name =  os.environ.get("BUNDLE_NAME")

api_instance = client.NetworkingV1Api()
ingress = api_instance.read_namespaced_ingress(name=ingress_name,namespace=ingress_namespace)

if ingress:
   ingress.metadata.annotations["nginx.ingress.kubernetes.io/server-snippet"] = "if ($reject) { return 403; }"
   ingress.metadata.annotations["nginx.ingress.kubernetes.io/auth-tls-secret"] = bundle_namespace + "/" + bundle_name
   ingress.metadata.annotations["nginx.ingress.kubernetes.io/auth-tls-verify-client"] = "on"
   api_instance.patch_namespaced_ingress(name=ingress_name,namespace=ingress_namespace, body=ingress)
else: 
   print("Ingress Rule is not existing in the namespace")
