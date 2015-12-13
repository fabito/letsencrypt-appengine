# letsencrypt-appengine

Google App engine python module for [letsencrypt](https://letsencrypt.org/) challenge/response verification.


## Deploying module on GAE

```!bash
export PROJECT_ID=myproject

# installs the module
appcfg.py -A $PROJECT_ID update app.yaml 

# Dispatches /.well-known/* to this module
appcfg.py -A $PROJECT_ID update_dispatch .
```

## Certificates generation

```!bash
docker run -it --rm -p 443:443 -p 80:80 --name letsencrypt -v "/etc/letsencrypt:/etc/letsencrypt" -v "/var/lib/letsencrypt:/var/lib/letsencrypt" quay.io/letsencrypt/letsencrypt:latest certonly --manual -d sub.example.com -d sub2.example.com
```

Before triggering the challenge response verification we need to store each challenge (and its respective response). The commaond below does exactly that. Note that you need to replace the `<challenge>.<response>` part at the end of the URL.

```!bash
curl 'https://myproject.appspot.com/.well-known/acme-challenge/OziHcpbKR9SYH0L6tl12345Hv-WvPEIoMVhweeZG9LU.hYSj9EX5tPUQbd5NHpd12345XGVVy24pIXLIPg12345' -X POST --compressed
```

## Upload certificates to GAE

Before uploading the certiicates we need to convert the generated private key (privkey.pem) to the RSA format.

```!bash
sudo openssl rsa -inform pem -in /etc/letsencrypt/live/sub.example.com/privkey.pem -outform pem | less
```

Copy the output of the above command and go to [appengine -> settings -> certificates](https://console.developers.google.com/appengine/settings/certificates?project=myapplication).

Click in "upload a new certificate" and fill in the "Unencrypted PEM encoded RSA private key" field with the copied key.
For the "PEM encoded X.509 public key certificate" field use the generated "fullchain.pem" 

