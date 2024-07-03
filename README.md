# 🌀 blue-options

🌀 `blue_options` implements an `options` argument for Bash.

here is an example use of an `options` in the [vancouver-watching 🌈](https://github.com/kamangir/vancouver-watching) ingest command:


```bash
 > vanwatch help
vanwatch ingest \
	area=<vancouver>,~batch,count=<-1>,dryrun,gif,model=<model-id>,~process,publish,~upload \
	-|<object-name> \
	[<args>]
 . ingest <area> -> <object-name>.
```

this command takes in an `options`, an `object`, and `args`. an `options` is a string representation of a dictionary, such as,

```bash
area=<vancouver>,~batch,count=<-1>,dryrun,gif,model=<model-id>,~process,publish,~upload
```

or in json notation,
```json
{
    "area": "vancouver",
    "batch": false,
    "count": -1,
    "dryrun": true,
    "gif": true,
    "model": "<model-id>",
    "process": false,
    "publish": true,
    "upload": false,
}
```

for more refer to [🔻 giza](https://github.com/kamangir/giza).

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
