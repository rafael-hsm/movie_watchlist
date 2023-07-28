#!/bin/bash
gunicorn movie_library:create_app --bind 0.0.0.0:8000