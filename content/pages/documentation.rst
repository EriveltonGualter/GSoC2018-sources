##############
Documentation
##############

.. raw:: html
	
	<a href="https://raw.githubusercontent.com/EriveltonGualter/GSoC2018/master/images/sisotool_overview.png" title="sisotool" target="_blank"><img class="avatar2" src="https://raw.githubusercontent.com/EriveltonGualter/GSoC2018/master/images/sisotool_overview.png" /></a>



The **Interactive Tool for Single Input Single Output (SISO) Linear Control System Design** let you design SISO controllers for feedback system modeled in GNU Octave. 

Currently, it presents the following functionalities:

* Interactive plots: Bode, Root Locus and Nyquist diagrams;
* Root Locus graphical editos for adding, modifyng, and removing controller poles, zeros and gains.
* Analyze control system designs using time-domain by step responses. 
* Save the controller to workspace.
* Arbitrary list of response plots.
* Compare response plots for multiple control system designs.
* Tune compensators for different loop control structures.

Instalation
############

To get the latest updates as they come, install sisotool from git. To download the repository execute the following from the command line:

.. code-block:: matlab

	git clone git@github.com:EriveltonGualter/octave-control.git

To update to the latest version, go into your repository and execute:

.. code-block:: matlab
	
	git pull origin master

Open GNU Octave and go to the folder *octave-control/TARGET*. Then, run the following commands to install:

.. code-block:: matlab
	
	pkg install control-3.1.0_gsoc.tar.gz

After installation, you need to load the control package and finally run the sisotool as following:

.. code-block:: matlab
	
	pkg load control
	
Run sisotool
############

**sisotool (G)** specifies the plant model G to be used in the SISO Tool.  Here G is any linear model created with TF, ZPK, or SS.

**sisotool (G, C, H, F)** further specify values for the feedback compensator C, sensor H, and prefilter F. By default, C, H, and F are all unit gains.

**sisotool (..., VIEWS)** specifies the initial set of views for graphically editing C. You can set VIEWS to any of the following strings or combination of strings:

- *'rlocus'* : Root locus plot.
- *'bode'* : Bode diagram of the open-loop response.
- *'nichols'* : Nichols plot of the open-loop response.

Example:

.. code-block:: matlab
	
	G = zpk([],[-10 -2],0.01); 	% Plant
	C = zpk([-2 -20], [0], 1000);	% Controller 
	
	sisotool(G); 
	sisotool(G,C);
	sisotool(G,C, 'bode'); 
	sisotool(G,C, 'locus','bode');
	
Additionally, the user can also add the plant at following edit box.

.. figure:: images/final6.png
   :alt: alternate text
   :align: center

Display Diagrams
#################

Sisotool can show three different diagrams plus the step response which will be always displayed in the main tool. The interactive diagrams are: Root locus, Nyquist and Bode. The user can select the check box with the desired diagrams; Select the tab View or either using the shortcuts as showing in the following image:

.. figure:: images/final7.png
   :width: 800px
   :alt: alternate text
   :align: center

Design a Controller
####################

In order to desing a controller, the user tool provides many options to support this task. The user can add, adjust and remove poles, zeros, gains, differentiator and integrator transfer function. Therefore the user can:

- Select the radio button "Add" and select the desired feature;
- Go to Add -> 'x' Real Pole (for example);
- Press with right button on Root Locus Diagram, then Add Pole/Zero;
- Or by using the icons in the top of Root Locus Diagram.

.. figure:: images/final8.png
   :width: 800px
   :alt: alternate text
   :align: center

Then, the user can add the feature to the desired position; adjust the position or delete the feature. Additionally, the user can open the **Edit Controller Tool** by clicking in the top of the page.

.. figure:: images/final9.svg
   :width: 800px
   :alt: alternate text
   :align: center

Compare Controllers Performance
###############################

In order to compare the performance of two or more different control system designs, we need to salve all the desired compensators using the button Save.  All the controllers will be saved and can be showed in the tab "Controller/Desing.../..."

.. figure:: images/final4.png
   :alt: alternate text
   :align: center

Control Architecture
#####################

In sisotool you can also specify multiple models for any plant or sensor using an array of LTI models (see Model Arrays). This tool can be execute in the following way. The front-end of this functionality is working; however, it still need a bit work in order to upload the LTI system. 

.. figure:: images/final10.svg
   :width: 800px
   :alt: alternate text
   :align: center


**Questions**

If you have a question about installation or sisotool in general, feel free to contact myself. In addition, Octave mailing list is an excellent source of community support.

If you think there’s a bug or you would like to request a feature, please open an issue `ticket`_.

.. _ticket: https://github.com/EriveltonGualter/octave-control/issues




