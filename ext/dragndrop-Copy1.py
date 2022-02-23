from docutils import nodes
from docutils.parsers.rst import directives, Directive

from sphinx.util import logging
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

import random

logger = logging.getLogger(__name__)

def randomize (arr):
    length = len(arr)
    for a in range(length * 5):
        for i in range(length):
            x = random.randrange(0, length)
            y = random.randrange(0, length)
            arr[x], arr[y] = arr[y], arr[x] 

class dragndropnode(nodes.Admonition, nodes.Element):
    
    def __init__(self, **kwargs):
        logger.info("new-dragndropnode")
        super().__init__(**kwargs)

class DragndropQuestion(nodes.General, nodes.Element):
    pass

class DragndropSourceList(nodes.General, nodes.bullet_list):
    pass

class DragndropSourceItem(nodes.General, nodes.Element):
    pass

class DragndropTargetList(nodes.General, nodes.bullet_list):
    pass

class DragndropTargetItem(nodes.General, nodes.Element):
    pass

class DragndropDirective(SphinxDirective):
    has_content = True
    optional_arguments = 1    # title
    required_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "random": directives.flag,
    }
    
    def run(self):
        logger.info("run-dragndrop")
        
        title_node = nodes.title(text="Toetsvraag")
        
        # Parse custom subtitle option
        if self.arguments != []:
            subtitle = nodes.inline()
            subtitle_text = f" - {self.arguments[0]}"
            subtitle_nodes, _ = self.state.inline_text(subtitle_text, self.lineno)
            subtitle.extend(subtitle_nodes)
            title_node += subtitle

        content_node = nodes.section(ids=["question"])  # question-part
        self.state.nested_parse(self.content, self.content_offset, content_node)
        
        logger.info("content-length: {:d}".format(len(content_node)))
        
        if not(len(content_node) > 0 and isinstance(content_node[-1], nodes.bullet_list)):
            raise self.error("dragndrop: element list missing")

        bulletlist = content_node[-1]
        content_node.pop()                 # remove from content
        sourcelist = DragndropSourceList() # dit moet een node zijn....
        targetlist = DragndropTargetList() # idem
        
        itemnr = 0
        itemnames = "abcdefghijklmnopqrstuvwxyz"
        dragndropnr = self.env.new_serialno("dragndrop")
        logger.info("dragndrop-{}".format(dragndropnr))
        for item in bulletlist:
            if len(item) > 0 and isinstance(item[-1], nodes.bullet_list):
                logger.info("target item found")
                listitem = item[-1][0] # first item of sublist
                item.pop()             # remove sublist from original item        
#                if len(listitem) > 0 and isinstance(listitem[0], nodes.paragraph):
#                    listitem = listitem[0]
                targetitem = DragndropTargetItem(
                                 listitem.rawsource, 
                                 *listitem.children,
                                 **listitem.attributes)
                targetdata = itemnames[itemnr]
                targetitem["data-value"] = targetdata           
                targetlist.append(targetitem)  
            else:     # no target item
                targetdata = "dummy"
            
            logger.info("item letter: " + itemnames[itemnr])
#            if len(item) > 0 and isinstance(item[0], nodes.paragraph):
#                item = item[0]
             
            source = DragndropSourceItem(
                        item.rawsource,
                        *item.children,
                        **item.attributes)
            source["data-value"] = targetdata
            source["ids"].append("dragndrop-{}{}".format(dragndropnr, itemnames[itemnr]))    
            sourcelist.append(source)
            itemnr += 1

        randomize(sourcelist)
        
        dndnode = dragndropnode(rawsource=self.block_text)
        dndnode.source, dndnode.line = self.state_machine.get_source_and_line(self.lineno)

        dndnode.extend([title_node, content_node, sourcelist, targetlist])
        dndnode["dnd-title"] = self.arguments[0]

        return [dndnode]

def visit_dragndropnode (self, node):
    self.body.append('<div class="dragndrop admonition">')
    logger.info("visit-dragndropnode")    

def depart_dragndropnode (self, node):
    logger.info("depart-dragndropnode")
    self.body.append('<button class="dndcheckbutton">Check</button>')
    self.body.append('</div>\n')

def visit_dndquestion (self, node):
    self.body.append('<div class="dndquestion">\n')

def depart_dndquestion (self, node):
    self.body.append('</div>\n')

def visit_dndsourceitem (self, node):
    self.body.append('<div class="dndsourceitem" draggable="true" id="{id}" data-value="{a}">\n'.format(a=node["data-value"], id=node["ids"][0]))

def depart_dndsourceitem (self, node):
    self.body.append('</div>\n');   

def visit_dndsourcelist (self, node):
    self.body.append('<div class="dndcontainer">\n  <div class="dndsourcelist" data-value="dummy">\n')

def depart_dndsourcelist (self, node):
    self.body.append('</div>\n');   

def visit_dndtargetitem (self, node):
    self.body.append('<div class="dndtargetitem" id="dndtarget-{a}" data-value="{a}">\n'.format(a=node["data-value"]))

def depart_dndtargetitem (self, node):
    self.body.append('</div>\n')

def visit_dndtargetlist (self, node):
    self.body.append('  <div class="dndtargetlist">\n')

def depart_dndtargetlist (self, node):
    self.body.append('  </div>\n</div>\n')                      

def setup(app):
    logger.info("setup-dragndrop")
    
    app.add_js_file("js/dragndrop.js")
    
    app.add_directive("dragndrop", DragndropDirective)
    
    app.add_node(dragndropnode, html=(visit_dragndropnode, depart_dragndropnode))
    app.add_node(DragndropQuestion, html=(visit_dndquestion, depart_dndquestion) )
    app.add_node(DragndropSourceItem, html=(visit_dndsourceitem, depart_dndsourceitem))
    app.add_node(DragndropSourceList, html=(visit_dndsourcelist, depart_dndsourcelist))
    app.add_node(DragndropTargetList, html=(visit_dndtargetlist, depart_dndtargetlist))
    app.add_node(DragndropTargetItem, html=(visit_dndtargetitem, depart_dndtargetitem))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
