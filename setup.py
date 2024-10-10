from blue_options import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup


setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.assets",
        f"{NAME}.help",
        f"{NAME}.host",
        f"{NAME}.list",
        f"{NAME}.logger",
        f"{NAME}.options",
        f"{NAME}.string",
        f"{NAME}.terminal",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            ".bash/**/*.sh",
            "assets/*",
        ],
    },
)
