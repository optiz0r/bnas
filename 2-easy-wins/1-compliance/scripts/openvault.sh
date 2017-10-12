#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
gpg2 --batch --use-agent --decrypt ${DIR}/../secrets/vault_passphrase.gpg
