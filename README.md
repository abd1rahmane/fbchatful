# Fbchatful



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Fbchatful is a simple resftul service for sending message to users using fbchat.
  - Fast (1s to send message) and ver stable .
  - No limits .
  - Magic .


### Installation

Fbchatful support Python >2.7 & >3.4.
Install the dependencies and devDependencies and start the server.
# ubuntu
```sh
$ sudo pip install fbchat flask
$ python app.py
```
# Example

```sh

curl http://127.0.0.1:5050/facebook/user/send?contact="Abderrahmane"&message="Thank you" 
# true

```

### Todos

 - Write more examples
  - Multi accounts support.
  - Proxy support .
  - Web interface !.
