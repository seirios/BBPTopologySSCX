# Q&A

+ [seirios] What files do you work with when analyzing connectivity? (e.g. synapse files, target files, etc.)

    [JasonPSmith] Ideally some kind of adjacency matrix is best. To compute the counts using flagser the data needs to be
    either just a text file with a list of edges (i.e. a list of the form A B, where there is a connection from neuron A to B), 
    or as a compressed sparse matrix in the same format as the mouse data here: https://portal.bluebrain.epfl.ch/downloads/. 
    But any format is fine as we can easily map it into one of these "flagser-friendly" formats.

+ [seirios] When you count simplices, can you also list them (i.e. list what GIDs are members of each simplex and their positions therein)? I'm thinking it may be interesting to stimulate specific (groups of) simplices and see what happens, specially if we consider their layer-specific directionality.

    [JasonPSmith] It straighforward to list the GIDs of the neurons in the simplices, however issues arise due to the sheer 
    quantity of data this produces. Using the count we have for the somatosensory I estimate we'd need at least 0.5TB to store
    a list of all the GIDs of all the simplices. What might be better is to just store the GIDs of all the top dimensional
    simplices, this shouldn't take too much space.
    [jlazovskis] Partial answer: Aberdeen group is also working on understanding which "communities" (neuron with high clustering coefficient and all its neighbors) rather than simplices are interesting. GIDs of neurons in top 15 communities are in <code>home/lazovski/visualizing-neuron-communities/gid_position_voltage_spikes/n_gid</code> for <code>n</code> in <code>00,...,14</code>.
   
    
## Template

+ [userA] Example question?

    [userB] Example reply
    
    [userC] Example second reply
