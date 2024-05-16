"""
This module script a customized vnocat nuage obj fetcher for discovery
Author: Muzaffer Kahraman
email: muzaffer.kahraman@outlook.com
Date: 2024-05-05
v 1.0
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from opentelemetry import metrics
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter
from pygnmi.client import gNMIclient
import time

host = ('clab-muzolab-leaf1', '57400')
username = 'admin'
password = 'NokiaSrl1!'

def grab_outpackets(interface_name):
    with gNMIclient(target=host, username=username, password=password) as gc:
        path = f'/interface[name={interface_name}]/statistics/out-packets'
        data = gc.get(path=[path], datatype='state')        
        return data['notification'][0]['update'][0]['val']
    
     
if __name__ == '__main__':
    
    ethernet_1_1_previous=0
    ethernet_1_2_previous=0
    
    _meter = metrics.get_meter(__name__)
    
    _readers = [PeriodicExportingMetricReader(OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics"),export_interval_millis=1000,export_timeout_millis=5000),
                PeriodicExportingMetricReader(ConsoleMetricExporter())
                ]
    
    metrics.set_meter_provider(MeterProvider( metric_readers= _readers))
    
    _ethernet_1_1_counter = _meter.create_counter("ethernet-1/1", description="Number out packets from the interface", unit="1")
    _ethernet_1_2_counter = _meter.create_counter("ethernet-1/2", description="Number out packets from the interface", unit="1")
    
    while True:
    
        ethernet_1_1=int(grab_outpackets("ethernet-1/1"))
        ethernet_1_2=int(grab_outpackets("ethernet-1/2"))
        
        _ethernet_1_1_counter.add((ethernet_1_1-ethernet_1_1_previous), {"result": "pass"})
        _ethernet_1_2_counter.add((ethernet_1_2-ethernet_1_1_previous), {"result": "pass"})
        
        ethernet_1_1_previous=ethernet_1_1
        ethernet_1_2_previous=ethernet_1_2
        
        time.sleep(5)
        



