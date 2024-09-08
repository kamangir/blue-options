import os

ABCUL = " \\\n\t"


abcli_log_filename = os.getenv(
    "abcli_log_filename",
    "",
)


CYAN = os.getenv("CYAN", "")
GREEN = os.getenv("GREEN", "")
NC = os.getenv("NC", "")
