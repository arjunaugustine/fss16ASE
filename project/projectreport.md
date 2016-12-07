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


##Motivation

##Algorithms Used
In this project we have tried different variants of genetic algorithms such as the regular GA, the NSGA II and the SPEA II. We have also used two dominance functions, the Binary Domination and the Continuous Domination with each of the above mentioned algorithms. For the 6 resulting variations, we have considered 200 members (populations size) for 250 generations. The different variants are compared using stats.py for comparison in terms of Spead and IGD (Median and IQR). 

###GA


###NSGA II


###SPEA II

  
##Graphs


##Observations


##Learnings

