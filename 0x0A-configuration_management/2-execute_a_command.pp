#This puppet manifest kills a process named killmenow
exec { 'killmenow':
  command => '/bin/pkill -15 killmenow',
}
