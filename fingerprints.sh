#!/bin/bash

$nginx_conf = $1"/nginx_conf"

echo 'map $ssl_client_fingerprint $reject {' >> $nginx_conf
echo "default 0;" >> $nginx_conf

for cert in $(/usr/bin/find $1 -path **/TLS/* -name TLS*.pem)
do
    fingerprint=$(openssl x509 -in "$cert" -noout -fingerprint -sha1 | sed 's/SHA1 Fingerprint=//; s/://g')
    echo "$fingerprint 1;" >> $nginx_conf
done

echo "}" >> $nginx_conf

