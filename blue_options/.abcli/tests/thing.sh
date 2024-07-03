#! /usr/bin/env bash

function test_blue_options_thing() {
    local options=$1

    local test_options=$2

    abcli_eval ,$options \
        "echo 📜 blue-options: test: thing: $test_options: ${@:3}."
}


