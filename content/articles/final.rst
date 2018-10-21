###########################
Final Post
###########################

:date: 2018-08-13 00:00
:modified: 2018-08-13 00:01
:tags: GSoC, Octave
:category: GSoC
:slug: final
:authors: Erivelton Gualter

The Google Summer of Code program is over and I am positive I have gained so many experience in this period and additionally I have been done a significant work for GNU Octave about the Sisotool. Therefore, in this last post I all will go over in the project, describe what have been done and also point out what still pending of improvements.

Overview of the task
####################

The proposal of my project is aiming to create an Interactive Tool for Single Input Single Output (SISO) Linear Control System Design, also known as sisotool. The main goal consist in create a tool which allows the user to interactively modify a controller and apply it to the plant in a variety of closed-loop configurations/topologies. The interactivity allow the user to add & move poles and zeros in the root locus diagram, and implement common controller architectures like PD, PID, and Lead & Lag controllers, as well as assess performance through common diagrams such at Bode plots, Nyquist plots, root locus plots, and step response plots.

All the work were posted along the summer and can be found on this blog, as weel, in the following shortcut for the posts:

- `Welcome to Octave and Google Summer of Code`_.
- `Community Bonding Period`_.
- `Code begins - week 1`_.
- `Plots are Working - week 2`_.
- `Geeting closer to the First Evaluation - week 3`_.
- `First Evaluation - week 4`_.
- `Back to Coding`_.
- `Edit Compensantor Dynamics`_.																																																																														
- `Second Evaluation - week 8`_.

.. _Geeting closer to the First Evaluation - week 3: https://eriveltongualter.github.io/GSoC2018/week3.html
.. _Plots are Working - week 2: https://eriveltongualter.github.io/GSoC2018/week2.html
.. _Code begins - week 1: https://eriveltongualter.github.io/GSoC2018/week1.html
.. _Community Bonding Period: https://eriveltongualter.github.io/GSoC2018/bonding.html
.. _Welcome to Octave and Google Summer of Code: https://eriveltongualter.github.io/GSoC2018/welcome-gsoc.html
.. _Back to Coding: https://eriveltongualter.github.io/GSoC2018/week5-6.html
.. _Edit Compensantor Dynamics: https://eriveltongualter.github.io/GSoC2018/week7.html
.. _First Evaluation - week 4: https://eriveltongualter.github.io/GSoC2018/week4.html
.. _Second Evaluation - week 8: https://eriveltongualter.github.io/GSoC2018/week8.html

and the repository for the project is found in: https://github.com/EriveltonGualter/octave-control/

Overview of the tool 
####################

The interactive tool (sisotool) lets the user design a Single Input Single Output Linear Controller for feedback system. This tool allow the user to perform this task by:

- Adding, Modifying and Removing poles, zeros and gains of the controller;
- Interactive Root Locus graphical editor;
- Compare multiple control system design through the step or impulse response, as well, control effort of the controller;
- Design controller for a traditional feedback control architecture or  multi-loop control architectures.

The following subsections will describe what the tool is able to do; however, the reader can jump to the documentation page: https://eriveltongualter.github.io/GSoC2018/pages/documentation.html

.. figure:: images/final1.png
   :alt: alternate text
   :align: center

Diagrams
########

The tool provide an interactive visualization of the tool. The user can visualize the feature of the controller and plants by the diagrams:

- Root Locus diagram;
- Bode diagram;
- Nyquist diagram.

Additionally, the root locus diagram contains the feature to add, adjust and remove poles, zeros and gains.

.. figure:: images/final2.png
   :alt: alternate text
   :align: center

Edit Compensantor Dynamics
###########################

In order to achieve the design goals, the user can choose to use the *Edit Compensantos Dynamics*. It consist in another dialog box where the features of the controller can be edited. This dialog box provides the option to select the desired compensator. By default, the compesator transfer function *C* is selected. However, it can be easily modified by the compensator menu. As weel, the user can add, edit and remove poles, zeros, gains, Integrator and differentiator plants. 

.. figure:: images/final3.png
   :alt: alternate text
   :align: center

Compare Controllers Performance
###############################

The tool also provides the user an option to compare performance of multiple control system designs. This is very useful for the user to evaluate the controllers, and make assumptions about effort control tradeoffs and other analysis. 

.. figure:: images/final4.png
   :alt: alternate text
   :align: center

Control Architecture
####################

Besides the traditional feedback control architecture, the tool also allow the user to choose between 5 others architecture which contains a variety of inner and outer loop with feedback controllers. 

.. figure:: images/final5.png
   :alt: alternate text
   :align: center

Notes for developers
####################

All the code is written in M scripting language and the following files were added: 

- **sisotool.m** – Consist in the algorithm to read the inputs and treat it before open the sisotool interface.
- **GUI_sisotool.m** – Contains the main code for the Interface.
- **editcontroller.m** – Contains the code of the Edit Controller Interface.
- **editarchitecture.m** – Contains the code of the Control Architecture.

Also, the following existent files were slightly modified: 

- **bode.m**.
- **rlocus.m**.


Future
########

I had a wonderful summer working for GNU Octave and I plan on continuing to contribute on this project. I believe I have accomplished nice achievements in such a short time period. The tool is ready to be used, but it still needs to be more stable and there are a lot of features that still can be added. I already know a lot of folks which are interesting in help to improve this tool. 

I would like to say thank you for my mentors, Doug Stewart and John Swensen. Also I would like to say thank you Alexander Wilms for such great tips on github. Finally, A huge thank you for the community for the opportunity to work on this project.

