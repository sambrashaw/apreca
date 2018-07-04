# Apreca - Sam Brashaw Fork
[Original Project](https://github.com/aaronduce/apreca)

Apreca - (app • ree • sha)

_a lot of bytes of open source goodness_

**WARNING** Requires Python 3.5+

Apreca is a basic open-source python3-based web server. It grabs information from a text file of the website contents and broadcasts it using HTTP protocols over a port of your choice.

## How to use your information or HTML code

Apreca relies on grabbing the information it presents on the webpage from a text file called ```WebpageContents.txt```, of which you can get a sample copy of from the sample folder in the repo.

The contents of this file can be as simple as just plain text, just like it can be in HTML, but the file must always start with a ```HTTP/1.1 200 OK```. - **Ammendment - This is not the case anymore. The code does this for you so don't worry :).**

If the file was to contain:
```
Hello, World!
```
it would output ```Hello, World!``` in the client browser.

Expanding on this, just like any other website, you can use HTML tags to style and format the document.

For example, to put the text in a paragraph that will have it's font family as Helvetica, we could use

```<p style="font-family: Helvetica;">Hello, World!</p>```

Or to make the text bold, we could use

```<b>Hello, World!</b>```

## Changelog

   - Fixed the status system
   - Added the logging system. Will be made better in the future.
   - Started on making the program host the page based on the code in [Release V1.0](https://github.com/sambrashaw/apreca/blob/master/version-hist/release/v1.0/apreca-web-server.py)

### Release

```v1.0``` - Huh, I created something, and it works, so I guess you could class this as version one.

### Betas

```b2.0-1``` - A beta? of the new version 2? that doesnt work? yeah, you could say that.

```b2.0-2``` - It 'technically' works now, so theres that, but then again none of the actual functionality is there yet.

```b2.0-3``` - Functionality is trickling back in, and as usual fixing stuff that shouldnt need to be fixed but have to.

```currently-working``` - NOT FOR USE. JUST SO I CAN ACCESS IT FROM OTHER PLACES - Sam

|**Release Name**|**Change**|
|----------------|----------|
|**v1.0**|Huh, I created something, and it works, so I guess you could class this as version one.|
|**b2.0-1**|A beta? of the new version 2? that doesnt work? yeah, you could say that.|
|**b2.0-2**|It 'technically' works now, so theres that, but then again none of the actual functionality is there yet.|
|**b2.0-3**|Functionality is trickling back in, and as usual fixing stuff that shouldnt need to be fixed but have to.|


## Usage rights

Apreca is open source, meaning you can use the code, change it, mould it into something better, basically do anything you want with it.

Made something amazing? Show me at aaronduce@lymelite.co.uk

## Credits

Well Sam fixed the port entry limit on the new GUI, thanks - [GitHub](https://github.com/sambrashaw) - [Twitter](https://twitter.com/trsambrashaw)

Also done most if not all of the programming in this fork.

## Suggestions

If you have any suggestions on how I can improve Apreca to make it better, create an issue on the repo.

Buzz me at [@TRSamBrashaw](https://twitter.com/sambrashaw) if you have any questions.
