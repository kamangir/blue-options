#! /usr/bin/env bash

function abcli_pause() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local message=$(abcli_option "$options" message "press any key to continue...")
    message=$(echo $message | tr - " ")
    abcli_log "$message"

    if [[ "$do_dryrun" = 0 ]]; then
        read -p ""
    fi
}
