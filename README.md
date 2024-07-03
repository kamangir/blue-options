# 🌀 blue_options

🌀 `blue_options` implements an `options` for Bash. 

## installation

```bash
pip install blue_options
```

add this line to your `~/.bash_profile` or `~/.bashrc`,

```bash
source $(python -m blue_options locate)/.bash/blue_options.sh
```

## use

```bash
function func() {
    local options=$1

    local var=$(abcli_options "$options" var default)
    local key=$(abcli_options_int "$options" key 0)

    [[ "$key" == 1 ]] &&
        echo "var=$var"
}
```

---

[![PyPI version](https://img.shields.io/pypi/v/blue_options.svg)](https://pypi.org/project/blue_options/)
