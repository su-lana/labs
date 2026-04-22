import sqlite3
import time



def get_connection():
    return sqlite3.connect('lab3.db')

def process_block(cur, block_id):
    cur.execute("SELECT * FROM BLOCKS WHERE id = ?", (block_id,))
    block = cur.fetchone()
    print("Processing block:", block)


def process_vote(cur, voter_id):
    cur.execute("SELECT * FROM VOTES WHERE voter_id = ?", (voter_id,))
    votes = cur.fetchall()
    print("Processing votes:", votes)


def process_person(cur, person_id):
    cur.execute("SELECT * FROM PERSONS WHERE id = ?", (person_id,))
    person = cur.fetchone()
    print("Processing person:", person)


def process_source(cur, source_id):
    cur.execute("SELECT * FROM SOURCES WHERE id = ?", (source_id,))
    source = cur.fetchone()
    print("Processing source:", source)


def process_events():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT row_id, type, id 
        FROM event_stream 
    """)

    events = cur.fetchall()

    for row_id, event_type, event_id in events:

        if event_type == "block":
            process_block(cur, event_id)

        elif event_type == "vote":
            process_vote(cur, event_id)
            
        elif event_type == "person":
            process_person(cur, event_id)

        elif event_type == "source":
            process_source(cur, event_id)

        cur.execute(
            "UPDATE event_stream SET processed = 1 WHERE row_id = ?",
            (row_id,)
        )
    

        print(f"New event: {event_type} {event_id}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    while True:
        process_events()
        time.sleep(1)