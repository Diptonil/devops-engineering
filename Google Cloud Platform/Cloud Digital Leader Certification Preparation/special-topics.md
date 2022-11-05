# Special Topics


## Data Warehouses

- It is a relational datastore designed for *analytic workloads*. It is generally *column-oriented*. It needs to consume data from a relational database on a regular basis. If the database is not SQL, we need to first use ETL to transform the data for use.
- Companies would have terrabytes of data and millions of rows. They need a fast way to analyse this bunch of data.
- Data Warehouses perform *aggregations* by grouping data: find total or average, etc. They are optimized around columns since they quickly need to aggregate column data.
- They are designed to be hot - quick to retrieve or process data despite the bulk.
- They are used rather infrequently - once or twice a day just to generate user or business reports.
- Databases efficiently ingest large amounts of real-time data, while data warehouses rapidly analyze multi-dimensional datasets.


## Key-Value Stores

- This type of a database is NoSQL that uses a simple key-value pair method to store data. They lack features such as indexes, relationships and aggregations.
- The method to store data is similar to a hashtable or associative arrays. They don't have columns and rows (hence the name schemaless) like RDBMS but they can be represented in that way.
- They are extremely scalable just because they don't have too much of complexity like RDBMS.


## Document Data Store

A document store is a NoSQL database that stores documents as its primary data structure. It can be XML, JSON or JSON-like stores. They are somewhat of a subclass of key/value stores.


## Apigee

- Apigee is a founding member of the OpenAPI initiative. Apigee Corporation was an API management and predictive analysis software provider before merging into GCP.
- The OpenAPI Specification is an open-source standard for writing declarative struture of an API. It is written in JSON or YAML format. This specification is generally used to declare the routes of the APIs, the possible responses, a brief summary, schemas, etc.
- Every CSP has a fully-managed API service offering which would act as the API Gateway. They generally support the OpenAPI standard so that quick imports and exports may be done for the API.
- The API Gateway for GCP is Apigee. It is solely used for API management and for APIs to provide security policies for identity verification, authentication, and access control. The name of the service is Apigee API Platform.
- Look at the GCP Services section under Management Services to see what it does.


## Anthos

It is a service to modernise existing apps on other CSPs or on-premises and build new apps rapidly in multi-cloud or hybrid environments. It also allows us to maintain consistencies. Primarily, it is a single control pane to manage K8s compute in hybrid scenarios.
- Core components:
    - Managed service mesh.
    - Serverless
    - Migration
    - Marketplace
    - Logging and monitoring
    - Service management.
- **Anthos on VMWare**: Modernise existing apps and build new apps on VMWare environments.
- **Anthos GKE**: Anthos has a major component of it associated to containers. In fact, **Migrate for Anthos** is a service that *only* aloows migration into containers and nothing else (frequently asked).
- **Marketplace for Anthos**: Easily deploy containerised apps that have prebuilt templates and consolidated billing.
- **Cloud Run for Anthos**: Combine the strengths of K8s and serverless.


## Cloud Deployment Manager

- IaC (Infrastructure as Code) is the process of managing and provisioning cloud services through machine-readable definition fies (JSON, YAML) rather than manual configuration. Terraform is a great example of a service that does just that.
- **Cloud Deployment Manager** is the native GCP service for the same. We can write yaml files and execute them with the Cloud CLI. This would result in the cloud services spinning up clusters and nodes by themselves, upon the execution of the configuration.
- This is similar to Terraform. Google Cloud, however, recommends the use of Terraform over the native service (seemingly). 


## Firebase

- It is a PaaS offering that is fully managed and is completely serverless (unlike App Engine). It is good for repidly developing web and mobile applications of somewhat small or moderate scale.
- Firestore is the database service that goes hand-in-hand with this.
- Some services that is assocaiated to it:
    - **Firebase Crashlytics**: Get clear, actionable insight into app issues.
    - **Firebase Test Lab**: Test your mobile apps across a wide variety of devices and device configurations.
- Some features that it provides:
    - Test labs.
    - ML/ Predictions
    - Hosting
    - Authentication
    - Testing
    - In-App Messaging
    - Remote Configs
    - Dynamic Links
    - Performance monitoring
    - Distribution
    - Google Analytics


## Migrations

- There are, in-theory, many types of migration patterns from on-premises to the cloud. Some patterns are:
    - **Invent in Brownfield**: As the name suggests, we *invent* in already explored (brown - old) land. We:
        - Build on existing codes.
        - Use tech that has already been chosen.
        - Work around limitations.
    - **Invent in Greenfield**: As the name suggests, we *invent* in newly found (green - new) land. We:
        - Start from scratch.
        - Can choose new technologies.
        - Learn from mistakes.
- There are forms of migrations as well in which some are easy to implement with less benefits but some are diffuclt to implement with greater benefits. They are:
    - **Lift & Shift**: Move workloads from a source to a target cloud environment with little to no modifications or refactoring. It is ideal when *workloads can operate as-is in the new environments* as well as *little to no need for business changes*. They take the least time as refactoring is minimum. Teams continue using tools that they wre using previously. It *doesn't take full advantage* of the cloud.
    - **Move & Improve**: Modernize the workloads and then move to take greater advantage of the Cloud. Refactoring is necessary here. We need to learn new skills as well to shift to the cloud. Greater advantages can be achieved from the cloud. Ideal when *a major update or refactor of app is necessary* and *target fails to support the growing demands of the app*.
    - **Rip & Replace**: Completely build an app from scratch for the cloud environment. It is ideal when *leveraging too much of the cloud tech is a requirement* and *legacy code debt needs to be cleared off*. Requires a *lot of time to learn and develop*, on the downside.
- Like forms and patterns, we also have strategies of migrations. The common 6R model:
    - **Rehost**: This is a *lift-and-shift* method to just rehost entire apps from on-premises to the cloud.
    - **Repurchase**: This is a method that lets the business subscribe to different models of a CSP to better suit their needs.
    - **Replatform**: This is a *lift-and-shift* method to make certain changes to the code so that it is suited for the cloud environment arther than being just a copy-paste of the original. This helps the app adapt better to the environment and theer exists at least less issues with the cloud platforms in such cases.
    - **Refactor**: This is a *move-and-improve* method that involves rearchitecting the app to better enjoy the benefits of the cloud.
    - **Retain**: Useful for a Cloud hybrid model when parts of the app (legacy, perhaps) are kept in the on-premises systems while parts of it (new parts) are migrated to cloud.
    - **Retire**: This is a *rip-and-replace* method that scraps the useless legacy software and retires it. Everything starts afresh in the new environment.
- The migration, for any body, generally happens in a road with 4 milestones:
    - **Assess**: The need to migrate and the new features that need migration are assessed and measured. Costs are calculated, budgets are set, personnel are trained and requirements are identified.
    - **Plan**: Create the basic plan of moving infrastructure. Service identities are realised and accounts are created. Resource organisation at different heirarchial levels tak eplace.
    - **Deploy**: Shift infrastructure and refactor so as to run things smoothly.
    - **Optimize**: Take advantage of all the services that the cloud offers to launch business profits better.


## Single Sign-Ons (SSO)

- It is an authentication scheme that allows users to enter their username and passwords just one time for accesing different systems and softwares.
- Login is seamless. As soon as they access a software, they are presented with a logic screen. That is the only one time they need to login. They don't have to keep on reentering their details again and again.


## Agreements

These terms might look fancy on papaer but are actually quite self-explanatory from the context itself.
- **Service Level Agreements**: It is a formal commitment between a customer and a provide about the *expected level of service*. When a customer meets its obligations under the SLA but the service level by the vendor is not met, customer will be eligible to recieve the compensation: financial or service credits.
- **Service Level Indicators**: It is a metric that indicates that measure of performance a customer is recieving at a given time. It can be uptime, performance, latency, error rate, etc.
- **Service Level Objective**: The objective(s) that a provider has agreed to provide. It is represented as a specific target percentage over a period of time.


## Charging Cycle

There are two ways GCP charges us:
- **Monthly Billing**: Costs are charged on a regular monthly basis.
- **Threshold Billing**: Cost is charged when the account has incurred a specific value and has went over it. <br />
We get to choose the payment cycle if only we have an invoiced account.


## Pricing Overview

There are 7 models, all of which are very intuitive to understand:
- **Free Trial**: Trial with limitations.
- **Free Tier**: Services with minimum monthly limits of free-use (even when the project is associated with a billing account).
- **On-Demand**: Regular prices.
- **Committed Use Discounts**: Price lower than on-demand by agreeing to a contract of 1 or 3 years.
- **Sustained Use Discounts**: Passive savings when using resources past a period of continued use.
- **Preemptible VM discounts**: Instances with a lot of savings but with the cost of being interrupted at any time.
- **Flat-Rate Pricing**: Prefer a stable cost for queries rather than paying on-demand (only BigQuery).
- **Sole-Tenant Model**: Higher cost of ownership of a single compute machine in absolute terms.