---
title: "Android P(9.0/API Level 28) 升级不完全教程"
date: 2019-03-12
author: pengjianqing
categories: ['Android', 'Tech']
tags: ['Android', 'Android Support', 'AndroidX', 'API', 'Google', 'Google Play', 'JetPack']
---

自从去年Google强制升级target API到26之后，Google就开始计划着下一波的升级，而这次是要升级到9, 也就是target API level 28，而且日期也已经定了 "November 1, 2019"。

以前每次API升级都是小打小闹，并不会有那种大规模的改动，而这次改动就有点大了。当然这次强制target API升级对国内开发者的影响会小一些，因为毕竟不用发布到Google Play，而国内应用市场这么多，各个要求也都参差不齐，所以短期还是安全的。

这次改动其实动的最大的就是非官方API的调用，也包含"Java Reflection"，基本上可以说国内要用到的那些动态APP升级方案都基本被伤了，网上搜了一下，也找到一些厅淫技巧，可以绕过去官方的这个限制，正所谓道高一尺，魔高一丈，但总的来说这样做是不推荐的，因为不知道系统又做个升级，就把这些方案给干掉。官文给了黑名单列表和灰名单列表，黑名单是一定要修复的，灰名单只是一个过渡阶段，后面看Google的心情什么时候在系统层面强制执行，那就必须都修复。2019年的Google IO大会在即，就看这次Google有什么表示。

#### 具体我们需要做什么/take away

把官方相关的文档都看过了，下面这些是我认为比较重要的地方

- Migration to androidx/JetPack
- Network TLS enabled by default, so need double check https is enable by default.
- Non SDK APIs call scanning, and fix all the black APIs usage.
- All the "Java Reflection" usage in the code should be migration
- JNI Native code usage, JNI via env->GetFieldID(), JNI via env->GetMethodID()
- Apache HTTP client deprecation
- FLAG_ACTIVITY_NEW_TASK requirement is now enforced, if the context is not Activity.
- Foreground service permission，Apps wanting to use foreground services must now request the FOREGROUND_SERVICE permission first.
- 3rd party libraries comply with the Non SDK Restrictions, need check/upgrade one by one.

其中"Migration to androidx/JetPack"并不是必须的，只是官方其实一直推荐大家都升级，官方宣称以后不会给android.suppor提供技术支持。

### Java Reflection 非官方扫描命令

非官方API调用会是一个比较大的麻烦，因为这个不单单需要修复应用内的有关调用，这个还涉及到其它第三方library。

下面这个命令可以过滤到所有相关"Java Reflection"的调用，之后就是case by case去修。

```
` grep -n -R -i -E  "\.getMethod|\.getDeclared|\.getField\(|\.getFields\(|Class.forName" */src`
```

这些相对来说还比较直接，但如果有用到像JNI Native so的这就需要去查询相关C/C++源码，看是否有相关的调用了。而如果没有源代码，那可能就会比较麻烦，需要去像提供源头确认。

#### Tools to scan the black/grey list

Google还提供了相关工具用来静态扫描APK中的非法调用

```
`./appcompat.sh --dex-file=app-debug.apk`
```

- [https://android.googlesource.com/platform/prebuilts/runtime/+/master/appcompat/](https://android.googlesource.com/platform/prebuilts/runtime/+/master/appcompat/)

可以在上面下载这个工具，需要在Linux下运行，会产生下面的这个列表，最后给出了有多少黑名单，多少灰名单。其实过完这个列表之后，发现然并卵，并没有给出具体涉及的应用内的调用路径，这叫人情何以堪，还有这个工具也直接表明了对"Reflection"会有遗漏，而且它也不能对运行时的API使用，给出结果，所以看到这个扫描结果，真的觉得有点鸡肋，所以目前我还是通过上面grep命令，查到直接的调用结果更靠谱一些，当前这个列表只是作为参考用。

```
`NOTE: appcompat.sh is still under development. It can report
API uses that do not execute at runtime, and reflection uses
that do not exist. It can also miss on reflection uses.
#1: Linking greylist Lsun/misc/Unsafe;->arrayBaseOffset(Ljava/lang/Class;)I use(s):
       Lcom/google/common/primitives/UnsignedBytes$LexicographicalComparatorHolder$UnsafeComparator;->()V

#2: Linking greylist Lsun/misc/Unsafe;->arrayIndexScale(Ljava/lang/Class;)I use(s):
...
#8: Reflection blacklist Landroid/graphics/drawable/Drawable;->getOpticalInsets use(s):
       Landroidx/appcompat/widget/DrawableUtils;->getOpticalBounds(Landroid/graphics/drawable/Drawable;)Landroid/graphics/Rect;
...
#48: Reflection greylist Llibcore/icu/ICU;->addLikelySubtags use(s):
       Landroidx/core/text/ICUCompat;->()V

#49: Reflection greylist Lsun/misc/Unsafe;->allocateInstance use(s):
       Lcom/google/android/gms/internal/zzaqa;->bo()Lcom/google/android/gms/internal/zzaqa;
       Lcom/google/gson/internal/UnsafeAllocator;->create()Lcom/google/gson/internal/UnsafeAllocator;

#50: Reflection greylist Lsun/misc/Unsafe;->theUnsafe use(s):
       Lcom/google/android/gms/internal/zzaqa;->bo()Lcom/google/android/gms/internal/zzaqa;
       Lcom/google/common/primitives/UnsignedBytes$LexicographicalComparatorHolder$UnsafeComparator$1;->run()Ljava/lang/Object;
       Lcom/google/gson/internal/UnsafeAllocator;->create()Lcom/google/gson/internal/UnsafeAllocator;

50 hidden API(s) used: 3 linked against, 47 through reflection
       48 in greylist
       2 in blacklist
       0 in greylist-max-o
       0 in greylist-max-p
To run an analysis that can give more reflection accesses,
but could include false positives, pass the --imprecise flag.`
```

```
`Limitations of the veridex tool include the following:
It can't detect invocations through JNI.
It can detect only a subset of invocations through reflection.
Its analysis for inactive code paths is limited to API level checks.`
```

#### androidx/JetPack migration

自从去年Google发布了JetPack，官方就一直推荐大家升级到androidx, 之前一直被大家吐槽的android support v4/v7/vXXX这次终于有了一个最终的解决方案。以后再也不用为这些个破烂版本号烦心了。

所以这个升级其实会影响到所有有关android support 和material design相关的API。

当然Google官方还是很贴心的，提供了一键升级到androidx的解决方案

> 
Refactor-> Migrate to AndroidX

只是这个方案看似贴心，但其实也是一堆坑等着你去填，因为现在的项目结构会比较复杂，所以一键升级完之后，需要有一堆的编译错误等着你去修。关键是修完这些编译错误，还是无法保证所有的升级都完成了。

事实发现有些错误只是会在运行时出现，所以编译没有错误，不代表运行不会有错误。这个坑就有点可怕了。

所以看来还是需要手工去做一些验证，因为主要改动是android.support ->androidx的改动 还有material design相关API。

所以第一步，生成相关的patch文件

```
`git diff develop > upgrade_28.patch`
```

之后再通过grep命令来查找所有xml相关的改动，因为毕竟widget/view的种类有限，所以可以查到所以的类型，然后手工再一个一个确认一下。

```
` grep -i -E "

```
`	
			

确认好上面这些都没问题之后，还有一个漏洞需要补上，需要确认所有的android.support不再有任何引用，使用下面这个命令就可以查到漏网之鱼

```
`grep -R "android\.support" */src`
```

#### 关于第三方library

目前并没有什么好的办法，只能一个一个去查证，看是否兼容API 28的要求。当然这个需要去再做更多的调查，看是否有什么更好的解决方案。假设真的需要一个一个去验证，那就真的是比较麻烦了。

#### 关于推迟target API 28的想法

因为目前Google给的日期是要到11月1号，所以还有8个月左右的时间去做升级。所以其实也不用这么着急，但计划一定要先做起来。当前我们项目中需要升级到androidx去支持最新的Espreso Automation，所以compile SDK version一定要先升级到28，但至于target SDK，就不是必须的。可以暂时先停留在27。当然这个需要进一步验证，如果这样可行的话，这不失为一个折中方案，因为要完全确定所有Non SDK usage需要比较漫长的时间，而且也可能在个过程中需要涉及现在第三方library的升级。

#### Reference

参考了好多篇官方的文档，所以建议大家都去看看官方升级文档。

- [https://developer.android.com/about/versions/pie/restrictions-non-sdk-interfaces](https://developer.android.com/about/versions/pie/restrictions-non-sdk-interfaces)
- [https://developer.android.com/distribute/best-practices/develop/target-sdk](https://developer.android.com/distribute/best-practices/develop/target-sdk)
- [https://support.google.com/googleplay/android-developer/answer/113469#targetsdk](https://support.google.com/googleplay/android-developer/answer/113469#targetsdk)
- [https://developer.android.com/about/versions/pie/android-9.0-changes-28](https://developer.android.com/about/versions/pie/android-9.0-changes-28)
- [https://developer.android.com/about/versions/pie/android-9.0-migration](https://developer.android.com/about/versions/pie/android-9.0-migration)
- [https://developer.android.com/guide/topics/manifest/uses-sdk-element.html?utm_campaign=adp_series_sdkversion_010616&utm_source=medium&utm_medium=blog#ApiLevels](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html?utm_campaign=adp_series_sdkversion_010616&utm_source=medium&utm_medium=blog#ApiLevels)