#!/bin/sh
sudo apt-get update
sudo apt-get install apache2 apache2-doc apache2-mpm-prefork apache2-utils libexpat1 ssl-cert  git -y

sudo git clone https://github.com/CETHER/OpenStack.git/my-web-pokedex/. /var/www/html/
