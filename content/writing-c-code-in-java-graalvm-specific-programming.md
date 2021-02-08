---
Status: published
Lang: en
Title: "Writing C code in Java/Clojure: GraalVM specific programming"
Date: 2021-02-08T05:41:23.469Z
Author: Huahai
Category: notebook
Tags: Clojure, Java, GraalVM
---
One of the latest fashions in the Java world is [GraalVM](https://www.graalvm.org/). For someone who has been around, I still remember the "Write once, run anywhere" slogan of Java virtual machine. Apparently, the wheel has spun back, now people want to write native code in Java, which has to be compiled to different machine codes in different platforms. 

The driven forces for this change may include the often lamented slow startup time of Java programs. For the brave new world of serverless functions, a quick starting program makes a lot of economic sense. The small but vibrant [Clojure](https://clojure.org/) community, which I consider myself a part of, is particularly excited about this new found capability of JVM, for we now have one more way to write quick starting command line programs using our beloved language. The other way is to use ClojureScript on one of the Javascript engines, but Javascript engines are slower than JVM and not as nice. For example, [Babashka](https://github.com/babashka/babashka) is one such example that has taken the community by storm. 

As the author of [Datalevin](https://github.com/juji-io/datalevin), a relatively new open source Datalog database, I have decided to answer the users' call for a native version of Datalevin using GraalVM native image technology. After some trials and errors, I have gotten a native version of Datalevin to pass all the tests. Now I can share some experience.

## Failed attempts to compile Datalevn to native image

The difficulty of directly compiling Datalevin to GraalVM native image lies in our use of [JNR](https://github.com/jnr/jnr-ffi) library to wrap [LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database), the underlying key-value store that is written in C. As far as I know, no one has succeeded in getting JNR to work with native image. This is not for the lack of trying, see for example [this effort](https://github.com/borkdude/datalevin-native) and [this issue](https://github.com/oracle/graal/issues/675). I myself have tried really hard. Although I think I have gone further than many, the need to rerun some class initialization at runtime prevented me from succeeding. Apparently, some GraalVM team members also think it is not easy to do at this point.

I am left with two options: one is to use a different LMDB wrapper that does not use JNR. For example, a [JNI based LMDB wrapper](https://github.com/deephacks/lmdbjni) is available and GraalVM native image does support JNI. However, that code has not been updated for a long time and its maintainer seems to have joined [LMDBJava](https://github.com/lmdbjava/lmdbjava), the LMDB wrapper that uses JNR. The other option is to write a LMDB wrapper of my own that can run in native image. So I [did just that](https://github.com/juji-io/datalevin/tree/master/native).

## Writing C code in Java/Clojure

As a native technology, GraalVM obviously has the facility to interface with C code. Not just that, it must also have the facility to write native code on its own. Fortunately, such facility is also packaged as a SDK that is publicly available. To use this SDK, one has to be familiar with not just Java, but also C programming, because effectively, it is writing low level C code in Java syntax. 

The only problem is that there isn't an official documentation for this kind of programming, just a [Java doc](https://www.graalvm.org/sdk/javadoc/index.html?org/graalvm/nativeimage/c/package-summary.html) and a [coding example](https://github.com/oracle/graal/blob/master/substratevm/src/com.oracle.svm.tutorial/src/com/oracle/svm/tutorial/CInterfaceTutorial.java). After some research, I also found a few other examples: an [OpenGL demo](https://github.com/praj-foss/opengl-graal-examples), a [neo4j native driver](https://github.com/michael-simons/neo4j-java-driver-native-lib) and an [uname utility](https://github.com/praj-foss/uname-graalvm-demo). I hope that this blog post adds to this growing library of GraalVM specific programming examples.  

### Import C data and functions

Our goal is to write a LMDB wrapper with GraalVM SDK without using JNI. 

The first step is to make Java aware of the LMDB C data structures and functions declared in the header file `lmdb.h`, so that our Java code can use them. This step is fairly easy and pleasant, compared with JNI. All one needs to do is to write a Java class to list all those C structs, enums and functions as native interfaces and annotate these with appropriate GraalVM specific annotations. 

For example, for a C struct definition:

```C
typedef struct MDB_val {
	size_t		 mv_size;	/**< size of the data item */
	void		*mv_data;	/**< address of the data item */
} MDB_val;
```
The corresponding Java declaration is the following:

```Java
    @CStruct("MDB_val")
    public interface MDB_val extends PointerBase {

        @CField("mv_size")
        long get_mv_size();

        @CField("mv_size")
        void set_mv_size(long value);

        @CField("mv_data")
        VoidPointer get_mv_data();

        @CField("mv_data")
        void set_mv_data(VoidPointer value);
    }
```
The `CStruct` annotation tells Java which C struct to import. I gave the Java interface the same name as C so it is easier for me to keep track. One could also name it otherwise, e.g. "MDBVal" if one wants to follow CamelCases. It does not matter.

`PointerBase` interface indicates a native word type, and is the root of all C pointers being imported into Java. Most things in GraalVM SDK work with these native word types.

`CField` annotation import a C struct field as a Java method. Setters and getters need to be declared separately. Again, I give these methods similar names as C field names, but you may prefer to follow Java name convention instead, e.g. "getMvSize".

`VoidPointer` is a faithful translation of `void *`.

For an opaque C struct declaration that does not list its fields, one must add an `incomplete` option to the annotation, otherwise compilation will fail with a "sizeOf" error. For example, for a C struct like this:

```C
typedef struct MDB_env MDB_env;
```
The corresponding Java declaration is this:
```Java
    @CStruct(value = "MDB_env", isIncomplete = true)
    public interface MDB_env extends PointerBase {}
```

C functions are directly translated into Java static native methods, e.g.:

```C
int  mdb_env_get_maxkeysize(MDB_env *env);
```
The corresponding Java declaration is the following:
```Java
    @CFunction("mdb_env_get_maxkeysize")
    public static native int mdb_env_get_maxkeysize(MDB_env env);
```
Notice that the pointer to `MDB_env` struct is replaced by `MDB_env` Java interface declared above, as it extends `PointerBase`.

For parameters with double pointer type, one can declare them as `WordPointer` in Java, as they point to another pointer (i.e. word). For example, this C function:
```C
int  mdb_env_create(MDB_env **env);
```
is translated into this Java code:
```Java
    @CFunction("mdb_env_create")
    public static native int mdb_env_create(WordPointer envPtr);
```
Finally, for these annotations to work, the containing class must be annotated with appropriate C context, which is often defined as a static inner class of the class, like so:
```Java
@CContext(Lib.Directives.class)
public final class Lib {

    public static final class Directives implements CContext.Directives {
        @Override
        public List<String> getHeaderFiles() {
            return Collections.singletonList("<lmdb.h>");
        }

        @Override
        public List<String> getLibraries() {
            return Arrays.asList("lmdb");
        }
    }
    ...
}
```
The `CContext.Directives` class imports the necessary C header file and finds the corresponding C library. In this particular example, we are importing the system wide LMDB header file and library installed by `apt install liblmdb-dev` on Debian/Ubuntu. An example of importing local header file and library can be found in Datalevin source code [here](https://github.com/juji-io/datalevin/blob/master/native/src/java/datalevin/ni/Lib.java#L55).

The code of all C to Java translations is [here](https://github.com/juji-io/datalevin/blob/master/native/src/java/datalevin/ni/Lib.java)

### Clojure specific considerations

Clojure `deftype` supports Java annotations, so that is what I used to implement the higher level constructs of the LMDB wrapper. For example:
```Clojure
(deftype ^{Retention RetentionPolicy/RUNTIME
           CContext  {:value Lib$Directives}}
    LMDB [^Env env
          ^String dir
          ^RtxPool pool
          ^ConcurrentHashMap dbis
          ^:volatile-mutable closed?]
  ...)
```

One limitation that one needs to be aware of when writing native image related Clojure code, is that most things in the GraalVM SDK inherit from `org.graalvm.word.WordBase`, not from `java.lang.Object`, which breaks the hidden assumption of a lot of Clojure constructs. For example, one cannot do this: 
```Clojure
(let [env ^Lib$MDB_env (Env/create)]
  ...)
```
Because `Lib$MDB_env` extends `PointerBase`, but Clojure `let` seems to assume everything getting bound is an `Object`. An "expecting Object but got Word" or vice visa error will be thrown during compilation for these cases. So writing a thin layer of wrapper for these GraalVM word types seems to be inevitable, unless Clojure can be enhanced to be more native image programming friendly.

Another point of caution is about arrays. GraalVM uses reflection to create array objects, but if these array objects are not declared at build time, the code won't run. For instance, for Clojure `into-array` function, we should not omit the optional second argument for element data type, otherwise, one has to manually specify the array type in the [`reflection.json` file during compilation](https://www.graalvm.org/reference-manual/native-image/Reflection/), or the Graal runtime will complain about "Class such and such is instantiated reflectively but was never registered". For Clojure dynamically generated classes with names such as these, "datalevin.test.query$fn__12734$fn__12739$fn__12740[]", it is impossible to add them manually in `reflection.json`. So the only solution is to specify the element data type in code, e.g. `(into-array Object data)`, instead of `(into-array data)`.

The full Clojure project for native Datalevin is [here](https://github.com/juji-io/datalevin/tree/master/native). 

### Memory management and pointer wrangling

The main challenge of building a LMDB wrapper is to find a way to put transaction data into and get retrieved data out of LMDB. As shown above, LMDB use a `MDB_val` struct to represents input/output data. All it contains is a data size and a pointer to the data. LMDBJava uses JNR and `Unsafe` or reflections to manipulate a `java.nio.ByteBuffer` to achieve this. Since we cannot use these in this project, we have to come up with a GraalVM specific solution.

It turned out the code to do this is quite pleasant. Instead of allocating the ByteBuffer in Java and presenting it to C, we manage the memory in C and presenting it as a ByteBuffer in Java, without all that `Unsafe` and reflection shenanigans. 

```Java
/**
 * Wrap LMDB MDB_val to look like a ByteBuffer at the Java side
 */
@CContext(Lib.Directives.class)
public class BufVal {

    private int capacity;
    private ByteBuffer inBuf;

    private VoidPointer data;
    private Lib.MDB_val ptr;

    public BufVal(int size) {
        capacity = size;

        data = UnmanagedMemory.calloc(size);
        ptr = UnmanagedMemory.calloc(SizeOf.get(Lib.MDB_val.class));

        ptr.set_mv_size(size);
        ptr.set_mv_data(data);

        inBuf = CTypeConversion.asByteBuffer(data, size);
        inBuf.order(ByteOrder.BIG_ENDIAN);
    }

    /**
     * Set the limit of internal ByteBuffer to the current position, and update
     * the MDB_val size to be the same, so no unnecessary bytes are written
     */
    public void flip() {
        inBuf.flip();
        ptr.set_mv_size(inBuf.limit());
    }

    /**
     * Set the limit of internal ByteBuffer to capacity, and update
     * the MDB_val size to be the same, so it is ready to accept writes
     */
    public void clear() {
        inBuf.clear();
        ptr.set_mv_size(inBuf.limit());
    }

    /**
     * Free memory
     */
    public void close() {
        UnmanagedMemory.free(data);
        UnmanagedMemory.free(ptr);
    }

    /**
     * Return a ByteBuffer for getting data out of MDB_val
     */
    public ByteBuffer outBuf() {
        ByteBuffer buf = CTypeConversion.asByteBuffer(ptr.get_mv_data(),
                                                      (int)ptr.get_mv_size());
        buf.order(ByteOrder.BIG_ENDIAN);
        return buf;
    }

    /**
     * Reset MDB_val pointer back to internal ByteBuffer, and return it
     * for putting data into MDB_val
     */
    public ByteBuffer inBuf() {
        ptr.set_mv_data(data);
        return inBuf;
    }

    /**
     * Return the MDB_val pointer to be used in LMDB calls
     */
    public Lib.MDB_val getVal() {
        return (Lib.MDB_val)ptr;
    }

    /**
     * factory method to create an instance
     */
    public static BufVal create(int size) {
        return new BufVal(size);
    }
}
```
We allocate the memory for the data and the `MDB_val` struct with the `UnmanagedMemory.calloc` static method from the SDK. This allocates memory from the heap just like in C. We will then need to free the memory ourselves. 

If the memory is needed only for a short period of time, the other options are `PinnedObject` or `StackValue` classes of the SDK. The former allows creating Java objects and then pinning them down, so that the garbage collector does not move them or delete them, in order to get a stable pointer to work with at the C side. The latter allocates objects from the stack so it is short-lived. These cases do not fit our need for long term pointers to database data structures, so we use `UnmanagedMemory`. 

The SDK utility `CTypeConversion.asByteBuffer` static method is what makes our effort possible. We can simply expose a `MDB_val` as a `ByteBuffer` to Java in the constructor for incoming data, and in `outBuf()` for outgoing data.  The rest of the code is just bookkeeping on the ByteBuffer.

## Conclusion

I am happy that this effort is turning out well. The GraalVM SDK is quite pleasant to use, once one figures it out. I wish that this API can be available in regular JVM as well, so we can truly write it once, and use it everywhere, regardless the underlying languages and platforms.