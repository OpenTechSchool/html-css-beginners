# OpenTechSchool HTML & CSS Introduction

This is a friendly how-to for contributors to the HTML and CSS workshop
at OpenTechSchool. 
About the course:

A HTML and CSS basic workshop for beginners that have never written HTML/CSS
before and want to know how to start.

## Class format

At OpenTechSchool we tend to go *practical* and *at your own pace*.

At your own pace means that we provide access to the complete course notes at
the beginning of the session. Then students can progress individually. Some
students will get through very quickly, others will take some time, and others
will finish the core work with time to spare. The core work should be
completable by everyone. To keep things interesting we supply various
additional topics which are entirely optional.

A class schedule looks like this:

    1100 - Students still arriving, writing name tags, setting up laptops.
    1230 - Introductions, wifi instructions and location of coursework.
    1235 - Students learn stuff.
    1800 - Thankyous, maybe demonstrations.


## Author Guide

This material is built with the help of [Sphinx][sphinx], [Invoke][invoke],
and translated with [Transifex][transifex].

To get started, you should have the python packages needed. To do this, use
[pip][pip] like so (probably in a virtualenv you've made to work on this):

    pip install -r requirements.txt

You can then use the invoke task runner to run things. E.g, build the project
from the source files you've edited:

    invoke build -l en

(builds them in English). To serve the built sphinx project on your own computer,
you can run:

    invoke serve

And visit the url that your console prints to view the result.

The `setup` invoke task should git checkout the `gh-pages` branch correctly, should
you wish to push to that branch to publish a new version of the workshop.

Translation should be coming soon.

[sphinx]: https://pypi.python.org/pypi/Sphinx/
[invoke]: https://pypi.python.org/pypi/invoke/
[transifex]: http://transifex.com/
[pip]: https://pip.pypa.io/en/latest/
