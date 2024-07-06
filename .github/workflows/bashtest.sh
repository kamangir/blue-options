#! /usr/bin/env bash

function bashtest() {
    # set -x # verbose-mode

    source $(dirname $(dirname "$(realpath "${BASH_SOURCE[0]}")"))/blue_options/.bash/tests/option.sh

    ls

    echo "🪄"

    return
}

bashtest "$@"
