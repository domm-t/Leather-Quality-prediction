# Leather-Quality-prediction
This repository contains a Flask application designed to predict leather defects from uploaded images.

# Overview
The application allows users to upload an image of leather, and it then predicts the type of defect (if any) present in the leather using a pre-trained deep-learning model.

## Features:
Image Upload: Users can upload leather images via a simple web interface.

Defect Prediction: The uploaded image is processed and fed into a deep-learning model to predict the leather defect.

Result Display: Predicted results are showcased to the user on a separate page.
## Code Breakdown
**Imports**
- Flask: Used to create and manage the web application.
- SQLAlchemy: A potential addition for database operations (though not used in the provided code).
- OpenCV (cv2): Used for image processing tasks.
- NumPy: For numerical computations, especially array manipulations.
- Keras: To load and utilize the pre-trained deep learning model.

**Initialization:**
- A Flask application instance is created.
- A deep learning model, leather_defect_model.h5, is loaded.
- Leather defect labels are initialized in the defect_classes list.

**Routes:**

Homepage (/):
> Displays an index.html page, likely allowing users to upload an image.

**Prediction (/output):**
> Handles image upload from the user.
> Preprocesses the image (resizing and normalization).
> Predicts the leather defect using the deep learning model.
> Displays the prediction result on an output.html page.

**Execution:**
> If the script is run directly, the Flask application starts with debugging enabled.


## What leather defects can this predict:

- Folding marks
- Grain off
- Growth marks
- Loose grains
- Non-defective
- Pinhole
# Future Enhancements:
Integration with a database (hinted by the SQLAlchemy import) to store prediction results or user uploads.


FELL FREE TO CONTACT thirshathadom@gmail.com for any clarification.
