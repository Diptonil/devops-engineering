# Percentile Tail Latency

It is a metric that we use to measure the latency that we have in our backend. Unlike faulty metrics such as milliseconds needed for the processing of a query, this is a robust standard that is gaining fast ground.


## Why Percentile?

We assume that we automate a million requests to our backend at any given time and then claim that the minimum latency of the backend is 1 ms. This does not mean a thing because:
- Many other requests could have taken more time.
- We are not sure how evenly distributed and varied the request automation is. <br />
We could even say that the maximum latency is 300ms in the backend, which is wrong as well because:
- It might be that all others take 299ms and one takes 300ms. It is not a fair delivery.
- It might also be that all others take 2ms while there is only one elusive case in which we get a 300ms latency. That is again, quite unfair. <br />
Averages are also not a proper metric because all requests would be within 2ms except some occasional ones that take up to a minute or so, ruining the math.


## What is Percentile?

When we say that the *tail latency* or the *high-percentile latency*, we are talking about the percentage of requests of the total ones made that take up a certain specified time. For example:
- A "95 percentile tail latency of 10ms" means that 95% of the requests being made are all within 10ms.
- A "99% tail latency of 11ms" means that 99% of the requests being made are all within 11ms.


## Impact

- Obviously, to make such metrics work, we need to have multiple requests, not just 10s or 50s, preferrably thousands of requests. People like to show off by quoting their values of "99.9999 percentile tail latency" to show how large their samples are.
- An important thing to remember when surveying percentiles is that sometimes, the backend might service all requests almost within 10ms (which is assumed to be a fancy metric) and not less. The promoter might say that their 99 percentile is 10ms, which might seem fancy. The question that should be asked then is about the 95 percentile. If the numbers are the same and they didn't go down, something is fishy. That shows that the backend takes more time to process smaller requests as well, not just larger ones.
- A good report must have a percentile latency of both 95 and 99.