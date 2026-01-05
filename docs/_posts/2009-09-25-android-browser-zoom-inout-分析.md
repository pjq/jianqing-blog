---
title: "Android Browser zoom In/Out 分析"
date: 2009-09-25
author: pengjianqing
categories: ['Android']
---

当我们在用browser浏览网页的时候，上下拖动页面，就会出现一个放大缩小的按键了。
现在要在browser上做multi-touch，可以用两个手指对页面进行放大缩小操作，现在既然已经存在了现在的放大缩小功能，我只要能够
找到它相应的操作就行了。
主要的操作都是在framework下面:WebView.java.
在类WebView的说明里就有一段：
To enable the built-in zoom, set
 * {@link #getSettings() WebSettings}.{@link WebSettings#setBuiltInZoomControls(boolean)}
可以通过这个选择开启还是关闭zoom功能。

在查找的过程中找到了：

```

    /**
     * Perform zoom in in the webview
     * @return TRUE if zoom in succeeds. FALSE if no zoom changes.
     */
    public boolean zoomIn() {
        // TODO: alternatively we can disallow this during draw history mode
        switchOutDrawHistory();
        return zoomWithPreview(mActualScale * 1.25f);
    }

    /**
     * Perform zoom out in the webview
     * @return TRUE if zoom out succeeds. FALSE if no zoom changes.
     */
    public boolean zoomOut() {
        // TODO: alternatively we can disallow this during draw history mode
        switchOutDrawHistory();
        return zoomWithPreview(mActualScale * 0.8f);
    }

```

后来对browser进行调试，在这里设了断点，这里就是zoom in 和zoom out的处理函数了。
找到了这个我就要对browser进行一个简单的测试了：
在BrowserActivity.java里有一个onKeyDown函数，被Override,这个函数可以用来接收按键事件，我就用按下0和1能对应zoom in和zoom out.
在这个函数里我加上这么一段：
```

        Log.v(LOGTAG, "onKey,keyCode:"+keyCode);
        final WebView webView = getTopWindow();
        switch (keyCode) {
            case KeyEvent.KEYCODE_0:
                Log.v(LOGTAG, "KEYCODE_0,zoomIn");
                webView.zoomIn();
                return true;
                //break;

            case KeyEvent.KEYCODE_1:
                Log.v(LOGTAG, "KEYCODE_1,zoomOut");
                webView.zoomOut();
                return true;
                //break;

            default:
                break;
        }

```

这样就可以对按键0和1进行拦截了，然后进行zoomIn和zoom out操作了。
编译，打包，测试，果然和我想的一样，按下0，1后分别会进行zoom in 和zoom out操作了。
测试到这里以后multi-touch也按这种方式处理就行了。

在显示zoom in/out的同时，browser上还会显示，一个“1X”和“X”大概这样的两个按钮，这两个按键又是在哪里进行处理的呢？
继续调试，运气很好，我之前在zoomWithPreview();打了断点，按下“1X”后，就跑到这个函数了，从debug stack中很容易就找到了前面跑过的一些函数了：
最主要的就是这个了：
```

 private void initZoomController(Context context) {
        // Create the buttons controller
        mZoomButtonsController = new ZoomButtonsController(this);
        mZoomButtonsController.setOnZoomListener(mZoomListener);

        // Create the accessory buttons
        LayoutInflater inflater =
                (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        ViewGroup container = mZoomButtonsController.getContainer();
        inflater.inflate(com.android.internal.R.layout.zoom_browser_accessory_buttons, container);
        mZoomOverviewButton =
                (ImageView) container.findViewById(com.android.internal.R.id.zoom_page_overview);
        mZoomOverviewButton.setOnClickListener(
            new View.OnClickListener() {
                public void onClick(View v) {
                    mZoomButtonsController.setVisible(false);
                    zoomScrollOut();
                    if (mLogEvent) {
                        Checkin.updateStats(mContext.getContentResolver(),
                                Checkin.Stats.Tag.BROWSER_ZOOM_OVERVIEW, 1, 0.0);
                    }
                }
            });
        mZoomFitPageButton =
                (ImageView) container.findViewById(com.android.internal.R.id.zoom_fit_page);
        mZoomFitPageButton.setOnClickListener(
            new View.OnClickListener() {
                public void onClick(View v) {
                    zoomWithPreview(1f);
                    updateZoomButtonsEnabled();
                }
            });
    }

```

这里面分别对"1X","X"设置了OnClickListener,具体怎么操作我还没看。
找到这里，就算将Browser的zoom操作具体路线找全了，至于更详细的操作还需要进一步分析。

![](http://img.zemanta.com/pixy.gif?x-id=30b7359f-d8d9-8404-8dbe-5d1924d8709e)