Step 1 — Open Docker Desktop

Step 2 — Open PowerShell / CMD

Step 3 — Create docker-compose.yml

notepad docker-compose.yml

Write this and save it.

version: '3'
services:
  web1:
    image: nginx
    ports:
      - "8081:80"
  web2:
    image: nginx
    ports:
      - "8082:80"

Step 4 — Run Compose

docker-compose up -d

Step 5 — Check running containers

docker ps

Step 6 — Verify in browser

http://localhost:8081

http://localhost:8082

Step 7 — Stop all containers

docker-compose down

only cmds:::

notepad docker-compose.yml

docker-compose up -d

docker ps

docker-compose down
