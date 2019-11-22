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
+ [slice00-03 aka outer ring](fig/Slice03.png)
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


**home/bolanos/2019-10-02_bluelight_test**  
Contains Sirios preliminary simulation done begining of october

**home/reimann/S1.v6_group_con_mats/group_con_mats.h5**  
Contains matrix that Michael extracted of column like division of a previous version of S1.v6

**home/ninin/neuron_data_oldcircuit.pickle**<br>
A panda dataframe with the list of neuron of S1.V6 (aka old circuit) and their information such as mtype layer position and so on. 

**/gpfs/bbp.cscs.ch/home/lazovski/visualizing-neuron-communities/cons_locs_pathways_mc2_Column.h5**<br>
Contains old circuit information (type, xyz location, gid, etc). All GIDs are shifted by 62693. I think this is also available on the BlueBrain Portal somewhere. [Nicolas] I believe this one is the v5 there might be some confusion because I wrote "oldcircuit.pickle" for the first version of s1v6 we had (hence old in regard to the new one we will get) [jlazovskis] Agreed. I'll keep it here for now because I'm used to accessing this, not yet the newer-older files.
