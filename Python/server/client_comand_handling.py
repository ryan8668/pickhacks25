import pose_data_processing as pose_data_processing

# This function will handle the commands sent by the client and return the response to the client
def proccess_command(command):
    # This is a stand in currently
    match command:
        case "nose_position":
            return pose_data_processing("nose").to_bytes()