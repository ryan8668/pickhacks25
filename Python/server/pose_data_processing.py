def get_feature(feature_name, pose, confidence_threshold=0.5):
    # Dictionary of feature and their index
    feature_by_name = {
        "nose": 0,
        "left_eye": 1,
        "right_eye": 2,
        "left_ear": 3,
        "right_ear": 4,
        "left_shoulder": 5,
        "right_shoulder": 6,
        "left_elbow": 7,
        "right_elbow": 8,
        "left_wrist": 9,
        "right_wrist": 10,
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14,
        "left_ankle": 15,
        "right_ankle": 16
    }

    feature_index = feature_by_name[feature_name]

    # Return the point if the network is sufficeintly confident in its position
    if pose[0][0][feature_index][2] >= confidence_threshold:
        return [pose[0][0][feature_index ][0], pose[0][0][feature_index][1]]