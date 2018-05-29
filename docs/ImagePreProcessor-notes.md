# ImagePreProcessor
NB: These notes are here to help me remember what I am doing and to help me learn how to do Python
development.

## General Notes
The intent of the class is to prepare the MS images as I get them and prepare them for use in the
machine learning / CV program. This will take some trial and error, I suspect.


### Loading a file into ipython from the root directory of the project

    import sys
    sys.path.append('../')
    from lib.imageProcessor import loadImage

### Running the one test
(This took time to figure out. See `docs/TODO.md` for more).
From project root directory, run

    python -m unittest tests.lib.TestImageProcessor
