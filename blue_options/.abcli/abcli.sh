#! /usr/bin/env bash

abcli_source_path - caller,suffix=/tests

abcli_env dot load \
    plugin=blue_options
abcli_env dot load \
    filename=blue_options/config.env,plugin=blue_options


