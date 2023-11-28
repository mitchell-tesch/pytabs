# pyTABS - ETABS .NET API python wrapper
# pyTABS configuration handler


# general library imports
import os
import configparser


# location of pytabs configuration file (pytabs_config.ini)
PYTABS_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pytabs_config.ini')


def read_config():
    """Read pyTabs configuration file (pytabs_config.ini)"""
    pytabs_config  = configparser.ConfigParser()
    pytabs_config.read(PYTABS_CONFIG_PATH)
    return pytabs_config