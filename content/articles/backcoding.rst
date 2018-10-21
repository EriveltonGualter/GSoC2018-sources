###############
Back to Coding
###############

:date: 2018-06-24 1:19
:modified: 2018-06-24 1:19
:tags: GSoC, Octave
:category: GSoC
:slug: week5-6
:authors: Erivelton Gualter

Results from the first evaluation came 9 days ago. All of the three gsoc student were successful! For the readers of my blog, you can find them at http://planet.octave.org/. If you already a reader of planet octave, you are in the right place. 

The feedback from my mentors could not better and doable. Basically, it consisted of:

- Start writing some documentation on the capabilities of the tool;
- Write a checklist of the pieces of the tool that are working;
- Test the tool in other common platforms (MacOS and Windows);
- Improve on commenting throughout the code.

Therefore, this last couple of weeks was divided into two tasks. During the first week, I started working with UIMENU elements. The second week, I completed some of the tasks in which my mentors mentioned in the evaluation and fixed some bugs from the menu. 

**Uimenu elements**

UI components are the user's interface controls, such as buttons, check boxes, and sliders. In case you already follow this blog, you noticed that the first concept of sisotool already has buttons, radio buttons, sliders and ckeckbox to perform the design of a controller by adding/adjusting and removing poles, zeros and gains. 

The next UI components, I added uimenus in the interface. They are the menus we found at the top of the page, such as File, Edit, Tools, and Help for the majority of tools. Therefore, for the first week, I added the following menus:

- View;
- Add;
- Controller.

.. figure:: images/uimenu.svg
   :width: 800px
   :alt: alternate text
   :align: center

*View Menu*

To display the desired diagrams, the user has the option to go to the top of the main interface and press *View*. It will open three different options: Root Locus, Bode, and Nyquist Diagram. Additionaly, we can use the shortcut as despicted in the figure above. 

*Add Menu*

To add poles and zeros, complex or not, the user now has the alternative to go to the top of the page, click in *Add* and choose the desired option. Right now, only the poles/zeros are working. The Integrator, Differentiator, Lead and Lag are still pending tasks. 

*Controller Menu* 

For now, it consists of only the submenu *Save*. It will store the controller in a variable C in the workspace and save it to a Mat file.  

**Feedback Evaluation Tasks**

During the second week after the evaluation period, I started adjusting the code according to my mentors' feedback and I am adding more comments for the code. Therefore, the first thing I did was to cleaneup the code and add more comments. Additionally, I added a Documentation page to my website to centralize all the information about the tool.

For now, you will find on the documentation page about how to download, install and run the sisotool. One of my tasks of this week is to add more to this page. I will add more explanation on how to desing a simple controller and provide an example. Also, I will use this page to create a checklist of pieces of the tool which are working and also which are pending. 

You can go to the top of this page and click on *Documentation* or click in this link: https://eriveltongualter.github.io/GSoC2018/pages/documentation.html





See you in my next post. 
