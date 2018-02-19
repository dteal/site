#!/bin/bash

# Will, assuming correct permissions, deploy the site.
# Define the environment variable QAUTE_USER to be the username.

set -o nounset
set -o errexit

_die () { err_code=$1; shift 1; echo $@ >&2; exit $err_code; }

rsync -rlz --delete --partial --info=progress2 -e "ssh" * \
    ${QAUTE_USER}@hactar.dreamhost.com:~/qaute.com || \
    _die 2 "Failed to upload website"
