#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Modified version of https://github.com/ovh/python-ovh to fit with my API config
# Copyright (c) 2013-2017, OVH SAS.
# My modifications 2017, Fredrik Lundhag


from flask import Flask, request
import sys
import ovh

app = Flask(__name__)

# Get our config
app.config.from_object('config.DevelopmentConfig')


if '<' not in app.config['ENDPOINT']:
    print "You alread have a consumer key in config.py, exiting"
    sys.exit(1)

client = ovh.Client(
    endpoint = app.config['ENDPOINT'],
    application_key = app.config['KEY'],
    application_secret = app.config['SECRET'],
)

# Request RO, API access
ck = client.new_consumer_key_request()
ck.add_rules(ovh.API_READ_ONLY, "/*")

# Request token
validation = ck.request()

print "Please visit %s to authenticate" % validation['validationUrl']
raw_input("and press Enter to continue...")

# Print nice welcome message
print "Welcome", client.get('/me')['firstname']
print "Btw, your 'consumerKey' is '%s', please add it to CONSUMER in config.py" % validation['consumerKey']
