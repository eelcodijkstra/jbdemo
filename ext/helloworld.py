from docutils import nodes
from docutils.parsers.rst import directives, Directive  # type: ignore

from sphinx.util import logging

class HelloWorld(Directive):
    has_content = True
    optional_arguments = 2
    required_arguments = 1
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
    }

    def run(self):
        logger = logging.getLogger(__name__)
        logger.info("run-helloword")
 
        args_node = nodes.paragraph(text=self.arguments)
        opts_node = nodes.paragraph(text=self.options)
        
        paragraph_node = nodes.paragraph(text='Hello World!')

        content_node = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, content_node)
      
        
        return [paragraph_node, args_node, opts_node, content_node]


def setup(app):
    logger = logging.getLogger(__name__)
    logger.info("setup-helloword")
    
    app.add_directive("helloworld", HelloWorld)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }