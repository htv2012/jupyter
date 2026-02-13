#!/usr/bin/env bash

SERVICE_NAME=python_notebooks

sudo cp ./${SERVICE_NAME}.service /etc/systemd/system
sudo systemctl enable ${SERVICE_NAME}
sudo systemctl start ${SERVICE_NAME}

