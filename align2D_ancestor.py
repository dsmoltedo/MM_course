from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1uwq', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1uwq', atom_files='1uwq.pdb')
aln.append(file='node9.fasta', align_codes='node9', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned_ancestor.fasta', alignment_format='FASTA')
aln.write(file='aligned_ancestor.ali', alignment_format='PIR')
aln.write(file='aligned_ancestor.pap', alignment_format='PAP')
