# Size Optimization Techniques

For most use cases, it is highly recommended for a Docker image size to be as small as possible. While any exteranl optimization tools such as Dive or , the size of an image mostly depends on how the Dockerfile is written. Succinct knowledge about writing Dockerfiles is a great skillset and that is actually what is really needed for professional work. <br />
Below are certain known techniques that can be used.


## Use `.dockerignore`: Docker

There are times in which we use the COPY instruction in a Dockerfile to copy data over to the image that shall get built. It is a powerful feature that can lead to bloating of the image as well by copying unnecessary files. To tag out the files that doesn't need to be copied over, use the `.dockerignore` file and list out everything that doesn't need to be included in the image.


## Minimal Base Image: Docker

If we have specialized work for an image, we mostly would be using base images of OSs. They are best suited for customized work that doesn't follow a standard, traditional template. However, if we choose OS images that come shipped with features irrelevant to our work, we would be bloating up the build unnecessarily. So, the following guidelines should be ensured before choosing an image:
- Alpine base images can be small and secure as well. Use them over the main OS image. The cons associated are less support and need for a lot of debugging.
- Slim OS images are better than the main OS build. They provide enough functionality to get the work done without having the cons of the alpine images.


## Distroless Base Images: Docker

If the task for the image to build is quie common and can be generalized, it can be based off from a template. Most of the work in Docker is generally like this. Distroless images for Java, Python, Maven, etc. come with the capacity to provide use of these technologies without the overhead of the associated OS image. These images are highly gaining traction and are being recommended more and more.


## Knowing When to Compress Layers: Docker

It is well known that having multiple RUN commands can increase build time as well as increase size *very faintly* (it is almost unnoticed in many cases). Multiple commands should always be packaged into one RUN command **iff** it seeks to solve to the same functionality (like a group of `apt-get` package commands under one RUN, which is acceptable). At times this grouping is done to reduce layers but with no clear logic (like grouping together commands for pip installation with git instructions, which is *not* acceptable). <br />
We must learn when to compress layers as it offers no optimization in terms of size. However, it provides bug gains with respect to the build time. Hence, RUN commands should be logically grouped and compressed with justification.


## Avoid Unnecessary Dependencies: Linux's `apt-get`

The default behaviour of `apt-get` is to download softwares that are not really required dependencies but are just recommended. Their presence is not at all required. So, we just diable that option using the `--no-install-recommends` option. <br />
```sh
apt-get -y --no-install-recommends install <package-name-list>
```


## Clean Up Cache: Linux's `apt-get` 

By default, there are a lot of files stored in the `apt-get` cache. Their presence won't affect the build of the image in any way. So it is just better to remove such packages. The command to do so can be appended to the RUN instruction that deals with the installation of Linux packages:
```sh
rm -rf /var/lib/apt/lists/*
```


## Disable Package Caching: Python

The default package installation by `pip` is configured by default to cache the installed packages for future downloads. However, for Dockerfiles with exact specifications, that is vastly useless, since most of the times the requisites for a Dockerfile is known clearly. Hence, we install our requirements with the `--no-cache-dir` option.
```sh
pip3 install --no-cache-dir -r requirements.txt
```
