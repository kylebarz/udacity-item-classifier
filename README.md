# UDacity Capstone: Item on Shelf Image Classifier
Each day, many people from sales organizations go into retail stores and audit what products are available on the shelf.
They generally do that by performing a manual assessment of store shelves and answering a series of survey questions.
We asked ourselves if it would be possible to do this using computer vision. The ideal computer vision model would assess
the photo to measure both what products are available as well as the quality of the display. In this example. we have proved
that it would be possible to use an Object Detection algorithm to detect items on a shelf, followed by an Image Classifier
algorithm to determine which specific item is visible.

I set out to test my ability on building a computer vision algorithm based upon a pre-trained model. There are two components
to this code:
* Vision Algorithm Training - This was conducted using a DataBricks GPU cluster from an Azure Data Lake. 
* Flask Web App Deployed to Azure App Services. This is different than what was included in the UDacity course, but was the 
environment I wanted to learn about. 

A demo of this code is available at: https://productid.azurewebsites.net/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Data Training:
* Databricks Cluster with Python3 + GPU for Fastest Performance
* Datalake for Storage of Raw Image Data
* Torch
* Flask
* Numpy

For Web Front End:
* Python 3
* Flask
* Numpy
* Torch


### Installing

Files contained within the "build_model" will generate the CNN to be consumed in subsequent steps. 

*Step 1: "Data Access" will open a Tab-Seperated File from the Data Lake and copy it to local storage for performance reasons. 
This TSV is formatted to contain the original image and all annotated data with relative coordinates. Running this notebook will
extract the contents from each section of the image to it's own sequentially-numbered file inside of a directory corresponding to the tag. Finally, the data is compressed and copied to the Data Lake for storage.

*Step 2: "Data Explore & Prep" shows the distribution of images by tag/product. I've decided to remove items with a substantially large
number of photos or too few. In a later release, I would add image augmentation processed to try to equalize the dataset and reduce
the images removed. Finally, this notebook will split the files into a TRAIN/VALID/TEST structure for use in PYTORCH.

*Step 3: "Model Building" will build the model for use in the web app. This is designed to use a pre-trained model (ie. RESNET50),
removes the last layer, and updates based upon the training day. I've designed this to save a checkpoint at the end of each epoch.
The number of epochs is configurable. In a future relase, I would add testing of multiple models and have it automatically end when
training is no longer improving. 

*Step 4: Copy the output model (saved to the datalake) into the "model/" folder for access.

*Step 5: Run "python app.py" to launch Flask. Access the model through the web browser.

*Step 6: Submit Test Images to the front-end and watch the results!


## Built With

* Azure Data Lake
* Azure Data Bricks
* PyTorch
* ResNet50

## Authors

* Kyle Barz


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Udacity for some code and a LOT of instruction!
* Other links embedded in the code where inspiration was used from others. 
* Microsoft for assistance in tagging the data.
