#!/bin/bash

set -o allexport
source thesettlements-api/.env
set +o allexport

docker run --rm --name neo4j -e NEO4J_AUTH -p 7474:7474 -p 7687:7687 -d neo4j:latest
