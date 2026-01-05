---
title: "Android Browser Fakewebview和tabPicker分析"
date: 2009-10-12
author: pengjianqing
categories: ['Android']
---

研究了下Android Browser的Fakewebview和tabPicker,在这里做个[笔记](http://docs.google.com/View?id=dg9p7dc4_43hcr83fgr).

Android Browser支持多个tab,最多支持8个:
在TabControl里有设置:
class TabControl {
    // Log Tag
    private static final String LOGTAG = "TabControl";
    // Maximum number of tabs.
    static final int MAX_TABS = 8;

第一次进Browser后,先择Menu会有一个"New Window"的功能,选择后会打开一个新的tap(具体位置直接用SourceInsight查找就行了):
第一次默认会打开设置的HomePage:  openTabAndShow(mSettings.getHomePage(), null, false, null);:
        case R.id.windows_menu_id:
                if (mTabControl.getTabCount() == 1) {
                    openTabAndShow(mSettings.getHomePage(), null, false, null);
                } else {
                    tabPicker(true, mTabControl.getCurrentIndex(), false);
                }
                break;
1.  private TabControl.Tab openTabAndShow(UrlData urlData, final Message msg,
            boolean closeOnExit, String appId)
2.tabPicker(false, ImageGrid.NEW_TAB, false);
3.mTabOverview = new ImageGrid(this, stay, l);
4.   Tab createNewTab(boolean closeOnExit, String appId, String url)

然后再按Menu键会出现"Windows"功能,这个就是由"New Window"变过来的,操作过程:
1. tabPicker(true, mTabControl.getCurrentIndex(), false);
2.  public ImageGrid(Context context, boolean live, Listener l)
3.  mAdapter = new ImageAdapter(context, this, live);
        setAdapter(mAdapter);

之后就会出现一个tap选择界面了,并且是带网页缩略图的.

下面就要找找这个界面是怎么创建出来的:
由于我已经找到了整过过程,所以从下面整理一下整个过程:
1.先从它的定义UI出手:
layout\tabitem.xml里定义了每个item的UI:
```

  
  
  
  

```

包括了一个FakeWebView:显示网页缩略图的,一个TextView:显示网页名称的,一个ImageView显示close按键的.

2.再看看显示网页缩略图的FakeWebView:
public class FakeWebView extends ImageView
extends自ImageView,我们最关注的就是如何将图片显示出来了:
最重要的就是:
   @Override
    protected void onDraw(Canvas canvas) {
        if (mUsesResource) {
            super.onDraw(canvas);
        } else {
            // Always draw white behind the picture just in case the picture
            // draws nothing.
            // FIXME: We used to draw white only when the WebView was null but
            // sometimes the picture was empty. So now we always draw white. It
            // would be nice to know if the picture is empty so we can avoid
            // drawing white.
            canvas.drawColor(Color.WHITE);
            if (mPickerData != null) {
                final Picture p = mPickerData.mPicture;
                if (p != null) {
                    canvas.save();
                    float scale = getWidth() * mPickerData.mScale
                            / mPickerData.mWidth;
                    // Check for NaN and infinity.
                    if (Float.isNaN(scale) || Float.isInfinite(scale)) {
                        scale = 1.0f;
                    }
                    canvas.scale(scale, scale);
                    canvas.translate(-mPickerData.mScrollX,
                            -mPickerData.mScrollY);
                    canvas.drawPicture(p);
                    canvas.restore();
                }
            }
        }
    }
画图像的就是这句:canvas.drawPicture(p);这个picture就是保存在这个tap里的网页缩略图了,这里关于canvas的用法,看说明大概都是:
先canvas.save();然后进行各种操作,如旋转等,再 canvas.restore();

这个类里还有一个重要方法就是:public void setTab(TabControl.Tab t),它提供了给这个FakeWebView绑定数据的功能,所以的数据都是通过它绑定上去的.

3.找到了tapPicker的组成item,再讲讲它是怎样将这些个tabitem放到一起的:
说起来其它也挺简单的,先创建一个ImageGrid,用来摆放这些个item,将给它设置一个ImageAdapter:通过getView方法来创建一个个tabitem,整个过程大概就是这个样子的.
下面先讲讲ImageGride:
class ImageGrid extends GridView implements OnItemClickListener,
        OnCreateContextMenuListener
在它的构造方法里面进行了初始化,最重要的就是设置listener和Adapter了,需要注意的是public interface Listener,
这个接口就是用来监听tabitem点击事件的,包括打开网页和remove掉一个tabitem, 这个接口的具体实现在BrowserActivity里:
private class TabListener implements ImageGrid.Listener
在remove函数里实际了remove掉tabitem的功能,同时它这里也说明了如果仅剩下一个tabitem,remove的操作就相当于是打开一个新的tabitem了.
在onClick函数里就实现了打开一个tabitem的操作.

再讲讲ImageAdapter:
public class ImageAdapter implements ListAdapter
是一个ListAdapter,在getView方法里就有创建一个tabitem的过程:
 LayoutInflater factory = LayoutInflater.from(mContext);
            v = factory.inflate(R.layout.tabitem, null);
在这里也设置了那个关闭按键的listener:
      close.setOnClickListener(new View.OnClickListener() {
                        public void onClick(View v) {
                            ImageAdapter.this.confirmClose(pos);
                        }
                    });
最终在confirmClose里也是调用了s ImageGrid.Listener里的remove方法来关闭.
在这里它也有另外创建一个"New window"的tabitem:ImageGrid.NEW_TAB,
这个地方它用的很巧,它将这个position设置为-1,这样就好区别于其它正常的tabitem了.

关于Fakewebview的整个过程差不多就是这些了,当然这个操作过程中用到的animation就不在这里了.
以后找时间再看看tabitem切换的animation是怎样实现的.

![](http://img.zemanta.com/pixy.gif?x-id=7b1ad3d0-3486-81a3-a5dd-bfabb47bf66f)