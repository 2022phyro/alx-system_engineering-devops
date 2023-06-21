# Web Server

What's a web server? In my own understanding a web server answers requests for clients. Bu's it's much more than that. A web server serves or send http responses to http requests. In this repo I will install and configure an ``Nginx`` web server to suit my requirements.

## Files :notebook:

Below in a tabular format is the available files in this directory and its basic functions
|Files|Actions|Language|
|:---|:---|:---|
|[0-transfer_file](./0-transfer_file)| In this file I will use the the ``scp`` utility which makes use of ssh to transferfiles over a network between two systems| ``Shell``
|[1-install_nginx_web_server](./1-install_nginx_web_server)|This script installs an nginx server and then changes the default welcome page from the bunchy html to a simple normal _Hello World!_|``Shell``|
|[2-setup_a_domain_name](./2-setup_a_domain_name)|**.TECH Domain** was so kind to give us a free domain name for a year. So i went and set up mine. THis file simply contains my domain name _phyro.tech_|``text file``|
|[3-redirection](./3-redirection)|This script will install nginx, change the contents of its default page to _Hello World!_ and also give a redirect to my github address :laughing: at the location /redirect_me|``Shell``|
|[4-not_found_page_404](./4-not_found_page_404)| THis builds on the ``3-redirection`` file but then customises my error page to return French|``Shell``|
|[7-puppet_install_nginx_web_server.pp](./7-puppet_install_nginx_web_server.pp)|This puppet manifest install nginx on on a server|``Puppet``|
