################################################
Geeting closer to the First Evaluation - week 3
################################################

:date: 2018-06-03 5:48
:modified: 2018-06-03 5:48
:tags: GSoC, Octave
:category: GSoC
:slug: week3
:authors: Erivelton Gualter

First Evaluation period is around in the corner. As was proposed on my `first post`_ of my timeline, the work I have been doing is on time. 

.. _first post: https://eriveltongualter.github.io/GSoC2018/welcome-gsoc.html

For this past week, I added some functionalities to the Root Locus Editor. This time, the user can add: real poles, complex poles, real zeros and complex zeros for the plant. Therefore, with the current sisotool update we already can design a suitable controller. The pending tasks for this week are the dragging functionality which is not difficult to solve. I already solved this problem in my proposed code for the GSoC which can be found here: https://github.com/EriveltonGualter/Concept-SISO-tool-for-Octave. So, I would like to invite you to try the work I have done by executing the following few lines of code:

.. code-block:: bash

	git clone git@github.com:EriveltonGualter/octave-control.git
	cd octave-control
	make install

Run Octave, add the control package and open sisotool by running: 

.. code-block:: matlab

	pkg load control
	GUI_sisotool
