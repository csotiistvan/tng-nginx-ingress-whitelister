# Introduction

The usage of client certificates together with nginx ingress controllers is always a long trip to study the documentation and find out what needs to be set. Multiple annotation must be set to enable it, and some more magic must be added to make it secure by certificate pinning. This tool shall do it out of the box:) 

# Features

- [x] Creating a CA Bundle from an predefined Folder
- [x] Creating a Fingerprint List for Certificate Pinning
- [x] Enable automatically Certificate Pinning
- [x] Enable automatically Client Authentication by using Custom CA Bundle
- [x] Update it by sheduled Job

# Usage

Clone the Repository Tag v1 and install the chart by using:

```
helm install  --values val.yaml whitelisting ./k8s
```

The val.yaml is a values file where you can override the default values e.g. : 

```
config:
 tag: v1
bundle:
 repo: https://github.com/{CHANGEME}/{CHANGEME}.git
ingress:
 name: myIngress
job:
 shedule: {yourShedule} # Unix Cron Format
```
More about the Cron Format can you find [here](https://en.wikipedia.org/wiki/Cron)  
