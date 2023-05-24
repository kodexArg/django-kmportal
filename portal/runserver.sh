#!/bin/bash

python manage.py runserver 0.0.0.0:8000 &

./tailwind.sh &

read -rsn1 key
while [[ $key != $'\e' ]]; do
    read -rsn1 key
done

pkill -P $$  # Kill child processes
kill $$      # Kill the current script

