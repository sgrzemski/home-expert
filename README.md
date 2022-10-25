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

## Access the service running on minikube
### Service of a type LoadBalancer
1. Start `minikube tunnel` in a separate terminal. 
```commandline
minikube tunnel
```
2. Apply Kubernetes resources to your minikube.
```commandline
kubectl apply -f k8s-resources.yaml
```
3. Get service's external IP address.
```commandline
kubectl get svc home-expert -o jsonpath="{.status.loadBalancer.ingress[*].ip}"
```
4. Access the service.
4.1. cURL
```commandline
curl -iv -X GET http://localhost:8080/
```
4.2. Web Browser
```commandline
Open your browser and go to http://localhost:8080/.
```
