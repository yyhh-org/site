---
Status: draft
Lang: en
Title: "Writing C code in Java: GraalVM specific programming"
Date: 2021-02-08T05:41:23.469Z
Author: Huahai
Category: notebook
Tags: Java, GraalVM
---
One of the latest fashions in the Java world is [GraalVM](https://www.graalvm.org/). For an old guy who have been around, I still remember the "Write once, run anywhere" slogan of Java virtual machine. Apparently, the wheel has spun back, now people want to write native code in Java, which has to be compiled to different machine codes in different platforms. 

The driven forces for this change may include the often lamented slow startup time of Java programs. For the brave new world of serverless functions, a quick starting program makes a lot of economic sense. The small but vibrant [Clojure](https://clojure.org/) community, which I am part of, is particularly excited about this new found capability of JVM, for we can now write fast starting command line programs using our beloved language. For example, [Babashka](https://github.com/babashka/babashka) is one such program that has taken the community by storm. 

As the author of [Datalevin](https://github.com/juji-io/datalevin), a relatively new open source Datalog database, I have decided to answer some of my users requests to build a native version of Datalevin using GraalVM native image technology. After some trials and errors, I have gotten a native version of Datalevin to pass all the tests, I am ready to share some of my experience and tips.

## Failed attempt to compile Datalevn to native image

The difficulty of directly compiling Datalevin to GraalVM native image lies in our use of [JNR](https://github.com/jnr/jnr-ffi) library to talk to [LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database), the underlying key-value store that is written in C. As far as I know, no one has succeeded in getting JNR to work with native image. This is not for the lack of trying. See for example [this issue](https://github.com/oracle/graal/issues/675). I myself have tried a couple of days. Although I think I have gone further than most, the need to rerun some class initialization prevented me from succeeding. Apparently, GraalVM team also does not think it is feasible at this point.

So I am left with two options: one is to use a different LMDB wrapper that does not use JNR. For example, a JNI based LMDB wrapper is available and GraalVM native image does support JNI. However, that code has not been updated for a long time and the author of the said code actually joined the team that uses JNR. The other option, is to write a LMDB wrapper of my own that can run in native image. So I did just that.

## Writing C code in Java

As a native technology, GraalVM obviously has the facility to interface with C code. Not just that, it must also have the facility to write native code. Fortunately, such facility is also packaged as a SDK that is publicly available. The only problem is that there's no official documentation for it, just a [Java API doc](https://www.graalvm.org/sdk/javadoc/index.html?org/graalvm/nativeimage/c/package-summary.html) and a [coding example](https://github.com/oracle/graal/blob/master/substratevm/src/com.oracle.svm.tutorial/src/com/oracle/svm/tutorial/CInterfaceTutorial.java). After some search, I also found a couple of more samples: [OpenGL demo](https://github.com/praj-foss/opengl-graal-examples), [neo4j native driver](https://github.com/michael-simons/neo4j-java-driver-native-lib) and [uname utility](https://github.com/praj-foss/uname-graalvm-demo). I hope that this blog post adds to this growing samples of GraalVM specic programming.  

### Import C data and functions

### Memory management and pointer wrangling

### 