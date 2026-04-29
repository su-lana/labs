import pytest
from pydantic import ValidationError

from lab6_4based import Block, Person, Source, Vote



#Block
@pytest.mark.parametrize("data", [
    {"id": "0xabcdef12", "view": 10, "desc": "ok", "img": "img.png"},
])
def test_block_valid(data):
    assert Block(**data)


@pytest.mark.parametrize("data", [
    {"id": "0xabcdef12", "view": -1, "desc": "ok", "img": "img.png"},
    {"id": "0xabcdef12", "view": 1, "desc": "", "img": "img.png"},
    {"id": "abcdef12", "view": 1, "desc": "ok", "img": "img.png"},
])
def test_block_invalid(data):
    with pytest.raises(ValidationError):
        Block(**data)

       
#Person
@pytest.mark.parametrize("data", [
    {"id": 1, "name": "John", "addr": "Lviv"},
])
def test_person_valid(data):
    assert Person(**data)


@pytest.mark.parametrize("data", [
    {"id": -1, "name": "John", "addr": "Lviv"},
    {"id": 1, "name": "", "addr": "Lviv"},
    {"id": 1, "name": "John", "addr": ""},
])
def test_person_invalid(data):
    with pytest.raises(ValidationError):
        Person(**data)


#Source
@pytest.mark.parametrize("data", [
    {"id": 1, "ip_addr": "192.168.0.1", "country_code": "UA"},
])
def test_source_valid(data):
    assert Source(**data)


@pytest.mark.parametrize("data", [
    {"id": -1, "ip_addr": "192.168.0.1", "country_code": "UA"},
    {"id": 1, "ip_addr": "", "country_code": "UA"},
    {"id": 1, "ip_addr": "192.168.0.1", "country_code": "U"},
])
def test_source_invalid(data):
    with pytest.raises(ValidationError):
        Source(**data)



#Vote
@pytest.mark.parametrize("data", [
    {
        "block_id": "0xabcdef12", "voter_id": 1,
        "timestamp": "2025-03-03 12:00:00", "source_id": 1,
    },
])
def test_vote_valid(data):
    assert Vote(**data)


@pytest.mark.parametrize("data", [
    {
        "block_id": "abcdef12", "voter_id": 1,
        "timestamp": "2025-03-03 12:00:00", "source_id": 1,
    },
    {
        "block_id": "0xabcdef12", "voter_id": -1,
        "timestamp": "2025-03-03 12:00:00", "source_id": 1,
    },
    {
        "block_id": "0xabcdef12", "voter_id": 1,
        "timestamp": "2025-03-03 12:00:00", "source_id": -1,
    },
])
def test_vote_invalid(data):
    with pytest.raises(ValidationError):
        Vote(**data)