from datetime import datetime

from flask import abort, make_response  # import abort() function; used to send an error msg


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# generates a string representation of the current timestamp
# PEOPLE dictionary stands for a proper database
PEOPLE = {

    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return list(PEOPLE.values())
#  server will run read_all() function when it receives an http request


def create(person):  # create() function
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {  # lname is unique; if the data in the request body, update people with new object
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:  # request body doesn't contain a last name
        abort(406, f"Person with last name {lname} already exists")  # abort() function


def read_one(lname):
    if lname in PEOPLE:  # Flask app finds the provided last name in PEOPLE
        return PEOPLE[lname]  # then returns the data for this particular person
    else:  # otherwise error
        abort(404, f"Person with last name {lname} not found")


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
