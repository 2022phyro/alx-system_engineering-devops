# Configures my client ssh configuration
exec {'Turn off passwd':
  path    => '/usr/bin/',
  command => 'echo "    PassswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  returns => ['0', '1'],
}
