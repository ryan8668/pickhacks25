import tensorflow as tf

def initialize_movenet(path_to_model):
    # Setup TF Lite Interpreter
    interpreter = tf.lite.Interpreter(model_path=path_to_model)

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.allocate_tensors()

    return interpreter, (input_details, output_details)

# Function to predict keypoints
def keypoint_prediction(interpreter, model_details, input_img):
    interpreter.set_tensor(model_details[0][0]['index'], [input_img])
    interpreter.invoke()
    
    return interpreter.get_tensor(model_details[1][0]['index'])