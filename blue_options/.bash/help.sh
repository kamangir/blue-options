#! /usr/bin/env bash

function abcli_help() {
    local callable=$1
    if [[ -z "$callable" ]]; then
        abcli_version
        return
    fi

    if alias "$callable" &>/dev/null; then
        callable=$(alias "$callable" | sed -E "s/^alias $callable='(.*)'$/\1/")
    fi

    local module=$(python3 -m blue_options.help \
        get_module \
        --callable "$callable")

    local suffix=$(python3 -m blue_options.help \
        get_suffix \
        --callable "$callable")

    local command="${@:2}"

    python3 -m $module.help \
        --command "$suffix $command"
}
