#! /usr/bin/env bash

function abcli_show_usage_2() {
    local module=$1
    local command="${@:2}"

    python3 -m $module.help \
        --command "$command"
}
