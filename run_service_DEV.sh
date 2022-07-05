#!/bin/bash

# shellcheck disable=SC2164
cd "C:\Users\Luis Sulbaran\PycharmProjects\output_final"

pip install -r requirements.txt

source venv/Scripts/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run