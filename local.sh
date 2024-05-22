#!/bin/bash

python3.11 -m venv venv --prompt metric-api-app
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8080