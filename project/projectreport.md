#Sofwtare Product Line Optimization

##Introduction and Overview

What is SPLOT ? 
SPLOT stands for Software Product Lines Online Tools. The primary goal of SPLOT is to put Software Product Lines research into practice through the delivery of state-of-the-art online tools targeting academics and practitioners in the field. With SPLOT one can edit, debug, analyze, configure, share and download feature models instantly. SPLOT supports the notion of feature-based interactive configuration in which users make configuration decisions over a feature model (e.g select/deselect a feature) and the configuration engine automatically propagates those decisions to enforce their consistency. This results in a backtrack-free configuration process benefiting users that are never forced to review past decisions (unless they wish to do so intentionally).
This project looks at a couple of models with varying number of decisions and objectives and applies various genetic algorithms to find the optimal pareto frontier of solutions. The leaf nodes of a feature tree constitute the decisions for a model. They are populated randomly and the tree is evaluated bottom up to find the number of features implemented, the total cost of implementation and the number of constraints violated in the process. These objectives are optimized as the algorithm proceeds. It also compares the results of the genetic algorithms with different dominance functions and makes some observations as to which algorithms performs better with SPLOT models in general and some models in particular.

##Source Code and Description

The project source code can be found at here[https://github.com/arjunaugustine/fss16ASE/tree/master/_project]

The file project.py is the executable for the project. It has dependencies on constraintrepo.py, constraint.py, flag.py, node.py, statutils.py, tree.py and xmlparser.py. 

* project.py - executable
* constraintrepo.py - Houses the Constraint Repository that evaluates the violations for a model
* constraint.py - A single constraint is represented by this class
* flag.py - A helper class that allows to toggle the constraints
* node.py - A single node in the feature tree
* statutils.py - A subset of utilities from stats.py
* tree.py - The feature tree is represented by this class
* xmlparser.py - This module reads an xml, parses it into the tree and the constraint repository.

To run the code:

Add the required model(s) in the list
models_ = ['Bike.xml'] 

Make sure the xml is present in the directory
The repo contains the 8 models this project is tested with.

Update the population size to a good value 
pop_size=250 (default)

Update the number of generations to a good value
gens=200

And run,
run ./project.py or python project.py

##About the Model(s)
This project looks at the following nine models.
* Smart Home
* Bike
* Classic Shell
* Arbol
* Enterprise System
* FM Test
* anking Software
* Car
* Billing

These models vary in the number of decisions and cross tree constraints and the algorithms aim at optimizing them with respect to the following objectives (expected direction in parantheses)

* Number of Features Implemented (Maximize)
* Number of Constraints Violated (Minimize)
* Total Cost of Implementation (Minimize)

The following table depicts the details for each of the nine models.

<p align="center">
  <img src="/project/img/models_.png?raw=true" alt="All the models image" width=600/>
</p>

And below is a feature diagram (from the Linux model)

<p align="center">
  <img src="/project/img/feature_diagram.png?raw=true" alt="feature diagram" width=600/>
</p>

and one of the features expanded into further finer features.

<p align="center">
  <img src="/project/img/feature_expanded.png?raw=true" alt="one feature expanded" width=600/>
</p>

The SPLOT models represent the features and their dependencies and constrainsts using an xml. For a model that represents mobile phone the feature tree and the corresponding xml can be represented as below.

<p align="center">
  <img src="/project/img/mobilephone_featuretree.png?raw=true" alt="feature tree for mobile phone" width=600/>
</p>

<p align="center">
  <img src="/project/img/mobile_xml.png?raw=true" alt="mobile phone xml" width=300/>
</p>
###XML Parser
In this project we developed a custom xml parser that reads an xml configuration file and populates the features, constraints, the cost, the presence(absence) of features etc for any model. The parser sets up any model in a way that a genetic algorithm can create points of, that we later evaluate and compare in order to select or discard as good or bad candidates for future generations of iterations. There is more or less a direct mapping between the feature tree and the tree that is coded up as part of the parsing of it. The following is a class diagram of a sample tree that gets parsed.

<p align="center">
  <img src="/project/img/featuretree_classdiagram.png?raw=true" alt="Feature Tree Class Diagram" width=600/>
</p>

Cross tree constraints, much like the cost associated with the product and the number of features that get implemented is another objective that we try to optimize(minimize). To evaluate the constraints better, we have created a constraint repository class that parses the constraint section of the xml and creates Flag objects and Constraint objects that can be evaluated easily based on the decisions a point is randomly assigned. The follwing class diagram represents the constraints. 

<p align="center">
  <img src="/project/img/constraints_classdiagram.png?raw=true" alt="Constrints Class Diagram" width=600/>
</p>

The following sequence diagram shows how the constraint repository class makes use of the constraint class and Flag class to evaluate the number of constraints which is a very important objective for these models.

<p align="center">
  <img src="/project/img/sequence_diagram.png?raw=true" alt="Sequence Diagram" width=600/>
</p>


##Algorithms Used
In this project we have tried different variants of genetic algorithms such as the regular GA, the NSGA II and the SPEA II. We have also used two dominance functions, the Binary Domination and the Continuous Domination with each of the above mentioned algorithms. For the 6 resulting variations, we have considered 200 members (populations size) for 250 generations. The different variants are compared using stats.py for comparison in terms of Spread and IGD (Median and IQR). These algorithms are briefly discussed below (taken from lecture slides)

###GA

Genetic Algorithm is a Meta-heuristic Inspired by Natural Selection. Quite simply, we consider a set of points and assign them random decision values, in this case True or False as to whether a leaf node in the SPLOT feature tree is a feature that is present or absent. We consider N such points where N is the pre-determined number that we call the population size. Each point is further evaluated to see how fit it is to be considered for future iterations. In this case we calculate the number of features that are implemneted, the cost associated with all the features associated and the number of constraints that are violated in the process. If we see a point is fit (No constraints violated is a good condition for this case) we consider it for future runs of the GA. Also, we pick two points that are fit and cross over a couple of their features and mutate the resulting point with a very low probability. The new points along with the fit parents and old points make the new ground set we do selection (elitism) from. For comparing two points we could use a binary domination method or a continuous domination method. We pick the best N points and continue the same method, until we no longer make any significant progress (early termination) or we run out of the number of runs. The resulting set of points form a pareto frontier of solutions. 

###NSGA II

The NSGA II basically follows the same underlying principle of a GA except for the following differences. The selection works a bit differently. Divide candidates into frontiers. For some small number, keep the top i-frontiers until we reach that number. If you fill up half way through a frontier, delete some using crowd-pruning. For the ranking mechanism we employ the fast non dominated sort algorithm as shown below. 

<p align="center">
  <img src="/project/img/nondominated.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

This change is wired into the elitism function. For the secondary sorting, instead of doing a crowd pruning, we have employed a sorting based on the fitness of all the points on the last frontier and kicked out the points that don't make the cut. As a rule of thumb this performs better than GA in almost all of the runs, as we will see below.

###SPEA II

SPEA II also is a genetic algorithm, with the following differences. The fitness function takes into account the dominance of each point along with the euclidean distance of a point in the frontier to k other points where k is the root of sum of sizes of the population and the archive. The following functions as shown below are used 

* CalculateRawFitness() number of solutions that a give solution dominate.
* CandidateDensity() estimates the density of local Pareto front
* Euclidean distance of the objective values to the K nearest neighbors (in objective space)
* K = sqrt( size(Archive) + size(Population) )
* PopulateWithRemainingBest() fills in Archive with remaining candidate solutions in order of fitness.
* RemoveMostSimilar() truncates Archive, removing members with the smallest difference in their objective scores.
* SelectParents: all pairs comparison, remove dominated ones
  
and the algorithm is as shown below :

<p align="center">
  <img src="/project/img/spea2.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

##Output

Like already discussed above we have 3 objectives to optimize for all the SPLOT models in this project. For every model, we have Cost vs. Features, Cost vs. Constraints and Constraints vs. Features graphs in 2D and Cost vs. Constraint vs. Features graph in 3D. The 2D graphs are to better visualize the pareto frontier (we might not always have a better looking pareto frontier because of the third objective not being represented in the graph). 
Each of the above mentioned graphs is there for each of the 6 variants that we are running here. (GA with CDOM, GA with BDOM, NSGA II with BDOM, NSGA II with CDOM, SPEA II with BDOM, SPEA II with CDOM). Following are various algorithms for the Arbol model.

###Cost vs. Constraints
####GA with BDOM

<p align="center">
  <img src="/project/img/4.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####GA with CDOM

<p align="center">
  <img src="/project/img/2.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with BDOM

<p align="center">
  <img src="/project/img/3.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with CDOM

<p align="center">
  <img src="/project/img/1.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with BDOM

<p align="center">
  <img src="/project/img/6.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with CDOM

<p align="center">
  <img src="/project/img/5.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

###Constraints vs. Features
####GA with BDOM

<p align="center">
  <img src="/project/img/2_5.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####GA with CDOM

<p align="center">
  <img src="/project/img/2_1.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with BDOM

<p align="center">
  <img src="/project/img/2_3.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with CDOM

<p align="center">
  <img src="/project/img/2_4.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with BDOM

<p align="center">
  <img src="/project/img/2_2.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with CDOM

<p align="center">
  <img src="/project/img/2_6.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

###Features vs. Cost

####GA with BDOM

<p align="center">
  <img src="/project/img/3_3.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####GA with CDOM

<p align="center">
  <img src="/project/img/3_6.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with BDOM

<p align="center">
  <img src="/project/img/3_5.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with CDOM

<p align="center">
  <img src="/project/img/3_2.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with BDOM

<p align="center">
  <img src="/project/img/3_4.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with CDOM

<p align="center">
  <img src="/project/img/3_1.png?raw=true" alt="Sequence Diagram" width=600/>
</p>


###Cost vs. Constraints vs. Features

####GA with BDOM

<p align="center">
  <img src="/project/img/gabdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####GA with CDOM

<p align="center">
  <img src="/project/img/gacdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with BDOM

<p align="center">
  <img src="/project/img/spea2bdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####SPEA2 with CDOM

<p align="center">
  <img src="/project/img/spea2cdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with BDOM

<p align="center">
  <img src="/project/img/nsga2bdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>

####NSGA2 with CDOM

<p align="center">
  <img src="/project/img/nsga2cdom.png?raw=true" alt="Sequence Diagram" width=600/>
</p>


##Observations on Graphs

* There are a couple of observations we made from the output and the graphs above. In almost all of the models, the good old GA with Binary Domination fell short of a major goal. To produce models that have zero constriant violations. For the purpose of this project, the number of constraints violated was just another objective and was not wired into the validity of a point. However, a product that violates no constraints is really a desirable outcome.This however was mitigated in two ways - Either by changing the algorithm to the better counterparts - nsga2 and spea2 or by changin the binary domination to continuous domination.

* One thing is invariably obvious in all the models and their output. The algorithms that run the continuous domination function tend to have the solutions kind of clustered together and not spread across evenly as binary domination would have.

* The SPEA2 algorithm prunes data from the more clustered regions of the graph and retains the points on the pareto frontier that are distant from other points. This increases the variability in the solutions. However when SPEA2 is used with binary domination, since most of the models have multiple objectives domination functions often do not return a clear winner. This leads to the fitness function being dominated by the euclidean distance than by the regular fitness count (the number of people dominated by the point under consideration). This in turn led to some graphs with solutions split across the pareto frontier. 

##Statistical Performance Comparison
The following part shows the statistical performance output using stats.py
Project implementation details : 

* Population size = 200,
* Number of runs = 250,
* Number of models : 9,
* Number of variants = Number of algorithms x Number of dominance functions = 6, 
* Number of repeats = 10.

####Enterprise System
<p align="center">
  <img src="/project/img/enterprisesys.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/enterprisesysmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/enterprisesysiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Billing
<p align="center">
  <img src="/project/img/billing.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/billingmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/billingiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Arbol
<p align="center">
  <img src="/project/img/arbol.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/arbolmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/arboliqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####FM Test
<p align="center">
  <img src="/project/img/fmtest.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/fmtestmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/fmtestiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Banking Software
<p align="center">
  <img src="/project/img/bankingsw.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/bankingswmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/bankingswiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Classic Shell
<p align="center">
  <img src="/project/img/classicshell.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/classicshellmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/classicshelliqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Car
<p align="center">
  <img src="/project/img/Car.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/carsmedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/carsiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
####Bike
<p align="center">
  <img src="/project/img/bike.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/bikemedian.png?raw=true" alt="Sequence Diagram" width=600/>
</p>
<p align="center">
  <img src="/project/img/bikeiqr.png?raw=true" alt="Sequence Diagram" width=600/>
</p>



##Observations on statistical comparison

* Even though observations like these vary from model to model, nsga2 with cdom is a clear winner over other 5 variants for most of these models. The choice of cdom is great for the algorithms, but the time complexity - performance tradeoff needs to be studied further for this. The Spread (Median) comparison shows that the bdom variants of all the algorithms have better spread. The Banking Software Model is a very good example to study this trend. Also on the same note, NSGA II fares well with cdom compared to SPEA II with cdom. This is very evident in the Billing model. This trend is however not maintained in the Car model.

* The IGD (Median) on the other hand is more for the ga algorithm irrespective of the dominance functions that were used. This trend is fairly uniform across all the models.

* When it comes to the Spread (IQR) comparison, we find high variability in values as are visible from the percentile charts and histograms. If you take the Billing model for example, the Spread is value is better for the BDOM algorithms, but NSGA II with cdom deserves a special mention here because it does just as well as its bdom counterpart. However for most other models, the spread is really high for the bdom algorithms especially the NSGA II and SPEA II versions. It would Classic Shell and Billing models are anomalies here.

* The IGD (IQR) comparison unfortunately does not give us any conclusive trends. The models happen to be so different that the values do not show a specific trend. However GA with BDOM consistently has higher IGD (IQR) values in all the models that were tested.

##Lessons, Mistakes, Future

* CDOM function implementation requires a special mention here. The ranking scheme of fast non dominated sort in NSGA II assumes transitivity of dominance. It says when the rank 0 point exits the system (after decrementing the rank each of the points that it dominates by one) it expects automatically that the next best in the system will have a rank 0. This might not always be the case. This issue made the NSGA II algorithm run in infinite loops. This was later fixed by considering the minimum rank of all the remaining points in the frontier and not looking for rank 0. Additionally we did not need to decrement the rank of every other point dominated by the rank 0 point. 

* The fitness function that is used in SPEA II takes into account the euclidean distance as well as the good old regular fitness by dominance count. This however proved really time consuming for not a much better result. The tradeoff was really not in favor of the new fitness function. So in this project the SPEA II version uses this fitness regime only as a secondary sorting mechnism for pruning from a clustered areas in the frontier. This considerably improved the performance. 

* SPEA II in combination with BDOM sometimes gives unexpected results, especially for models with very many objectives. This was because BDOM is indecisive when it comes to multiple objectives and in such a case the fitness function is overwhelmingly just a Euclidean Distance function. This sometimes divides the pareto frontier in a bad shape.

* As a future work, we could implement early termination technique into the number of runs for this GA variants measuring performance every step. Additionally, the point evaluation can be made faster by evaluating every node statically by introducing some pre-processing. 
