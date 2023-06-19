#!/bin/bash

while true; do
    python manage.py runserver 0.0.0.0:8080

    if [[ "$?" != "0" ]]; then
        echo "Server crashed with exit code $?.  Respawning.." >&2
        sleep 3
    else
        break
    fi
done

