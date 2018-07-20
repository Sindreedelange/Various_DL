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
GPU that supports newer versions of Cuda 
```

### Installing
```
Anaconda (Python and Jupyter Notebook)
```
First things first: Virtual Environment or not? 
I would recommend using Virtual Environments, at least for this project, because it makes using the _fast ai_ submodule much easier  

One way to do this is to install Anaconda, which also works as a packet manager (think Pip): https://www.anaconda.com/download/. 

__NOTE__: The Anaconda (and Python) version needs to be > 2.7.

For complete walk through installing and set up of Anaconda: https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444

Using Anaconda one gets Python and Jupyter Notebook with minimum hassle.

## Google Images Downloader
The Google Images Downloader is described in the *FemaleFace_MaleFace_Unknown_Classification* notebook.
However, if you have pip installed:

```pip install google_images_download```

*NOTE* If one wants to download > 100 images pr. searchword: 

```http://chromedriver.chromium.org/downloads```

Download correct version, and, if necessary, edit path to the `.exe` file (_chromedriver_path_)

## Running the project
After installation of necessary software there are still quite a few more programs to download, but as mentioned Conda makes this quite easy. 
Run the usual:

```git clone```

In order to get the submodule, rest of the necessary software and making a virtual environment: 

```cd FastAi/```

```git submodule init```

```git submodule update```

```conda env update``` (coffe break!) 
> Amongst other things, downloads Cuda, which is why one needs a GPU that supports a newer version of this software.

#### If one does not have a GPU and wishes to try and run deep learning on a CPU:

```conda env update -f environment-cpu.yml```


### Starting the virtual environment
After the fast.ai submodule and necessary software are downloaded, and the virtual environment is made:

```cd ..```

```conda activate fastai``` (for GPU)

```conda activate fastai-cpu``` (for CPU)

*Note* Just follow the instructions in the command windows after running the *conda env update* (on some computers I had to run *conda activate ..* and some just *activate ..* 

Everything is set up - run a Jupter Notebook, open the _.ipynb_ file and follow the instructions in the notebook :) 

## Error Messages
When trying to run the CPU version, one might encounter different error messages. 

On of these are ```Cunda Runtime Error (8)``` , I found the solution to be to edit the *environment-cpu.yml* file in the FastAi-folder. More specifically, edit line 90 from *- pytorch<0.4* to *- pytorch-cpu<0.4*. 





