![OrkPack-2](https://raw.githubusercontent.com/0x06060606/OrkPack-2/master/logo.png) <br/>

# Disclaimer
neither John Bell, OrkSec, or the members take responsibility for what you do with this tool. We do not take responsibility for what you do with this tool! We do not support any illegal actions performed with this tool.<br/>

# Modules
We've got bunch of modules you can use. Some are faster (requests, mechanize) and some are slower but work.<br/>
| Website      |  Python Module |
|--------------|----------------|
| Nest.com     | requests       |
| Call of Duty | Selenium       |
| freebitco.in | WIP            |

# Installation
 * Make sure python3 is installed:<br/>
==> macOS `brew install python`<br/>
==> Linux `sudo apt-get update && sudo apt-get install python3.6`<br/>
==> Windows `https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe`<br/>
 * Installing missing python modules:<br/>
`python3 -m pip install requirements.txt`<br/>
 * Installing firefox WebDriver:<br/>
==> macOS `brew install geckodriver`<br/>
==> Linux `sudo apt-add-repository ppa:mozillateam/firefox-next && sudo apt-get update && sudo apt-get install firefox xvfb`<br/>
==> Windows `https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip`<br/>

# running
```
$  python3 Main.py
```

----

```
MIT License

Copyright (c) 2020 John Bell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
