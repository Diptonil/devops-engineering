# Logging and Monitoring

Logging and Monitoring are integral in learning about the health and status of an already deployed app. These two tools are important in delivering us the data as to what is happening behind the scenes of the application in GCP. <br />
It is highly recommended to explore the whole section of Logging and Monitoring within GCP itself to gain a better insight as to nuances of the whole system, leveraging the features of *Error Reporting*, *Tracing*, *Debugging*, *Log Streaming*, *Profiling*, *Alerting*, *Metrics*, etc.


## Monitoring

- Monitoring is the process of keeping a check on the usage of physical resources by an application running on the Cloud architecture as well as a close inspection on the performance and overall health of the app.<br />
In the *Site Reliability Engineering* book at Google, monitoring is defined as "collecting, processing, aggregating and displaying real-time data about a system such as query & error counts, processing times, server lifetimes, etc".
- The *Cloud Monitoring* service has continuous improvements from the data gathered to prevent incidents (events of potential failures), provides dashboards stating metrics with respect to the physical resource utilisation, automated alerts if any event (that we can customise as well) occurs and provides various monitoring tools to actually manage the app with reference to all the collected data.


## Four Golden Signals

There are four golden signals measuring the system's performance and reliability. They are:
- **Latency**: Measures how long it takes a particular part of a system to return a result. Sample latency metrics include page load latency, number of requests waiting for a thread, query duration, service response time, transaction duration, time to first response, and time to complete data return. It matters because:
    - It affects user experience.
    - Increased latency means emerging issues.
    - It may be directly tied to capacity demands.
    - Used to measure system improvements.
- **Traffic**: Measures how many requests reach our system. Sample traffic metrics include the number of HTTP requests per second, number of requests for static versus dynamic content, network IO, number of concurrent sessions, number of transactions per second, number of retrievals per second, number of active requests, number of write operations, number of read operations, and number of active connections. It is important because:
    - Core measure when infrastructure speed is calculated.
    - Historical trends are used for future plans.
    - Indicator of current system demand.
- **Saturation**: Measures how close to capacity a system is. Sample capacity metrics include the percent memory utilization, percent thread pool utilization, percent cache utilization, percent disk utilization, percent CPU utilization, disk quota, memory quota, number of available connections, and number of users on the system. It is important because it indicates how full the service is.
- **Errors**: Events that measure system failures or other issues. Errors are often raised when a flaw, failure or faults in a computer program or system causes it to produce incorrect or unexpected results or behave in unintended ways. Errors are often raised when a flaw, failure or faults in a computer program or system causes it to produce incorrect or unexpected results or behave in unintended ways. Errors are important because they may indicate that something is failing, they may indicate configuration or capacity issues. They can indicate service level objective violations, and an era might mean it's time to send out an alert. Sample error metrics include wrong answers or incorrect content, the number of 400 and 500 HTTP codes, the number of failed requests, the number of exceptions, the number of stack traces, servers that fail liveness checks, and the number of dropped connections. They are important because:
    - They can indicate service level objective violations and might mean it's time to send out an alert.
    - Indicates configuration or capacity issues


## Types of Logs

- **Cloud Audit Logs**: Keeps track of Admin activity, tells us what was done in which service as well as system events.
- **Agent Logs**: They run on Fluentd agents and can ingest logs of AWS EC2 instances, Compute Engines, etc.
- **Network Logs**: VPC flows, firewalls, NAT gateways, network security, etc.
- **Service Logs**: Standard I/O logs of the GCP services.


## Cloud Debugger

The error-state of a console can be captured and made into a shareable URL that can be helpful in the debugging sessions with other team members. It also can integrate pretty easily with the existing developer workflows and versioning systems.


## Cloud Trace

An automated error and malfunction analysis tool that provides near-realtime analysis to generate in-depth reports on latencies and flaws. Traces from most Cloud services are considered. <br />
It is used for latency data, which is important to remember.