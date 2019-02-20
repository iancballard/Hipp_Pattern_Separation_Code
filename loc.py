"""Preprocessing parameters for loc experiment."""
source_template = "{subject_id}/func/loc/run_?_crop.nii.gz"
n_runs = 2
TR = 1.5
frames_to_toss = 8
temporal_interp = False
interleaved = False
coreg_init = "header"
intensity_threshold = 4.5
motion_threshold = 0.5
smooth_fwhm = 4
surf_smooth = 4
hpf_cutoff = 128
grf_pthresh = .05
hrf_model = 'GammaDifferenceHRF'
confound_pca = False
temporal_deriv = False
units = "secs"
remove_working_dir = True
confound_sources = ['wm']
fieldmap_template = "{subject_id}/cal/lyman/fm_loc_?_mc_pe0_pe1.nii.gz"
fieldmap_pe = ['y','y-']
design_name = 'loc'
contrasts = [('Face',['face','body','object','place','character'],[4,-1,-1,-1,-1]), \
('Body',['face','body','object','place','character'],[-1,4,-1,-1,-1]), \
('Object',['face','body','object','place','character'],[-1,-1,4,-1,-1]), \
('Place',['face','body','object','place','character'],[-1,-1,-1,4,-1]), \
('Wordform',['face','body','object','place','character'],[-1,-1,-1,-1,4])]