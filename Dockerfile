FROM python:alpine3.15

# Install the kubernetes module
RUN pip install kubernetes==23.3.0

# Copy the script to the container
COPY sync.py .

# Set the required variables by the script
ENV WHITELIST_CUSTOM_DOMAIN=
ENV WHITELIST_MIDDLEWARE_NAME=ip-whitelist
ENV WHITELIST_TRAEFIK_NAMESPACE=traefik-system

# Run the script
CMD ["python", "sync.py"]
