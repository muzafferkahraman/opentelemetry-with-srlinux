# My Demo

![](pics/demo_topology.png)

<br/>

I prepared this demo to show how we can collect metrics from SRLINUX routers and generate charts at Grafana, after setting up the pipeline that leverages OpenTelemetry and Prometheus.

I developed a simple script metric_manager.py that grabs packets_out counters from interfaces (ethernet-1/1 and ethernet-1/2) every 5 secs using **gNMI**. 
The path where the metrics are stored can be discovered by the **YANG** model documentation of the SRLinux (https://yang.srlinux.dev/). The script then pushes that metrics towards the **OpenTelemetry Collector**.

The metrics are stored in Prometheus after which will be polled by Grafana.

Grafana Dashboard is as:

<br/>

![](pics/grafana_dashboard.png)


<br/>

**Here are the steps for the demo**

### Important Pre-requisites
Docker, Docker Compose and Containerlab must have been deployed.

Containerlab is a utility that provides a CLI for orchestrating and managing container-based networking labs. With presenting a topology file in yaml, one can easily build up the lab. Containerlab spins up routers and hosts as docker containers and creates the wiring  that interconnect them together.

You can find the installation steps for Containerlab at <br/>
https://containerlab.dev/install/

##Steps
<br>

> git clone https://github.com/muzafferkahraman/opentelemetry-with-srlinux <br>
> cd opentelemetry-with-srlinux <br>
> clab deploy -t  /topology-files/muzolab.yml --reconfigure <br>

At the end you should see

![](pics/clab_result.png)

> docker compose -f /topology-files/docker-compose.yml up

> docker exec -ti  clab-muzolab-host10 ping clab-muzolab-host20





### Accessing to Grafana

Grafana: http://localhost:3000

