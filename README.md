# mtrigger
A minimal DSLR cable release trigger using a USB-serial converter

The reasoning behind this project is that I wanted to trigger a DSLR to take timelapse pictures of an experiment.
The experiment in question has a UV LED which would cause problems with the photos, however that can already be controlled from a Python script.
The solution was then to switch off the LED, take the picture, and switch the LED back on again, all under Python.

Canon do provide software allowing timelapse to a PC, but it requires Windows and the best synchronisation we could hope for would be using sendkeys or similar.

Other suggested uses are timelapse photos of system where the rate of change is non-linear, or any event-based triggering.

I've tested this on a 350D and a 700D.  All the xxxD cameras appear to use the 2.5mm audio jack, while the xxDs use a proprietary 3-pin connector.
These are available quite cheaply in the form of third-party adaptors and releases, which also suggests that other makes/models could do something similar.

I strongly suggest using manual focus, as the simple cable-release approach doesn't give any feedback as to whether focus or shooting was successful.
