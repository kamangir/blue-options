from typing import List
import os

from blueness import module
from blue_options import NAME, env, fullname, string
from blue_options.logger import crash_report

NAME = module.name(__file__, NAME)


def get_name(cache: bool = True):
    if not cache or env.HOST_NAME is None:
        env.HOST_NAME = get_name_()

    return env.HOST_NAME


def get_name_() -> str:
    default = string.random(5)

    if is_docker():
        return os.getenv("abcli_container_id", default)

    if is_ec2():
        return os.getenv("abcli_ec2_instance_id", default)

    if is_jetson():
        return os.getenv("abcli_jetson_nano_serial_number", default)

    if is_ubuntu():
        return os.getenv("abcli_ubuntu_computer_id", default)

    if is_mac():
        return os.getenv("USER", default)

    if is_jupyter():
        return "Jupyter-Notebook"

    try:
        if is_rpi():
            # https://www.raspberrypi-spy.co.uk/2012/09/getting-your-raspberry-pi-serial-number-using-python/
            with open("/proc/cpuinfo", "r") as fp:
                for line in fp:
                    if line.startswith("Serial"):
                        return line[10:26]

        with open("/sys/firmware/devicetree/base/serial-number", "r") as fp:
            for line in fp:
                return line.strip().replace(chr(0), "")

    except:
        crash_report(f"-{NAME}: get_name(): failed.")

    return default


def get_seed_filename() -> str:
    return (
        "/media/abcli/SEED/abcli/jetson.sh"
        if is_jetson()
        else (
            "/Volumes/seed/abcli/ubuntu.sh"
            if is_ubuntu()
            else "/media/pi/SEED/abcli/rpi.sh" if is_rpi() else ""
        )
    )


def is_aws_batch() -> bool:
    return os.getenv("abcli_is_aws_batch", "false") == "true"


def is_docker() -> bool:
    return os.getenv("abcli_is_docker", "false") == "true"


def is_ec2() -> bool:
    return os.getenv("abcli_is_ec2", "false") == "true"


def is_github_workflow() -> bool:
    return os.getenv("abcli_is_github_workflow", "false") == "true"


def is_headless() -> bool:
    return os.getenv("abcli_is_headless", "false") == "true"


def is_jetson() -> bool:
    return os.getenv("abcli_is_jetson", "false") == "true"


# https://github.com/ultralytics/yolov5/blob/master/utils/general.py#LL79C18-L79C18
def is_jupyter() -> bool:
    # verified on Colab, Jupyterlab, Kaggle, Paperspace.
    try:
        from IPython import get_ipython

        return get_ipython() is not None
    except:
        return False


def is_mac() -> bool:
    return os.getenv("abcli_is_mac", "false") == "true"


def is_rpi() -> bool:
    return os.getenv("abcli_is_rpi", "false") == "true"


def is_ubuntu() -> bool:
    return os.getenv("abcli_is_ubuntu", "false") == "true"


def signature() -> List[str]:
    import platform

    return (
        [fullname()]
        + tensor_processing_signature()
        + [
            "Python {}".format(platform.python_version()),
            "{} {}".format(platform.system(), platform.release()),
            env.abcli_hostname,
            get_name(),
        ]
        + ([env.abcli_wifi_ssid] if env.abcli_wifi_ssid else [])
    )


def tensor_processing_signature() -> List[str]:
    output: List[str] = []

    try:
        import tensorflow  # type: ignore

        output += [f"TensorFlow {tensorflow.__version__}"]
    except:
        pass

    try:
        from tensorflow import keras  # type: ignore

        output += [f"Keras {keras.__version__}"]
    except:
        pass

    try:
        import tflite_runtime.interpreter as tflite  # type: ignore

        output += ["TensorFlow Lite"]
    except:
        pass

    try:
        import torch

        output += [f"torch-{torch.__version__}"]
    except:
        pass

    return output
