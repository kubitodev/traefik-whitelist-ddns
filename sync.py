import os
import socket

from pprint import pprint
from urllib.request import urlopen
from kubernetes import client, config


def main():
    config.load_incluster_config()
    api = client.CustomObjectsApi()

    custom_domain = os.environ.get('WHITELIST_CUSTOM_DOMAIN')

    current = []
    public_ip = urlopen('https://api.ipify.org').read().decode('utf8')
    current.append(public_ip)

    if custom_domain:
        ip_list = socket.gethostbyname_ex(custom_domain)[2]
        for ip in ip_list:
            current.append(ip)

    patch_body = {
        "spec": {
            "ipWhiteList": {
                "sourceRange": current
            }
        }
    }

    name = os.environ.get('WHITELIST_MIDDLEWARE_NAME', 'ip-whitelist')
    namespace = os.environ.get('WHITELIST_TRAEFIK_NAMESPACE', 'traefik-system')

    patch_resource = api.patch_namespaced_custom_object(
        group="traefik.containo.us",
        version="v1alpha1",
        name=name,
        namespace=namespace,
        plural="middlewares",
        body=patch_body,
    )

    print("Current state of the middleware: ")
    pprint(patch_resource)

if __name__ == '__main__':
    main()
