# Docker Hub

It is the official, central container repository offering by Docker. A Container Repository is any place that a developer (or an organization) may store their own images in. There are many public ones available but this is the most popular service.


## Basic Things to Know

- Official images are labelled as `imagename`, followed by a secondary label of `official`. They get to have the name of the repo. Normal images do not have such distinguishing facilities.
- Official images are made with the best practices, in the most proper way by the makers of the software itself. So, in general, there would not be an image that is better than that. They are very well documented.
- Normal images have the Docker username, followed by the image name. It would be a public automated build, mostly. We can create and pus our own images to Docker.


## Choosing the Corrrect Image

- Choose the image with the most number of stars upon searching.
- In case of non-official images, look at the pulls as well.
- Check out the repository from which the image comes from. If it has a lot of creds, then it should be legitimate.
- Inspect the GitHub repository as well along with the Hub repo.


## Tags

- Tags are identifiers that we can use to label an image. It is (loosely, not exactly) used to denote a particular version of a given image. Ex: `nginx:1.11`.
- There are actually three ways to uniquely identify an image - *user*, *repository* and *tag*.
- We can use the `docker pull` command to get the image with the tag that we so desire.
- Generally, the `latest` image tag means that the particular version of the image is the one that is officially recommended for latest use and is hard-tested, optimized and stable. It doesn't necessarily mean that it is indeed the newest release.
- It is a *very important production practice* that we do not just use the tags like `alpine` or `latest` or `slim`. We should most definitely use the **image tags representing versions numerically**. It eliminates confusions with respect to the issue for other developers as well as DevOps tools.