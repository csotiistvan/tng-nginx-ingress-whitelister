import os
import glob
import base64
from kubernetes import client, config

config.load_incluster_config()

bundle_namespace = os.environ.get("BUNDLE_NAMESPACE")
bundle_name=os.environ.get("BUNDLE_NAME")

folder = os.environ.get("CERTIFICATEFOLDER")
print(folder)
files = glob.glob(folder+"/**/TLS/CA*.pem", recursive=True)
print(files)

ca_bundle = ""
for file in files:
  with open(file) as f:
    data = f.read()
  ca_bundle = ca_bundle+"\n"+data
  
print(ca_bundle)
 
if len(files) and ca_bundle:
  api_instance = client.CoreV1Api()
  body = client.V1Secret()
  body.api_version = 'v1'
  body.data = {'ca.crt': base64.b64encode(ca_bundle)}
  body.kind = 'Secret'
  body.type = 'Opaque'
  api_instance.patch_namespaced_secret(namespace=bundle_namespace,name=bundle_name, body=body)
    
