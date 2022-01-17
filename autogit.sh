#!/bin/bash
git add .
if [-z"$1"] 
then
git commit -m "auto update"
else
git commit -m "%s" $1
fi
git push
