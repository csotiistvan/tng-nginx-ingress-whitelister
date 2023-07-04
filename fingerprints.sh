#!/bin/bash

nginx_conf="./nginx/proxy.conf"

# Durchlaufe alle .pem-Dateien im Verzeichnis
for cert in $(/usr/bin/find ../. -path **/TLS/* -name TLS*.pem)
do
    fingerprint=$(openssl x509 -in "$cert" -noout -fingerprint -sha1 | sed 's/SHA1 Fingerprint=//; s/://g')
    echo "$fingerprint 1;" >> $nginx_conf
done

echo "}" >> $nginx_conf

cat ./nginx/proxy.conf
