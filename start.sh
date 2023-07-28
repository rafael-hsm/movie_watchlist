#!/bin/bash
gunicorn movie_library:app -b 0.0.0.0:$PORT --timeout 600