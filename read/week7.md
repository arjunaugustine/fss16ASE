# MobiGUITAR Automated Model-Based Testing of Mobile Apps

## Key Words

## Motivation:
People adopt mobile platforms largely because of the apps they offer. Hence, quality assurance techniques like Software Testing is very important. Even though there are different techniques for testing mobile apps they are mostly stateless and never handled security. This is a big limitation because mobile apps are extremely state sensitive and have enhanced security. So there is a need for novel techniques. 

MobiGUITAR - Model GUI Testing Framework models the states of the app's GUI. It also have a test adequacy criteria based on state machines. The model and the criteria are used to generate test-cases and automate the app testing.

## Informative Visualizations:
An abstract State-Machine for the app - Aard Dictionary, a dictionary and online Wikipedia reader is shown in the paper. It shows different states and transitions between them making it easy to identify the different transitions which led to termnation of the app.

## Baseline Results:


## Related Work
MobiGUITAR was compared with two tools for Android testing - Monkey and Dynodroid. MobiGUITAR produces several types of artifacts - crash reports, finite state machine models, GUI sequences and also executable JUnit test-cases. However, Monkey produces only an Android LogCat report and Dynodroid produces a LogCat report and a code coverage report. Also when it comes to configurability MobiGUITAR is superior bcause it even lets you choose a whitelist of input values to be assigned with input widgets. Both Monkey and Dynodroid could detect only 3 bugs when MobiGUITAR detected 10 bugs.

## Scope for improvement :
