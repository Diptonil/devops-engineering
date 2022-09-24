# GitHub Actions

Many people start off by saying that GitHub Actions is a well-known CI/CD pipelining tool. But that is not all. The correct definition is that it is a *platform to automate developer worflows*. The pipeline tool is just a part of the great many things that it encompasses.


## What are Workflows?

Developers work on projects collaboratively. In each project, apart from developing features, there are certain organizational tasks meant to be there for the preservation of integrity as well as check on the code quality if it adheres to the standards of the projects and so on. Larger and more important a project is, the greater is the number of such issues that need to be actively monitored just because the number of developers might be too large or a project is open sourced. <br />

Examples of workflows:
- An issue if created on a GitHub repo. The assignment of contributers and labels to that issue is a workflow.
- Say a contributer fixes the issue. Checking that the issue solves what it was meant to solve is a workflow.
- Does the merged code that fixes the issue break any other part of the application? Checking if all tests are running fine is a workflow.
- The whole process of building and deploying after the merge is correct is also a workflow.

As one can see, tthe definition of a workflow doesn't only extend up to CI and CD. It is a bunch of other things as well. <br />
Obviously we would need to automate such workflows because keeping track of all these things manually is impossible for a large projects like Apache or Elastic projects.


## GitHub Events & Actions

- Every occurence that happens to or in our repository is an **Event**. It might mean the creation of an issue, pushing of changes into a new branch to the origin, new pull requests, etc. GitHub Actions is meant to keep track of all these events.
- Every response to the event that we want to automate with an appropriate workflow is an **Action**.


## Pros of Actions for CI/CD

- GitHub is the default choice for version control. With Actions, we are just getting more functionality in the same familiar space. We do not need to run another 3rd party tool like Jenkins on our system to build code in this case.
- Setup process of CI/CD pipeline is very easy.
- Simple tool for developers that ensures that they do not really need a DevOps person for the job.
- To build using softwares like Jenkins we need to install on the build machine (locally or on the Cloud) all the necessary softwares that are required for the build to proceed. Here, that overhead is not involved.


## Workflow Templates

- Now that the uses are clear, it is worth knowing that when a repository would need use for Actions, we should choose from the existing templates rather than write our own files. This makes things simpler for bigger projects that are more general. However, there are some projects for which the existing templates might not result in proper workflows.
- The templates are segregated into sections like:
    - Cloud Deployment workflows
    - Security
    - CI workflows
    - Automation workflows
- Workflows for a repo would get stored in `.github/workflows`.


## Workflow Syntax

GitHub Docs provide a pretty exhaustive list of all the commands.
- `name` (optional): Name of workflow.
- `on` (optional): Name of the GitHub event that triggers the workflow.
- `runs-on`: The OS on which the servers run.
- `matrix`: Specifies a set of options for multiple OSs or Python versions or JDK versions, etc. All of them would be executed. Needs to be referenced later separately.
- `branches`: Specifies which all branches the workflow would run on. To match every branch, use `- '**'`.
- `branches-ignore`: Specifies all the branches the workflow would not run on. Never used with `branches`.
- `jobs`: Specifies what to do.
- `build`: Under job, specifies that build would run.
- `steps`: Enumerate the number of steps taken to run the workflow. It also lists out the commands.
- `uses`: Selects an action from a given few options. The `actions/` is the place from where the actions get chosen. That is a project by GitHub. It has repos like Checkout, etc. that we can ue directly for our work.
- `run`: Used to run a command on the terminal.


## Dissecting the Example

Consider the `example.yaml` file thoroughly. It is a workflow for testing and building a Django project.
- It gets triggered when a pull request or a push is made on the main branch.
- Runs on the latest Ubuntu version.
- It uses the Python version as specified in matrix. All versions from those should pass the checks. It sets up Python, installs dependencies as per the requirements.txt file. Then it runs tests.
- If everything gets succesfully done, only then will everything pass and the workflow would get a success flag.


## GitHub Actions Runner

- GitHub manages everything for us by themselves on their servers. We can also choose to do it by ourseves but mostly it is best to stick to the default.
- At a time when a workflow runs, every job specified in the yaml file (in example we only have the build job) runs on a seperate GitHub server. By default, the jobs happen in parallel. However, it may happen sometime that our 2nd job would have a dependency on the first. In such a case, in the specification of the second job, we add:
```
needs: build
```