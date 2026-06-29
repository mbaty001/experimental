#!/usr/bin/env bash
set -x

if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    uv run flask --env-file .env db init
fi
echo --------------------
echo Generate migration DDL code
echo --------------------
uv run flask --env-file .env db migrate
echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
uv run flask --env-file .env db upgrade

