# Version Control

Version Control means basically keeping a track of all changes done to a particular project. This can be done for many reasons:
- To avoid important code loss after making changes.
- To revert back to a previous state of a project in case of any severe bugs.
- To keep track of the pace of growth of a project.<br />

There are multiple versioning tools available out there like Mercurial and Git. We would focuss on the latter here. Installtion of Git is a must, in this case.


## Git V GitHub

Git is the basic tool for versioning that can be individually used by developers to make changes or add features to a project. GitHub is the software platform that exists to add a layer of collaborative capability over to Git. It is a place where software is built and delivered and it supports various tools and techniques to achieve impeccable standards and perfections in doing so. Using GitHub, different developers can work on software at the same time without interfering in each others' work.


## Initializing a Repository

When we work on any project, we can create a private folder (inaccessible and invisible in IDEs by default) that is responsible for versioning our code. It is called `.git`. It can be created using:
```sh
git init
```
This initialization of the Git repository is basically a license that any changes occuring in the directory would get versioned and tracked. Ideally this step should be taken at the starting of development of any project so that the history is recorded right from the beginning.


## Status of a Repository

After initialization, development may begin. However, at any given time, we may want to see the changes that we may have made to our project and information about the state of our project. To see the state of the project at the current moment:
```sh
git status
```
The command will show different results at different stages of the project (some concepts are discussed ahead):
- If files have not been added, they will be untracked. They are shown in red.
- If files have been added, they will be tracked. They are shown in green.
- Modifications to a file are also noted.
- If no changes have been done to a project (or all changes have been pushed), we see the message that the working tree is clean.


## Tracking of Files

As such, even if we create files or folders, Git would not be aware of it. We as developers can make Git aware of anything that is happening in our project. The process of Git being aware of the existence and state of a file or directory is called tracking. To track changes:
```sh
git add <file1> <file2> ...
```
We can add all the files one by one that need tracking. If we want to track all the changes that are made to a project:
```sh
git add .
```


## Restoring Tracked Files

At times, we may track files that we did not intend to. To redo such errors and make the file untracked again, we can restore any staged changes.
```sh
git restore --staged <file1> <file2> ...
```


## Committing Files

After tracking all the files, we may need, at a point of time, to permanently create a snapshot or a record that establishes the changes. It is somewhat like a marker signifying an important event in a period of time. This process is called committing. This seeks to solidify the changes and make them permanent:
```sh
git commit -m "An appropriate message"
```
There are many norms of creating very professional commit messages that shall be discussed later. The `-m` flag means that an additional message is to be supplied as well.


## Looking at Commit History

We have an option to look at the history of the commits that were made locally without going to GitHub. We can log the history to see the entire history (right from the starting).
```sh
git log
```
The information displayed is the commit, the commit hash, the author and the date and time.


## Removing Previous Commit

The log produced has a hash for every commit. In case we have a commit that we would like to remove from our history, it can be done by selecting the hash of the commit right below it and giving the command:
```sh
git reset <commit-hash>
```
We must note that:
- There is no loss of data in this case. All work done doesn't disappear. Files only get unstaged.
- Commits are dependent on each other. If there are 5 commits and we choose the hash for the third commit to execute the command, only the third commit remains. The fourth and the fifth are gone.
- Latest commits cannot be removed by this method.
- Works for commits that haven't been pushed yet.


## Removing Latest Commit

The previous method doesn't do anything to remove a commit that has just been done by mistake (the latest one). This can be done by:
```sh
git reset HEAD~1
```
We must note that:
- There is no loss of data in this case. All work done doesn't disappear. Files only get unstaged.
- Works for commits that haven't been pushed yet.
- Change the number to 2, 3 or whatever to pop that many commits (that are made recently). This can also be done by using the hash with reset of the commit that we want to retain.


## Removing Latest Commit & the Files

The previous method takes care of reverting back to the state before the commit. Except, however, all the changes that were made would still be there. To throw out all the changes along with the commit as if nothing ever happened:
```sh
git reset HEAD~1 --hard
```


## .gitignore

At times we may want to have certain files that do not go into the version control either because the changes they require do not needed to be known by others or the files don't need to be shared. Sometimes environment variables, secrets and credentials are kept in such manners so that a public repo does not have the secrets stored out there in GitHub.<br />
The `.gitignore` file ignores any newly created file *that has not already been committed* to be versioned.


## Stashing Changes

There exist times in a project when we are working on a feature that is not really complete. We do not want to commit all those changes yet but at the same time we do not want to lose them. Creating a branch for such cases may be an option (explained later) but we can do something more quick and economical. We can work on those changes and when we are done and would like to deal with those later, we can stash them. Once we do that, the working tree has no idea about the existence of such files at all. They are completely gone until we bring them back again when we would want to resume work on them (probably after a few useful commits that relate to other parts of the project or when it is time to actually start working on the new feature in question).<br />
To stash:
```sh
git stash
```
To bring items back from the stash:
```sh
git stash pop
```
To clear the stash (very risky, please consider twice before making such moves):
```sh
git stash clear
```
We must note that:
- For large changes, create branches. Fo a local, temporary store to contain few minor, short-term changes (nothing too major), use stashing.
- In violation of the above suggestion, use depends on individual comfort and cnvenience.
- Consider clearing the stash very carefully. All stashed changes are lost.
- If a file with the same name as the stashed file is created, popping a stash cannot be done unless the new file is renamed or deleted. The stashed files don't handle such conflicts.
- Remembering that a stash exists is important as well.
- When inexperienced, falling back to committing and then reverting back only to go to GitHub and copy pasting the new feature changes might be better than to risk losing stashed changes. However, the process kills too much of time for experienced people who can handle stashes better.


## Stages of a File

1. **Untracked**: The file is new and Git knows nothing about it. Upon adding, it becomes...
1. **Staged & Tracked**: The file is made ready for a commit and is being tracked by Git. Upon committing, it becomes...
1. **Unchanged**: No changes are done after a commit, so there is no alteration and file is unmodified. If modified...
1. **Unstaged**: The file is *modified* (not new) and Git already knows about it. It is not, however, made ready for another commit. We have to add it again for that to happen.


## Connecting to Repositories

Say we have created a repo on GitHub and we want to connect to it locally. As such, when a repo is made locally it is not really connected to any repo (unless it is cloned). To connect:
```sh
git remote add origin <project-url>
```
This process is adding a remote (connection). This ensures that we are able to push and pull changes to and from that repo. This allows collaboration. We must know that `origin` here is the name assigned to the URL provided. Upon typing this:
```sh
git remote -v
```
We can see the url assigned to fetch and push, which means the link to which the changes would get pulled to and pushed from.


## Pushing Changes

Adding a connection does not mean that everything done in the local repository would automatically get sorted out at GitHub as well. To inform the `origin` of all the changes made, we need to push our commits:
```sh
git push origin <branch-to-push-to>
```
By default, when a repo is newly created the branch is most likely to be called `main`. So the command would be:
```sh
git push origin main
```
This means pushing commits in the main branch of the `origin`.


## Branches

- A branch is a sequential representation of the work history and changes on Git. This allows users to concurrently work on code and contribute without the hassle of some other commit messing up their work.
- There can exist more than one branch that may be independent or dependent on each other.
- Technically, it is represented by a directed acyclic graph (tree) where each node represents the changes (commits) and each edge represents the relation between the previous and the current changes.
- A few possible branch examples usually seen in a small project include the development, testing, deployment branch, etc. Ideally, while working on a new feature as well, we should switch to a new branch.
- The default branch is the main branch.
- To see all branches present in project (the currently chosen branch is denoted by a star):
    ```sh
    git branch
    ```
- The HEAD is what decides which branch we are currently at. It is on main branch by default. Changing a branch indirectly means changing the HEAD's location.
- To create a new branch:
    ```sh
    git branch <new-branch-name>
    ```
This command creates a new branch with the point of origin at the current branch. It means that whatever contents are present in the current branch would get copied over to the newly created branch.
- To switch branches (make sure to commit your work before switching branches):
    ```sh
    git checkout <branch-to-switch-to>
    ```


## Merging Branches

The process of merging all the changes of a particular branch into the current branch so that every changes made in both the branches are visible at the same time, in one branch (the current branch), is called merging. Assume we are in the default main branch and we have to merge changes contained in development branch:
```sh
git merge development
```


## Pulling Changes

When working on a project concurrently, we need to be up to date with every changes being pushed to the project. This enables us to avoid unnecessary conflicts. If a developer makes some changes to our project in a particular branch and we want to update our own branch with their changes:
```sh
git pull origin main
```
This means pulling commits from the main branch of the `origin` into the main branch locally being worked with.


## Contributing to Other Projects

- Check out the `contributions.md` file to understand how to contribute to existing projects. Forks, cloning, pull requests are explained there.
- As such, pushing changes to any branches of any public project to which we have no write access doesn't lead to any changes. We first need access to make any changes as such.
- Cloning a project automatically sets the origin to the url that is being cloned from.


## Origin & Upstream

- We understand what an origin is: the URL that we are allowed to push our changes to. If we are using a forked repository, the origin is the fork itself.
- Consider the scenario in which a fork of a popular project is created. While we are working on the addition of any features on our fork, some other changes may be happening in the original project. To be up to date with all those changes, we need to pull those into our working environment. This is different from regular pulling because the pull cannot happen from `origin` since that belongs completely to us. That is known as the `upstream`.
    ```sh
    git remote add upstream <main-project-url>
    ```
The main project URL belongs to the main repository from which we made the fork. As such, pushing to upstream is not going to help because we generally would not have any access to write to upstream. We have to go through the fork-PR-merge cycle described in `contributions.md`.


## Pulling Changes from Upstream

To sync our working environment with the original upstream project, we can fetch all the changes into our main branch since any PRs made for the main project would generally be merged on its main branch.
```sh
git checkout main
git fetch --all --prune
git reset --hard upstream/main
```
This entire thing can be done simply with:
```sh
git pull upstream main
```
We should note that executing this command only updates our local environment with the upstream changes. This is not reflected in our fork. To make that happen (make the fork's main up to date with the upstream's main), just commit and push all the new things that we have locally.


## Pull Requests (PRs)

- These are requests to public projects asking them to merge any changes done by the individual creating the pull request.
- Only one PR for one branch. Every commit added to that branch would successively we added into that pull request itself. This means that never work on more than one feature in a branch or a PR.


## Interactive Rebasing

We might choose to squash a lot of similar unnecessary commits into one (before pushing changes) to make the history look cleaner. A simple way to do it is to use reset on the hash of the commit after which all the commits need to be thrown out of. Then we have all the changed files and no snapshots. We can do a simple commit and push the changes.<br />
Interactive rebasing applies certain more features to it. If we have many commits, instead of making all those commits into one, we can choose which commits to remove and make a part of which while alos choosing the commits that we would like to stay the same.<br />
Apply `s` to squash all commits into the commit done before (the commit at the top). Apply `pick` to let a commit remain the way they were made to be.
```sh
git rebase -i
```


## Merge Conflicts

These are the conflicts that developers may run into when working on the same part of the same file. Different contributors may have different code at the very same place. This confuses Git as to which change to consider. This is something that shall only be resolved manually (these days fancy IDEs also help) after communication.


## Commands Explored

1. `git init`
1. `git status`
1. `git restore`
1. `git commit`
1. `git log`
1. `git reset`
1. `git stash`
1. `git remote`
1. `git push`
1. `git branch`
1. `git checkout`
1. `git merge`
1. `git pull`
1. `git clone`
1. `git rebase`


## Common Use-Cases

Check out the `Convenience Scripts` folder for the commands on common use cases:
1. `forget-last-commit.sh`/ `forget-last-commit.bat`: Run this command to remove the last commit forever that could have had some commit message mistakes or something that did not need to be committed. Changes should not have been pushed. Any changes made would also stay. Changes would be unstaged.
1. `fast-push.sh`/ `fast-push.bat`: Run this command while supplying the commit message in quotes and branch name to make a quick push of all changed files with one line of 