#!/usr/bin/env bash

ME=$(basename $0)
BASE=$(readlink -f $(dirname $0)/..)

err(){ echo "$@" 1>&2; }

VENV_DIR=${VENV_DIR:-$BASE/venv}

[[ -d ${VENV_DIR} ]] && rm -rf ${VENV_DIR}

#PATH=${DEPLOYER_PYTHON_PATH}:-/usr/bin/python3}:$PATH -m venv $VENV_DIR

python3 -m venv $VENV_DIR

${VENV_DIR}/bin/pip install --upgrade pip

[[ -f ${BASE}/requirements.txt ]] && ${VENV_DIR}/bin/pip --no-cache-dir install --upgrade -r requirements.txt


