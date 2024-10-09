#! /usr/bin/env bash

function abcli_source_path() {
    local path=$1

    if [[ "$path" == help ]]; then
        local options="ignore_error,~log"
        abcli_show_usage "abcli_source_path <path> [$options]" \
            "source <path>."

        options="$options,caller,suffix=/tests"
        abcli_show_usage "abcli_source_path - [$options]" \
            "source caller path."
        return
    fi

    local options=$2
    local ignore_error=$(abcli_option_int "$options" ignore_error 0)
    local use_caller=$(abcli_option_int "$options" caller 0)
    local do_log=$(abcli_option_int "$options" log 0)
    local suffix=$(abcli_option "$options" suffix)

    [[ "$use_caller" == 1 ]] &&
        path=$(dirname "$(realpath "${BASH_SOURCE[1]}")")

    [[ ! -z "$suffix" ]] &&
        path=$path$suffix

    if [[ ! -d "$path" ]]; then
        [[ "$ignore_error" == 0 ]] &&
            abcli_log_error "abcli: source_path: $path: path not found."
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
