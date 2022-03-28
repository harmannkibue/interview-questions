#!/usr/bin/env bash

source ./line_separator.sh

BRANCH=`git rev-parse --abbrev-ref HEAD`

# Showing git status.Copy files to add.
repeat_space 20
echo "YOUR GIT STATUS: "
git status
# Function call from the source import above
repeat_space 20
echo "Pushing to branch ${BRANCH}"
repeat_space 20
echo
echo -n "Enter file path() to commit, (Press enter to commit all): "
read FILE_PATH

repeat_space 20

# Check if there is a file path
if [ -z "${FILE_PATH}" ]
then
      git add .
else
      git add $FILE_PATH
fi

echo -n "Enter commit message: "
read COMMIT

git commit -m "$COMMIT"
git push origin ${BRANCH}