# Rate Limiting

Rate limiting is a process used while designing networks to improve Quality of Service (QoS) of networks. While generation and transmission of data, a host tends to transmit data in an irregular manner which is termed as *bursty traffic* (combination of unexpected traffic peaks and depressions). Multiple hosts may transmit data in such a way over a network. This leads to unprecedented losses and congestion. This is to be avoided. To avoid this, we have many techniques. <br />
On a more technical level, *rate limiting refers to preventing the frequency of an operation from exceeding some constraint.* In large-scale systems, rate limiting is commonly used to protect underlying services and resources.


## Why Use Rate Limiting?

- **Prevent Resource Starvation**: Unregulated traffic might be disruptive to the functions of an API service. The reason for that might not always be malicious, at times there might even be a *friendly-fire DoS* (denial of service that is not malicious). The API beackend infrastructure often employs certain techniques to not let this happen.
- **Managing Policies or Quotas**: Considering a paid API service that exists and charges on the basis of request per minute or something like that, it is important to be able to calculate accurately and monitor the traffic so as to accordingly evaluate it. Quotas should not be exceeded as well. Rate limiting helps to limit any borderline instances.
- **Avoiding Excess Costs**: If a paid service is being used, limiting helps to use that service under a moderation so that a certain barrier may not be reached in terms of usage. This also helps reducing cost spikes.
- **Controlling Flow**: In large distributed systems, flow is a huge thing. It must be regulated across all services and machines, otherwhise backends might fail. To ensure a layer of failsafeness, flow control mechanisms are put in place.


## Rate Limiting Strategies

In the design of a complex architecture, we must keep in mind what we have to do to enforce rate limiting in our systems. All cases need to be considered where limiting can be done and the consequence of the implementation to fail.
- **No Rate Limiting**: This is the worst-case scenario and must always be considered in an architecture at the ground level. They need to be gracefully handled. Using timeouts, deadlines, and circuit-breaking patterns helps your service to be more robust in the absence of rate limiting.
- **Pass Through**: If your service calls other services to fulfill requests, you can choose how you pass any rate-limiting signals from those services back to the original caller. The simplest option is to only forward the rate-limiting response from the downstream service to the caller. An alternative is to enforce the rate limits on behalf of the downstream service and block the caller.
- **Enforce Limits**: Use the limiting techniques as given below (Leaky Bucket, Token Bucket, etc.). A strong understanding as to why the limit is being applied must be the done. When limits are reached, the service returns a limiting signal (usually a 429 HTTP response).
- **Client Strategies**: In response to rate-limiting, a client should generally retry the request after a delay. It is a best practice for this delay to increase exponentially after each failed request, which is referred to as exponential backoff. When many clients might be making schedule-based requests (such as fetching results every hour), additional random time (jitter) should be applied to the request timing, the backoff period, or both to ensure that these multiple client instances don't become periodic thundering herd, and themselves cause a form of DDoS.
- **Defer Responses**: If computing a response is expensive or time-consuming, a system might be unable to provide a prompt response to a request, which makes it harder for a service to handle high rates of requests. An alternative to rate limiting in these cases is to shunt requests into a queue and return some form of job ID. This allows the service to maintain higher availability, and it reduces the compute effort for clients that otherwise might be doing long blocking calls while waiting for a response.


## Leaky Bucket Algorithm

Analogous to how an irregular flow of water can be controlled by having a small hole at the bottom of a bucket, we have this algorithm for rate limiting. Run the `LeakyBucket.java` program to simulate a case with a custom example.
- The *leak rate* or *operation rate* is the number of packets that are allowed to be transferred in a given amount of time.
- The *bucket size* is the number of packets that are allowed to be held or considered at a given time. If the number of packets queues exceed this amount, the packets get dropped off. If the theoretical bucket is assumed to be a simple queue during implementation, the size is just the queue size.
- Assume we have the bucket size as 5, leak rate as 2 and at seconds 1, 2 and 3, we have packets sized as 5, 4 and 3 units being sent out by the host:
    - At second 1, we have arriving packet: 5, current bucket load: 5, sent packet size: 2 (leak rate is 2), 3 remaining packets & no discarded packets yet.
    - At second 2, we have arriving packet: 4, current bucket load: 3 from previous + 2 from incoming = 5, sent packet size: 2 (leak rate is 2), 3 remaining packets & 2 discarded packets since only 2 out of 4 incoming packets were considered in the bucket.
    - At second 3, we have arriving packet: 3, current bucket load: 3 from previous + 2 from incoming = 5, sent packet size: 2 (leak rate is 2), 3 remaining packets & 1 discarded packet since only 2 out of 3 incoming packets were considered in the bucket.
    - At second 4, we have no arriving packets, current bucket load: 3 from previous, sent packet size: 2 (leak rate is 2), 1 remaining packet & no discarded packets.
    - At second 5, we have no arriving packets, current bucket load: 1 from previous, sent packet size: 1 (leak rate is 2), no remaining packets & no discarded packets.


## Fixed Window Algorithm

This algorithms works for distributed systems by assigning a user authorized to access a particular source an ID, against which they keep a count check for a given time duration. The count goes up by one per request. If the count reaches a certain threshold, further requests are not entertained. Refer to `FixedWindow.java`. <br />
Assume an example case in which an user gets assigned an ID of 101. They get assigned a window of 1 hour: from 4 PM to 4:59 PM. They are allowed to make 30 requests within that hour at max. If they make more, their requests aren't entertained.