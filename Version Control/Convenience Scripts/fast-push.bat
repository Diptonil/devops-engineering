:: Use double quotes to specify commit message as 1st parameter.
:: Specify the branch name as the 2nd parameter.
:: Example: `.\fast-push.bat "Commit message" branch-name`

git add .
git commit -m %1
git push origin %2