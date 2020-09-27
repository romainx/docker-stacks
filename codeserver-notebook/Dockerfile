# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# ---- Prerequisites
RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Code-server install
RUN curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run && \
    curl -fsSL https://code-server.dev/install.sh | sh

# ---- jupyter-server-proxy install
RUN conda install --quiet --yes \
    'jupyter-server-proxy' && \
    jupyter labextension install @jupyterlab/server-proxy && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# ---- configure code-server proxy
COPY codeserver-config.py vscode.svg /etc/jupyter/
RUN cat /etc/jupyter/codeserver-config.py >> /etc/jupyter/jupyter_notebook_config.py

USER $NB_UID
