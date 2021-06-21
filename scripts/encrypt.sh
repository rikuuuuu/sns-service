#!/usr/bin/env bash

APP_ROOT=$(dirname $0)/..


gcloud kms encrypt \
    --location=asia-northeast1 \
    --keyring=config \
    --key=snskey \
    --plaintext-file=${APP_ROOT}/.env \
    --ciphertext-file=${APP_ROOT}/.env.enc