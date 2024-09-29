#! /usr/bin/env bash

# wrap-around
export ABCUL=" \\\\\n\t"
export ABCUL2=" \n   "
export ABCUL3=" \n      "

# https://chatgpt.com/share/d354d916-3003-4a6d-84f3-5c51a59ed4b1
function xwrap {
    local output=""
    for arg in "$@"; do
        output+="${ABCUL}[${arg}]"
    done
    echo "$output"
}

# extra options
export EOP=$YELLOW
export EOPE=$LIGHTBLUE
export EARGS="$ABCUL$EOP[<args>]$EOPE"

function xtra() {
    echo "$EOP$*$EOPE"
}

if [[ "$abcli_is_colorful" == true ]]; then
    export BLUE='\033[1;34m'
    export LIGHTBLUE='\033[1;96m'
    export CYAN='\033[0;36m'
    export GREEN='\033[0;32m'
    export NC='\033[0m'
    export RED='\033[0;31m'
    export YELLOW='\033[0;33m'
else
    unset BLUE LIGHTBLUE CYAN GREEN NC RED YELLOW
fi

function abcli_cat() {
    local filename=${1:-help}

    if [ "$filename" == "help" ]; then
        abcli_show_usage "@cat <filename>" \
            "log <filename>."
        return
    fi

    if [ ! -f "$filename" ]; then
        abcli_log_error "@cat: $filename: file not found."
        return 1
    fi

    printf "🗒️  $YELLOW$filename$NC\n$BLUE"
    cat $filename
    printf "$NC\n🗒️  $YELLOW/$filename$NC\n"
}

function abcli_hr() {
    local width=80
    [[ "$abcli_is_github_workflow" == false ]] &&
        [[ "$abcli_is_aws_batch" == false ]] &&
        width=$(tput cols)

    python3 -m blue_options.terminal hr \
        --width $width
}

function abcli_log_list() {
    local items=$1

    if [[ "$items" == "help" ]]; then
        local args="[--before \"list of\"]$ABCUL[--after \"items(s)\"]$ABCUL[--delim space|<delim>]"
        abcli_show_usage "abcli_log_list <this,that>$ABCUL$EOP$args$EOPE" \
            "log list."
        return
    fi

    local message=$(python3 -m blue_options.list \
        log \
        --items "$items" \
        "${@:2}")
    printf "$message\n"
}

function abcli_log_local() {
    local message="$@"
    printf "$CYAN$message$NC\n"
}

function abcli_show_usage() {
    local what=$1

    if [ "$what" == "prefix" ]; then
        local prefix=$2

        local function_name
        # https://stackoverflow.com/a/2627461/17619982
        for function_name in $(compgen -A function $prefix); do
            $function_name "${@:3}"
        done
        return
    fi

    local command=$1
    local description=$2
    local comments=$3

    if [[ ! -z "$abcli_show_usage_destination" ]]; then
        echo "- - $command" >>$abcli_show_usage_destination
        echo "  - $description" >>$abcli_show_usage_destination
        return
    fi

    printf "${LIGHTBLUE}$command${NC}\n"
    [[ ! -z "$description" ]] &&
        printf "${CYAN} . $description${NC}\n"
    [[ ! -z "$comments" ]] &&
        printf "${GREEN} * $comments${NC}\n"

    return 0
}

function abcli_show_usage_2() {
    local module=$1
    local command="${@:2}"

    python3 -m $module.help \
        --command "$command"
}
