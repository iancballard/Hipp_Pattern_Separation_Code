# Hipp Pattern Separation Code

This repository contains analysis code for the following paper:

Ian C. Ballard, Anthony D. Wager, Samuel M. McClure. Hippocampal Pattern Separation Supports Reinforcement Learning, 2019. Nature Communications.

Raw behavioral and MRI data for this study can be accessed at: https://openneuro.org/datasets/ds001590

The code is contained within several IPython notebooks that performed the analyses and generated all figures used in the manuscript.

## Getting Started

The following software were used:
* FSL 5.0.8
* ANTS 1.9
* Lyman 0.0.10
* Freesurfer 5.3.3
* R 3.3.1

### fMRI Analysis with Lyman
First, the anatomical image for each subject was processed using Freesurfer's recon-all tool to generate the cortical surface models. 

Next, we prepare fieldmap images from two images taken with opposite phase encoding directions. Details can be found here: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup. The code for this analysis can be found in prepare_fieldmaps.ipynb.

Next, the functional data were preproccesed with FSL, Freesurfer, and Nipype using lyman. The processing used the experiment parameters in the sim.py and loc.py files included in this repository. This was performed with the following command line executions:

```
run_fmri.py -e sim -s subjects.txt -w preproc
run_fmri.py -e loc -s subjects.txt -w preproc
```

Next, we conducted an ICA decomposition (run_melodic.ipynb) and automatically classified and removed noise components (run_fix.ipynb). Details can be found at http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIX/UserGuide.

Next, first-level models were fit to each run, registered to the space of the first functional run, and a fixed effects analysis was conducted.

```
run_fmri.py -e sim -altmodel PE -s subjects.txt -w model reg ffx -regspace epi
```

For the localizer experiment, data were registered to the first run of the SIM experment by using the following command:

```
run_fmri.py -e loc -s subjects.txt -w model reg ffx -regspace epi -regexp sim
```

## Behavioral Analysis Notebooks

[analyze_behavioral_data.ipynb](analyze_behavioral_data.ipynb)

Runs model-free analysis of behavioral data

[RT_fitting.ipynb](RT_fitting.ipynb)

Fits RL models to reaction time data, analyzes with leave-one-subject-out approach, and simulates values for Figure 2

[RT_model_bayesian_model_comparison.ipynb](RT_model_bayesian_model_comparison.ipynb)

Compares RL models of reaction time data with Bayesian model comparison

[all_rts.csv](all_rts.csv)

Reaction time data

## fMRI Analysis Notebooks

[make_masks.ipynb](make_masks.ipynb)

Warp ROIs from group space to individual subject sufaces and write binary masks in functional space.

[prepare_fieldmaps.ipynb](prepare_fieldmaps.ipynb)

Create images with opposite phase encoding directions for topup field correction.

[striatum_analysis.ipynb](striatum_analysis.ipynb)

Main analysis code for ROI analysis of the striatal feedback response.

[run_fix.ipynb](run_fix.ipynb)

Run’s FSL’s automatic ICA denoising algorithm.

[run_melodic.ipynb](run_fix.ipynb)

Run’s FSL’s ICA decomposition on pre-processed data.

[roi_figure.ipynb](roi_figure.ipynb)

This notebook generates the ROI mask figure in the Supplement.

[compute_PSA.ipynb](compute_PSA.ipynb)

Compute PSA matrices and conduct mixed-effects analysis on them

[PSA_analysis.ipynb](PSA_analysis.ipynb)

Conduct permutation and control tests of regressions on PSA matrices

[pattern_content_analysis.ipynb](pattern_content_analysis.ipynb)

Analysis for Figure 6. Uses localizer data to probe content of task representations.

## Lyman software
The following scripts specify the analyses run by the Lyman ecosystem.

[project.py](project.py)

The lyman project file that defines general parameters for both the localizer and SIM experiments

[sim.py](sim.py); [loc.py](loc.py)

The lyman experiment file for preprocessing and modeling the fMRI data.

[sim-PE.py](sim-PE.py) 

contrasts for model of prediction errors

[sim-betas.py](sim-betas.py); [loc-betas.py](loc-betas.py)

The lyman experiment file for first-level beta series modeling the fMRI data.

[subjects.txt](subjects.txt)

The subject codes used in the processing.

## License

All code is freely available under the BSD (3-clause) license.


