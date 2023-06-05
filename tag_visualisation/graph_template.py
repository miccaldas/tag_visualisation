"""
This module will produce a file template to generate
files that'll run Streamlit's Graphviz widgets.
"""
import snoop
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def template_creation(edge_list, answr):
    """
    Creates the template for the file that'll
    generate the code for the Streamlit app.
    """
    inst = f"/home/mic/python/tag_visualisation/tag_visualisation/{answr}_graph.py"

    with open(inst, "w") as d:
        d.write('"')
        d.write('"')
        d.write('"\n')
        d.write("This is an instantiated file from 'graph_template' and it'll create a graph\n")
        d.write(f"of all relations of the '{answr}' tag in the Note's app.\n")
        d.write('"')
        d.write('"')
        d.write('"\n')
        d.write("import snoop\n")
        d.write("from snoop import pp\n")
        d.write("import graphviz\n")
        d.write("import streamlit as st\n\n\n")
        d.write("def type_watch(source, value):\n")
        d.write("    return f'type({source})', type(value)\n\n\n")
        d.write("@snoop\n")
        d.write("def template():\n")
        d.write('    "')
        d.write('"')
        d.write('"\n')
        d.write("    We'll map each tuple item as one node, and produce an undirected graph.\n")
        d.write('    "')
        d.write('"')
        d.write('"\n')
        d.write("    gr = graphviz.Graph(format='png')\n")
        for i in edge_list:
            d.write(f"    gr.edge('{i[0]}', '{i[1]}')\n")
        d.write("\n")
        d.write(f"    gr.render(filename='{answr}', view=True, outfile='{answr}.png')\n\n\n")
        d.write('if __name__ == "__main__":\n')
        d.write("    template()")


if __name__ == "__main__":
    template_creation()
