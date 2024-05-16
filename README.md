# My Demo

![](pics/demo_topology.png)

<br/>

I prepared this repo to demo to show how we can collect metrics from SRLINUX routers and generate charts at Grafana, after setting up the pipeline that leverages OpenTelemetry and Prometheus.

<br/>

I developed a simple script metric_manager.py that grabs packets_out counters from interfaces (ethernet-1/1 and ethernet-1/2) every 5 secs using gNMI. The script then pushes that metrics towards the OpenTelemetry Collector.

The metrics are stored in Prometheus after which will be polled by Grafana.

The Dashboard at Grafana is as:

<br/>

![](grafana_dashboard.png)






**Here are the steps for the demo**

### Deploy the test topology
> git clone https://github.com/muzafferkahraman/network_automation_demo <br>
> cd network_automation_demo <br>
> clab deploy -t lab_deploy.yml --reconfigure <br>

### Testing connectivity between the hosts
> docker exec -ti host10 ping 192.168.200.15 <br>
> docker exec -ti host20 ping 192.168.100.15 <br>

### Run the python code to push the missing static route configs
> python3 gnmi_push_config.py 



### Pre-requisite
You need to deploy containerlab, beforehands to run this lab

To install containerlab (CentOS 7)
> yum-config-manager --add-repo=https://yum.fury.io/netdevops/ && echo "gpgcheck=0" | 
> sudo tee -a /etc/yum.repos.d/yum.fury.io_netdevops_.repo <br>
> yum install containerlab

for other distros, please refer to 
https://containerlab.dev/install/



Prometheus: http://localhost:9090
Grafana: http://localhost:3000
OpenTelemetry Collector:
http://localhost:55679/debug/tracez
http://localhost:1777/debug/pprof/

