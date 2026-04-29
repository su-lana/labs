# Labs for current course in range from 2-6.
In here is implemented the use of Block Processor system with SQL db backend. Based on BLocks, Votes, Persons and Sources.
## The structure is such:
- `lab2/` - components read and added from csv
- `lab3/` - components desc with sqlite3 and executed inserts
- `lab4_fin/` - selection and retrieval of components
- `updater/` and `block_processor/` - lab5 event stream insertion / component processor
- `lab6/` and `test_lab6/` - lab6 testing

## Main:
- **Components** - aka Block(id, view, desc, img), Vote(voter_id, block_id, timestamp, source_id), Source(id, ip_addr, country_code), Persons (id, name, addr)
- **Processor** – logic for handling blocks and events\
- **Database** - SQL connection and implementation


## Mermaid flowchart diagram for the project
```mermaid
flowchart TD
    A[Input event] --> B(Event string)
    B --> C{Block processor}
    C -->|Process new| D[Stay in Event string]
    C -->|Process dublicate| E[Ignore in Event string]
    D --> F[Results]
