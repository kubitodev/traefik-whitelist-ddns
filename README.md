# Traefik Whitelist DDNS

This is a simple Traefik v2 DDNS updater script, which can be used in home lab setups to synchronize the allowed IP addresses for your [IP Whitelist Middleware](https://doc.traefik.io/traefik/middlewares/http/ipwhitelist/), which allows you to configure a VPN protected setup for your applications. It also support setting a custom domain for its IP(s) to be added to the whitelist range of the middleware.

## Requirements

* The installation must be inside the Traefik namespace in the cluster, as it uses the `traefik` service account to run.

## Things it does

* Creates a role and role binding objects which allow the script to patch middleware objects inside the Traefik namespace.

* Creates a middleware for IP whitelisting which can later be injected into the Ingress Route objects.

* Creates a cronjob which runs every X minutes and updates the allowed IP in the middleware to your own.

## Installing with Helm

There is a helm chart available as well. Check [the ArtifactHub page](https://artifacthub.io/packages/helm/kubitodev/traefik-whitelist-ddns) for more details.

## Installing with `kubectl`

Go inside the `manifests` directory and change anything you'd like in the manifests. You can leave the IP in the middleware to the default value, it will get updated anyway. Especially take a look at the environment variables set in the cronjob manifest, as you might want to replace them. To install, run:

```bash
kubectl apply -f manifests --namespace <TRAEFIK_NAMESPACE>
```

## License

Copyright &copy; 2022 Kubito

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
