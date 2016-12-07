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
