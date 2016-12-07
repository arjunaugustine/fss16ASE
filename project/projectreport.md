#Sofwtare Product Line Optimization

##Introduction

What is SPLOT ? 
SPLOT stands for Software Product Lines Online Tools. The primary goal of SPLOT is to put Software Product Lines research into practice through the delivery of state-of-the-art online tools targeting academics and practitioners in the field. With SPLOT one can edit, debug, analyze, configure, share and download feature models instantly. SPLOT supports the notion of feature-based interactive configuration in which users make configuration decisions over a feature model (e.g select/deselect a feature) and the configuration engine automatically propagates those decisions to enforce their consistency. This results in a backtrack-free configuration process benefiting users that are never forced to review past decisions (unless they wish to do so intentionally).
This project looks at a couple of models with varying number of decisions and objectives and applies various genetic algorithms to find the optimal pareto frontier of solutions. It also compares the results of the genetic algorithms with different dominance functions and makes some observations as to which algorithms performs better with SPLOT models in general and some models in particular.


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
  <img src="/project/img/feature_diagram.png?raw=true" alt="All the models image" width=600/>
</p>

and one of the features expanded into further finer features.

<p align="center">
  <img src="/project/img/feature_expanded.png?raw=true" alt="All the models image" width=600/>
</p>

The SPLOT models represent the features and their dependencies and constrainsts using an xml. For a model that represents mobile phone the feature tree and the corresponding xml can be represented as below.

<p align="center">
  <img src="/project/img/mobilephone_featuretree.png?raw=true" alt="All the models image" width=600/>
</p>

<p align="center">
  <img src="/project/img/mobile_xml.png?raw=true" alt="All the models image" width=600/>
</p>
###XML Parser


###Feature Tree


###Constraint Repository
  
  
##Motivation

##Algorithms Used


###GA


###NSGA II


###SPEA II

  
##Graphs


##Observations


##Learnings

