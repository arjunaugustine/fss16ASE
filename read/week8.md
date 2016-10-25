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
The results on the 68 benchmark apps were shown in a very user-friendly and detailed manner. It includes the coverage, crashes and the length of the tests. It also includes progressive coverage on benchmark apps and pairwise comparison of found crashes. Additionally, performance comparison on 10 F-Droid subjects and the Vargha-Delaney effect size are also tabulated.

## Baseline Results:
The top 1,000 Google play apps were tested using Sapienz. It found 558 unique crashes. The crashing behaviour has been verified on real Android devices (as well as Android emulators). 14 have been confirmed to be genuine, previously undetected, faults, 6 of which have already been confirmed as fixed by their developers. These results demonstrate that Sapienz is a practical tool for Android developers as well as for researchers. Sapienz significantly outperforms (with large effect size) both the state-of-the-art technique Dynodroid and the widely-used tool, Android Monkey, in 7/10 experiments for coverage, 7/10 for fault detection and 10/10 for fault-revealing sequence length.

## Related Work:
The most closely related work employs search-based methods. Mahmood et al. introduced EvoDroid, the first search-based framework for Android testing. EvoDroid extracts the interface model (based on static analysis of manifest and XML configuration files) and a call graph model(based on code analysis by using MoDisco). Several previous approaches are based on random testing (fuzz testing), which inject arbitrary or contextual events into the apps. Monkey [36] is Google's official testing tool for Android apps, which is built into the Android platform, and therefore likely to be more widely used than any other automated testing tool for Android apps.

AndroidRipper (subsequently MobiGUITAR) builds a model using a depth-first search over the user interface. ORBIT is based on a combination of dynamic GUI crawling and static code analysis, using analysis to avoid generation of irrelevant UI events. PUMA is a 
flexible framework for implementing various state-based test strategies.

## Scope for improvement :
- The fitness value is trivially three times the objectives and this generally assumes that the objectives are of equal importance. This might not be the case, for a developer who does not worry about the sequence lenth as long as he is able to find bugs (especially in terms of software security)
- while choosing Hybrid exploration strategy over Random/Systematic strategies may ensure high overall coverage, it might not ensure catching more serious bugs(due to the metaheuristic nature) and hence a variant incorporating the best sides of all the strategies should have been used. 
