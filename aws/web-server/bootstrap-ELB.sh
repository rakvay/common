#!/bin/bash

sudo yum -y update
sudo yum -y install httpd

echo "<html><body bgcolor=gray><center><h1><p><font color=red>Web Server-2</h1></center></body></html>" > /var/www/html/index.html

sudo systemctl restart httpd.service
