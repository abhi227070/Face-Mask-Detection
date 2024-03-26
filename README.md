# Face Mask Detection

This project utilizes a deep learning CNN model to classify images into two categories: with mask and without mask. It employs OpenCV for image processing and model inference. Face mask detection has significant applications in situations such as the COVID-19 pandemic and industries where mask-wearing is mandatory.

## Table of Contents

- [Introduction](#introduction)
- [Technologies/Tools Used](#technologies-tools-used)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The Face Mask Detection project leverages a deep learning model to classify images into two classes: with mask and without mask. It uses OpenCV for image capturing and processing and a pre-trained CNN model for inference.

## Technologies/Tools Used

- Python
- OpenCV
- Keras
- Streamlit
- WebRTC

## Description

This project employs a deep learning CNN model trained to detect face masks in images. The model is loaded and applied to live video streams captured through the web camera using Streamlit and WebRTC. OpenCV is used for real-time image processing, including face detection and classification. The application displays a live video feed with annotations indicating whether each detected face is wearing a mask or not.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/face-mask-detection.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Allow access to the web camera if prompted.

3. The application will display a live video stream with annotations indicating whether faces are wearing masks or not.

## License

This project is licensed under the [MIT License](LICENSE).
