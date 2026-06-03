docker pull nginx

docker images

docker run -d --name mynginx -p 8080:80 nginx

docker ps

docker ps -a

docker exec -it mynginx bash

docker port mynginx

docker inspect mynginx

docker restart mynginx

docker stop mynginx

docker start mynginx

docker build -t myimage .

docker push myimage

docker rm mynginx

docker rmi nginx

  
Step 1 — Open Docker Desktop

Step 2 — Open PowerShell / CMD

Step 3 — Pull Image

docker pull nginx

Step 4 — View Images

docker images

Step 5 — Run Container

docker run -d --name mynginx -p 8080:80 nginx

Step 6 — View Running Containers

docker ps

Step 7 — View All Containers

docker ps -a

Step 8 — Execute Command Inside Container

docker exec -it mynginx bash

Step 9 — View Port Mapping

docker port mynginx

Step 10 — Inspect Container

docker inspect mynginx

Step 11 — Restart Container

docker restart mynginx

Step 12 — Stop Container

docker stop mynginx

Step 13 — Start Container

docker start mynginx

Step 14 — Build Image

docker build -t myimage .

Step 15 — Push Image

docker push myimage

Step 16 — Remove Container

docker rm mynginx

Step 17 — Remove Image

docker rmi nginx
