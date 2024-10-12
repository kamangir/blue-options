#! /usr/bin/env bash

function abcli_source_path() {
    local path=$1

    if [[ "$path" == help ]]; then
        local options="ignore_error,~log"
        abcli_show_usage "abcli_source_path <path>$ABCUL[$options]" \
            "source <path>."
        return
    fi

    local options=$2
    local ignore_error=$(abcli_option_int "$options" ignore_error 0)
    local do_log=$(abcli_option_int "$options" log 0)

    if [[ ! -d "$path" ]]; then
        [[ "$ignore_error" == 0 ]] &&
            abcli_log_error "abcli_source_path: $path: path not found."
        return 1
    fi

    pushd $path >/dev/null

    local filename
    for filename in *.sh; do
        [[ "$do_log" == 1 ]] &&
            abcli_log "🔹 ${filename%.*}"

        source $filename
    done

    popd >/dev/null
}

function abcli_source_caller_suffix_path() {
    local suffix=$1

    if [[ "$suffix" == "help" ]]; then
        options="ignore_error,~log"
        abcli_show_usage "abcli_source_caller_suffix_path <suffix>$ABCUL[$options]" \
            "source <caller-path>/<suffix>."
        return
    fi

    local path=$(dirname "$(realpath "${BASH_SOURCE[1]}")")

    [[ ! -z "$suffix" ]] &&
        path=$path$suffix

    abcli_source_path "$path" \
        "${@:2}"
}
