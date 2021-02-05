# mnist-n--prediction-dbot
Simple discord bot the incorporates tensorflow trained mnist number recognition and enables you to post images of numbers into discord channel and it will predict it.

To run the bot command.
- Upload an image to chat - if it is operation it should say "Downloading content"
- Then type "predict" (case sensitive)

Naturally the bot must be hosted from a server before being able to be run.


Requirements:

Python:
- Nodejs
- tensorflow
- Matplotlib
- numpy


JS:
- Discord.js
- Express
- Python-shell
- Request

Numbers must be black with white background for model to be accurate. This is just a small project so I have not implemented scewing and other anti-overfitting and underfitting techniques.
