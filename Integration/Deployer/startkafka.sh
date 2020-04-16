#! /bin/bash
# echo $1
a=$1
eval 'cd $1'
eval 'pwd'
eval 'bin/zookeeper-server-start.sh config/zookeeper.properties &'
eval "bin/kafka-server-start.sh config/server.properties &"