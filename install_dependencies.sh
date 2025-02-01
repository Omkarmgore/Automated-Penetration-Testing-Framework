#!/bin/bash

# Update package list
sudo apt-get update

# Install system requirements
sudo apt-get install -y \
    nmap \
    nikto \
    hydra \
    python3-pip \
    python3-dev \
    libffi-dev \
    libssl-dev \
    xdg-utils

# Install Python requirements
pip3 install -r requirements.txt

# Create necessary directories
mkdir -p reports scans
chmod 700 reports scans
