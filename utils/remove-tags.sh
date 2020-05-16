#! /bin/bash

# pass tags as arguments to script
# if no arguments, nothing will be removed
# for example to remove all tags run ./remove-tags.sh $(git tag)
tags=( "$@" ) 
for i in ${tags[@]}
do
  git push --delete origin $i
  git tag -d $i
done
