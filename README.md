> [!NOTE]
> The package is now available in the official Fedora repositories [here](https://packages.fedoraproject.org/pkgs/web-eid/web-eid/).

# RPM Package: web-eid

This repository holds the RPM package source for [web-eid-app](https://github.com/web-eid/web-eid-app).

> The Web eID application performs cryptographic digital signing and authentication operations with electronic 
> ID smart cards for the Web eID browser extension 

## Usage
You can use this package by enabling the copr repository at [abn/web-eid](https://copr.fedorainfracloud.org/coprs/abn/web-eid/) as described [here](https://fedorahosted.org/copr/wiki/HowToEnableRepo).

```sh
dnf copr enable abn/web-eid
dnf install web-eid
```

### Firefox
Once the native package is installed you should also install the [Web eID extension](https://addons.mozilla.org/en-US/firefox/addon/web-eid-webextension/).
