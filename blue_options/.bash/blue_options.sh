#! /usr/bin/env bash

function blue_options() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blue_options version
        return
    fi

    abcli_generic_task \
        plugin=blue_options,task=$task \
        "${@:2}"
}

function blue_options_action_git_before_push() {
    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blue_options pypi build
}

python3 -m blue_options version \
    --show_icon 1

source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/options.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/source.sh

source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/browse.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/env.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/eval.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/generic_task.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/install.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/list.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/logging.sh
source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/string.sh

source $(dirname "$(realpath "${BASH_SOURCE[0]}")")/alias.sh
