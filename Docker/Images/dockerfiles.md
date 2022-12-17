# Dockerfiles

These files are responsible for creating the images that we can use with certain alterations over the base image that we use. <br />
Generally these are to be named `Dockerfile` but these days a single project may have multiple Dockerfiles. In that case, we do `Dockerfile.identifier`.


## Common Clauses

We can refer to the documentation for getting the proper instructions and notes. Here is the discussion of the most used commands.

- `FROM`: Specifies the base image from which the custom image derives. It is usually best practice to choose slimmer builds that come with exactly what we need and doesn't require further installation of tools that we'd need. It is also recommended to not have things that we'd not be using.
- `ENV`: Specifies the list of environment variables the containers of the image would have by default.
- `RUN`: Specifies the bunch of commands that get executed while the image builds itself. So, everytime a container starts up (is created), it is expected to have everything already done that are specified in the RUN command.
- `CMD`: It specifies the list of commands that would run when a container starts up. It has no role in the making of an image (apart from adding layers of not much load).
- `WORKDIR`: This defines the working directory within a container where all the operations are executed later. It is followed by the path. So, this generally comes way up in the Dockerfile. It is similar to running a `RUN cd path`. But using RUNs are discouraged if we have other better alternatives like this.
- `COPY`: This specifies what goes from the local system while image is built into the image. This data would exist in the container when it starts.
- `EXPOSE`: This informs Docker that the container listens on the specified network ports at runtime. It does not make the ports of the container accessible to the host. <br />
A container being generated from an image having such ports exposed can communicate, at runtime, with other containers using the exposed ports, given both containers are in the same network. <br />
This only instructs which port to actually expose so that making a connection to that port and that port alone would make the services by the container accessible. We actually connect to that conatiner port by forwarding it over to the host machine (using the -p option). <br />
We can have one or multiple exposeable ports listed one after the other.


## Recommendations

- It is important, in order to be able to extend the use of a particular Dockerfile by varying its builds or versions. So, keep things that are less likely to ever change at the top. Items in flux can be kept at the bottom.