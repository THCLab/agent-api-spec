#!/bin/bash 
BASEDIR=$(dirname "$0")
swagger-marshmallow-codegen $BASEDIR/swagger-spec.yaml > $1generated_models.py
