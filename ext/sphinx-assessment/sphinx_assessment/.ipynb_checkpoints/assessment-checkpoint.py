from docutils import nodes
from docutils.parsers.rst import directives, Directive

from sphinx.util import logging
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

import mchoice
import dragndrop
import fitb
import parsons

logger = logging.getLogger(__name__)


def init_numfig(app, config):
    """Initialize numfig"""

    config["numfig"] = True
    numfig_format = {"assessment": "Toetsvraag %s"}
    # Merge with current sphinx settings
    numfig_format.update(config.numfig_format)
    config.numfig_format = numfig_format


def setup(app):

    app.connect("config-inited", init_numfig)  # event order - 1

    mchoice.setup(app)
    dragndrop.setup(app)
    fitb.setup(app)
    parsons.setup(app)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
