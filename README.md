# py-payments-testing

#### Build the docker
`docker build . -t py-payments-testing`

#### To run with the firefox browser inside docker:
`docker run -t py-payments-testing`

#### To run with a remote browser via browserstack:
`docker run --env AUTOMATION_REMOTE='true' --env AUTOMATION_REMOTE_BROWSER="Firefox" --env AUTOMATION_REMOTE_BROWSER_VERSION='55.0'
 --env AUTOMATION_COMMAND_EXECUTOR="https://<USERNAME>:<PASSWORD>@hub.browserstack.com/wd/hub" -t py-payments-testing`