---
title: "Whisper.cpp Playground"
date: 2023-11-30
author: pengjianqing
categories: ['Uncategorized']
---

## Download and try the demo

Here is the github of whisper.cpp

- [https://github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)

```
`make base.en
make medium
make large-v3`
```

```
`/main -m models/ggml-base.en.bin -f samples/jfk.wav`
```

## For Chinese Support

- https://github.com/ggerganov/whisper.cpp/issues/1531

- https://wulu.zone/posts/whisper-cn

```
`./main -m ./models/ggml-medium.bin  -t 8 --step 500 --length 5000 --prompt "请用简体中文输出" -l zh`
```

## Live stream

```
` make stream
 ./stream -l auto -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000 
 ./stream -l auto -m ./models/ggml-medium.bin -t 8 --step 500 --length 5000 
 ./stream -l auto -m ./models/ggml-large-v3.bin -t 8 --step 500 --length 5000 `
```

## Download Youtube

```
`./examples/yt-wsp.sh https://www.youtube.com/watch\?v\=j_8PLI_wCVU\&t\=3321s;`
```

## Subtitle

```
`./main -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -owts
source ./samples/jfk.wav.wts
ffplay ./samples/jfk.wav.mp4`
```

## Models

- https://github.com/ggerganov/whisper.cpp/tree/master/models

## Convert mp4 to wav/mp3 via ffmpeg

```
`ffmpeg -i input.mp4 input.mp4.wav`
```

You can reduce the file size

```
`ffmpeg -i input.mp4 -ar 22050 -ab 128k output.wav
ffmpeg -i input.mp4 input.mp4.mp3`
```

## Bash Script

Put the  convert code into the bash script.

```
`function .toWAV() {
  .log "ffmpeg -i $1 ${1%.mp4}.wav"
  ffmpeg -i $1 ${1%.mp4}.wav
}

function .toSrt() {
  .log "./main -m ./models/ggml-base.en.bin -f $1 -osrt"
  cd ~/pythonProject/whisper.cpp && ./main -m ./models/ggml-base.en.bin -f $1 -osrt
}`
```