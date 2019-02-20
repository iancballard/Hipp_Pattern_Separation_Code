"""parameters for PE regressors experiment."""
design_name = 'sim_PE_diff_one'
contrasts = [('feedback',['feedback'],[1]), \
('neg_feedback',['feedback'],[-1]), \
('neg_state',['b_plus','b_minus','c_plus','c_minus'],[-1,1,1,-1]), \
('target',['b_plus','b_minus','c_plus','c_minus'],[1,-1,1,-1]), \
('neg_target',['b_plus','b_minus','c_plus','c_minus'],[-1,1,-1,1]), \
('A',['b_plus','c_minus'],[1,1]), \
('neg_A',['b_plus','c_minus'],[-1,-1]), \
('all',['b_plus','b_minus','c_plus','c_minus'],[1,1,1,1]), \
('neg_all',['b_plus','b_minus','c_plus','c_minus'],[-1,-1,-1,-1]), \
('b_state',['b_plus','b_minus'],[1,-1]), \
('neg_b_state',['b_plus','b_minus'],[-1,1]), \
('c_state',['c_plus','c_minus'],[-1,1]), \
('neg_c_state',['c_plus','c_minus'],[1,-1]),\
('PE_mf',['PE_mf'],[1]),\
('PE_mb',['PE_mb'],[1]),\
('PE',['PE_mf','PE_mb'],[1,1]),\
('neg_PE_mf',['PE_mf'],[-1]),\
('neg_PE_mb',['PE_mb'],[-1]),\
('neg_PE',['PE_mf','PE_mb'],[-1,-1])]