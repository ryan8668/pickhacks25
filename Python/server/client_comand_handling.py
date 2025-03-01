# This function will handle the commands sent by the client and return the response to the client
def proccess_command(command):
    # This is a standin currently
    match command:
        case "":
            return "abc".to_bytes()