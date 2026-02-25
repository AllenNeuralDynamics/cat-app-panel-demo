# hash:sha256:f83d12e9912f23488b7cde34f894f5decd8102cb97c867711ef8cb82d5c83659
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:23.1.0-4-python3.10.12-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    eval-type-backport==0.3.1 \
    pydantic==2.12.5 \
    pydantic-settings==2.11.0
