package {'nginx':
  ensure   => present,
  name     => nginx,
  provider => apt-get,
}
package {'nginx-extras':
  ensure   => present,
  name     => nginx,
  provider => apt-get,
}
file {'welcome page':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0600',
  content => 'Hello World!',
}
file {'Error page':
  ensure  => present,
  path    => '/var/www/html/error404.html',
  mode    => '0600',
  content => 'Ceci n\'est pas une page',
}
exec {'redirection':
  command => "sed -i '/# pass PHP scripts to FastCGI server/i \\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n' /etc/nginx/sites-enabled/default",
  path    => /usr/bin,
}
exec {'404_error page':
  command => "sed -i '/\tlocation \/redirect_me {/i \\terror_page 404 /error404.html;\n' /etc/nginx/sites-enabled/default",
  path    => /usr/bin,
}
