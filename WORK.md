# Work assignment

[jlazovskis] This document contains information about who will do which jobs / run which experiments. Also information on what to do differently.

## Redoing Frontiers experiments

[jlazovskis] This is about redoing the Frontiers analysis on a larger circuit, either the whole somatosensory cortex, or a cylinder of it.

+ [Figure 2](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g002.jpg)

+ [Figure 3](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g003.jpg)
    + A1 - A3 will be different, as now L2 and L3 are separate. 

+ [Figure 4](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g004.jpg)
    + E is very interesting

+ [Figure 5](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g005.jpg)

+ [Figure 6](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g006.jpg)
    + Something like C would be great

+ Figure S5
    + Similar to Figure 6E, but in more detail

+ Figure S8


## New experiments

+ [JasonPSmith] For each neuron G we can compute the number of simplices for which G is a sink/source,
  we can then look at the distribution of sink/source neurons by type.

    - [seirios] Cool! Definitely, doing analyses at the level of cell type is the next step!




# Global view
[Nicolas] I'll try to details for each proposed experiments what I think the goals are, what needs to be done, how we can do it, and what I(we) might expect.
For clarity it may be easier to give each experiments his own file.

We soon(ish) will have access to three S1v6 somatosensory circuit each based on the same rat statistics but with different seeds (as opposed to frontier where we had five different rat and an average one).

Such a circuit was already created a  year ago, those three  have seen some improvment (in what?) from the earlier version. 

To have some numbers in mind here is the results of the counting of simplices of this earlier circuit that Gard did a year ago.

+ Dim 0: 1722604 (~1.7 million)
+ Dim 1: 1059736608 (~1.1 billion)
+ Dim 2: 22705492972 (~22 billion)
+ Dim 3: 58421988203 (~58 billion)
+ Dim 4: 30838397649 (~31 billion)
+ Dim 5: 5082042041 (~5.1 billion)
+ Dim 6: 337370565 (~0.33 billion)
+ Dim 7: 9360457 (~9.4 million)
+ Dim 8: 108025 (~0.1 million)
+ Dim 9: 458

We probably cannot compute any homology on such a big complexe, but possibly on smaller subgraph.


# Structural vs activity
The experiments we want to do can be divided  roughly into the one who needs activity and the one who only looks at the circuit( structural). Obviously we will use structural results also with activity.
So first lets descibe the *easy* structural computation and their variation

## Structural Experiments
### Couting Simplices (motifs) aka figure 2 (also part of figure 3)

+ [Figure 2](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g002.jpg)

**Goal**:  
The goal here is to redo the computation Gard Did on the three new circuit. We then compare those number to other more or less random graph with similar properties (ER with same number of vertex and edges for example).


**How to do it**:
This is pretty straightforward with flagsercount, but it can takes time. Also storing simplices might not be possible (at least not all of them) something that would often be nice. One possible way to get around this is to only store the highest dimension, to store a random subset, or to store simplices for smaller (meaningfull) subgraph, whatever meaningfull would mean.

**Variations**:  
Here is a non comprehensive list of variation around this, some may be stupid/useless:

+ Divide the big circuit into *columns* then compare them or compare to v5
+ Grow the circuit from a small one to the complete one (maybe start with a cylinder to keep all layers then increase the radius)
+ On the same idea, I think Henry M. asked what is the smallest region with highest dimensional simplices (this would be the smallest volume of the highest dimensional simplices
but I think he meant more on something related to the previous item)
+ Harder but may be possible, count other motifs (cliques or tournaments), all motifs on 3 vertices 

 [Figure 3](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g003.jpg)
 give us some other things we can do

+ divide by excitatory/inhibitory
+ by layers

### Describing Simplices
**Goal**:  
Understand simplices with respect to usual descriptor of the neuron, here we are still looking at thing without any activity.

**How to do it**:
With the list of simplices its elementary to do. What takes time is to analyze and trying to makes sense of what you see. There is a ton of variation 
so its easy to get lost.

**Variations**:
So the goal is to look at things like *information given by simplices* vs *information of the neuron*.

For example : "highest dimension a neuron is part of" vs "EXC/INH" ( or mtype or layer) etc.

Here are a few neuronal information you can get from the listing of the simplices (in fig3 for instance):
+ the highest dimension of a simplice a neuron is part of
+ number of n-simplices  a neuron belongs to


jason proposal:
+ number of simplices a neuron is a sink or source

We can also look at population and not only at a neuron level, ie fig3.C.


## Activity Experiments

Like we discussed on the meeting of october the 29th, we need to define stimuli. This is probably something that would need to be discussed in the next meeting 
with Henry M. and maybe before with Michael.

I think that in the context of following frontiers protocol, we should take the same stimuli (but this might be a bad idea for many reason)
+ [Figure 4](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g004.jpg)

In any case this stimuli were designed for one column, so even if we settled on using this, how do we apply this to the whole SSCx?
One idea was to activate only one column (so very close to frontiers). At the opposite there is giving the stimuli to the whole network and every combination in between.
Also even this is not well defined for me, is the circuit strictly divided into column to which we can give the same stimulus or is it more blurry?

For now lets suppose we have some stimuli given to the circuit, and describes the experiments:

### Correlations
**Goal**:  
compute pearson correlation between any pairs of neuron. This would be a preliminary steps  to a lot of things.

**How to do it**:

I'm not sure how much time it'd take to compute those though. I think computing correlation on 30K took a few minutes so on 1.7M it may be 50^2 times longer so at least a week.
Obviously we can use many nodes (I'm also not sure if the computation was using all the core It was a scipy thing so I would say no). Overall if we are efficient with parallelization it should actually be pretty fast (250 cpu per node should make this takes a few hours top).

**Variations**:
Its not always clear what data we want to compute correlation on. By this I mean we can have many correlation for each simulation, or we can concatenate those( what they did in frontier) to get only one number per pair of neuron.

Once we have correlations and simplices computed we can do:

+ [Figure 4](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g004.jpg) E, ie correlation in a simplex depeding on respective position
+ [S5](S5.png) same as 4E with variation
+ also other in fig 4
+ [S8](S8_corelation_VS_topology.png) but I dont understand fully this one, we should ask Micheal how everythin is defined


### Transmission Response 
**Goal**:  
Compute the TR graphs and their topology

**How to do it**:
Micheal's code, we should probably take frontiers parameter. Its not clear atm wether or not we will be able to compute homology of those TR.


Once TR computed we can do:

+ [Figure 6](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g006.jpg)C doesnt necesseraly require 6B,
+ [Figure 6](https://www.frontiersin.org/files/Articles/266051/fncom-11-00048-HTML-r3/image_m/fncom-11-00048-g006.jpg)A,B,D require betti computation but we could try just with cell count or EC

### Calcium Scan Activity

It might be interesting to look at those.







