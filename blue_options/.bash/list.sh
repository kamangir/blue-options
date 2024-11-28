#! /usr/bin/env bash

function abcli_list() {
    local task=$1

    local function_name=abcli_list_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m blue_options.list "$@"
}

function abcli_list_filter() {
    python3 -m blue_options.list \
        filter \
        --items "$1" \
        "${@:2}"
}

function abcli_list_in() {
    python3 -m blue_options.list \
        in \
        --item "$1" \
        --items "$2" \
        "${@:3}"
}

function abcli_list_intersect() {
    python3 -m blue_options.list \
        intersect \
        --items_1 "$1" \
        --items_2 "$2" \
        "${@:3}"
}

function abcli_list_item() {
    python3 -m blue_options.list \
        item \
        --items "$1" \
        --index "$2" \
        "${@:3}"
}

function abcli_list_len() {
    python3 -m blue_options.list \
        len \
        --items "$1" \
        "${@:2}"
}

function abcli_list_log() {
    abcli_log_list "$@"
}

function abcli_list_next() {
    python3 -m blue_options.list \
        next \
        --item "$1" \
        --items "$2" \
        "${@:3}"
}

function abcli_list_prev() {
    python3 -m blue_options.list \
        prev \
        --item "$1" \
        --items "$2" \
        "${@:3}"
}

function abcli_list_nonempty() {
    python3 -m blue_options.list \
        nonempty \
        --items "$1" \
        "${@:2}"
}

function abcli_list_resize() {
    python3 -m blue_options.list \
        resize \
        --items "$1" \
        --count "$2" \
        "${@:3}"
}

function abcli_list_sort() {
    python3 -m blue_options.list \
        sort \
        --items "$1" \
        "${@:2}"
}
