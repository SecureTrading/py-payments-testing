# py-payments-testing

#### Build the application docker

You need an `js-payments` application image built to be able to run tests. You can either pull it from the docker hub or
build it yourself.

To check if you have the image on your local system:

`docker images | grep js-payments`

To build it, open the `js-payments` project and run:

`docker build . -t securetrading1/js-payments:develop`

You can change the default tag `:develop` to any other just to create images with different branches.

#### Start up the docker containers

`docker-compose up -d`

The example page is available under address `https://merchant.securetrading.net/`. You should add this domain to your `hosts` file
and point to address `127.0.0.1` (here you can find how to do it https://support.rackspace.com/how-to/modify-your-hosts-file/).

The Wiremock is available under `https://webservices.securetrading.net:8443/` so to access it you should also add this address
to the `hosts` file.

#### To run the tests

`docker-compose run tests poetry run behave features`

#### To test a different branch

If you have multiple application images with different branches you can specify which image should be used for tests, eg.:

`APP_TAG=master docker-compose up -d`

#### To test a different application (eg. js-payments-card)

`APP_REPO=js-payments-card docker-compose up -d`


#### To run with a remote browser via browserstack:
 `docker-compose run -e LOCAL=true -e REMOTE=true -e BROWSER="Chrome" -e BROWSER_VERSION=80.0 -e OS="Windows" -e OS_VERSION=10
 -e BS_USERNAME=<BROWSERSTACK_USERNAME> -e BS_ACCESS_KEY=<BROWSERSTACK_ACCESS_KEY> tests poetry run behave features`