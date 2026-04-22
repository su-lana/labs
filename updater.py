import sqlite3
import typer

app = typer.Typer()


def get_connection():
    return sqlite3.connect('lab3.db')


@app.command()
def add_block(id: str, view: int, desc: str, img: str = None):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO BLOCKS VALUES (?, ?, ?, ?)",
        (id, view, desc, img)
    )

    cur.execute(
        "INSERT INTO event_stream (type, id, processed) VALUES (?, ?, 0)",
        ("block", id)
    )

    conn.commit()
    conn.close()

    print("Block added.")


@app.command()
def add_vote(block_id: str, voter_id: int, timestamp: str, source_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO VOTES VALUES (?, ?, ?, ?)",
        (block_id, voter_id, timestamp, source_id)
    )
    
    cur.execute(
        "INSERT INTO event_stream (type, id, processed) VALUES (?, ?, 0)",
        ("vote", voter_id),
    )

    conn.commit()
    conn.close()

    print("Vote added.")



@app.command()
def add_person(id: int, name: str, addr: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO PERSONS VALUES (?, ?, ?)",
        (id, name, addr)
    )

    cur.execute(
        "INSERT INTO event_stream (type, id, processed) VALUES (?, ?, 0)",
        ("person", id)
    )

    conn.commit()
    conn.close()

    print("Person added.")



@app.command()
def add_source(id: int, ip_addr: str, country_code: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO SOURCES VALUES (?, ?, ?)",
        (id, ip_addr, country_code)
    )

    cur.execute(
        "INSERT INTO event_stream (type, id, processed) VALUES (?, ?, 0)",
        ("source", id)
    )

    conn.commit()
    conn.close()

    print("Source added.")



if __name__ == "__main__":
    app()