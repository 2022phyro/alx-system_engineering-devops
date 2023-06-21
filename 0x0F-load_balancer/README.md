# LOAD BALANCER

Well when you have a successfull website, one with a lot of traffic, the ``load`` becomes too much to handle :grin: So we get two more servers to help us out. The problem is that we still have to connect these two servers together oyrwe may end up building two different websites under the same name :laughing:. In comes the **load balancer** The load balancer helps us to distribute our traffic across several servers perfectly. It make suse of different algorithms to do so like the  ``roundrobin`` probably the simplest, taking into factors like the speed of each server, the number of requests handled in real time, etc. Sometimes the extra may just be a failsafe device. ALX gave us two extra servers and one to serve as a load balancer. In this repo we install the load balancer on the server tagged ``lb-01``, We're using ``HAproxy``. We also edit our nginx configurations to include a custom header that'll tell us which server served us whetehr it wa ``web-01`` or ``web-02``

## Files :notebook:

|Files|Actions|Language|
|:---|:---|:---:|
|[0-custom_http_response_header](./0-custom_http_response_header)|This script installs and configures nginx to resemble the earlier modles _See older directories_ but adds a custom header ``X-Served-By`` that tells us which server answered our request|``Shell``|
|[1-install_load_balancer](./1-install_load_balancer)|This script installs ``haproxy``  on ``lb-01``and configures it to balance our web servers on ``web-01`` and ``web-02``|``Shell``|
|[2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp)|his manifest uses puppet to configure an nginx server to have a custom header same as the function of _0-custom_http_response_header_|``Puppet``|
