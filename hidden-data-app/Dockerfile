# while building image in ADP environment use below
# FROM docker.artifactory.us.caas.oneadp.com/innerspace/debian:bookworm
# or get it from chaingaurd 
FROM debian:bookworm

# Set the working directory
WORKDIR /app

USER root

# Install LibreOffice
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libreoffice-draw libreoffice-script-provider-python python3 python3-pip python3-uno \
      default-jre-headless libreoffice-java-common ure-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Allow pip to manage system site-packages (avoids PEP 668 stop)
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ ./app/
COPY entrypoint.sh ./entrypoint.sh
RUN sed -i 's/\r$//' /app/entrypoint.sh && chmod +x /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 2002 5000

ENTRYPOINT ["/app/entrypoint.sh"]

# docker run -it -d -p 5000:5000 --restart unless-stopped --name LibreOffice libreoffice:latest