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

which is equivalent, in json notation, to,

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

for more refer to 🔻 [giza](https://github.com/kamangir/giza).

## installation

```bash
pip install blue_options
```

add this line to your `~/.bash_profile` or `~/.bashrc`,

```bash
source $(python -m blue_options locate)/.bash/blue_options.sh
```

## usage

let your function receive an `options` argument, then parse it with `abcli_options` and `abcli_options_int`.

```bash
function func() {
    local options=$1

    local var=$(abcli_options "$options" var default)
    local key=$(abcli_options_int "$options" key 0)

    [[ "$key" == 1 ]] &&
        echo "var=$var"
}
```

## example 1

from [reddit](https://www.reddit.com/r/bash/comments/1duw6ac/how_can_i_automate_these_tree_commands_i/)

> How can I automate these tree commands I frequently need to type out?
I would like to run:
```bash
git add .
git commit -m "Initial "commit"
git push
```
> I got bored of typing them out each time. Can I make an alias or something like "gc" (for git commit). The commit message is always the same "Initial commit".

first, install `blue-options`. this will also install [`blueness`](https://github.com/kamangir/blueness).

```bash
pip install blue_options
```

then, copy [`example1.sh`](./blue_options/assets/example1.sh) to your machine and add this line to the end of your `bash_profile`,

```bash
source <path/to/example1.sh>
```

now, you have access to the `@git` super command. here is how it works.

1. `@git help` shows usage instructions (see below).
1. `@git commit` runs the three commands. you can customize the message by running `@git commit <message>`. you can also avoid the push by running `@git commit <message> ~push`.
1. for any `<task>` other than `commit`, `@git <task> <args>` runs `git <task> <args>`.

```
 > @git help
 @git commit [<message>] \
	~push
 . git commit with <message> and push.
@git <command>
 . git <command>.
 ```

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-options/example1.png)

---

[![pylint](https://github.com/kamangir/blue-options/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/blue-options/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/blue-options/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/blue-options/actions/workflows/pytest.yml) [![PyPI version](https://img.shields.io/pypi/v/blue-options.svg)](https://pypi.org/project/blue-options/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/blue-options)](https://pypistats.org/packages/blue-options)
