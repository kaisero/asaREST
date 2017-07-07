import logging
import sys

from rainbow_logging_handler import RainbowLoggingHandler

from lib.asaREST import AsaREST


class ASA(object):
    def __init__(self, device=None, username=None, password=None, verify_cert=False, loglevel=20):
        self.logger = logging.getLogger('ASA')
        self.logger.setLevel(loglevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'yellow', True))
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.api = AsaREST(device, username, password, verify_cert)

    def get_network_objects(self):
        network_objects = list()
        for response in self.api.get_networkobjects():
            try:
                items = response.json()['items']
                return_items = list()
                for i, v in enumerate(items):
                    if v['host']['kind'] == 'IPv4Network':
                        return_items.append(v)
                network_objects.extend(return_items)
            except Exception as error:
                self.logger.critical('Could not parse response. Response must contain valid json with items.')
                self.logger.critical('Exception: %s' % error.message)
        return network_objects

    def get_host_objects(self):
        host_objects = list()
        for response in self.api.get_networkobjects():
            try:
                items = response.json()['items']
                return_items = list()
                for i, v in enumerate(items):
                    if v['host']['kind'] == 'IPv4Address':
                        return_items.append(v)
                host_objects.extend(return_items)
            except Exception as error:
                self.logger.critical('Could not parse response. Response must contain valid json with items.')
                self.logger.critical('Exception: %s' % error.message)
        return host_objects

    def get_range_objects(self):
        range_objects = list()
        for response in self.api.get_networkobjects():
            try:
                items = response.json()['items']
                return_items = list()
                for i, v in enumerate(items):
                    if v['host']['kind'] == 'IPv4Range':
                        return_items.append(v)
                range_objects.extend(return_items)
            except Exception as error:
                self.logger.critical('Could not parse response. Response must contain valid json with items.')
                self.logger.critical('Exception: %s' % error.message)
        return range_objects

    def get_networkgroup_objects(self):
        return None

    def get_protocol_services(self):
        return None

    def get_icmp_services(self):
        return None

    def get_policy(self, policy_name):
        return None

    def get_static_routes(self):
        return None

    def get_object_nat(self):
        return None

    def get_twice_net(self):
        return None
