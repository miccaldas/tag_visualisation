"""
Here are concentrated all the functions dedicated to collecting and
transforming information.
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
This module is called by 'graph_management.py'
"""
import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def db_data(tg):
    """
    Makes calls to Note's db to find all posts
    who have a given tag.
    """
    print(f"db_date in graph_factory. The value for answer is {tg}")

    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="notes",
            use_pure=True,
        )
        cur = conn.cursor(buffered=True)
        query = "SELECT k1, k2, k3 FROM notes WHERE MATCH(title, k1, k2, k3) AGAINST (%s) ORDER BY TIME"
        cur.execute(query, tg)
        db = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    return db


@snoop
def pairing(db):
    """
    From the triple tuples representing the tags per
    post, we will break them into double tuples, in
    such a way that all possible pairings are represented.
    This function only runs on the second part of the
    process. All other functions in this module are
    specific to the first part.
    """
    tag_edges = [[(a, b), (a, c), (b, c)] for a, b, c in db]

    return tag_edges


@snoop
def flattentups(db):
    """
    Flattens the information from the db, so we have just a
    list of strings representing tags.
    """
    flttup = [i for t in db for i in t]

    return flttup


@snoop
def uniques(flttup):
    """
    Creates a list with only unique entries.
    """
    set_tup = set(flttup)
    distinct = list(set_tup)

    return distinct
