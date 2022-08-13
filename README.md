# CodeFuryWebDev Web Track 5.0

# Incubation Cell Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/BCS2003/CodeFuryWebDev.git
$ cd CodeFuryWebDev
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd .\CodeFuryWebDev\ 
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

As it runs, a user is requested to login or signup.

Then he/she has an option to add their company to this platform. They can describe the Business model and specify the financials with profit till the current date, etc.

Then they can mention the required funds for the company with the equity that they want to offer.

As soon as the offering is registered, they can create a chat room where they can chat with the interested investors.


### Basic UI

The simplest design. We didn't go in depth about the design. As we were focused on the content.
We took a lot of time to figure out few new things and learnt a lot while building this website.

## Navigation

User can navigate through various routs 

## Webhooks

Set up `localtunnel` to test out Webhooks. The `localtunnel` package should be
installed as a dependency to the project.
Note, however, that the port number is the same as the port that `python manage.py runserver` is
running on, which is 8000.
```sh
(env)$ localtunnel-beta 8000
=> Port 8000 is now publicly accessible from http://5bebd69e5222.v2.localtunnel.com ...
```

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test gc_app
```


###Contribution

1.Amith (https://github.com/Amith225)<br>
2.Shravan (https://github.com/myselfshravan)<br>
3.Ansh<br>
4.Gautam<br>
