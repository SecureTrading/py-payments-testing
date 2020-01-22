"""Separate module to handle framework logging"""
import logging
import sys


def _get_logger():
    nlogger = logging.getLogger()
    nlogger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    nlogger.addHandler(handler)
    return nlogger
