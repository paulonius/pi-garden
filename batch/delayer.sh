#!/bin/bash

usage() 
{
    echo "usage: delayer.sh <sunrise|sundown> <script>"
}

if [ $# -lt 2 ]; then
    usage
    exit 1
else 
    case $1 in
        sunrise) 
            period=rise
            ;;
        sunset)
            period=set
            ;;
        * )                 
            usage
            exit 1
    esac
fi

echo $PERIOD
sunwait wait civ $period 42.342742N 7.858719W
if [ $? = 0 ]; then
    shift
    $@
else
    echo "too late to execute for sun$period"
    exit 0
fi
