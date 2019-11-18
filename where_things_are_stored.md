Sometimes we look for some data and we dont remember where they are, conversely sometimes we are not sure what this folder contains.

I'll try to maintain a description of the directory that are useful to us on proj64
Unless specified otherwise everything is under :
/gpfs/bbp.cscs.ch/project/proj64/

**home/bolanos/2019-11-14_central_flick_full**  
4s simulation when we feed a flick stimulus (one spike in 16 fibers at 2s) to the central column (as defined by S.)

**home/bolanos/2019-11-14_S1_slices**  
Subdivivision of the S1.v6 circuit into "horizontal" layer following the shape of the whole thing.
Each subdivision is simply a text file containing the gids of the neurons

**home/bolanos/2019-10-02_bluelight_test**  
Contains Sirios preliminary simulation done begining of october

**/gpfs/bbp.cscs.ch/project/proj64/home/reimann/S1.v6_group_con_mats/group_con_mats.h5**  
Contains matrix that Michael extracted of column like division of a previous version of S1.v6

**/home/ninin/neuron_data_oldcircuit.pickle**
A panda dataframe with the list of neuron of S1.V6 (aka old circuit) and their information such as mtype layer position and so on. [jlazovskis] I don't see this file in this directory

**/home/lazovski/visualizing-neuron-communities/cons_locs_pathways_mc2_Column.h5**
Contains old circuit information (type, xyz location, gid, etc). All GIDs are shifted by 62693. I think this is also available on the BlueBrain Portal somewhere.
