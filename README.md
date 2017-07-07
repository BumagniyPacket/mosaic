# Simple PIL-based mosaic generator
[![Build Status](https://travis-ci.org/BumagniyPacket/mosaic.svg?branch=master)](https://travis-ci.org/BumagniyPacket/mosaic)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e64a530989d041aca562145fb49fa872)](https://www.codacy.com/app/bumagniypacket/mosaic?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BumagniyPacket/mosaic&amp;utm_campaign=Badge_Grade)
## Installation
Dependencies
~~~
 - click==6.7
 - Flask==0.12
 - gunicorn==19.7.0
 - itsdangerous==0.24
 - Jinja2==2.9.5
 - MarkupSafe==1.0
 - olefile==0.44
 - Pillow==4.0.0
 - Werkzeug==0.12
~~~
Install dependencies:
~~~
pip install -r requirements.txt
~~~

## Run
~~~
gunicorn run:app
~~~

## How it use

1. Press the "FILE" button
2. Select an image to create a mosaic
3. Press the "CREATE MOSAIC" button
4. Wait for a while
5. Save your mosaic

## Examples of result

![Guido](https://github.com/BumagniyPacket/mosaic/blob/master/examples/guido.png?raw=true)

![cat](https://github.com/BumagniyPacket/mosaic/blob/master/examples/cat.png?raw=true)
