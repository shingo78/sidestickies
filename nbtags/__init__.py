from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join
from . import handler


# nbextension
def _jupyter_nbextension_paths():
    return [dict(
        section='notebook',
        src='nbextension',
        dest='nbtags',
        require='nbtags/main')]


# server extension
def _jupyter_server_extension_paths():
    return [dict(
        module='nbtags'
    )]


def load_jupyter_server_extension(nb_app):
    nb_app.log.info('Loaded server extension nbtags')

    c_route_pattern = url_path_join(nb_app.web_app.settings['base_url'],
                                    r'/nbtags/tags/(?P<meme>[A-Za-z0-9\-]+)')

    nb_app.web_app.add_handlers(host_pattern, [
        (c_route_pattern, handler.CellTagsHandler, dict(nb_app=nb_app))
    ])