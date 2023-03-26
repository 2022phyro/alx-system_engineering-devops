# Configures my client ssh configuration
exec {"main":
	path "/usr/bin/env; /bin"
	command 'echo "    PassswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
	return [0,1]
}
