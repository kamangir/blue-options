#! /usr/bin/env bash

export abcli_is_colorful=true

alias @git=my_git

source $(python -m blue_options locate)/.bash/blue_options.sh

function my_git() {
    local task=${1:help}

    if [[ "$task" == "help" ]]; then
        abcli_show_usage "@git commit [<message>]$ABCUL$EOP~push$EOPE" \
            "git commit with <message> and push."

        abcli_show_usage "@git <command>" \
            "git <command>."
        return
    fi

    if [[ "$task" == "commit" ]]; then
        local message=${1:-"Initial commit"}

        local options=$2
        local do_push=$(abcli_options_int "$options" push 1)

        git add .

        git commit -m "$message"

        [[ "$do_push" == 1 ]] && git push

        return 0
    fi

    git "$@"
}
