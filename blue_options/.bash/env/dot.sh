#! /usr/bin/env bash

function abcli_env_dot() {
    local task=${1:-cat}
    [[ "$task" == "copy" ]] && task="cp"

    local function_name="abcli_env_dot_$task"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "get" ]; then
        pushd $abcli_path_abcli >/dev/null
        dotenv get "${@:2}"
        popd >/dev/null
        return
    fi

    if [[ "$task" == "list" ]]; then
        abcli_ls $abcli_path_assets/env/
        return
    fi

    if [ "$task" == "set" ]; then
        pushd $abcli_path_abcli >/dev/null
        dotenv set "${@:2}"
        popd >/dev/null
        return
    fi

    abcli_log_error "@env: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /dot
