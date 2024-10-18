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
    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    blue_options pypi build
}

python3 -m blue_options version \
    --show_icon 1

function blue_options_source_dependencies() {
    local path=$1

    source $path/options.sh
    source $path/source.sh

    source $path/assert.sh
    source $path/bool.sh
    source $path/browse.sh
    source $path/code.sh
    source $path/env.sh
    source $path/eval.sh
    source $path/generic_task.sh
    source $path/install.sh
    source $path/list.sh
    source $path/logging.sh
    source $path/open.sh
    source $path/pause.sh
    source $path/plugins.sh
    source $path/pylint.sh
    source $path/pytest.sh
    source $path/string.sh
    source $path/terminal.sh
    source $path/test.sh

    source $path/alias.sh
}

blue_options_source_dependencies $(dirname "$(realpath "${BASH_SOURCE[0]}")")
