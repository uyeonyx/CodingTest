#!/bin/bash
echo "######## git add ########"
git add .
echo "##########################"
if [-z $1] 
then
	echo "######## git commit ########"
	git commit -m "auto update"
else
	echo "######## git commit ########"
	git commit -m "%s" $1
fi
	echo "##########################"
	echo "######## git push ########"
	git push
	echo "##########################"
