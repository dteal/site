#!/bin/bash

# Will, assuming correct permissions, build and deploy the site.
# Define the environment variable DTEAL_SITE to be username@server.

python3 ./site.py
ssh $DTEAL_SITE rm -rf dteal.org/*
rsync -rlz --partial --info=progress2 -e "ssh" bin/ $DTEAL_SITE:~/dteal.org/
bash -c "read -p \"continue to set permissions...\""
ssh $DTEAL_SITE "chmod -R 755 dteal.org/*"