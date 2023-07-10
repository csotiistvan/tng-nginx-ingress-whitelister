# Introduction

The usage of client certificates together with nginx ingress controllers is always a long trip to study the documentation and find out what needs to be set. Multiple annotation must be set to enable it, and some more magic must be added to make it secure by certificate pinning. This tool shall do it out of the box:) 

# Features

[x] Creating a CA Bundle from an predefined Folder
[x] Creating a Fingerprint List for Certificate Pinning
[x] Enable automatically Certificate Pinning
[x] Enable automatically Client Authentication by using Custom CA Bundle
[x] Update it by sheduled Job
