#!/bin/bash
location=$HOME
file_name="sentinel"
if [ -d $location ]
then
  echo "ok on the $location direction"
  echo " checking on the file,$file_name... "
  if [ -e $location/$file_name ]; then
      echo "ok on the file $file_name"
      echo " update file"
      date >> $location/$file_name
  else
    echo "the $location/$file_name is not exist"
    echo " nothing to do"
  fi
else
  echo "Directory, $location, does NOT exist."
  echo "Nothing to update."
fi