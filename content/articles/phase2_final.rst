###########################
Second Evaluation - week 8
###########################

:date: 2018-07-06 11:36
:modified: 2018-07-16 11:36
:tags: GSoC, Octave
:category: GSoC
:slug: week8
:authors: Erivelton Gualter

So, here is my last post before the second evaluation. If you have been following `my blog`_ or the `octave blog`_, you know that the purpose of this google summer of code project is to create an `Interactive Tool for Single Input Single Output (SISO) Linear Control System Design`_. Also, well-known as sisotool in matlab control system desgin toolbox. 

.. _my blog: https://eriveltongualter.github.io/GSoC2018/
.. _octave blog: http://planet.octave.org/
.. _Interactive Tool for Single Input Single Output (SISO) Linear Control System Design: https://summerofcode.withgoogle.com/projects/#5842927301951488


Since my last evaluation results on June 15th, it has passed 3 or 4 weeks, counting the evaluation week. In the meantime, I was able to code a significant work about *Edit Controller Windows*. It resulted in two posts. The first post was regarding the evaluation week as well as my mentors´ feedback and the actions I took from it, such as improving the coding comments, software documentation, and adding menu functionalities for all interfaces. Lastly, the second post was an introduction to the *Edit Compensantor Dynamics*, as you can go over in the following links:

- `Edit Compensantor Dynamics`_.
- `Back to Coding`_.

.. _Back to Coding: https://eriveltongualter.github.io/GSoC2018/week5-6.html
.. _Edit Compensantor Dynamics: https://eriveltongualter.github.io/GSoC2018/week7.html

This last week I have continued working on Edit Compensantor Dynamics to which I added more functionlities. Now the user is able to:

- Adjust the gain of the controller by the edit box input;
- Change the location of the real zeros and poles;
- Change the location of the complex zeros and poles (imaginary part and real part);
- Change the damping and frequency of the complex zero and poles.

Here is a video where I explain how to install/run and use the sisotool: 

.. youtube:: w7VHZT6MNEI
    :width: 640
    :height: 480

The tool is already entirely suficient to desing a compensator. With the help of the adding/dragging fuctionlity, we can adjust the controller to the desired performance. Additionally, we can use the Edit Compensator Dynamics to enter with the desired point.

Next Steps
##########

For the next steps, we have the following list of tasks:

- Missing Add Pole/Zero in Compensator Editor;
- Add Feedback Control Architectures (https://www.mathworks.com/help/control/ug/feedback-control-architectures.html);
- Add multiple controller options;
- Replace Slider Gain of the Main function (because the right way to perform this task is by dragging the closed-loop eigenvalues);
- Complete documentation.








