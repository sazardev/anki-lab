# Jupyter server configuration for the Algebra Lab on Omarchy.
#
# Install to ~/.jupyter/jupyter_server_config.py
#
# The server binds to 127.0.0.1 only, so it is unreachable from the network.
# That is what makes it safe to leave the token empty: the launcher can then
# build the notebook URL itself and open it without scraping a token out of the
# log. If you ever change ServerApp.ip to 0.0.0.0, set a real token first.
#
# Adjust LAB_DIR below if you cloned the repo somewhere other than
# ~/Work/anki-lab. install.sh does this for you.

import os

LAB_DIR = os.environ.get("ALGEBRA_LAB_DIR", "~/Work/anki-lab/algebra-lab")
LAB_DIR = os.path.expanduser(LAB_DIR)

c.ServerApp.ip = "127.0.0.1"
c.IdentityProvider.token = ""
c.ServerApp.open_browser = False
c.ServerApp.root_dir = LAB_DIR
c.ServerApp.allow_origin = ""
c.ServerApp.disable_check_xsrf = False

# Land straight on the lab notebook.
c.ServerApp.default_url = "/lab/tree/Algebra_Lab.ipynb"
