"""
nbprocusage init
"""

from notebook.utils import url_path_join
from .handler import ResourceUsageHandler


def _jupyter_server_extension_paths():
    return [{
        "module": "nbprocusage"
    }]


# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [
        dict(
            section="notebook",
            dest="nbprocusage",
            src="static",
            require="nbprocusage/main"
        )
    ]


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.
    Args:
        nb_server_app (NotebookWebApplication):
        handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/resource')
    web_app.add_handlers(host_pattern, [(route_pattern, ResourceUsageHandler)])
