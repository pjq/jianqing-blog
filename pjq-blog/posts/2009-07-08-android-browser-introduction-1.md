---
title: "Android Browser Introduction 1"
date: 2009-07-08
author: pengjianqing
categories: ['Android']
tags: ['Android', 'Webkit', '浏览器']
---

最近一直在看Android 浏览器的代码。现在主要在看MMI方面的，还有framework里的，还有Gears（现在支持的网站还不是太多，但确实是一个不错的应用），webkit暂时还没去看了。有时间将心得写下来。不知道有同行吗？可以一起交流交流。
MMI的代码主要在：packages/apps/Browser/
```

pjq@gentoo-pjq /var/www/localhost/htdocs/android_src $ ls packages/apps/Browser/ -lR
packages/apps/Browser/:
total 40
-rw-r--r--  1 root root 11135 2009-06-20 05:23 AndroidManifest.xml
-rw-r--r--  1 root root   372 2009-06-20 05:23 Android.mk
drwxr-xr-x  4 root root  4096 2009-06-20 05:23 assets
-rw-r--r--  1 root root     0 2009-06-20 05:23 MODULE_LICENSE_APACHE2
-rw-r--r--  1 root root 10695 2009-06-20 05:23 NOTICE
drwxr-xr-x 22 root root  4096 2009-06-20 05:23 res
drwxr-xr-x  3 root root  4096 2009-06-20 05:23 src

packages/apps/Browser/assets:
total 8
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 html
drwxr-xr-x 3 root root 4096 2009-06-20 05:23 plugins

packages/apps/Browser/assets/html:
total 4
-rw-r--r-- 1 root root 513 2009-06-20 05:23 flashtest.html

packages/apps/Browser/assets/plugins:
total 1188
drwxr-xr-x 2 root root    4096 2009-06-20 05:23 gears-0.5.17.0
-rw-r--r-- 1 root root 1204872 2009-06-20 05:23 gears.so

packages/apps/Browser/assets/plugins/gears-0.5.17.0:
total 4
-rw-r--r-- 1 root root 58 2009-06-20 05:23 dummy

packages/apps/Browser/res:
total 80
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 anim
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 drawable
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 layout
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 layout-land
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 menu
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-cs
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-de
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-es
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-fr
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-it
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-ja
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-ko
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-nb
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-nl
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-pl
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-ru
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-zh-rCN
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 values-zh-rTW
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 xml

packages/apps/Browser/res/anim:
total 8
-rw-r--r-- 1 root root 1031 2009-06-20 05:23 find_dialog_enter.xml
-rw-r--r-- 1 root root 1031 2009-06-20 05:23 find_dialog_exit.xml

packages/apps/Browser/res/drawable:
total 200
-rw-r--r-- 1 root root  616 2009-06-20 05:23 app_web_browser_sm.png
-rw-r--r-- 1 root root  968 2009-06-20 05:23 browser_bookmark_tab.xml
-rw-r--r-- 1 root root  962 2009-06-20 05:23 browser_history_tab.xml
-rw-r--r-- 1 root root  962 2009-06-20 05:23 browser_visited_tab.xml
-rwxr-xr-x 1 root root 2921 2009-06-20 05:23 dialog_divider_horizontal_light.9.png
-rwxr-xr-x 1 root root  186 2009-06-20 05:23 fav_icn_background.png
-rw-r--r-- 1 root root 1399 2009-06-20 05:23 gears_button_default.9.png
-rw-r--r-- 1 root root 1543 2009-06-20 05:23 gears_button_pressed.9.png
-rw-r--r-- 1 root root 1085 2009-06-20 05:23 gears_button_selected.9.png
-rwxr-xr-x 1 root root 1245 2009-06-20 05:23 gears_button.xml
-rw-r--r-- 1 root root 2421 2009-06-20 05:23 gears_icon_32x32.png
-rw-r--r-- 1 root root 4735 2009-06-20 05:23 gears_icon_48x48.png
-rw-r--r-- 1 root root 1297 2009-06-20 05:23 gears_local_data.png
-rw-r--r-- 1 root root 1640 2009-06-20 05:23 gears_location_data.png
-rw-r--r-- 1 root root 3802 2009-06-20 05:23 gears.png
-rw-r--r-- 1 root root  814 2009-06-20 05:23 ic_btn_close_panel.png
-rw-r--r-- 1 root root  592 2009-06-20 05:23 ic_btn_find_next.png
-rw-r--r-- 1 root root  615 2009-06-20 05:23 ic_btn_find_prev.png
-rw-r--r-- 1 root root 3805 2009-06-20 05:23 ic_dialog_bookmark.png
-rwxr-xr-x 1 root root 4255 2009-06-20 05:23 ic_dialog_browser_certificate_partially_secure.png
-rwxr-xr-x 1 root root 4291 2009-06-20 05:23 ic_dialog_browser_certificate_secure.png
-rwxr-xr-x 1 root root 3556 2009-06-20 05:23 ic_dialog_browser_security_bad.png
-rwxr-xr-x 1 root root 3415 2009-06-20 05:23 ic_dialog_browser_security_good.png
-rwxr-xr-x 1 root root 1187 2009-06-20 05:23 ic_dialog_menu_generic.png
-rwxr-xr-x 1 root root 3610 2009-06-20 05:23 ic_launcher_browser.png
-rw-r--r-- 1 root root 2738 2009-06-20 05:23 ic_launcher_drm_file.png
-rw-r--r-- 1 root root 2899 2009-06-20 05:23 ic_launcher_shortcut_browser_bookmark.png
-rw-r--r-- 1 root root 1080 2009-06-20 05:23 ic_menu_bookmark.png
-rw-r--r-- 1 root root 1244 2009-06-20 05:23 ic_menu_windows.png
-rw-r--r-- 1 root root 3010 2009-06-20 05:23 ic_new_window.png
-rwxr-xr-x 1 root root  806 2009-06-20 05:23 ic_search_category_bookmark.png
-rw-r--r-- 1 root root 2395 2009-06-20 05:23 ic_search_category_browser.png
-rwxr-xr-x 1 root root  900 2009-06-20 05:23 ic_search_category_history.png
-rwxr-xr-x 1 root root  819 2009-06-20 05:23 ic_search_category_suggest.png
-rw-r--r-- 1 root root 4125 2009-06-20 05:23 ic_tab_browser_bookmark_selected.png
-rw-r--r-- 1 root root 4207 2009-06-20 05:23 ic_tab_browser_bookmark_unselected.png
-rw-r--r-- 1 root root 2315 2009-06-20 05:23 ic_tab_browser_history_selected.png
-rw-r--r-- 1 root root 2528 2009-06-20 05:23 ic_tab_browser_history_unselected.png
-rw-r--r-- 1 root root 4362 2009-06-20 05:23 ic_tab_browser_visited_selected.png
-rw-r--r-- 1 root root 4416 2009-06-20 05:23 ic_tab_browser_visited_unselected.png
-rw-r--r-- 1 root root 1224 2009-06-20 05:23 page_indicator.png
-rw-r--r-- 1 root root  188 2009-06-20 05:23 page_indicator_unselected2.png
-rw-r--r-- 1 root root 3216 2009-06-20 05:23 ssl_icon.png

packages/apps/Browser/res/layout:
total 112
-rw-r--r-- 1 root root  2484 2009-06-20 05:23 add_new_bookmark.xml
-rw-r--r-- 1 root root  3656 2009-06-20 05:23 browser_add_bookmark.xml
-rw-r--r-- 1 root root  1084 2009-06-20 05:23 browser_bookmarks_page.xml
-rw-r--r-- 1 root root  3340 2009-06-20 05:23 browser_download_item.xml
-rw-r--r-- 1 root root   904 2009-06-20 05:23 browser_downloads_page.xml
-rw-r--r-- 1 root root  2867 2009-06-20 05:23 browser_find.xml
-rw-r--r-- 1 root root  2092 2009-06-20 05:23 browser_subwindow.xml
-rw-r--r-- 1 root root  1005 2009-06-20 05:23 empty_history.xml
-rw-r--r-- 1 root root  3510 2009-06-20 05:23 gears_dialog_permission.xml
-rw-r--r-- 1 root root  3928 2009-06-20 05:23 gears_dialog_settings_row.xml
-rw-r--r-- 1 root root  1806 2009-06-20 05:23 gears_dialog_settings.xml
-rw-r--r-- 1 root root  5215 2009-06-20 05:23 gears_dialog.xml
-rw-r--r-- 1 root root  3303 2009-06-20 05:23 gears_settings_row.xml
-rw-r--r-- 1 root root  1585 2009-06-20 05:23 gears_settings.xml
-rw-r--r-- 1 root root  1056 2009-06-20 05:23 history_header.xml
-rw-r--r-- 1 root root  2681 2009-06-20 05:23 history_item.xml
-rw-r--r-- 1 root root  2598 2009-06-20 05:23 http_authentication.xml
-rw-r--r-- 1 root root  1004 2009-06-20 05:23 no_downloads.xml
-rw-r--r-- 1 root root  2767 2009-06-20 05:23 page_info.xml
-rw-r--r-- 1 root root 11588 2009-06-20 05:23 ssl_certificate.xml
-rw-r--r-- 1 root root  1723 2009-06-20 05:23 ssl_success.xml
-rw-r--r-- 1 root root  1873 2009-06-20 05:23 ssl_warnings.xml
-rw-r--r-- 1 root root  1563 2009-06-20 05:23 ssl_warning.xml
-rw-r--r-- 1 root root  2035 2009-06-20 05:23 tabitem.xml
-rw-r--r-- 1 root root  1498 2009-06-20 05:23 tabs.xml

packages/apps/Browser/res/layout-land:
total 20
-rw-r--r-- 1 root root  2911 2009-06-20 05:23 http_authentication.xml
-rw-r--r-- 1 root root  2635 2009-06-20 05:23 page_info.xml
-rw-r--r-- 1 root root 10824 2009-06-20 05:23 ssl_certificate.xml

packages/apps/Browser/res/menu:
total 48
-rw-r--r-- 1 root root 1659 2009-06-20 05:23 bookmarkscontext.xml
-rw-r--r-- 1 root root  899 2009-06-20 05:23 bookmarks.xml
-rw-r--r-- 1 root root 2774 2009-06-20 05:23 browsercontext.xml
-rw-r--r-- 1 root root 5254 2009-06-20 05:23 browser.xml
-rw-r--r-- 1 root root  850 2009-06-20 05:23 downloadhistorycontextfailed.xml
-rw-r--r-- 1 root root  951 2009-06-20 05:23 downloadhistorycontextfinished.xml
-rw-r--r-- 1 root root  852 2009-06-20 05:23 downloadhistorycontextrunning.xml
-rw-r--r-- 1 root root 1106 2009-06-20 05:23 downloadhistory.xml
-rw-r--r-- 1 root root 1404 2009-06-20 05:23 historycontext.xml
-rw-r--r-- 1 root root  916 2009-06-20 05:23 history.xml
-rw-r--r-- 1 root root 1153 2009-06-20 05:23 tabscontext.xml

packages/apps/Browser/res/values:
total 56
-rw-r--r-- 1 root root  1535 2009-06-20 05:23 colors.xml
-rw-r--r-- 1 root root 42028 2009-06-20 05:23 strings.xml
-rw-r--r-- 1 root root  1992 2009-06-20 05:23 styles.xml
-rw-r--r-- 1 root root  1223 2009-06-20 05:23 themes.xml

packages/apps/Browser/res/values-cs:
total 24
-rw-r--r-- 1 root root 22875 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-de:
total 24
-rw-r--r-- 1 root root 22911 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-es:
total 24
-rw-r--r-- 1 root root 23070 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-fr:
total 24
-rw-r--r-- 1 root root 23315 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-it:
total 24
-rw-r--r-- 1 root root 22487 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-ja:
total 24
-rw-r--r-- 1 root root 24252 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-ko:
total 24
-rw-r--r-- 1 root root 23102 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-nb:
total 24
-rw-r--r-- 1 root root 21506 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-nl:
total 24
-rw-r--r-- 1 root root 22562 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-pl:
total 24
-rw-r--r-- 1 root root 22926 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-ru:
total 28
-rw-r--r-- 1 root root 28399 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-zh-rCN:
total 24
-rw-r--r-- 1 root root 21071 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/values-zh-rTW:
total 24
-rw-r--r-- 1 root root 20727 2009-06-20 05:23 strings.xml

packages/apps/Browser/res/xml:
total 20
-rw-r--r-- 1 root root 8291 2009-06-20 05:23 browser_preferences.xml
-rw-r--r-- 1 root root 2558 2009-06-20 05:23 debug_preferences.xml
-rw-r--r-- 1 root root 1446 2009-06-20 05:23 searchable.xml

packages/apps/Browser/src:
total 4
drwxr-xr-x 3 root root 4096 2009-06-20 05:23 com

packages/apps/Browser/src/com:
total 4
drwxr-xr-x 3 root root 4096 2009-06-20 05:23 android

packages/apps/Browser/src/com/android:
total 4
drwxr-xr-x 2 root root 4096 2009-06-20 05:23 browser

packages/apps/Browser/src/com/android/browser:
total 540
-rw-r--r-- 1 root root   9312 2009-06-20 05:23 AddBookmarkPage.java
-rw-r--r-- 1 root root   2207 2009-06-20 05:23 AddNewBookmark.java
-rw-r--r-- 1 root root   3318 2009-06-20 05:23 BookmarkItem.java
-rw-r--r-- 1 root root 190922 2009-06-20 05:23 BrowserActivity.java
-rw-r--r-- 1 root root  20379 2009-06-20 05:23 BrowserBookmarksAdapter.java
-rw-r--r-- 1 root root  16045 2009-06-20 05:23 BrowserBookmarksPage.java
-rw-r--r-- 1 root root   9056 2009-06-20 05:23 BrowserDownloadAdapter.java
-rw-r--r-- 1 root root  18026 2009-06-20 05:23 BrowserDownloadPage.java
-rw-r--r-- 1 root root  17139 2009-06-20 05:23 BrowserHistoryPage.java
-rw-r--r-- 1 root root   2212 2009-06-20 05:23 BrowserHomepagePreference.java
-rw-r--r-- 1 root root   1834 2009-06-20 05:23 Browser.java
-rw-r--r-- 1 root root   2592 2009-06-20 05:23 BrowserPluginList.java
-rw-r--r-- 1 root root   5472 2009-06-20 05:23 BrowserPreferencesPage.java
-rw-r--r-- 1 root root  26851 2009-06-20 05:23 BrowserProvider.java
-rw-r--r-- 1 root root   2427 2009-06-20 05:23 BrowserSearchpagePreference.java
-rw-r--r-- 1 root root  16466 2009-06-20 05:23 BrowserSettings.java
-rw-r--r-- 1 root root   2207 2009-06-20 05:23 BrowserYesNoPreference.java
-rw-r--r-- 1 root root   4744 2009-06-20 05:23 CombinedBookmarkHistoryActivity.java
-rw-r--r-- 1 root root   2511 2009-06-20 05:23 Dots.java
-rw-r--r-- 1 root root   3690 2009-06-20 05:23 FakeWebView.java
-rw-r--r-- 1 root root   4940 2009-06-20 05:23 FetchUrlMimeType.java
-rw-r--r-- 1 root root   7465 2009-06-20 05:23 FindDialog.java
-rw-r--r-- 1 root root  12950 2009-06-20 05:23 GearsBaseDialog.java
-rw-r--r-- 1 root root   8616 2009-06-20 05:23 GearsNativeDialog.java
-rw-r--r-- 1 root root   4358 2009-06-20 05:23 GearsPermissionsDialog.java
-rw-r--r-- 1 root root   5260 2009-06-20 05:23 GearsPermissions.java
-rw-r--r-- 1 root root  15877 2009-06-20 05:23 GearsSettingsDialog.java
-rw-r--r-- 1 root root   5142 2009-06-20 05:23 HistoryItem.java
-rw-r--r-- 1 root root   8128 2009-06-20 05:23 ImageAdapter.java
-rw-r--r-- 1 root root   7643 2009-06-20 05:23 ImageGrid.java
-rw-r--r-- 1 root root   3924 2009-06-20 05:23 KeyTracker.java
-rw-r--r-- 1 root root   6520 2009-06-20 05:23 MostVisitedActivity.java
-rw-r--r-- 1 root root  35937 2009-06-20 05:23 TabControl.java

```

Framework的在：frameworks/base/core/java/android/webkit/
```

pjq@gentoo-pjq /var/www/localhost/htdocs/android_src $ ls frameworks/base/core/java/android/webkit/ -Rl
frameworks/base/core/java/android/webkit/:
total 836
-rw-r--r-- 1 root root  28906 2009-06-20 05:22 BrowserFrame.java
-rw-r--r-- 1 root root   3806 2009-06-20 05:22 ByteArrayBuilder.java
-rw-r--r-- 1 root root   2169 2009-06-20 05:22 CacheLoader.java
-rw-r--r-- 1 root root  26745 2009-06-20 05:22 CacheManager.java
-rw-r--r-- 1 root root  39919 2009-06-20 05:22 CallbackProxy.java
-rw-r--r-- 1 root root   4349 2009-06-20 05:22 ContentLoader.java
-rw-r--r-- 1 root root  35564 2009-06-20 05:22 CookieManager.java
-rw-r--r-- 1 root root   6611 2009-06-20 05:22 CookieSyncManager.java
-rw-r--r-- 1 root root   2559 2009-06-20 05:22 DataLoader.java
-rw-r--r-- 1 root root   3882 2009-06-20 05:22 DateSorter.java
-rw-r--r-- 1 root root   1300 2009-06-20 05:22 DownloadListener.java
-rw-r--r-- 1 root root   4943 2009-06-20 05:22 FileLoader.java
-rw-r--r-- 1 root root  13886 2009-06-20 05:22 FrameLoader.java
drwxr-xr-x 2 root root   4096 2009-06-20 05:22 gears
-rw-r--r-- 1 root root   4722 2009-06-20 05:22 HttpAuthHandler.java
-rw-r--r-- 1 root root   6326 2009-06-20 05:22 HttpDateTime.java
-rw-r--r-- 1 root root   1578 2009-06-20 05:22 JsPromptResult.java
-rw-r--r-- 1 root root   2289 2009-06-20 05:22 JsResult.java
-rw-r--r-- 1 root root   6142 2009-06-20 05:22 JWebCoreJavaBridge.java
-rw-r--r-- 1 root root  54751 2009-06-20 05:22 LoadListener.java
-rw-r--r-- 1 root root  26861 2009-06-20 05:22 MimeTypeMap.java
-rw-r--r-- 1 root root  10207 2009-06-20 05:22 Network.java
-rw-r--r-- 1 root root    224 2009-06-20 05:22 package.html
-rw-r--r-- 1 root root   1475 2009-06-20 05:22 PerfChecker.java
-rw-r--r-- 1 root root   3831 2009-06-20 05:22 PluginContentLoader.java
-rw-r--r-- 1 root root   3384 2009-06-20 05:22 PluginData.java
-rw-r--r-- 1 root root   3430 2009-06-20 05:22 Plugin.java
-rw-r--r-- 1 root root   2236 2009-06-20 05:22 PluginList.java
-rw-r--r-- 1 root root   6930 2009-06-20 05:22 SslErrorHandler.java
-rw-r--r-- 1 root root   6897 2009-06-20 05:22 StreamLoader.java
-rw-r--r-- 1 root root  23870 2009-06-20 05:22 TextDialog.java
-rw-r--r-- 1 root root   1766 2009-06-20 05:22 UrlInterceptHandler.java
-rw-r--r-- 1 root root   4275 2009-06-20 05:22 UrlInterceptRegistry.java
-rw-r--r-- 1 root root  12297 2009-06-20 05:22 URLUtil.java
-rw-r--r-- 1 root root   6434 2009-06-20 05:22 WebBackForwardList.java
-rw-r--r-- 1 root root   7331 2009-06-20 05:22 WebChromeClient.java
-rw-r--r-- 1 root root   5570 2009-06-20 05:22 WebHistoryItem.java
-rw-r--r-- 1 root root   8927 2009-06-20 05:22 WebIconDatabase.java
-rw-r--r-- 1 root root  36389 2009-06-20 05:22 WebSettings.java
-rw-r--r-- 1 root root   5150 2009-06-20 05:22 WebSyncManager.java
-rw-r--r-- 1 root root   8222 2009-06-20 05:22 WebViewClient.java
-rw-r--r-- 1 root root  66050 2009-06-20 05:22 WebViewCore.java
-rw-r--r-- 1 root root  35258 2009-06-20 05:22 WebViewDatabase.java
-rw-r--r-- 1 root root 211118 2009-06-20 05:22 WebView.java

frameworks/base/core/java/android/webkit/gears:
total 128
-rw-r--r-- 1 root root  5935 2009-06-20 05:22 AndroidGpsLocationProvider.java
-rw-r--r-- 1 root root  9004 2009-06-20 05:22 AndroidRadioDataProvider.java
-rw-r--r-- 1 root root  5029 2009-06-20 05:22 AndroidWifiDataProvider.java
-rw-r--r-- 1 root root 42345 2009-06-20 05:22 ApacheHttpRequestAndroid.java
-rw-r--r-- 1 root root  4522 2009-06-20 05:22 DesktopAndroid.java
-rw-r--r-- 1 root root  4876 2009-06-20 05:22 NativeDialog.java
-rw-r--r-- 1 root root    22 2009-06-20 05:22 package.html
-rw-r--r-- 1 root root  2960 2009-06-20 05:22 PluginSettings.java
-rw-r--r-- 1 root root 14685 2009-06-20 05:22 UrlInterceptHandlerGears.java
-rw-r--r-- 1 root root  5217 2009-06-20 05:22 VersionExtractor.java
-rw-r--r-- 1 root root  7583 2009-06-20 05:22 ZipInflater.java

```

其中文件Android.mk，中定义了编译规则，简单说应该就是一个简化版的Makefile了。其中定义了编译时的模块名称，所以如果配置好了编译环境，可以用mm Browser来编译Browser.

BrowserActivity.java是程序主入口了。