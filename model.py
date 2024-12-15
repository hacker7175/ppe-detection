import os

from ultralytics import YOLO
from PIL import Image


def yolov8_image_processing(model_path, source, output_dir, conf=0.25):
    """
    Perform object detection with a YOLOv8 model.

    :param output_dir:
    :param model_path: Path to the trained YOLOv8 model.
    :param source: Path to image/video or directory of images.
    :param conf: Confidence threshold for predictions.
    """
    model = YOLO(model_path)  # Load the trained YOLOv8 model

    # Perform inference
    results = model.predict(
        source=source,  # Path to an image or video
        conf=conf,# Confidence threshold
        save=False
    )

    os.makedirs(output_dir, exist_ok=True)

    # Process the results and draw bounding boxes
    for result in results:
        if hasattr(result, 'plot'):  # Check if the result has a plot method
            result_image = result.plot()  # Get annotated image

            # Save the annotated image to the output directory
            output_path = os.path.join(output_dir, "processed_image.jpg")
            Image.fromarray(result_image).save(output_path)
            return output_path
    return ""