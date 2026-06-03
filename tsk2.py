Step 1 — Open Docker Desktop

Step 2 — Open PowerShell / CMD

Step 3 — Create project folder

mkdir myapp

cd myapp

Step 4 — Create a simple application

notepad index.html

Inside html file Paste:

<h1>Hello from Docker Application</h1>

Step 5 — Create Dockerfile

notepad Dockerfile

Write this code and save it

FROM nginx

COPY index.html /usr/share/nginx/html

Step 6 — Build Docker Image

docker build -t myappimage .

Step 7 — Run Container

docker run -d -p 8080:80 --name myappcontainer myappimage

Step 8 — Verify

Open browser:

http://localhost:8080

Output:

Hello from Docker Application
::::
only cmds:::

mkdir myapp

cd myapp

notepad index.html

notepad Dockerfile

docker build -t myappimage .

docker run -d -p 8080:80 --name myappcontainer myappimage
