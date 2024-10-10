#! /usr/bin/env bash

function abcli_browse() {
    local url=$1
    local description=$2

    if [[ "$url" == "help" ]]; then
        abcli_show_usage "@browse <url>$ABCUL[<description>]" \
            "browse <url>."
        return
    fi

    [[ ! -z "$description" ]] &&
        abcli_log "$description"

    abcli_log "🔗 $url"
    if [ "$abcli_is_mac" == true ]; then
        open "$url"
    elif [ "$abcli_is_ec2" == true ]; then
        firefox "$url"
    elif [ "$abcli_is_rpi" == true ]; then
        DISPLAY=:0 chromium-browser -kiosk --no-sandbox "$url"
    else
        abcli_log_warning "@browse: $url: skipped."
    fi
}
