docker build -t myimage:0.1.0 .

docker run -d --name mycontainer -p 8000:8000 myimage:0.1.0