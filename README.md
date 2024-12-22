## Deployment
### 1. Set PI_HOST=xxx.xxx.xx.xx where xxx.xxx.xx.xx is your local raspberry pi IP
```
export PI_HOST=xxx.xxx.xx.xx
```
### 2. Run setup to set up ssh keys and create docker context
(A context "pi-car" will be created and used)
```
./setup.sh
```
### 3. Start the app
```
docker compose up
```
