---
title: "Android AppWidget如何支持复杂的View"
date: 2009-11-13
author: pengjianqing
categories: ['Android']
tags: ['Android', 'AppWidget', 'EditText', 'ListView', 'RemoteView']
---

如果看不惯博客排版，请点[这里](http://docs.google.com/View?id=dg9p7dc4_52hkb7psc4)。

Android AppWidget如何支持复杂的View

一直想知道如何在AppWidget里面添加 ListView,EditText 这些复杂的View.我们知道要在AppWidget里添加 View都是通过RemoteView来做到了，然而RemoteView本身功能很弱，支持的操作很少，而且支持RemoteView的Widget很少:
在Dev Guide中有下面这段：
```

A RemoteViews object (and, consequently, an App Widget) can support the following layout classes:

    * FrameLayout
    * LinearLayout
    * RelativeLayout

And the following widget classes:

    * AnalogClock
    * Button
    * Chronometer
    * ImageButton
    * ImageView
    * ProgressBar
    * TextView

Descendants of these classes are not supported.

```

所以从这里可以知道，为什么在AppWidget里添加EditText会显示LoadError了，因为本身它就不支持这些复杂的 Widget.

但我们又会有疑问了，为什么Google Search会有EditText呢？其实这些都是假象，并不是AppWidget支持EditText.

具体怎么回事，我猜有两种情况：

1.一种确实是EditText但确不是AppWidget 支持的，而是集成到Home里面去了。

具体可以参考这里：http://www.eoeandroid.com/archiver/tid-1729.html

2.最新的SDK 1.6中，显示在桌面的EditText只是一个ImageView,而这个ImageView的背景就是EditText的截图了。我们点中这个“EditText”后，会调起一个Activity,

而这个Activity就是复杂输入的EditText，并且会全屏显示。所以我们就误以会那是一个单纯的EditText.

最近看过HTC Hero Sense UI的人都看到了，它的AppWidget是确实支持复杂Widget的，比如：Bookmark Widget:ListView/GridView,Twitter Widget:EditText. 这些确实是我们可以看到的，但它是怎么做到的呢？我也很想知道，AppWidget支持到那么强大，甚至超过了本身AP的功能，很抢眼。但不管是怎么实现的，我想人家肯定是花了大力气去做到了，我猜想可能是将Google 提供的AppWidget进行了比较大的改动。我们查看一下framework下的appwidget:
```

pjq@gentoo-pjq ~/android/donut $ ls frameworks/base/core/java/android/appwidget/ -lh
total 60K
-rw-r--r-- 1 pjq users 7.9K 2009-09-29 21:49 AppWidgetHost.java
-rw-r--r-- 1 pjq users  12K 2009-09-29 21:49 AppWidgetHostView.java
-rw-r--r-- 1 pjq users  14K 2009-09-29 21:49 AppWidgetManager.java
-rw-r--r-- 1 pjq users  691 2009-09-29 21:49 AppWidgetProviderInfo.aidl
-rw-r--r-- 1 pjq users 5.6K 2009-09-29 21:49 AppWidgetProviderInfo.java
-rwxr-xr-x 1 pjq users 6.3K 2009-09-29 21:49 AppWidgetProvider.java
-rw-r--r-- 1 pjq users 1.5K 2009-09-29 21:49 package.html

```

可以看到，appwidget的文件很少，虽然不能说明什么，但按照正常的推理，文件少功能一般也强大不到哪里去，这种想法虽然有些牵强，但暂且就这样认为吧。

所以我想HTC一定是将这里给改动了，以支持复杂的Widget,有知道内情的透露一点最好了。

要知道RemoteView的功能很少，特别是对事件处理的能力，都需要通过PendingIntent，传到BroadcastReceiver去处理。所以这里对一些事件处理也仅限于比较简单事件：比如说：Button Clicked，其它的我好像还没怎么用过，orz....  对复杂的View:比如ListView(当然这里还不支持，打个比方)，ListView里面那么多Item,要设置Listener，要传值，这些 RemoteView都不能像一个单纯的Activity那样处理，呵呵 ，扯远了，如果能的话，我也就没有必要这么费劲的写这篇博客了。

写这篇文章的时候，我已经实现了在 AppWidget里显示ListView/GridView这些复杂的Widget了，我这里只说显示，并不是说我已经能让AppWidget支持 ListView/GridView了。所以我这里更倾向于教你如何在AppWidget里支持显示ListView/GridView这些复杂的 Widget.

我们知道AppWidget只支持RemoteView,那哪些Widget是RemoteView呢，我来教你搜一下：
```

pjq@gentoo-pjq ~/android/donut/frameworks/base/core/java/android/widget $ grep -i -n -A 1  @remoteview *.java
AbsoluteLayout.java:40:@RemoteView
AbsoluteLayout.java-41-public class AbsoluteLayout extends ViewGroup {
--
AnalogClock.java:39:@RemoteView
AnalogClock.java-40-public class AnalogClock extends View {
--
Button.java:58:@RemoteView
Button.java-59-public class Button extends TextView {
--
Chronometer.java:45:@RemoteView
Chronometer.java-46-public class Chronometer extends TextView {
--
FrameLayout.java:47:@RemoteView
FrameLayout.java-48-public class FrameLayout extends ViewGroup {
--
ImageButton.java:66:@RemoteView
ImageButton.java-67-public class ImageButton extends ImageView {
--
ImageView.java:55:@RemoteView
ImageView.java-56-public class ImageView extends View {现在没什么问题。
--
LinearLayout.java:44:@RemoteView
LinearLayout.java-45-public class LinearLayout extends ViewGroup {
--
ProgressBar.java:122:@RemoteView
ProgressBar.java-123-public class ProgressBar extends View {
--
RelativeLayout.java:66:@RemoteView
RelativeLayout.java-67-public class RelativeLayout extends ViewGroup {
--
TextView.java:186:@RemoteView
TextView.java-187-public class TextView extends View implements ViewTreeObserver.OnPreDrawListener {

```

就是这些了，类名前面加了"@RemoteView"，和我前面列出的那些是不是一样的呢？--对了，就是这些了，所以以后你想知道你在AppWidget支持哪些Widget就可以像我这样去搜一下就知道了，这样最适时。

写到这里我已经将最关键的内容都已经写出来了，还不明白？

其实简单点讲就是在一个Widget类前面加上"@RemoteView",加上了它就等于说RemoteView可以支持它， RemoteView支持就等于是AppWidget支持这它了。

好了，现在你只需要自定义一些你需要的Widget，加上"@RemoteView"标记，你就可以在AppWidget里使用它了。

关于如何自定义一个Widget你完全可以参照frameworks/base/core/java/android/widget已有的这些Widget.依样加一个。

其实如果你需要自定义一个Widget，比如说支持ListView,你可以先在一个activity里实现它，然后将它移到framework下面去。

这里说一下可能需要注意的地方：

1.如果有多个文件，需要Package的时候，名字最好按照这样的形式：android.widget.bookmark

其中bookmark就是你要添加一个Widget存放的地方，这样的话你就可以在frameworks/base/core/java/android/widget 目录下新增bookmark文件夹，将java文件放在这个目录下。

如果你新增的Widget只有一个java文件就可以不用这样了，可以完全按照已经存在的Widget的样子，直接将java文件放到frameworks/base/core/java/android/widget目录下。

2.资源文件存放：

frameworks/base/core/res/res

资源文件都放到这个目录下。

3.资源的引用：

要用这样的方式引用：com.android.internal.R.drawable.**

4.记着在这个Customer Widget类名前加上"@RemoteView"标记.

这些都做完了，你就已经将一个自定义的Widget添加到framework了。之后要做的工作就是编译整个工程了，重新生成SDK。

最后你就可以在AppWidget引用你新加的这个Widget了：com.widget.bookmark.***。

至此，你已经用上了你新加的这个Widget,并且可以加到AppWidget.

在新加Widget的时候可能会遇到的一些问题：

1.构造函数初始化问题。

如果在XML里写的layout不能直接指定哪个构造函数进行初始化，如果你不确定会跑哪个构造函数，最好在每个构造函数里对加上log,这样你就知道初始化时会跑哪个构造函数，并将初始化的工作加到里面。我当时就遇到了这个问题，因为用XML写layout，你不能显示调用哪个构造函数进行初始化，如果你将初始化的操作放到一个不会自动跑到的构造函数里面，那面你运行的时候就好像没添加到Widget一样。

2.其它的再说吧。

后继我可能会写如何添加Bookmark Widget（支持ListView/GridView,见过HTC Hero Sense UI吗，就是那个样子）到AppWidget,敬请期待！

[![2009-11-14-133525_369x553_scrot](http://farm3.static.flickr.com/2671/4102463746_0868768e3b_o.png)](http://www.flickr.com/photos/pengjianqing/4102463746/)

![](http://img.zemanta.com/pixy.gif?x-id=02f373b7-370b-864e-978e-e39f95bc7df4)