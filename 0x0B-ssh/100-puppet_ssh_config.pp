# Configures my client ssh configuration
exec {'Turn off passwd':
  path    => '/usr/bin/',
  command => 'echo "    PassswordAuthentication no" >> /etc/ssh/ssh_config',
  returns  => ['0', '1'],
}

exec {'Declare identity file':
  path    => '/usr/bin/',
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  returns  => ['0', '1'],
}
