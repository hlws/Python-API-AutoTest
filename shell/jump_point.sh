#!/bin/bash
jump_directory=/home/test
if [ -d $jump_directory ]
then
  echo "the $jump_directory is exists"
  cd $jump_directory || { echo "Failure"; exit 1; }
  ls
else
  echo "the $jump_directory is not exists"
fi