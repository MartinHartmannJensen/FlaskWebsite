# Project Remembrance

-----

## Description - "What is this, and why is it?"

This is a tool for generating random passwords and storing them under keywords. It utilizes random.org and stores the passwords on your computer in an encrypted file.

If you have any knowledge of information security, you probably have some questions. Such questions might be: "Why would you store passwords on your pc in a text file?" or "Wouldn't anybody using your pc be able to access the passwords?". The answer is, yes, it's susceptible to being stolen and with time decrypted; and yes, someone could gain access to your passwords, because the client itself doesn't require a password. 

So what's the idea?

## Philosophy

In order to browse the internet or use any computer service these days, you probably need to authenticate with a service every once in while. After having had accounts for many years, I started discovering that some of them got broken into. Presumably a bot guessed my password. Now luckily it has always gone to a second step in validation, notifying me via email that I or someone else has logged in from a new location/machine. No harm done, except.. Those passwords are potentially compromised. If I had used the same password with the same email some other place, the bot now has the keys to the kingdom (well, only if there's not any sort of multi-step authentication). So I'd like to use a different password for each service, so no one account could give access to all of them.

The other aspect is that my password probably got guessed, because it wasn't a very good one. Passwords are all about amounts of permutations so large that a machine cannot hope to guess it in any relevant time. But hard passwords can be hard to remember, and industry attempts to keep passwords short but harder to guess has only resulted in a muddled mess nobody seems to be able to remember anyways.

[Relevant XKCD](https://xkcd.com/936/) 

Now, the long password approach is the better option here, no doubt. If you can keep it all up in your head, it's of course the safest option. If you, like me, just can't be bothered remembering all of them. Then this tool might be for you.

What I suggest: Establish a hierarchy of passwords. Passwords for emails, banking and such should be hard, unique, but kept stored by brainpower. All other are the wild west, and can be randomly generated. This ensures unique passwords for each site that doesn't say anything about you and the likelihood of these getting guessed is extremely low. All you have to do is remember a short keyword for the site or service, to be able to retrieve the long gibberish password that you created with the tool.

## How to Get It

The reason I built this for myself, despite having seen other existing solutions, is that I was always a bit suspicious when it comes to password management software. So I can imagine how you, the reader, must feel. That is why the project is open source. I built it for use with random.org, but the whole world can't be on my free API key. So building your own is the only way.

### Build Your Own - A List of Things

The program was written in Python 2.7, with a couple of imported packages. So what you'll need are:

| URL                                                          | Description                                         |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [Project Remembrance](https://github.com/MartinHartmannJensen/ProjectRemembrance) | The source code for the project                     |
| [Pyperclip](http://pyperclip.readthedocs.io/en/latest/introduction.html) | Python Module - For pasting to the clipboard        |
| [Json-rpc](https://pypi.python.org/pypi/json-rpc/1.10.8)     | Python Module - Used in interaction with random.org |
| [Requests](https://pypi.python.org/pypi/requests/2.7.0)      | Python Module - Used in interaction with random.org |
| [Random API](https://api.random.org/json-rpc/1/)             | Get a key                                           |

The only thing you need to independently change are the 3 variables (aeskey, aesIV and randomAPIkey) found in programcredentials.py