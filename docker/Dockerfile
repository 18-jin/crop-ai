FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# ===== system deps =====
RUN apt update && apt install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3-pip \
    git \
    ca-certificates \
    tzdata \
    build-essential \
    gdal-bin \
    libgdal-dev \
    openssh-server \
 && rm -rf /var/lib/apt/lists/*

# ===== python venv =====
RUN python3.10 -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install \
    "pip<24.1" \
    "setuptools<81" \
    "wheel"

# ===== ssh =====
RUN mkdir /var/run/sshd \
 && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# ===== workdir =====
WORKDIR /workspace

