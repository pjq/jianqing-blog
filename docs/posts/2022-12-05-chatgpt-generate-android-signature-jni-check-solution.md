---
title: "ChatGPT - Generate Android Signature JNI Check Solution"
date: 2022-12-05
author: pengjianqing
categories: ['Tech']
tags: ['AI', 'Android', 'ChatGPT', 'JNI']
---

ChatGPT太强了，这里展示一个如何让它帮你生成JNI校验Android Signature的代码，几分钟搞定

## Input

As Android developer, I want to protect my App from hacked during the App launch, so I need to do App signature check before the user start to use the App. The prefered way is hardcode the App's signature in the JNI code, and run the JNI code when the App start, can you show the solution and code?

后面我还试了修正的版本

> 

As Android developer, I want to do the check App signature check before the user start to use the App, so I know it's not hacked. The prefered way is hardcode the App's signature in the JNI code, and run the JNI code when the App start, The package name is me.pjq.android The JNI method name is `check_signature`, the return type is true or false. The App's original signature should be hardcoded in the JNI code but not the plaintext and readable, the original signature should be masked. can you show the solution and code and full structure of the App?

## Output

To perform an App signature check in JNI code, you can follow these steps:

- Get the App's signature:

First, you need to get the App's signature. You can use the PackageInfo class to retrieve the App's signature.

```
Copy code`PackageInfo packageInfo = getPackageManager().getPackageInfo(getPackageName(), PackageManager.GET_SIGNATURES);
Signature[] signatures = packageInfo.signatures;
`
```

- Convert the signature to a string:

Next, you need to convert the signature to a string. You can use the Signature.toCharsString() method to convert the signature to a string.

```
Copy code`String signatureString = signatures[0].toCharsString();
`
```

- Pass the signature string to the JNI code:

Then, you need to pass the signature string to the JNI code. You can use the JNI SetStringField() method to pass the signature string to the JNI code.

```
Copy code`jstring signatureString = env->NewStringUTF(signatureString);
env->SetObjectField(obj, env->GetFieldID(env->GetObjectClass(obj), "signature", "Ljava/lang/String;"), signatureString);
`
```

- Verify the signature in the JNI code:

In the JNI code, you can verify the signature by comparing the signature string with the hardcoded signature. If the signatures match, the App is considered to be authentic and can be launched. Otherwise, the App is considered to be hacked and should not be launched.

```
Copy code`jstring signature = (jstring) env->GetObjectField(obj, env->GetFieldID(env->GetObjectClass(obj), "signature", "Ljava/lang/String;"));
const char* signatureString = env->GetStringUTFChars(signature, 0);

if (strcmp(signatureString, "hardcoded_signature") == 0) {
    // App is authentic, launch the App
} else {
    // App is hacked, do not launch the App
}

env->ReleaseStringUTFChars(signature, signatureString);
`
```

Note: The hardcoded signature should be kept secret and not included in the App's code to prevent it from being hacked.

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

Continue

After verifying the App's signature in the JNI code, you can launch the App by calling the appropriate Android activity. For example, you can use the JNI StartActivity() method to launch the main activity of the App.

```
Copy code`jclass activityClass = env->FindClass("android/app/Activity");
jmethodID startActivityMethod = env->GetMethodID(activityClass, "startActivity", "(Landroid/content/Intent;)V");

jclass intentClass = env->FindClass("android/content/Intent");
jmethodID intentConstructor = env->GetMethodID(intentClass, "", "(Landroid/content/Context;Ljava/lang/Class;)V");

jclass mainActivityClass = env->FindClass("com/example/app/MainActivity");

jobject intent = env->NewObject(intentClass, intentConstructor, obj, mainActivityClass);

env->CallVoidMethod(obj, startActivityMethod, intent);
`
```

Note: The main activity class name, "com/example/app/MainActivity" in the above code, should be replaced with the actual main activity class name of your App.

The complete JNI code for performing an App signature check and launching the App can be as follows:

```
Copy code`#include 
#include 

extern "C"
JNIEXPORT void JNICALL
Java_com_example_app_App_launch(JNIEnv *env, jobject obj) {
    // Verify the App's signature
    jstring signature = (jstring) env->GetObjectField(obj, env->GetFieldID(env->GetObjectClass(obj), "signature", "Ljava/lang/String;"));
    const char* signatureString = env->GetStringUTFChars(signature, 0);

    if (strcmp(signatureString, "hardcoded_signature") == 0) {
        // App is authentic, launch the App
        jclass activityClass = env->FindClass("android/app/Activity");
        jmethodID startActivityMethod = env->GetMethodID(activityClass, "startActivity", "(Landroid/content/Intent;)V");

        jclass intentClass = env->FindClass("android/content/Intent");
        jmethodID intentConstructor = env->GetMethodID(intentClass, "", "(Landroid/content/Context;Ljava/lang/Class;)V");

        jclass mainActivityClass = env->FindClass("com/example/app/MainActivity");

        jobject intent = env->NewObject(intentClass, intentConstructor, obj, mainActivityClass);

        env->CallVoidMethod(obj, startActivityMethod, intent);
    } else {
        // App is hacked, do not launch the App
    }

    env->ReleaseStringUTFChars(signature, signatureString);
}
`
```

In the Java code, you can call the JNI launch() method to perform the App signature check and launch the App.

```
Copy code`public class App {
    public static native void launch();

    static {
        System.loadLibrary("app");
    }
}
`
```

You can call the launch() method in the onCreate() method of the App's main activity to perform the App signature check

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

Continue

and launch the App when the App is launched.

```
Copy code`public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Perform App signature check and launch the App
        App.launch();
    }
}
`
```

Note: The above code assumes that the JNI library "app" is already built and placed in the App's libs directory.

This is the general solution for performing an App signature check in JNI code and launching the App. It is important to note that this solution is not foolproof and can be hacked if the attacker is determined and skilled enough. Therefore, it is recommended to use other security measures such as using a secure server to store the App's signature and performing the signature check on the server.

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

Show me the make file

To build the JNI library, you need to create a makefile with the following content:

```
Copy code`LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE    := app
LOCAL_SRC_FILES := app.cpp

include $(BUILD_SHARED_LIBRARY)
`
```

You can use the make command to build the JNI library.

```
Copy code`$ make app
`
```

The JNI library will be built and placed in the libs directory. You can then include the JNI library in your Android project and use it as explained in the previous solution.

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

Show me the full structure of the App

Here is the general structure of the App that performs an App signature check in JNI code and launches the App.

```
Copy code`- app/
  - src/
    - main/
      - java/
        - com/
          - example/
            - app/
              - App.java
              - MainActivity.java
      - jni/
        - app.cpp
  - libs/
    - armeabi/
      - libapp.so
  - Makefile
  - Android.mk
`
```

The App.java file contains the JNI launch() method that performs the App signature check and launches the App.

```
Copy code`public class App {
    public static native void launch();

    static {
        System.loadLibrary("app");
    }
}
`
```

The MainActivity.java file contains the onCreate() method that calls the JNI launch() method to perform the App signature check and launch the App.

```
Copy code`public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Perform App signature check and launch the App
        App.launch();
    }
}
`
```

The app.cpp file contains the JNI code that verifies the App's signature and launches the App.

```
Copy code`#include 
#include 

extern "C"
JNIEXPORT void JNICALL
Java_com_example_app_App_launch(JNIEnv *env, jobject obj) {
    // Verify the App's signature
    jstring signature = (jstring) env->GetObjectField(obj, env->GetFieldID(env->GetObjectClass(obj), "signature", "Ljava/lang/String;"));
    const char* signatureString = env->GetStringUTFChars(signature, 0);

    if (strcmp(signatureString, "hardcoded_signature") == 0) {
        // App is authentic, launch the App
        jclass activityClass = env->FindClass("android/app/Activity");
        jmethodID startActivityMethod = env->GetMethodID(activityClass, "startActivity", "(Landroid/content/Intent;)V");

        jclass intentClass = env->FindClass("android/content/Intent");
        jmethodID intentConstructor = env->GetMethodID(intentClass, "", "(Landroid/content/Context;Ljava/lang/Class;)V");

        jclass mainActivityClass = env->FindClass("com/example/app/MainActivity");

        jobject intent = env->NewObject(intentClass, intentConstructor, obj, mainActivityClass);

        env->CallVoidMethod(obj, startActivityMethod, intent);
    } else {
        // App is hacked, do not launch the App
    }

    env->ReleaseStringUTFChars(signature, signatureString);
}
`
```

The Makefile contains the instructions to build the JNI library.

```
Copy code`LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE    := app
LOCAL
`
```

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

The package name is me.pjq.android

Here is the updated structure of the App that performs an App signature check in JNI code and launches the App.

```
Copy code`- app/
  - src/
    - main/
      - java/
        - me/
          - pjq/
            - android/
              - App.java
              - MainActivity.java
      - jni/
        - app.cpp
  - libs/
    - armeabi/
      - libapp.so
  - Makefile
  - Android.mk
`
```

The App.java file contains the JNI launch() method that performs the App signature check and launches the App.

```
Copy code`package me.pjq.android;

public class App {
    public static native void launch();

    static {
        System.loadLibrary("app");
    }
}
`
```

The MainActivity.java file contains the onCreate() method that calls the JNI launch() method to perform the App signature check and launch the App.

```
Copy code`package me.pjq.android;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Perform App signature check and launch the App
        App.launch();
    }
}
`
```

The app.cpp file contains the JNI code that verifies the App's signature and launches the App.

```
Copy code`#include 
#include 

extern "C"
JNIEXPORT void JNICALL
Java_me_pjq_android_App_launch(JNIEnv *env, jobject obj) {
    // Verify the App's signature
    jstring signature = (jstring) env->GetObjectField(obj, env->GetFieldID(env->GetObjectClass(obj), "signature", "Ljava/lang/String;"));
    const char* signatureString = env->GetStringUTFChars(signature, 0);

    if (strcmp(signatureString, "hardcoded_signature") == 0) {
        // App is authentic, launch the App
        jclass activityClass = env->FindClass("android/app/Activity");
        jmethodID startActivityMethod = env->GetMethodID(activityClass, "startActivity", "(Landroid/content/Intent;)V");

        jclass intentClass = env->FindClass("android/content/Intent");
        jmethodID intentConstructor = env->GetMethodID(intentClass, "", "(Landroid/content/Context;Ljava/lang/Class;)V");

        jclass mainActivityClass = env->FindClass("me/pjq/android/MainActivity");

        jobject intent = env->NewObject(intentClass, intentConstructor, obj, mainActivityClass);

        env->CallVoidMethod(obj, startActivityMethod, intent);
    } else {
        // App is hacked, do not launch the App
    }

    env->ReleaseStringUTFChars(signature, signatureString);
}
`
```

The Makefile contains the instructions to build the JNI library.

```
Copy code`LOCAL_PATH := $(
`
```

![]()

![Jianqing Peng](https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp7rnbPWUnx5FfeOf_2Y5jgJ85lJEz1UGnoCErhsbYU%3Ds96-c&w=64&q=75)

continue

call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := app LOCAL_SRC_FILES := app.cpp

include $(BUILD_SHARED_LIBRARY)

```
Copy code`
You can use the make command to build the JNI library.

`
```

$ make app

```
Copy code`
The JNI library will be built and placed in the libs directory. You can then include the JNI library in your Android project and use it as explained in the previous solution.

Note: The package name, "me.pjq.android" in the above code, should be replaced with the actual package name of your App.`
```