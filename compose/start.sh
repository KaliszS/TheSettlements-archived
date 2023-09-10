#!/bin/bash

set -o allexport
source thesettlements-api/.env
set +o allexport

uvicorn app.main:app --reload