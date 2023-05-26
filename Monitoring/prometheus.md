# Prometheus

It is used to monitor highly containerized dynamic microservices (although it can also be used with bare-metal servers).  We may need to monitor the stats of our own application, sometimes:
- How many requests are inbound?
- How many exceptions are getting generated?
- How much resources are expended?


## Why?

When we are running highly distributed workloads over multiple servers, it becomes difficult to isolate the single point of failure since there are too many moving parts and one failure can kick off failures in other services. Debugging that wouldn't be easy in general because we need to work backwards to find the root issue. <br />
In any case, we have Prometheus to monitor all such services constantly, identifies the problems before they even occur and pushes alerts when certain thresholds are exceeded by these services.


## Architecture

At the heart of the setup lies the primary **Prometheus server**. It has:
- **Storage**: Time-servies database that stores metrics (instantaneous) such as CPU, exceptions, etc.
- **Retrieval**: Pulls metrics data and pushes to the database.
- **HTTP Server**: Accepts queries. Then relays the output information to some client like the browser or Grafana. <br />

Prometheus monitors any type of service - database, servers, applications, etc. All of these are called as **targets**. The metrics that get evaluated individually for a target are called as **units**: disk I/O, CPU, memory.

**Metrics** are made human-readable in simple text format. They are of two components: TYPE (exact event) & HELP (description).


## How Does Metric Collection Happen?

**Data Retrieval Worker** does that via pulling over HTTP endpoints that a target exposes at `address/metrics`. Some services may by default be able to give data in a correct format at `/metrics`. Others need an **Exporter**, responsible for fetching metrics from some target.


## Issues With Push Architecture fo Other Monitoring Tools

Tools like AWS Cloud Watch are also monitoring systems. However, they employ a push architecture. Every service on the network pushes their metrics periodically to the monitoring service. This creates a bottleneck at the point of monitoring and hence can be too overwhelming. This also requires daemons to be installed on the other systems. <br />
Prometheus scrapes and pulls. This also can alert it of the containe health.


## What About Services that Live for a Short Time?

Scheduling services, cleanup jobs, etc. run for a short duration before sleeping off. Under regular system, they would fail to be investigated by Prometheus. However, we use **Pushgateways** in this case. This basically lets those services push their metrics to Prometheus at the end of their job.


## How Are Alerts Managed?

**Alertmanager** is responsible for the triggers. It gets pushed to. Upon reception, it has a notification client configured, which it shall use to communicate the alert (email, Slack, etc.).


## Data Storage

Data is stored in the local disk in a custom time-series format. We cannot write that daat directly into an RDBMS.


## Querying Targets for Metrics

We can use PromQL to directly query the targets from the web UI. We can also use some better visualization tools like Grafana (which also uses PromQL under the hood).


## Cons

- It's architecture involving a time-series database is fairly difficult to scale when we are dealing with too many services.
- PromQL can have a steep learning curve.
- Due to low scalability, we need to let go of some its great features when it comes to design a large system.


## Pros

- Available for both Docker and k8s.
- Reliable. Does not die off even if others do.
- Independent on any service, because of which it can monitor all fairly.