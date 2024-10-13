#! /usr/bin/env bash

function abcli_assert() {
    local value=$1
    local expected_value=$2
    local sign=${3:-yes}

    local function_name="${FUNCNAME[1]}"

    if [[ "$sign" == "empty" ]]; then
        if [[ -z "$value" ]]; then
            abcli_log "✅ $function_name: $value is empty."
            return
        fi

        abcli_log_error "$function_name: non-empty value."
        return 1
    fi

    if [[ "$sign" == "non-empty" ]]; then
        if [[ ! -z "$value" ]]; then
            abcli_log "✅ $function_name: $value is non-empty."
            return
        fi

        abcli_log_error "$function_name: empty value."
        return 1
    fi

    if [[ "$sign" == "yes" ]]; then
        if [[ "$value" == "$expected_value" ]]; then
            abcli_log "✅ $function_name: $value == $expected_value."
            return
        fi

        abcli_log_error "$function_name: $value != $expected_value"
        return 1
    else
        if [[ "$value" != "$expected_value" ]]; then
            abcli_log "✅ $function_name: $value != $expected_value."
            return
        fi

        abcli_log_error "$function_name: $value == $expected_value"
        return 1
    fi
}

function abcli_assert_file_exists() {
    local filename=$1

    local function_name="${FUNCNAME[1]}"

    if [[ -f "$filename" ]]; then
        abcli_log "✅ $function_name: $filename - file exists."
        return 0
    fi

    abcli_log_error "$function_name: $filename - file not found."
    return 1
}

function abcli_assert_list() {
    abcli_assert \
        $(abcli_list_sort "$1") \
        $(abcli_list_sort "$2")
}
