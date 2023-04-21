from engine import Engine


# Create game engine
eng = Engine()


def main():

    # Create game environment
    eng.loader()
    eng.create_character(input("Input your characters name>>>"))
    create_teller()

    while True:

        # Read next script line
        line = next(eng.teller)

        # Check for events
        if event := find_event(line):

            # Start event
            result = eng.start_event(event)

            # Check event result
            check_event_res(result)

        else:
            eng.teletype(line)

        # Check user input for any ingame commands
        while True:
            if eng.check_feedback(input(">>>")): break


# Here are 3 functions to fulfill requirement
def check_event_res(num):
    """Check number and launch fuctions."""
    match num:
        case 404: eng.end()
        case _: return None


def create_teller():
    """Create link to script generator."""

    eng.teller = eng.tell(eng.get_chap(eng.chap))
    return eng.teller


def find_event(string):
    """Check string for events."""

    return int(string.rstrip()) if string.rstrip().isdecimal() else None


if __name__ == "__main__":
    main()
