#! /usr/bin/env bash

export abcli_path_env_backup=$HOME/env-backup
mkdir -pv $abcli_path_env_backup

function abcli_env() {
    local task=$(abcli_unpack_keyword $1)

    local function_name="abcli_env_$1"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    local command_line="env"
    for arg in "$@"; do
        command_line+=" | grep '$arg'"
    done
    command_line+=" | sort"
    abcli_eval - \
        "$command_line"
}

abcli_source_caller_suffix_path /env
