This repository contains analysis code for the following paper:

Ian C. Ballard, Anthony D. Wager, Samuel M. McClure. Hippocampal Pattern Separation Supports Reinforcement Learning.

Raw behavioral and MRI data for this study can be accessed at: https://openneuro.org/datasets/ds001590

The code is contained within several IPython notebooks that performed the analyses and generated all figures used in the manuscript.

fMRI Analysis
First, the anatomical image for each subject was processed using Freesurfer's recon-all tool to generate the cortical surface models. 

Next, for the Princeton subjects we prepare fieldmap images from two images taken with opposite phase encoding directions. Details can be found here: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup. The code for this analysis can be found in prepare_fieldmaps.ipynb.

Next, the functional data were preproccesed with FSL, Freesurfer, and Nipype using lyman. The processing used the experiment parameters in the mag.py file included in this repository. This must be run separately for ASU and Princeton subjects due to two differences described in mag.py. This was performed with the following command line.

run_fmri.py -s subjects.txt -w preproc
Next, we conducted an ICA decomposition (run_melodic.ipynb) and automatically classified and removed noise components (run_fix.ipynb). Details can be found at http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIX/UserGuide.

Next, first-level models were fit to each run, registered to the space of the first functional run, and a fixed effects analysis was conducted.

run_fmri.py -s subjects.txt -w model reg ffx -regspace epi
Once those commands have been executed, every analysis can be generated using these notebooks.

Behavioral Analysis
All behavioral analysis for the Hunger and Justify experiments can be found in behavioral/analyze_behavioral_studies.ipynb. Raw data for both datasets are also stored here as csv files.

### fMRI Analysis Notebooks

make_masks.ipynb
Link to static notebook

Warp ROIs from group space to individual subject sufaces and write binary masks in functional space.

prepare_fieldmaps.ipynb
Link to static notebook

Create images with opposite phase encoding directions for topup field correction.

recon-all.ipynb
Link to static notebook

All of the actual analyses are contained within this notebook.

rerun_bbregister.ipynb
Link to static notebook

For some subjects, bbregister failed and we needed to identify bad registrations and potentially create hand-made initializations.

roi_analysis.ipynb
Link to static notebook

Main analysis code for ROI analysis for the manuscript.

run_fix.ipynb
Link to static notebook

Run’s FSL’s automatic ICA denoising algorithm.

run_melodic.ipynb
Link to static notebook

Run’s FSL’s ICA decomposition on pre-processed data.

ROI_Figure.ipynb
Link to static notebook

This notebook generates the ROI figure in the manuscript.

Software Versions
MRI Processing
Freesurfer: 5.3
FSL: 5.0
R Packages
R: 3.3.1
Lyman
v0.0.10

Other Data
project.py
The lyman project file that was used to process the data.

mag.py
The lyman experiment file for preprocessing the fMRI data.

mag-SVtotaldiff.py
The lyman experiment file for first-level modeling the fMRI data.

subjects.txt
The subject codes used in the processing.
