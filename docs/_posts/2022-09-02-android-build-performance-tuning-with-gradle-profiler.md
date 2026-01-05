---
title: "Android Build Performance Tuning with gradle-profiler"
date: 2022-09-02
author: pengjianqing
categories: ['Android', 'Tech']
---

If your project have more and more modules and source code, the build will be the nightmare, it will take more than 10 mins to build, for release build, it will take even more time, so we can use the gradle-profiler to figure out the bottleneck, and take actions to do the build performance tuning accordingly.

### gradle-profiler in local environment

##### Install gradle-profiler

- [https://github.com/gradle/gradle-profiler#installing](https://github.com/gradle/gradle-profiler#installing)

curl -s "https://get.sdkman.io" | bash sdk install gradleprofiler 
gradle-profiler --benchmark help

##### Run gradle-profiler

gradle-profiler --profile chrome-trace --jprofiler-alloc --project-dir $PWD --output-dir out/profiler/apkBuild app:assembleRelease

##### Loading the json to Chrome

[chrome://tracing/](chrome://tracing/)

### gradle-profiler in docker environment

##### Start docker

docker run -it --memory="8g" --platform linux/amd64 -v $(pwd):/Develop alvrme/alpine-android:latest-jdk11 /bin/bash
cd /Develop

##### Install gradle-profiler

- [https://github.com/gradle/gradle-profiler#installing](https://github.com/gradle/gradle-profiler#installing)

apk add zip 
curl -s "https://get.sdkman.io" | bash sdk install gradleprofiler 
gradle-profiler --benchmark help

##### Run gradle-profiler

gradle-profiler --profile chrome-trace --jprofiler-alloc --project-dir $PWD --output-dir out/profiler/apkBuild app:assembleRelease

##### Loading the json to Chrome

[chrome://tracing/](chrome://tracing/)

### With scenarios for clean build

gradle-profiler --profile chrome-trace --jprofiler-alloc --project-dir $PWD --output-dir out/profiler/apkBuild --scenario-file scenarios.txt

scenarios.txt

clean_build {
 tasks = [":app:assembleRelease"] 
cleanup-tasks = ["clean"] 
}

## Benchmark with gradle-profiler

```
`gradle-profiler --benchmark --project-dir .  --scenario-file clean-build-scenario.txt`
```

### chrome://tracing Shortcut

- w/s:zoom in/out
- a/d: move left/right
- mouse: scroll up/down