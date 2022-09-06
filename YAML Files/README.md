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
- For indentations, the suggested number of spaces is 2. In most code editors, the Tab-space would correspond to that number. However, 2 is not a bound, albeit a followed standardization. Individuals can choose their own norm.
- Can represent key-value pairs, lists, etc.
- Like python, use '#' for comments.
- There is no definite file naming convention here. Use the convention that the surrounding dominant software is using. Kubernetes uses camelCase. Jenkins uses kebab-case. Circle-CI uses snake_case.
- Seperate documents using three dashes ('---'). A file may have no documents or as many as needed.
- To specify the end of a document, use three dots ('...').
- For block or key-value data representation, at times to avoid errors, we use the flow style if we have everything that can be represented within one line itself. However, this hardly ever is the case with real applications.
- See `structure.yaml` to get a sense of how a long text can be safely broken down for ease of reading.


## To JSON

- There are online tools to convert YAML representation to JSON.
- The examples `block-yaml.yaml` and `block-json.json` show the respective forms of the same representation done by two different languages.


## Data Types

- Refer to the `data-types.yaml` file for complete understanding.
- The strings can be represented in either single, double or no-quote format after the colon that is needed to declare a variable.
- For booleans there are multiple ways to represent true or false. Ex: N, No, False, false, Y, Yes, True, true, etc.
- All other data-types have been simply explored.
- We do not always need to provide the data type explicitly. YAML figures it out itself. However, in case we have to explicitly define a data-type, we can do that by applying exclamation points before the data-type. This is not always seen in most YAML files.
- Sets only allow unique values.
- Pairs allow two different values under the same flag.


## Anchors

- At times a defined property might need to be reused in multiple instances. Copy pasting does it, but leads to code redundancy.
- Anchors are like labels that can be used as a substitute for the redundant code.
- In `anchors.yaml`, all the defined persons share certain common likings. We use anchors to represent that.
- The `&label` declares that a particular block is about to be labelled to anchoring. The `label` can leter be used to make a call to that block for reusability.
- The `<<: *label` is the placeholder for the call to the main thing.
- Overriding properties may be done right after the placeholder as seen in case of `person3`.


## Serialized Data Representation

- Data stored or represented in XML is extremely easy to read and understand. It shows the basic heirarchies and parent-children relationships of elements to be stored. A sample scenario is realized in the file `data.xml` that deals with modelling a school.
- JSON is the most famous serialization formats out there and is widely used all over the web. The same scenario is realised in `data.json` as well.
- The same has been done for YAML as well in `data.yaml`.
- The key point to note is that we must know the syntax of all 3 formats but we don't need to know to exactly write them. There are tools for easy conversion to and from any of these 3. We should make use of them to save time. 


## Tools

- Websites like `https://www.json2yaml.com/` and such help in conversions with respect to the three serialization formats.
- `Datree` is a Cloud tool that has a bunch of functionalities. It's primary purpose is to look for Kubernetes misconfigurations. It is a very important DevOps tool that would be explored later in this repository. One of it's functionalities if checking if YAML files are proper (with respect to syntax, etc.).
- `Monocle` by Kubeshop is a tool that lets us easily make our Kubernetes manifests. Large YAML files can easily be created with the least bit of configuration from our side. The tool has a lot of boilerplate YAML as well as files tailored to specific use-cases. This would be helpful when working with Kubernetes.
- `Lens` is a tool that simplifies DevOps workflow by automatically generating YAML files (among a host of other things). We do not need to write too much of YAML at all, just understand them. This tool does all the heavy lifting for us.