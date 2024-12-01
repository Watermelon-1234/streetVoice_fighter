# streetVoice_fighter

## motivation
Due to one of emelentary school friend's commission of making a website for downloading music from [streetvoice](https://streetvoice.com/)

## previous making stuff

### python
using request to download the music steam file link(.m3u8)
and use **ffmpeg** to turn .m3u8 to .mp3

and use **PyInstaller** to turn it into .exe

### web
but my friend is really bad at using computer
so he hope i can make a web for him.

but i don't want to run a web server from my pc forever only for his music download purpose. that sounds **stupid** 
so i found a way to run ffmpeg on static web through **ffmpeg.min.js**
and it only availble on <0.12
and the **CORS** and a lot of restriction made the development so tiring
for the CORS header, i needed to use the netlify

so i turn to GPT and find a new module name hls.js
and end the project quickly.

