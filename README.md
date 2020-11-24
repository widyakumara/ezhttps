# ezhttps
Easy way to wrap your (legacy) web service on https for local development

## Prerequisites:
* [docker](https://www.docker.com/products/docker-desktop)
* [mkcert](https://github.com/FiloSottile/mkcert)

## Installation
* Install requirements above

* Generate root local CA
  `mkcert -install`

* Clone this repo
  `git clone git@github.com:widyakumara/ezhttps.git`

* Get your the **local IP address** of your working machine (there are several ways to do this, Google is your friend)

* Generate certificate with your IP
  `mkcert -cert-file ./confs/<YOUR_IP>.crt -key-file ./confs/<YOUR_IP>.key <YOUR_IP>`

* Copy (or rename) `env.sample` to `.env`

* In `.env`, replace `WEB_HOST` with your IP, and `SVC_PORT` with your web service port

* Run the container
 `docker-compose up`

* Open `https://<YOUR_IP>/` in browser

## Caveat
* This setup only support web service running on 127.0.0.1. For now. Maybe.
* If your web service requires more than one port to run (e.g. for HMR), that won't work. For now. Maybe.
* If you need to access your web service from mobile, follow [this instruction](https://github.com/FiloSottile/mkcert#mobile-devices)

## License

Copyright 2020 Dewa Widyakumara

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

