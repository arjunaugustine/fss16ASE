# Sapienz: Multi-objective Automated Testing for Android Applications

## Key Words
###[Search Based Testing:](https://philmcminn.staff.shef.ac.uk/publications/c18.pdf) 
Search-Based Software Testing is the use of a meta-heuristic optimizing search technique, such as a Genetic Algorithm, to automate or partially automate a testing task; for example the automatic generation of test data. Key to the optimization process is a problem-specific fitness function. The role of the fitness function is to guide the search to good solutions from a potentially infinite search space, within a practical time limit.

###[Pareto Optimality:](https://en.wikipedia.org/wiki/Pareto_efficiency)
Pareto efficiency, or Pareto optimality, is a state of allocation of resources in which it is impossible to make any one individual better off without making at least one individual worse off.

###[Fuzz Testing:](http://searchsecurity.techtarget.com/definition/fuzz-testing)
Fuzz testing or fuzzing is a software testing technique used to discover coding errors and security loopholes in software, operating systems or networks by inputting massive amounts of random data, called fuzz, to the system in an attempt to make it crash.

###SAPIENZ
Sapienz is an approach(tool) to Android testing that uses multi-objective search-based testing to automatically explore and optimise test sequences, minimising length, while simultaneously maximising coverage and fault revelation

## Motivation:
There are over 1.8 million apps available from the Google Play marketplace, as of January 2016. For developed internet markets such as the US, UK and Canada, mobile app usage now dominates traditional desktop software usage. Unfortunately, testing technology has yet to catch up, and software testers are faced with additional problems due to device fragmentation, which increases test effort due to the number of devices that must be considered. According to a study on mobile app development, mobile app testing still relies heavily on manual testing, while the use of automated techniques remains rare.
The currently used test sequences for the Automated test tool monkey are very large. Sapienz is the first approach offering multi-objective automated Android app exploratory testing that seeks to maximise code coverage and fault revelation, while minimising the length of fault-revealing test sequences.

## Informative Visualizations:
An abstract State-Machine for the app - Aard Dictionary, a dictionary and online Wikipedia reader is shown in the paper. It shows different states and transitions between them making it easy to identify the different transitions which led to termnation of the app.

## Baseline Results:
Four apps were selected for testing MobiGUITAR - Aard Dictionary, Tomdroid, Book Catalogue and WordPress. All these apps are open source and are maintained by an active community of developers. MobiGuitar detected 10 bugs in total out of which one is related to Activity and three concurrency. The activity bug was because of the incorrect management of the life cycle of the activity. Few bugs were because of bad inputs. There were 2 bugs because of incorrect code reuse. It also detected bugs depended on programming mechanisms that aren’t traditional but are typical of Android apps.

## Related Work:
The most closely related work employs search-based methods. Mahmood et al. introduced EvoDroid, the first search-based framework for Android testing. EvoDroid extracts the interface model (based on static analysis of manifest and XML configuration files) and a call graph model(based on code analysis by using MoDisco). Several previous approaches are based on random testing (fuzz testing), which inject arbitrary or contextual events into the apps. Monkey [36] is Google's official testing tool for Android apps, which is built into the Android platform, and therefore likely to be more widely used than any other automated testing tool for Android apps.

AndroidRipper (subsequently MobiGUITAR) builds a model using a depth-first search over the user interface. ORBIT is based on a combination of dynamic GUI crawling and static code analysis, using analysis to avoid generation of irrelevant UI events. PUMA is a 
flexible framework for implementing various state-based test strategies.

## Scope for improvement :
- The results of Monkey and Dynadroid lacks exhaustive research. The paper has admitted this and attributes it to lack of proper debugging support.
- The MobiGUITAR generated testcases do not add assertions in the tests which needs to be done manually.
