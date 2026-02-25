import cv2
from io import BytesIO
import numpy as np

from app.common.custom_exception import CustomException
from app.common.logger import get_logger

logger = get_logger(__name__)


def process_image(image_file):
    try:

        in_memory_file = BytesIO()
        image_file.save(in_memory_file)

        image_bytes = in_memory_file.getvalue()
        np_arr = np.frombuffer(image_bytes, np.int8)

        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascade+"haarcascade_frontalface_default.xml")

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        if len(faces) == 0:
            return image_bytes, None
            
        largest_face = max(faces, key = lambda r : r[2] * r[3])

        (x, y, w, h) = largest_face

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

        is_sucess, buffer = cv2.imencode(".jpg", img)

        logger.info("Image processing completed successfully.")

        return buffer.tobytes(), largest_face


    except Exception as e:
        logger.error(f"Error while processing image {e}")
        raise CustomException("Failed to process image : ", e)