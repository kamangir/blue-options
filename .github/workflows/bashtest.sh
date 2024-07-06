#! /usr/bin/env bash

function bashtest() {
    # set -x # verbose-mode

    ls $(pwd)/blue-options/blue_options/.bash/tests/option.sh

    echo "🪄"

    return
}

bashtest "$@"
