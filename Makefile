# Makefile

IMAGE_NAME = k3s-hello-world
VERSION = 0.1.1

all:
	@echo there is no default target

package:
	docker build -t ${IMAGE_NAME}:${VERSION} .
