import os

from pprint import pprint
from urllib.request import urlopen
from kubernetes import client, config


def main():
    config.load_incluster_config()
    api = client.CustomObjectsApi()

    current_ip = urlopen('https://api.ipify.org').read().decode('utf8')

    patch_body = {
        "spec": {
            "ipWhiteList": {
                "sourceRange": [
                    current_ip
                ]
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
