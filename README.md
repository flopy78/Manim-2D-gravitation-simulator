## Requirements

This project requires the [Manim CE](https://docs.manim.community/en/stable/installation.html) (and all its dependencies) library, as well as numpy.

When installing Manim, you might encounter the following problems :
 * The FFMPEG executable might not be configured. To fix that, you can download it [here](https://ffmpeg.org/download.html) (download the Static Build for your OS) and then add the path in the field "ffmpeg_executable" of the "manim.cfg" file. To do so, you can use if necessary the command "manim cfg export".
 * LaTex might not be installed. To do so, you might look up [here](https://www.latex-project.org/get/).

## Use

To execute the project, set your parameters in the dedicated lines of the "scene.py" file (an example is already in it), and then execute the "manim scene.py GravitInteraction" command.

Wait the time Manim does its job (it might take a while !) and grab the output video in the "video" folder, which will be automatically created by Manim.
