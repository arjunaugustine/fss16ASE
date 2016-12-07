# Essay


## Introduction
Smartphones are now ubiquitous even though they are new systems whose security and automated testing infrastructure is largely underdeveloped. As of 2011, the android share of the smartphone market was over 52.5% which was double what it was in 2010. The android market exceeded 10 billion app downloads with a growth rate of 1 billion app downloads per month. The features of Android devices and the complexity of their software continue to grow rapidly. 

A few problems ever since the boom of the Android smartphone industry from a software engineering perspective are defects related to:
* Improper management of limited resources, like memory, that leads to slowdowns, crashes, and negative user experience,
* GUI oriented application construction paradigm of android and its novelty, which means many existing android software correctness issues fall outside the scope of traditional verification techniques.
* Lack of cost-effective approaches for development and suitable techniques and tools for testing
* Primitive testing technology, and device fragmentation, which leads to heavy reliance on manual testing and increased test effort due to the number of devices that must be considered.
* Android framework that tries to abstract a lot of intra-process communication, thread management and synchronization within itself during run-time, which leaves the developer opaque to such aspects giving rise to a lot of concurrency bugs unless the delveloper spends considerable time on understanding the semantics of Android.

This paper looks at how automated testing of Android applications has evolved over time.


## Related Work

A. Using GUI Ripping for Automated Testing of Android Applications by Domenico Amalfitano, Anna Rita Fasolina, Porfirio Tramontana, and Salvatore De Carmine, Atif M. Memon:

GUI Ripping is a dynamic process in which the software's GUI is automatically traversed by opening all its windows and extracting all their widgets (GUI objects), properties, and values. The extracted information is then verified by the test designer and used to automatically generate test cases. Certain GUI exploration criterion decides whether GUI exploration using a particular input is to be continued or not. Certain metrics may help in making this decision - ensure the depth of resultant GUI tree is less than a specified maximum, or if the resultant state is equivalent to an already evaluated state. The authors implemented the AndroidRipper using the Robotium Framework and by the Android Instrumentation class. and used metrics like Defect Detection Effectiveness, Code Coverage Metric and Time (Resource) spent to arrive at a conclusion about how effective the automated test cases generated are, in detecting bugs in an application. The results (running on Wordpress - an opensource android blogging software with broad user community with an issue tracking system) were compared against the efficacy of Monkey - a non commercial random stress and crash testing tool for Android GUIs. It was chosen because that was the only non-commercial automated android testing tool "to the best of author's knowledge". The Monkey tool generates pseudo-random streams of user events such as clicks, touches, or gestures, as well as a number of system-level events. You can use the Monkey to stress-test applications that you are developing, in a random yet repeatable manner. They found that whereas the Monkey executes for 4.46 hours firing 45,000 events with the default value of event type statistical distribution finding 3 crashes reaching 25.27 % LOC coverage, the ripping tool covered about more than 35% of code in about the same amount of time to detect multiple undocumented bugs in the WordPress application. However, the paper lacks in comparing the performance of the tool against additional tools other than the Monkey, while running on additional applications other than the Wordpress app that they used.

B. Automating GUI testing for Android applications:

