GsoC Week 1
##########################

:date: 2017-10-21 1:47
:modified: 2017-10-27 1:18
:tags: GSoC, Octave
:category: GSoC
:slug: gsoc-week1
:authors: Erivelton Gualter

This summer I got accepeted to the Summer Google of Code under the GNU Octave. This program, admistred by Google, facilates the emergence of students to the Open Source Community.  My primary goal to participate in the GSoC is to build a long term relationship with the open source community.  I want to take it serious and get involved.  I have been using a lot of open source tools, and now I fell it is time to contribute for it.

For those who does not know GNU Octave is a high-level programming language for scientific and numerical computations which uses the m-script language compatible with MATLAB. The core of Octave is implemented using both C++ and the the well-known m-script language. Both Matlab and Octave provide many similar packages to the end-user (also known as toolboxes in matlab). One of the missing functionalities in the Octave controls package is the **Control System Designer tool** . This tool, also called sisotool, is used in Control Systems, Linear Systems, and Modern Control classes, as well as for hobbyist and industrial controller design. This tool is used in controller design to allow exploration of linear controllers through interactive tools. This tool allows the user to interactively modify a controller and apply it to the plant in a variety of closed-loop configurations/topologies. The interactivity allow the user to add & move poles and zeros in the root locus diagram, and implement common controller architectures like PD, PID, and Lead & Lag controllers, as well as assess performance through common diagrams such at Bode plots, Nyquist plots, root locus plots, and step response plots. 

Therefore, the goal of my project is to create an **Interactive Tool for Single Input Single Output (SISO) Linear Control System Design** to provide a much needed missing feature in the Octave controls package for the design and analysis of SISO system controllers. Here you can access the link of my proposal (https://summerofcode.withgoogle.com/projects/#5842927301951488). In this meantime, I will be supervised by my mentors: **Douglas Stewart** and **John Swensen**.

*Review currently sisotool (MATLAB)*

During this first week, I was advised to watch the following videos which briefly explain the functionalities of the currently Matlab version:

- https://www.youtube.com/watch?v=jXRD5Mc8Cy4
- https://www.youtube.com/watch?v=Hw-alRHnCzs
- https://www.youtube.com/watch?v=nHF5q44pAOg
- https://www.youtube.com/watch?v=FUyNFJGAy00

Since I haven't use the sisotool for while, I have been exploring this tool this past week.

Here are some basic notes. In order to run the Control System Designer, we can simply run *sisotool* or in case we have the plant, we use this as an attribute for the sistool function; for example: 

.. code-block:: matlab

	s = tf('s');
	plant = (s + 7)/(s*(s + 5)*(s + 15)*(s + 20));
	sisotool(plant)


.. figure:: images/sisotool.png
   :width: 600px
   :alt: alternate text
   :align: center

The Matlab R2016 and newer versions have presented a new concept for the sisotool. In this new window format, all the plots are constrained in a single window. The user can choose the plots it can be displayed and there are several interactive seetings which helps to design a controller. So, we come up with that creating something identical for this tool will ne necessary more than m script languages. Therefore, the main goal of the project will be developing the "back-end" capable to perform the same tasks with the current version and for the "front-end", it will be used the UI Elements that is more similar to the older version of sisotool. 

So far, it was identified some functionalities which will be presented in this version:

- Capable of choose different loop structures for the controller;
- Create multiple controller designs;
- Provide an arbitrary list of response plots.

Timeline
--------

I am still really busy with school and research work due the semester still is not over. However, I still have ome more week and I will have much more time to spent in this project. So, for this week I will presented a timeline which I extracted from my proposal, but probably it will be adapted for the new disussion I have this community bonding period.

**Community Bonding Period (23 April - 13 May)**

I will explore the control package created by Lukas Reichlin and maintainers Alexander Wilms and Doug Stewart. My goal is to become comfortable with the structure of the following codes:

- rlocus.m;
- nyquist.m;
- bode.m.

**Phase 1  Initial Phase of Coding - Week 1 (14 May - 20 May)**

- Setting up.

**Week 2 (21 May - 27 May)**

- Implement the function sisotool(Gp). This function will plot the Root Locus, Nyquist and Bode diagram in the same plot;
- The goal at this point is to create the layout of the plots.
- The distribution in the plots will be fixed at this point. However, in Phase 2 the function will have attributes to choose the desired diagrams in the interface. Example: sisotool(Gb, 'rlocus', 'nyquist');

**Week 3  (28 May - 3 June)**

- Add polos and zeros, being real or complex, to the plant through the UI elements.
- Position polos and zeros according to the mouse input.
- Polos and zeros can be reallocated by dragging with the left button of the mouse.

**Week 4 \& 5 (4 June - 17 June)**

-  Any remaining work will be completed;
-  Submission of Phase 1 evaluation;
-  Complete post about the phase with detailed documentation.

**Phase 2 - Week 6 (18 June - 24 June)**

- Create the layout of the complete GUI interface with buttons, sliders, and others, examples:
        - edit box for the compensator gain;
        - poles and zeros buttons;
        - listboxes for the desired plots to be shown.
        

**Week 7 \& 8(25 June - 8 July)**

- Add functionalities for the graphical elements from week 6. 

**Week 9 (9 July - 15 July)**

- Submission of Phase 2 evaluation;
- Complete post about this phase with detailed documentation.
 
**Phase 3 - *Week 10 \& 11 (16 July - 29 July)**

- Add Step Response Time functionality. The user can select the step response to visualize the characteristics of the output, such as: Rise time and Peak Overshoot.
- Export compensator design to the workspace.

**Week 12 (30 July - 5 August)**

- Any remaining work will be completed. 

**Week 13 (6 August - 14 August)**

- Complete post about the phase with detailed documentation.
- Final Submission



.. References
.. ----------

.. * `Control System Designer Matlab; <https://www.mathworks.com/help/control/ref/controlsystemdesigner-app.html>`_
.. * `Interactive plots; <https://wiki.octave.org/Interactive_plots>`_
.. * `GUI Development - Octave; <https://octave.org/doc/v4.2.0/UI-Elements.html>`_
.. * Discussion about sisotool in mailing list:
.. 	- `Closed-loop-control-GSoC-Design-Question: <http://octave.1599824.n4.nabble.com/closed-loop-control-GSoC-Design-Question-tt4653476.html#a4653528>`_
.. 	- `GSoC sisotool project <http://octave.1599824.n4.nabble.com/GSoc-sisotool-project-tt4663204.html>`_


