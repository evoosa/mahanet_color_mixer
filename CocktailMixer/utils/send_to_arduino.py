from urllib import urlopen

from CocktailMixer.utils.config import ARDUINO_PORT, ARDUINO_IP, HANDLE_DRINK_REDIRECTION


def send_to_ardi(pump_times: list):
    ard_url = "{ard_ip}:{ard_port}/{redirection}".format(ard_ip=ARDUINO_IP, ard_port=ARDUINO_PORT, redirection=HANDLE_DRINK_REDIRECTION)
    url = 'http://{ard_url}?pump_times={pump_times}'.format(url=ard_url, pump_times=pump_times)
    urlopen(url)