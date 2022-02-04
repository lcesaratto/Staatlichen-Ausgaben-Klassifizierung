#Dockerfile vars
pythonver=3.9
poetryver=1.1.12

#Makefile vars
IMAGENAME=myimage
IMAGEVER=0.1.0
CONTAINERNAME=mycontainer
IMAGEFULLNAME=${IMAGENAME}:${IMAGEVER}

.PHONY: help build run push all

help:
	    @echo "Makefile arguments:"
	    @echo ""
	    @echo "pythonver - Python Version (optional)"
	    @echo "poetryver - Poetry version (optional)"
	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
		@echo "run"
	    @echo "push"
	    @echo "all"

.DEFAULT_GOAL := all

build:
	    @docker build --build-arg PYTHON_VER=${pythonver} --build-arg POETRY_VER=${poetryver} -t ${IMAGEFULLNAME} .

run:
		@docker run -d --name ${CONTAINERNAME} -p 8000:8000 ${IMAGEFULLNAME}

push:
	    @docker push ${IMAGEFULLNAME}

all: 	build run push