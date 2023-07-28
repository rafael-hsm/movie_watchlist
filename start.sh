#!/bin/bash
gunicorn -c gunicorn.py "app:create_app()"
