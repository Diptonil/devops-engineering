# Apache Kafka

- It is a distributed stream processing system written in Scala and Java.
- It is a basic system in which a *producer* would produce some content and push it over to the *broker*, from which the *consumer* would consume the content.
- Kafka is, in many ways, both a message queue and a pub sub.


## Components

- **Broker or Server**
    - Basically a server that the clients interact with.
    - Has a default port at 9092
    - It is bi-directionally connected to the *producer*. Both can exchange information in two ways.
    - A TCP connection is established for both *producer* and *consumer*.

- **Topics**
    - A logical partitioning of the data that gets pushed into the broker.
    - Whenever data is pushed by the producer, it is pushed to a topic.
    - A consumer may subscribe to a topic that resides in a broker. Data that gets pushed to that topic can reach the consumer.
    - It is somewhat like a queue. Producers and consumers are the ones who are pushing and polling information respectively. However, data entering a topic never gets deleted, no matter how many times it uis polled. It is a principle.
    - Here in this data structure, we *only use indexes*. We don't use methods like start from here and go till there.

- **Partition**
    - Everything relating to data becomes slow the larger it becomes. Hence, we must split up things to reduce latency in queries.
    - Partitioning in Kafka essentially works the same way as database sharding.
    - Based on some logical segregation, each topic is split into different partitions. Data would correspondingly go into the topics.
    - A partition can serve only one consumer at a given time. But the vice versa case need not be true.

- **Producers**
    - It makes a request to the broker to publish data to a topic. The request goes as the *data* to publish as well as the *topic* to publish to.
    - There is a little bit of overhead if a topic has partitions since the partition to write to is also to be known.

- **Consumers**
    - It makes a request to the broker as to obtain data for a given topic. This is called polling of data.
    - There is a little bit of overhead if a topic has partitions since the partition to read from is also to be known.
    - A consumer can consume as many partitions it wants to at a given time. But the vice versa case is not possible.

- **Consumer Groups**
    - This is the concept in Kafka that makes it behave as both a message queue and a pub sub.
    - They were invented to do parallel processing of partitions. This removes the need for the consuer to know which partition to refer to.
    - It acts like a proper queue with the exact behavior. If a consumer in a consumer group reads a partition in a topic, the data gets updated to fetch the next position in teh queue. That is the default behaviour. This is how the message queue system is implemented.
    - So, if we want our system to act like a message queue, we put all consumers in a comsumer group. 
    - If we want our consumer to act like a pub sub, we put all consumers in a unique group.
    - The whole architecture allows us to have parallel processing for free.