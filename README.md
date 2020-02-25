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
* Flask Web App Deployed to Azure App Services. This is different than what was included in the UDacity course, but was the environment I wanted
to learn about. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Data Training:
Databricks with GPU for Fastest Performance
Datalake for Storage of Raw Image Data
Torch
Flask
Numpy

Python 3
Flask
Numpy
Torch
TorchVision


```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
