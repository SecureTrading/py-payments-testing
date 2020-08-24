FROM rodolpheche/wiremock:2.26.3 as wiremock

COPY ./wiremock/__files /home/wiremock/__files
COPY ./wiremock/mappings /home/wiremock/mappings
COPY ./wiremock/keystore /home/wiremock/keystore

EXPOSE 8443