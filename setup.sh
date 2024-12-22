ssh-keygen -t rsa -q -f "$HOME/.ssh/id_rsa" -N ""
ssh-copy-id $PI_HOST
docker context create pi-car --docker "host=ssh://$PI_HOST"
docker context use pi-car
