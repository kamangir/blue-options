#! /usr/bin/env bash

function blue_options() {
    echo "🪄"
}

function blue_options_action_git_before_push() {
    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blue_options pypi build
}

python3 -m blue_options version \
    --show_icon 1
