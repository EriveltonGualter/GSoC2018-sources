############################
Plots are Working - week 2
############################

:date: 2018-05-29 12:38
:modified: 2018-05-29 12:38
:tags: GSoC, Octave
:category: GSoC
:slug: week2
:authors: Erivelton Gualter


Here we go one more week of code. This week I have continued my work from previous week related to interface of sisotool. Just reiterating what was done last week, I created a couple GUI to understand a little better how the UI Elements works in Octave. For this week, I added some functionalities for this interface. 

This moment, I have been working on with two different interfaces. The first one that I call sisotool – Control System Designer consist in a main window with step response of the a dynamic system. Also, it has other elements such as : radio button in order to choose the desired complementary diagram to design the controller, input field for the plant, a variety of controllers to be added to the plant, as well a save button to save the controller. The second window contains the desired diagrams. 

For now, the user can choose between three diagrams: Root Locus, Bode and Nyquist diagram. Note, in the root locus diagram also was added the closed loop eigenvalues which was not implemented in the rlocus function. 

Therefore, to execute the sisotool, we can simply run GUIsisotool. The plant can be enter in the input field. You must enter with a LTI model, such as: *tf (num, den, tsam, …)*

Here is a video which illustrates my current work. 

.. youtube:: pfWhvKi6XTQ
    :width: 640
    :height: 480

