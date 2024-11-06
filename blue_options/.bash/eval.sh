#! /usr/bin/env bash

function abcli_eval() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_log=$(abcli_option_int "$options" log 1)
    local path=$(abcli_option "$options" path ./)

    [[ "$path" != "./" ]] && mkdir -pv $path

    local command_line="${@:2}"

    if [[ "$do_log" == 1 ]]; then
        abcli_log "⚙️  $command_line"
        [[ "$path" != "./" ]] && abcli_log " 📂 $path"
    fi

    [[ "$do_dryrun" == 1 ]] && return

    [[ "$path" != "./" ]] && pushd $path >/dev/null

    eval "$command_line"
    local status="$?"

    [[ "$path" != "./" ]] && popd >/dev/null

    if [[ $status -ne 0 ]]; then
        abcli_log_error "@eval: failed: status=$status: $command_line"
        return 1
    fi

    return 0
}
