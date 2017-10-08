#!/usr/bin/env bash

ME=$(basename $0)
BASE=$(readlink -f $(dirname $0)/..)

VENV_DIR=${VENV_DIR:-$BASE/venv}

${VENV_DIR}/bin/python3 ${BASE}/app/app.py

