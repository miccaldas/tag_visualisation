"""
This is an instantiated file from 'graph_template' and it'll create a graph
of all relations of the 'black' tag in the Note's app.
"""
import graphviz
import snoop
import streamlit as st
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


@snoop
def template():
    """
    We'll map each tuple item as one node, and produce an undirected graph.
    """
    gr = graphviz.Graph(format="png")
    gr.edge("vim", "hidden")
    gr.edge("vim", "characters")
    gr.edge("hidden", "characters")
    gr.edge("vim", "clipboard")
    gr.edge("vim", "ssh")
    gr.edge("clipboard", "ssh")
    gr.edge("vim", "auto format")
    gr.edge("vim", "formatting")
    gr.edge("auto format", "formatting")
    gr.edge("vim", "commentary")
    gr.edge("vim", "comment")
    gr.edge("commentary", "comment")
    gr.edge("php", "keybind")
    gr.edge("php", "vim")
    gr.edge("keybind", "vim")
    gr.edge("vim", "repeats")
    gr.edge("vim", "string")
    gr.edge("repeats", "string")
    gr.edge("vim", "find")
    gr.edge("vim", "replace")
    gr.edge("find", "replace")
    gr.edge("spelling", "vim")
    gr.edge("spelling", "spell")
    gr.edge("vim", "spell")
    gr.edge("vim", "open")
    gr.edge("vim", "files")
    gr.edge("open", "files")
    gr.edge("vim", "spellcheck")
    gr.edge("vim", "spelling")
    gr.edge("spellcheck", "spelling")
    gr.edge("vim", "paste")
    gr.edge("vim", "copy")
    gr.edge("paste", "copy")
    gr.edge("vim", "columns")
    gr.edge("vim", "len")
    gr.edge("columns", "len")
    gr.edge("vim", "ale")
    gr.edge("vim", "linter")
    gr.edge("ale", "linter")
    gr.edge("vim", "current file")
    gr.edge("vim", "files")
    gr.edge("current file", "files")
    gr.edge("vim", "comment")
    gr.edge("vim", "plugin")
    gr.edge("comment", "plugin")
    gr.edge("vim", "install")
    gr.edge("vim", "clipboard")
    gr.edge("install", "clipboard")
    gr.edge("vim", "configuration")
    gr.edge("vim", "clipboard")
    gr.edge("configuration", "clipboard")
    gr.edge("vim", "formatting")
    gr.edge("vim", "html")
    gr.edge("formatting", "html")
    gr.edge("vim", "quotes")
    gr.edge("vim", "apostrophes")
    gr.edge("quotes", "apostrophes")
    gr.edge("line break", "unix")
    gr.edge("line break", "vim")
    gr.edge("unix", "vim")
    gr.edge("vim", "argument")
    gr.edge("vim", "files")
    gr.edge("argument", "files")
    gr.edge("vim", "json")
    gr.edge("vim", "format")
    gr.edge("json", "format")
    gr.edge("vim", "multiline")
    gr.edge("vim", "repeat")
    gr.edge("multiline", "repeat")
    gr.edge("Vim", "eol")
    gr.edge("Vim", "od")
    gr.edge("eol", "od")
    gr.edge("Vim", "comment")
    gr.edge("Vim", "uncomment")
    gr.edge("comment", "uncomment")
    gr.edge("reusable_files", "insert")
    gr.edge("reusable_files", "command")
    gr.edge("insert", "command")
    gr.edge("Vim", "folders")
    gr.edge("Vim", "file explorer")
    gr.edge("folders", "file explorer")
    gr.edge("partials", "CONFIGS")
    gr.edge("partials", "partials")
    gr.edge("CONFIGS", "partials")
    gr.edge("vim", "limit")
    gr.edge("vim", "length")
    gr.edge("limit", "length")
    gr.edge("markdown", "plugin")
    gr.edge("markdown", "instant-markdown")
    gr.edge("plugin", "instant-markdown")
    gr.edge("black", "vim")
    gr.edge("black", "formatter")
    gr.edge("vim", "formatter")
    gr.edge("black", "vim")
    gr.edge("black", "formatter")
    gr.edge("vim", "formatter")
    gr.edge("black", "vim")
    gr.edge("black", "formatter")
    gr.edge("vim", "formatter")

    gr.render(filename="black", view=True, outfile="black.png")


if __name__ == "__main__":
    template()