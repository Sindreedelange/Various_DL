# Multiclass Classification

Training a neural network model able to distinguish between multiple different classes of objects. 

## Getting Started
How to replicate the project

### Prerequisites

```
Anaconda 
Python > 2.7
Jupyter Notebook
Google Images Downloader 
```

### Installing
```
Anaconda (Python and Jupyter Notebook)
```
First things first: Virtual Environment or not? 
I would recommend using Virtual Environments, at least for this project, because it makes using the _fast ai_ submodule much easier  

One way to do this is to install Anaconda, which also works as a packet manager (think Pip): https://www.anaconda.com/download/. 

__NOTE__: The Anaconda (and the Python) version needs to be > 2.7.

For a total walk through installing and set up of Anaconda: https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444

With Anaconda one gets Python and Jupyter Notebook with minimum hassle.

```
Google Images Downloader
```
The Google Images Downloader is described in the *FemaleFace_MaleFace_Unknown_Classification* notebook. 

## Running the project
After installation of necessary software there are still quite a few more programs to download, but as mentioned Conda makes this quite easy. 
Run the usual:

```git clone```

In order to get the submodule, rest of the necessary software and making a virtual environment: 

```cd FastAi/```

```git submodule init```

```git submodule update```

```conda env update``` (coffe break!) 

After the fast.ai submodule and necessary software are downloaded, and the virtual environment is made:
```cd ..```
```conda activate fastai```

Everything is set up - run a Jupter Notebook, open the _.ipynb_ file and follow the instructions in the notebook :) 






