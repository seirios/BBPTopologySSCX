Sometimes we look for some data and we dont remember where they are, conversely sometimes we are not sure what this folder contains.

I'll try to maintain a description of the directory that are useful to us on proj64
Unless specified otherwise everything is under :
**/gpfs/bbp.cscs.ch/project/proj64/**

**home/bolanos/2019-11-14_central_flick_full**  
4s simulation when we feed a flick stimulus (one spike in 16 fibers at 2s) to the central column (as defined by S.)

**home/bolanos/2019-11-14_S1_slices**  
Subdivivision of the S1.v6 circuit into "horizontal" layer following the shape of the whole thing.
Each subdivision is simply a text file containing the gids of the neurons.  
Here is some vizualization (its a sample of all thing), for some slice, especially the one close to the center since there is some disconnection happening
+ [slice00-03 outer onion layer](fig/Slice03.png)
+ [slice24-25](fig/Slice24-25.png)
+ [slice25-26](fig/Slice25-26.png)
+ [slice26-27](fig/Slice26-27.png)
+ [slice27-28](fig/Slice27-28.png)
+ [slice28-NNN](fig/Slice28-NNN.png)


**home/bolanos/2019-11-14_S1_radial**  
Subdivision of S1.v6, starting from a small cylinder across all layers, then growing (so each subdivision is a ring except the last one which is everything minus one big cylinder
+ [radial-030-000 only 459 neuron](fig/radial-030-000.png)
+ [radial-060-000](fig/radial-060-030.png)
+ [radial-660-630](fig/radial-660-630.png)
+ [radial-NNN-660](fig/radial-NNN-660.png)

**home/bolanos/2019-11-14_S1_central**  
Subdivision of S1.v6 at some distance to the border
central_gids.txt is the one with saturated connectivity.


**home/bolanos/2019-10-02_bluelight_test**  
Contains Sirios preliminary simulation done begining of october

**home/reimann/S1.v6_group_con_mats/group_con_mats.h5**  
Contains matrix that Michael extracted of column like division of a previous version of S1.v6

**home/ninin/neuron_data_oldcircuit.pickle**<br>
A panda dataframe with the list of neuron of S1.V6 (aka old circuit) and their information such as mtype layer position and so on. 

**/gpfs/bbp.cscs.ch/home/lazovski/visualizing-neuron-communities/cons_locs_pathways_mc2_Column.h5**<br>
Contains old circuit information (type, xyz location, gid, etc). All GIDs are shifted by 62693. I think this is also available on the BlueBrain Portal somewhere. [Nicolas] I believe this one is the v5 there might be some confusion because I wrote "oldcircuit.pickle" for the first version of s1v6 we had (hence old in regard to the new one we will get) [jlazovskis] Agreed. I'll keep it here for now because I'm used to accessing this, not yet the newer-older files.

**/gpfs/bbp.cscs.ch/project/proj102/simplices/S1V6**
Contains the list of all simplices of the S1v6 circuit, so far only dim 6,7,8 & 9 are stored, (due to space issues)

**/gpfs/bbp.cscs.ch/home/ninin/proj102/matrices/S1v6**  
Contains the old circuit in sparse format. You have either indices.npy and indptr.npy (should be csr) or coo format with col and row.  
The circuit is  here:  
/gpfs/bbp.cscs.ch/project/proj64/circuits/S1.v6a/20171206/  

The easiest way to access it is either via bluepy or directly looking at the nrn h5 file.  
/gpfs/bbp.cscs.ch/project/proj64/circuits/S1.v6a/20171206/ncsFunctionalAllRecipePathways/nrn.h5  
This file contain a dataset name "a+gid" for each neuron. This dataset contains an Mx19 dataset with M=number of presynapic neuron (or postsynapic for rn_efferent.h5). Here are the description I was given on those file that explain the 19 entry:
/a+gid (e.g. a60129)  
0: Connecting gid: presynaptic for nrn.h5, postsynaptic for nrn_efferent.h5  
1: Axonal delay: computed using the distance of the presynaptic axon to the post synaptic terminal (milliseconds) (float)  
2: postSection ID (int)  
3: postSegment ID (int)  
4: The post distance (in microns) of the synapse from the begining of the post segment 3D point, or \-1 for soma connections  (float)  
5: preSection ID (int)  
6: preSegment ID (int)  
7: The pre distance (in microns) of the synapse from the begining of the pre segment  3D point (float)  
8: g_synX is the conductance of the synapse (nanosiemens) (float)  
9: u_syn is the u parameter in the TM model (0-1) (float)  
10: d_syn is the time constant of depression (milliseconds) (float, was 'int' before 2017/10/13 see https://bbpteam.epfl.ch/project/issues/browse/BLPY-108)  
11: f_syn is the time constant of facilitation (milliseconds) (float, was 'int' before 2017/10/13 see https://bbpteam.epfl.ch/project/issues/browse/BLPY-108)  
12: DTC - Decay Time Constant (milliseconds) (float)  
13: synapseType, the synapse type Inhibitory < 100 or Excitatory >= 100 (specific value corresponds to generating recipe)  
14: The morphology type of the pre neuron.  Index corresponds with circuit.mvd2  
15-16: BranchOrder of the dendrite, BranchOrder of the axon (int,int)  
17: ASE Absolute Synaptic Efficacy (Millivolts) (int)  
18: Branch Type from the post neuron(0 for soma, 1 for axon and 2 for basal and 3 for apical) (int)  

**/gpfs/bbp.cscs.ch/home/ninin/proj102/matrices/bio1**
Here we should extract a sparse version of the bio1 circuit.
