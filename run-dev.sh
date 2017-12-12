#!/bin/bash

source flask/bin/activate

gunicorn app:app --bind=0.0.0.0:5001
