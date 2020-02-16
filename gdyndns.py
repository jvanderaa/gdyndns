#! /usr/local/bin/python
"""
Python application to update Google Dynamic DNS entry, IPv4 only at this time
"""
import os
import sys
from time import sleep
import socket
import requests

try:
    SLEEP_TIMER = int(os.environ["GDYNDNS_SLEEP_TIMER"])
    if SLEEP_TIMER < 300:
        SLEEP_TIMER = 300
    IP_ADDRESS_URL = os.environ["GDYNDNS_IP_ADDRESS_URL"]
    GOOGLE_DOMAIN = os.environ["GDYNDNS_GOOGLE_DOMAIN"]
    SUB_DOMAIN = os.environ["GDYNDNS_SUB_DOMAIN"]
    USERNAME = os.environ["GDYNDNS_USERNAME"]
    PASSWORD = os.environ["GDYNDNS_PASSWORD"]
except KeyError:
    print(f"Exception in loading required environmental variables.")
    print(f"Verify you have created the proper settings.env file.")
    sys.exit(1)


class NetworkIp:
    """
    Class to define the current local network and update Google Dynamic DNS if necessary
    """

    def __init__(self):
        """
        Initialization of class
        """
        self.previous_ip = self.verify_domain_exists()
        self.current_ip = self.get_current_ip()

    @staticmethod
    def get_current_ip():
        """
        Method to get the current IP address
        """
        request = requests.get(IP_ADDRESS_URL)
        return request.content.decode("utf-8")

    def update_google_dns(self):
        """
        Method to update Google DNS
        """
        # pylint: disable=line-too-long
        url = f"https://{USERNAME}:{PASSWORD}@domains.google.com/nic/update?hostname={SUB_DOMAIN}.{GOOGLE_DOMAIN}&myip={self.current_ip}"
        response = requests.post(url)
        print(response.status_code)
        print("Need to update Google DNS")

    @staticmethod
    def verify_domain_exists():
        """
        Function to verify the domain specified in the settings exists
        """
        try:
            return socket.gethostbyname(f"{SUB_DOMAIN}.{GOOGLE_DOMAIN}")
        except socket.error:
            print(f"Failed to find {SUB_DOMAIN}.{GOOGLE_DOMAIN}")
            print(f"Please verify that the sub domain is setup first on your Google Domain")
            sys.exit(1)


def main():
    """
    Main code execution
    """
    my_ip = NetworkIp()

    while True:
        print(f"Current IP: {my_ip.current_ip}, Previous IP: {my_ip.previous_ip}")
        if my_ip.current_ip == my_ip.previous_ip:
            print("Found same IP, no update necessary")
            sleep(SLEEP_TIMER)
        else:
            my_ip.update_google_dns()

        my_ip.previous_ip = my_ip.current_ip


if __name__ == "__main__":
    main()
