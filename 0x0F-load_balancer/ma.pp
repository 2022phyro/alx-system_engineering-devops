exec {'run':
  command  =>'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By $HOSTNAME;/" nnn',
  provider => shell,
}
