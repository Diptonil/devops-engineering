# Getting Started With Contributions

Whether it is open-sourcing or just normal contributions to a group-project, contributing to a public project that is large and has maintainers may seem daunting. To ease the process, luckily, there exist a number of programs out there. Hacktoberfest is an event that serves to familiarize new developers by enabling them to make contributions to repositories.<br />
<a href="https://github.com/firstcontributions/first-contributions">This</a> repository is a good starting point that guides one on how to make a contribution for the first time.


## Steps

The standard steps that one needs to follow to contribute to any project is:
1. **Fork the repository**: Forking is the process of making a copy of an existing public project that would belong to the person who forks. This allows one to freely experiment with changes without affecting the original project.
1. **Clone the fork**: The repository forked would now be cloned into the local machine so that changes may be done on it. Make note to clone the forked project and not the original project.
1. **Create a branch**: In your repo, create a branch that would identify the changes that you would do.
1. **Make changes**: Locally make changes to the project.
1. **Commit**: Make a commit with a detailed message. Make sure that the work done adheres to the guidelines of contributions.
1. **Push**: Push changes to your repository. 
1. **Pull request**: Go to GitHub to find `Compare & pull request`. Submit the pull request once everything is documented properly. <br />
After all this is done, it is up to the maintainer to accept the changes and merge the branch into their main working branch. It is important to refer to the guides on contributions and the code of conduct, if they have any, to adhere to any guidelines that they may have.


## Commands

- For cloning: <br />
```
git clone https://github.com/<your-username>/gcp-associate-cloud-engineer.git
```
- For creating a branch: (Assuming the directory is chosen correctly)<br />
```
git switch -c new-branch-name
```
- Committing: <br />
```
git add .
git commit -m "Very helpful"
```
- Pushing: <br />
```
git push origin -u new-branch-name
```
