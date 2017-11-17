#!/usr/bin/env bash
set -e 

#. ~/.virtualenvs/python2.7/bin/activate

virtualenv ci

. ci/python2.7/bin/activate

./test.py
