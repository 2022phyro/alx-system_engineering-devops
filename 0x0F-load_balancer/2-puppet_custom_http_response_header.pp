# This puppet file configures an ubuntu server with a custom header
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Package['nginx'],
}

package{'nginx':
  provider => apt,
  name     => 'nginx',
  before   => Exec['install myserver'],
}
exec {'custom header':
  provider => shell,
  command  => 'sudo sed -i "/include \/etc\/nginx\/sites-enabled\/\*;/a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
  before   => Exec['restart'],
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
