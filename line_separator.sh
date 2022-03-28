#!/usr/bin/env bash

LINES_SEPARATOR="<->"
WIDTH=50

# This is a function that takes an optional parameter width
# which is the number of times to print on screen LINES_SEPARATOR eg --------------

repeat_space(){
  NUMBER_CHECK_EXPRESSION=re='^[0-9]+$'
  INPUT=$1
  if ! [[ $INPUT =~ $NUMBER_CHECK_EXPRESSION ]]
  then
    WIDTH=$1
  fi
	for ((i=1;i<=WIDTH;i++));
	  do
	    echo -n "${LINES_SEPARATOR}";
    done
  echo -e "\n"
}