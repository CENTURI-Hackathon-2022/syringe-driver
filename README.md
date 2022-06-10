# Syringe driver
Delivering small (~µL) calibrated volumes of liquid is important in multiple fields such as microfluidics and animal testing (e.g.rewarding animals with water). The goal of this project will be to write an open-source code (Arduino/Raspberry Pi) to setup (volume calibration), control (delivery/recapture, refill, etc.) and collect data (lick sensor) from a syringe driver.


# Getting started

## Installing the dependencies
To install Python and the required dependencies we strongly recommend to use
[conda], [mamba] or [pipenv].

## Installing conda

Conda can be installed multiple ways. There is no recommendations about how to
but one can read [there](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
for a likely exhaustive list on ways to install conda.

Note that Anaconda is not necessarily recommended, [miniconda] might be a better
alternative.

Moreover, it is advised to start jupyter notebooks from a shell/terminal/prompt
to be able to better see the error messages.

## Installing the dependencies

Once conda is installed (or your favorite environment manager), you can create
and activate your environment:
```shell
conda create -n syringedriver
conda activate syringedriver
```

Then, there is a `setup.py` file with the basic dependencies present within this
repository. It means that you can easily install all the likely necessary
dependencies using [pip]. It might be necessary to install it first:
```shell
conda install pip
```

Then, it is possible to install the dependencies, from the placozoa-tracking
folder the following way:
```shell
pip install .
```

### List of dependencies:
Here is the list of dependencies that will be installed:
- [ipython] : interactive python terminal
- [jupyter] : python notebook
- ???


# **Road Map**

## Main goal
Automatically (monitor captor inputs) deliver a specified volume of liquid (parameter that we control) with the syringe.

## Objectives
Objectives are listed in ~chronological//difficulty order, but you can progress as you please.
We do not expect that all the objectives are completed (yes we do).

- **0** :wrench: Setup
- **1** :scream_cat: Learn how to tame the stepper motor (without syringe)
- **2** :ear: Learn how to listen to the captors (without motor)
    - 2.1 limit switches
    - 2.2 event captors (lick sensor (optic//capacitive), etc.)
- **3** :couple_with_heart: Connect them, verify if the two of them can work together.
- **4** :wedding: ASSEMBLE!
    - 4.1 :tada:
<br/><br/>
- **5** :left_right_arrow: Fill/Empty the syringe
- **6** :droplet: Deliver a calibrated drop when an event occurs
    - 6.1 Compute number of steps needed to have the volume we want
<br/><br/>
- **7** Bonus Goals
    - 7.1 Image analysis: use a webcam to estimate the size of the drop 
    - 7.2 Recapture: Use a second syringe driver to recapture the drop
    - 7.3 OpenLabFrame: :tropical_drink:
    - ...

You can find the roadmap for the project as an issue [there](https://github.com/CENTURI-Hackathon-2022/syringe-driver/issues/1).

# Objective dependencies

&rarr; 0 &rarr; 1  
&rarr; 0 &rarr; 2  
1 & 2 &rarr; 3 &rarr; 4  
4 &rarr; 5 & 6  

### Legend:

    #x → #y: #x needs to be completed before #y can be started
    #x | #y: #x **or** #y needs to be completed
    #x & #y: #x **and** #y needs to be completed
    
    
[conda]: https://docs.conda.io/en/latest/
[mamba]: https://mamba.readthedocs.io/en/latest/
[pipenv]: https://pipenv.pypa.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[pip]: https://pypi.org/project/pip
[ipython]: https://ipython.org
[jupyter]: https://jupyter.org


<br/><br/>  

*Arduino vs. Raspberry-pi*  
*Open each step as an Issue*  
