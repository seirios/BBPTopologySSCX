# Q&A

+ [seirios] What files do you work with when analyzing connectivity? (e.g. synapse files, target files, etc.)

    [JasonPSmith] Ideally some kind of adjacency matrix is best. To compute the counts using flagser the data needs to be
    either just a text file with a list of edges (i.e. a list of the form A B, where there is a connection from neuron A to B), 
    or as a compressed sparse matrix in the same format as the mouse data here: https://portal.bluebrain.epfl.ch/downloads/. 
    But any format is fine as we can easily map it into one of these "flagser-friendly" formats.

+ [seirios] When you count simplices, can you also list them (i.e. list what GIDs are members of each simplex and their positions therein)? I'm thinking it may be interesting to stimulate specific (groups of) simplices and see what happens, specially if we consider their layer-specific directionality (and also the cell types involved).

    [JasonPSmith] It straighforward to list the GIDs of the neurons in the simplices, however issues arise due to the sheer 
    quantity of data this produces. Using the count we have for the somatosensory I estimate we'd need at least 0.5TB to store
    a list of all the GIDs of all the simplices. What might be better is to just store the GIDs of all the top dimensional
    simplices, this shouldn't take too much space.
    
    [jlazovskis] Partial answer: Aberdeen group is also working on understanding which "communities" (neuron with high clustering coefficient and all its neighbors) rather than simplices are interesting. GIDs of neurons in top 15 communities are in <code>home/lazovski/visualizing-neuron-communities/gid_position_voltage_spikes/n_gid</code> for <code>n</code> in <code>00,...,14</code>.
    
    [Kepsa] It might be interesting to stimulate input neurons or simplices in few top communities. So to stimulate simplices whose sink is the neuron in the center of a community. The idea I'm thinking here is to see whether most of observed activity still propagates through the most densily connected communities. And if so, how many of the communities are activated with similar levels if stimulus is applied to only few of them.
    
    - [seirios] This sounds interesting. Have you observed if, after a given stimulus, the number of most active communities is small, and if it varies with the stimulus, so as to represent a kind of signature of the stimulus? Is it possible to infer (or discriminate) stimuli from the communities they activate the most? This could provide a concrete substrate for ideas of population coding in terms of communities and/or groups of simplices.
   
+ [seirios] How do we handle border effects? Both in the whole circuit and in any sub-target there will be cells whose connectivity is incomplete due to lack of neighbors within the target, and this may bias the computations. How do we guard against this? One idea for the whole circuit was to discard all cells within some distance of the border. However, given any sub-target, should we discard the connections with cells that don't belong to it?


## Template

+ [userA] Example question?

    [userB] Example reply
    
    [userC] Example second reply
