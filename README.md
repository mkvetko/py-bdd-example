# py-bdd-example
Minimal project structure for test automation of any app using behave and python

# Intro
I was starting couple of test automation projects from scratch in the past requiring still the same work to be done on start. 
So I have decided share my lessons learned on the way with you and I have created this minimalistic setup skeleton of the project using behave and python so you can start from it and add whatever features you need to accomplish your tasks.

# Audience
All test automation engineers can benefit from this as the project is very flexible. 

# Benefits
Behave is BDD framework for python and with use of behave yoy are getting clear description of your tests without the need shuffling the results to presentable form. Also you can run with your test code alongside development so you are not stuck because of the bugs etc. as you typically are if you reuse some code from your developers.
Python is fairly simple language so there is no steep learning curve, you can start immediately and you can end up with very complex test automation project allowing you to do anything you need to accomplish tasks you are assigned to.

# Project structure
BDD addition is actually nothing more and nothing less than just another abstraction layer above your test code. Main idea if this project is to keep one single object representing SUT (System under test) with all necessary features you need to do what you want, drive the application under the test.

Why so strict? Because then you can simply use power of your code with no focus on automation. You can drive your application simply from python console. This is huge benefit. There is nothing more frustrating knowing you have tests which sets environment somehow and you know the code is there, but due to complexity of you code you can't simply use it for manual validation.

There are couple of packages you should be aware of

# Your first steps
