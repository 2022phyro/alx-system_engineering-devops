#This manifest configures an nginx server
exec {'update':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx',
  provider => shell,
}
exec {'welcome page':
  command   => 'echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  provider => shell,
}
exec {'redirection':
  command => 'sudo sed -i "s/server_name _;/server_name;\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com;\n\t}/g" /etc/nginx/sites-enabled/default',
  provider => shell,
}
exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}

