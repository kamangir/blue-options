#! /usr/bin/env bash

function abcli_wait() {
    local message=$1
    [[ -z "$message" ]] &&
        message="Continue?"

    while true; do
        local user_input
        read -p "$message Y/N: " -n 1 -r user_input
        echo # Move to a new line

        case $user_input in
        [Yy])
            return 0
            ;;
        [Nn])
            abcli_log_warning "Aborted."
            return 1
            ;;
        *)
            echo "Invalid input, please enter Y or N."
            ;;
        esac
    done
}
