"""
Here are the functions that define when and what information is
to be treated. All decisions on the app flow are done here.
These were decoupled from the ones that define app flow.
This is because the program starts by searching information based on
the 'tag_option' that 'notes_on_tags' has currently active.
From this starting point we'll search for related tags, here defined
as tags that are part of the same post. We will then loop though them
to discover all relations, and collect them as a list of tuples, that
will eventually become edges in a graph. And, if the first part is
dedicated wholly to define the list of tags in question; the scond one
is an exploration of the connections between each other.
These are two very different moments that, for clarity's sake, are much
better designed if kept separate.
"""
import snoop
from graph_factory import db_data, flattentups, pairing, uniques
from graph_template import template_creation
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def answer():
    """
    Where we ask the user ehat tag he wants to use.
    """
    answr = input("Choose a tag: ")
    tg = [answr]

    return tg, answr


@snoop
def first_run(tg):
    """
    Based on what tag the user chooses, we'll give
    it as an argument to 'db_data' function, that will
    discover all related tags. The program will run
    based on the discovered list, and this functio
    won't run no more.
    """

    db = db_data(tg)
    flat = flattentups(db)
    tags = uniques(flat)

    return tags


@snoop
def tags_loop(tags):
    """
    With the tags collected in the former function, we'll
    iterate through them to achieve a collection of all
    connections for each of the tags.
    """
    edgelst = []

    for tag in tags:
        db = db_data([tag])
        tag_edges = pairing(db)
        edgelst.append(tag_edges)
        edge_lst = [i for t in edgelst for i in t]
        edge_list = [i for t in edge_lst for i in t]

    return edge_list


@snoop
def main():
    """
    The main function of the app. It starts all services.
    """
    answers = answer()
    tg = answers[0]
    answr = answers[1]
    tags = first_run(tg)
    tags_loop(tags)
    edge_list = tags_loop(tags)
    template_creation(edge_list, answr)


if __name__ == "__main__":
    main()
