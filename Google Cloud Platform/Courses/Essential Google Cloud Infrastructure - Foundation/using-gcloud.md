# Using Google Cloud

Four ways exist to interact with GCP. They are:
- **Cloud Console**: It is the GUI that one can use to do things around in the Cloud.
    - This may be helpful for parties with less experience in managing the shell environments.
    - This can be accessed in `console.cloud.google.com`.
    - It can be subject to change, unlike the Shell.
- **Cloud Shell**: It is the environment that is used generally by professionals who know their way around the shell environment. It is basically an Ubuntu machine (VM) that is specialised with 5 GB persistent disk storage. Sessions don't die easily. <br />
After an hour of inactivity, the Cloud Shell instance is recycled. Only the `/home` directory persists. Any changes made to the system configuration, including environment variables, are lost between sessions.
- **Cloud SDK**: It is a development environment that is used to leverage the Cloud services by communicating with the underlying system architecture. It is installed by defult in the Shell service.
- **GCP Client Libraries**: It is a tool used to allow other frameworks or software making tools to integrate with the Cloud environment.
- **Cloud Mobile App**: This can be used on a phone to manage VMs, databases, apps in the *App Engine*, bill management, dashboard visualisations. Functionality is limited but quite helpful for projects requiring around-the-clock support and surveillance.


## The Shell & Console

The two tools may be understood to do the same things in different ways. This should not discourage anyone from adopting both the learnings because primarily, both *cannot* be used vice-versa. Sometimes the Console might offer a more visually comprehensive survey of reports. Sometimes the Shell might help in troubleshooting or understanding an error more clearly. <br />
We should not view these two devices as separate and in fact, see them as two components of the same singular interface.


## Labs: Infrastructure, Console & Shell

1. Deployment of an app using the GCP Marketplace.
1. Creating a Storage bucket using the Console and the Shell.