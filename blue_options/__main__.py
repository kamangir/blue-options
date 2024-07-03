from blue_options import NAME, VERSION, DESCRIPTION, ICON
from blueness.argparse.generic import main

success, message = main(__file__, NAME, VERSION, DESCRIPTION, ICON)
if not success:
    print(f"❗️ {message}")
