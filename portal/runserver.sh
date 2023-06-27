#!/bin/bash

gunicorn portal.wsgi:application --bind 0.0.0.0:8080

