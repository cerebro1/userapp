# userapp
A Python user application deployed using Kubernetes that manages tests with Testkube, policies with Kyverno and on policy violations triggers test using ArgoEvents

## Deploy userapp application

### Start a Minikube cluster

```
minikube start --profile nova
```

### Enable ingress

```
$ minikube addons enable ingress
💡  ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.9.4
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled
```

### Deploy resources

```
kubectl apply -f k8s/
```

### Add cluster ip to /etc/hosts

```
$ echo "$(minikube ip) userapp.local" | sudo tee -a /etc/hosts
192.168.58.2 userapp.local
```

### Send curl request to application

```
$ curl http://userapp.local/?name=Sonali
{"message":"Hello Sonali, current date and time is 2025-08-29 11:38:36"}
```

