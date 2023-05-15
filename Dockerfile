# set base image (host OS)
FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Custom cache invalidation
ARG CACHEBUST=1

# set the working directory in the container
WORKDIR /workspace

RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# COPY etc/ /etc/.
COPY requirements.txt /workspace/

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# install editors - nano
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    nano

# Setup SSH with secure root login
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    openssh-server netcat \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /var/run/sshd \
    && echo 'root:password' | chpasswd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]