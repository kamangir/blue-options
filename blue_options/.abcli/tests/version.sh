#! /usr/bin/env bash

function test_blue_options_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_options version ${@:2}"

    return 0
}


