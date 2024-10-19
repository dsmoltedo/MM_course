from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='PROTEIN', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6eqeA', atom_files='6eqe.pdb')
aln.append(file='target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned_ancestor.fasta', alignment_format='FASTA')
aln.write(file='aligned_ancestor.ali', alignment_format='PIR')
aln.write(file='aligned_ancestor.pap', alignment_format='PAP')
