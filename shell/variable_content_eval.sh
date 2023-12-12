#!/bin/bash
# test the string lenth
string1=soccer
string2=''
if [ -n $string1 ]
then
  echo " the string '$string1' is not empty"
else
  echo " the string '$string1' is  empty"
fi
if [ -z $string2 ]
then
echo  " the string '$string2' is  empty"
else
  echo  " the string '$string2' is not  empty"
fi
if [ -n $string3 ]
then
  echo " the string '$string3' is  empty"
  else
  echo  " the string '$string3' is not  empty"
fi
