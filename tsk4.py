Step 1: open docker desktop

Step 2: open settings

Step 3: enable Kubernetes
Apply & restart
Wait for 5-10 mins

Step 4: Open Powershell or cmd

kubectl get nodes

kubectl cluster-info

kubectl get nodes

kubectl get all

kubectl create deployment ngnix --image=ngnix

kubectl get pods

kubectl describe pod ngnix-848cfc977b-jk68z

kubectl expose deployment ngnix --type=NodePort --port=80

kubectl get services

kubectl describe deployment ngnix

kubectl scale deployment ngnix --replicas=3

kubectl delete pod ngnix-848cfc977b-ffsx8

kubectl get pods

kubectl delete pod ngnix-848cfc977b-7np65

kubectl get pods

kubectl delete deployment ngnix

kubectl get all
