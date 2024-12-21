sudo docker save pi-car | bzip2 | pv | ssh $HOST "sudo docker rmi pi-car && sudo docker load"
