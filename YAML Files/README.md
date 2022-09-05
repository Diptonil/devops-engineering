# YAML Files

Previously, it used to be called "Yet Another Markup Language". However, recent alterations and changes have completely changed it and now its name's fullform has become "YAML Ain't a Markup Language" (which is somewhat recursive in itself if considered without its historical pretext).<br />
They form an important part of DevOps in general and are epecially required when working with the Cloud.


## Few Pointers

- It is not a programming language (its a different type of language). It is a data format used as a medium of exchange.
- Similar to XML and JSON in some ways. It deals with data serialization.
- It is only concerned with storing configurational data and not commands.
- It is used to write up configuration for various things like Kubernetes clusters, pods, Docker compose files, etc. so as to define how they are supposed to work.
- It is a collection of one or more documents.


## Serialization

*Serialization* is the process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file. Its main purpose is to save the state of an object in order to be able to recreate it when needed. The reverse process is called *deserialization*.


## Why is YAML Not Markup?

The simple answer to this would be that YAML does a lot of what all other markup languages do: represent data. However, the only difference is that YAML does it simply without using any markup.<br />
More intricately, it defines only the representational tree structure without any definition of the underlying data that is encapsulated beneath that level. It is, more aptly, a *data serialization language*.


## Pros of YAML

- Simple and easily readable.
- Easily convertible to XML or JSON.
- Strict syntax that is unmistakable.
- Most languages use YAML.
- Most powerful when representing complex data.


## Features

- Case-sensitive.
- For indentations, spaces are enough. Never use tabs.
- Can represent key-value pairs, lists, etc.
- Like python, use '#' for comments.
- There is no definite file naming convention here. Use the convention that the surrounding dominant software is using. Kubernetes uses camelCase. Jenkins uses kebab-case. Circle-CI uses snake_case.
- Seperate documents using three dashes ('---'). A file may have no documents or as many as needed.
- To specify the end of a document, use three dots ('...').
- For block or key-value data representation, at times to avoid errors, we use the flow style if we have everything that can be represented within one line itself. However, this hardly ever is the case with real applications.


## To JSON

- There are online tools to convert YAML representation to JSON.
- The examples `block-yaml.yaml` and `block-json.json` show the respective forms of the same representation done by two different languages.


## Data Types

- Refer to the `data-types.yaml` file for preview.
- The strings can be represented in either single, double or no-quote format after the colon that is needed to declare a variable.
- For booleans there are multiple ways to represent true or false. Ex: N, No, False, false, Y, Yes, True, true, etc.
- All other data-types have been simply explored.
- We do not always need to provide the data type explicitly. YAML figures it out itself. However, in case we have to explicitly define a data-type, we can do that by applying exclamation points before the data-type.