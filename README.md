# gdyndns

Google Domains has a REST API that allows you to use Dynamic DNS updates. This is based on the
information based on the Google DNS page:  

https://support.google.com/domains/answer/6147083?hl=en  

## System Requirements

- Docker
- Make
- Internet Access

## Installation

1) Clone the repository to a system that has Docker installed on it (https://docs.docker.com/install/)
2) Build the Docker container with the command `make build`
3) Update a file `settings.env` which will be loaded into your container at runtime (see below for a sample)
4) Execute command `make run` to start the container

### Settings Required

GDYNDNS_IP_ADDRESS_URL: URL to get your IP address from, built with http://ifconfig.me  
GDYNDNS_GOOGLE_DOMAIN: Your Google Domain, without any www. or http or anything else. Just domain.google  
GDYNDNS_USERNAME: Username as created on the Google Domains page  
GDYNDNS_PASSWORD: Password for Google Domains as created on the Google Domains page  
GDYNDNS_SUB_DOMAIN: The DNS entry that you wish to use, this **must** be created before starting the container  
GDYNDNS_SLEEP_TIMER: Time in seconds to sleep before checking to see if an update is needed  

### Example Settings File

An example settings file should look like the following:

```bash
GDYNDNS_IP_ADDRESS_URL=http://ifconfig.me
GDYNDNS_GOOGLE_DOMAIN=example.com
GDYNDNS_USERNAME=aROTvffJ9
GDYNDNS_PASSWORD=z0HlTqiwMTpzCND2
GDYNDNS_SUB_DOMAIN=dynamicdns
GDYNDNS_SLEEP_TIMER=300
```
