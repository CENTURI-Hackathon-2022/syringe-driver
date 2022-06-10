# Syringe driver
Delivering small (~µL) calibrated volumes of liquid is important in multiple fields such as microfluidics and animal testing (e.g.rewarding animals with water). The goal of this project will be to write an open-source code (Arduino/Raspberry Pi) to setup (volume calibration), control (delivery/recapture, refill, etc.) and collect data (lick sensor) from a syringe driver.


# Getting started
## Dependencies
**To do**  
*Likely install conda, install dependencies*

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

# Objective dependencies

→ 0 → 1  
→ 0 → 2  
1 & 2 → 3 → 4  
4 → 5 & 6  

### Legend:

    #x → #y: #x needs to be completed before #y can be started
    #x | #y: #x or #y needs to be completed
    #x & #y: #x and #y needs to be completed

<br/><br/>  
*Setup*  
*Example code*  
*Arduino vs. Raspberry-pi*  
*Open each step as an Issue*  
