#!/bin/bash

sudo yum -y update
sudo yum -y install httpd

PrivateIP=`curl http://169.254.169.254/latest/meta-data/local-ipv4`
echo "Web Server with Private IP: $PrivateIP" > /var/www/html/index.html

sudo systemctl restart httpd.service
