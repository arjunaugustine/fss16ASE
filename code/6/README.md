##TODO
Rewrite your SA and MWS code such that you can run the following loop:

    for model in [Schaffer, Osyczka2, Kursawe]:

        for optimizer in [sa, mws]:
    
              optimizer(model())

This is the generic experiment loop that allows for rapid extension to handle more models and more optimizers.

##Optimizer as function

The above code assumes that mws, sa are functions that accept one argument: a description of the model they are processing.

##Model as Class

For the above loop to work, each model (e.g. Schaffer) has to be class that produces an instance via model(). That model defines:
  * the number of decisions;
  * the number of objectives;
  * the name of each decision/objective;
  * the min/max range of each decision/objective;
  * the any function that generates an instance of the decisions(randomly between min and max for each decision)
  * the ok function that checks if a particular candidate is valid (for Schaffer and Kursawe, this returns True while for Osyczka2, this does some checking).
  * the eval function that computes the objective scores for each candidate
  
##Outputs

![alt tag](https://github.com/arjunaugustine/fss16ASE/blob/master/code/5/Screen%20Shot%202016-10-04%20at%209.25.40%20PM.png)
![alt tag](https://github.com/arjunaugustine/fss16ASE/blob/master/code/5/Screen%20Shot%202016-10-04%20at%209.26.34%20PM.png)

Making sense of MWS output:

1.  The first column indicates the current best solution.

2.  The second column indicates the energy of the random solution selected in this iteration.

3.  A '+' indicates a new maxima. A '+' in the line adds to line length.

4.  The class printed at the bottom is the best solution point.
