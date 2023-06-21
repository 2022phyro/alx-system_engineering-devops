# SSH

SSH stands for Secure Shell and is a network communications protocol, it is a set of rules for sending information across two  or more computers. One can send files to and fro each computer, hypertext, images, videos, manifests etc. In this repository we will learn how to iuse SSH and perform actions across a remote system. We will see how to connecto to my first server :joy: create a private, public key pair for secure connection and automate the whole stuff using puppet

## Files :scroll:

The following files are present
|Files|Actions|Language|
|:---|:---|:---|
|[0-use_a_private_key](./0-use_a_private_key)|Thiscript allows us to connect to my server using my privake key file| ``Shell``|
|[1-create_ssh_key_pair](./1-create_ssh_key_pair)|This script creates an ``rsa`` ssh key pair using  ``ssh-keygen`` utility with a passphrase ``betty``|``Shell``|
|[2-ssh_config](./2-ssh_config)|This file is the configuration file for my system tweaked so that I don't have to authenticate everytime I need to connect to my server|``text file``|
|[100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp)|This puppet manifest automates the process of configuring my ssh so that I don't have to always authenticate|``Puppet``|
