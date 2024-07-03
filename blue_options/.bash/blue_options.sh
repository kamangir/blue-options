#! /usr/bin/env bash

function blue_options() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blue_options version
        return
    fi

    abcli_generic_task \
        plugin=blue_options,task=$task \
        "${@:2}"
}

function blue_options_action_git_before_push() {
    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blue_options pypi build
}

python3 -m blue_options version \
    --show_icon 1
