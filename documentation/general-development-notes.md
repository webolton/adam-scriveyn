# Development Notes

## Basic Theory of Workflow

The work flow for transcribing and serving transcribed texts should take place in several steps:

1. MS images will have to be retrieved. It is probably going to be unrealistic to keep them all on
the size of server I am going to be able to afford, so the server might need to make a request to Dropbox or the like to get them. This step is not really important to initial development, but will
probably need to be addressed before too long.

2. MS images will need to be preprocessed. This will be ironed out in the next step, but I imagine that
whatever does the preprocessing will be handled by a Class. It might require ImageMagik.

3. Lexemes will need to be identified in the MS images. I am not sure if it makes sense to actually
copy the areas found out of the main image or to just deal with them as is. After they are identified
I need to come up with a way of making the individual lexeme images the same size. I imagine that this
will mean extracting them from the main image and adding background masking to the images that are too
big to fit in an easily defined square.

4. Using a NN, I will need a program to make guesses about what the individual image represents, based
on a set of predefined test data / trained model. Then I will need to be able to evaluate how well the
model does and when it is in accurate, I need to manually tell the program what the word is and add
the accurate data to the test data and retrain the model.

5. The step described above will probably require some sort of GUI, that I will probably make as a HTTP
client that will eventually run on the server. This will require a login to protect the server.

6. All of this will have to be managed with metadata that will probably be in MongoDB.

## Basic Theory of Project Architecture

I imagine that the entire SEL project will consist of three seperate services:

Adam-Scriveyn -- an Python OpenCV app that will do the transcription of the texts, and basic preperation
of the texts. It will store all of the metadata about constructing the texts, what the texts are, and
so on in MongoDB. Adam-Scriveyn will be ignorant about the structure of actual texts and will try to
be editorially agnostic.

DigitalSEL-API -- A Rails app that will ingest data from Adam-Scriveyn, which it will store in Postgres.
When the texts are first saved in Postgress, they will be saved in such a way that they will construct
individual pages, but will try to be agnostic about them. Editorial information can be added on. The
API will serve data to a webclient. The Rails app will do fun stuff like create PDFs of the texts.

DigitalSEL-Client -- This will be a React client that will provide the interaction between the DigitalSEL-API
and the world.

Future plans: Elastic Search for the texts in the Postgres DB. Logins for people who might like to
contribute to the editorial life of the text.
