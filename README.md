# home-expert
## Build the Docker image
```commandline
docker build . -t sgrzemski/home-expert:latest -t sgrzemski/home-expert:$TAG
```

### Push the Docker image to Docker Hub
```
docker push sgrzemski/home-expert:latest
docker push sgrzemski/home-expert:$TAG
```

## Run the app locally
### Python solo
```commandline
pip3 install -r src/requirements.txt
python3 src/main.py
```

### Dockerized
```commandline
docker run -p 8080:8080 sgrzemski/home-expert:latest
```

## Run on Kubernetes (or a sort of a Kubernetes, e.g. minikube)
```commandline
kubectl apply -f k8s-resources.yaml
```
