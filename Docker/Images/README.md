# Images

They are app binaries and other dependencies that contain all necessary data that may be used to be unpacked and used as a standalone setup of the particular app as a container. <br />
Officially, it is *an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime*.


## Docker Hub

This is a centralized place that we can go to for getting any image. Unless we are dealing with private images that have been exclusively created by companies for their personal use, we can find images in Docker Hub itself (provided they have been used for public use). <br />
Read `docker-hub.md` for more information.


## Image Layers

An image isn't simply a big blob of data. It is composed of numerous peels known as layers.
- It starts of with no layer - which is known as *scratch*. 
- Not every layer in an image adds on to the size. Some might just be a Dockerfile metadata information. These correspond to Dockerfile commands such as `MAINTAINER`, `ENV`, `CMD`, etc.
- There can be one very extensive layer, or dozens of layers that add up to the image size.
- Each and every Docker image layer has it's own identity (SHA). That means, once a particular layer has been downloaded, there is no need for it to be downloaded for it's use in another image. For example, an image using Ubuntu already has the Ubuntu layer downloaded on a system. If another image comes in which uses Ubuntu as its base, we already have the Ubuntu layer. No need to download that layer again. This particular concept alone saves a lot of space and also decouples images for efficiency.
- Hence, we do not really store the entire stack of layers more than once for each image.
- When a container is run, we get another layer atop all the image layers. That is the container layer. It gets destroyed as soon as the container gets destroyed. For each container, we can have a layer atop the image layers. That identifies a container.
- Conatiner layers can have write privileges but in context of running a container, the image layers become read-only.
- The term `<missing>` under the image just means that the image was updated to have another layer and hence displaying its ID is quite irrelevant.


## Dockerfiles

These are actually the scripts that are responsible for creating images. They have been dealt with in `dockerfiles.md`.
