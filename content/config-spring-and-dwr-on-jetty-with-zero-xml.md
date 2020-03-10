---
Title: Config Spring and DWR on Jetty with zero XML
Date: 2009-08-09 10:51
Author: Huahai
Category: notebook
Tags: Programming, Java
Slug: config-spring-and-dwr-on-jetty-with-zero-xml
Alias: /blog/2009/08/config-spring-and-dwr-jetty-zero-xml
Lang: en
---

I hate xml configuation files. They look awful. As a result, they can be very time-consuming to write, and are very error-prone. There's no type-safty checking whatsoever. I would rather keep configurations within my Java source code. After all, we programmers are the only people looking at these configurations, why create trouble for ourselves? Luckily, with annotation support in Java, we can now completely do away with xml files for developing Web applications. Here is my recent experience integrating Spring framework with DWR on a Jetty sever.

**Spring**

Spring framework seems to be very popular in enterprise Java world. The core idea of "inversion of control (IoC)" seems to be trival (I bet any good programmers are already doing IoC without knowing the name). But sometimes, taking a simple idea seriously can get you a lot of mileage. Map-Reduce is another example on top of my head. Anyway, I decided to use Spring to manage objects in one of my dependency-rapidly-getting-out-of-hand Web projejcts. Spring was known for its xml hell, but recently advances have given it annotation-based configuration and JavaConfig. Now we can do Spring configuration completely in Java source code.  To do this, I put these jars in my java built path:

-   spring.jar (Note that this is spring 2.5.6)
-   asm-3.2.jar
-   aspectj-1.6.5.jar
-   org.springframework.config.java-1.0.0.M4.jar
-   cglib-2.2.jar
-   dwr.jar
-   all jetty modules

JavaConfig needs at least one class annotated with @Configuation. Here's mine:

<font color="#800090">@Configuration</font>  
<font color="#800090">@AnnotationDrivenConfig</font>  
<font color="#800090">@ComponentScan</font>(<font color="#077807">"com.company.app"</font>)  
<font color="#912f11">**public**</font> <font color="#912f11">**class**</font> AppConfig {  
  <font color="#786000">// no need to list our own beans here </font>  
  <font color="#786000">// since we use autowiring and component scan</font>  
}

Yeah, the configuation file is pretty empty. In fact, @ComponentScan tells Spring to search for classes annotated with @Component (or several other stereotypes: @Controller, @Service, etc. See Spring doc for details) under "com.company.app" base package, and automatically inject all the dependencies labeled @Autowired. For example:

<font color="#800090">@Controller</font>  
<font color="#800090">@RemoteProxy</font>(  
  creator = SpringCreator.<font color="#912f11">**class**</font>,  
  creatorParams =  
    {  
      <font color="#800090">@Param</font>(name = <font color="#077807">"beanName"</font>, value = <font color="#077807">"UIController"</font>),  
      <font color="#786000">// this is needed due to a DWR bug</font>  
      <font color="#800090">@Param</font>(name = <font color="#077807">"javascript"</font>, value = <font color="#077807">"UIController"</font>)  
    },  
  name = <font color="#077807">"UIController"</font>)  
<font color="#912f11">**public**</font> <font color="#912f11">**class**</font> UIController {  
  <font color="#800090">@Autowired</font>  
  <font color="#912f11">**private**</font> BackEnd backEnd;  
  <font color="#800090">@Autowired</font>  
  <font color="#912f11">**private**</font> QueryProcessor queryProcessor;

  <font color="#786000">// other stuff here </font>  
}

Both backEnd and queryProcessor will be automatically instantiated and injected here. This is really cool! What a time saver! Oh, don't forget to write setter for these private members. And the @RemoteProxy annotation is for DWR. More later.

**Jetty**

Now we can start our Web server this way too, without the damned web.xml and all that. Basically, we will embody a Jetty server in our Java application. Why Jetty? It's small, fast and flexible. I created a class to wrap it up and also created two servlets for it. One serves regular files, another handles ajax request using DWR. 

<font color="#800090">@Component</font>  
<font color="#912f11">**public**</font> <font color="#912f11">**class**</font> UIServer {  
  <font color="#912f11">**public**</font> <font color="#912f11">**static**</font> <font color="#912f11">**final**</font> File HTML\_FILE\_DIR = <font color="#1f3f81">**new**</font> File(<font color="#077807">"../Web"</font>);  
  <font color="#912f11">**private**</font> <font color="#912f11">**int**</font> port = <font color="#077807">80</font>;  
  <font color="#912f11">**private**</font> Server jettyServer;  

  <font color="#912f11">**public**</font> <font color="#912f11">**void**</font> start() {  
    <font color="#1f3f81">**try**</font> {  
      <font color="#786000">// Create an instance of Jetty Web server</font>  
      jettyServer = <font color="#1f3f81">**new**</font> Server(port);  
      ContextHandlerCollection contexts = <font color="#1f3f81">**new**</font> ContextHandlerCollection();  
      jettyServer.setHandler(contexts);

      <font color="#786000">// this servlet serves static files</font>  
      ServletContextHandler ctxDocs=  
      <font color="#1f3f81">**new**</font> ServletContextHandler(contexts, <font color="#077807">"/"</font>, ServletContextHandler.SESSIONS);  
      ctxDocs.setResourceBase(HTML\_FILE\_DIR.toString());  
      ServletHolder ctxDocHolder= <font color="#1f3f81">**new**</font> ServletHolder();  
      ctxDocHolder.setInitParameter(<font color="#077807">"dirAllowed"</font>, <font color="#077807">"false"</font>);  
      ctxDocHolder.setServlet(<font color="#1f3f81">**new**</font> DefaultServlet());  
      ctxDocs.addServlet(ctxDocHolder, <font color="#077807">"/\*"</font>);

      <font color="#786000">// this DWR servlet handles UI requests</font>  
      ServletContextHandler ctxUI =  
      <font color="#1f3f81">**new**</font> ServletContextHandler(contexts, <font color="#077807">"/ui"</font>, ServletContextHandler.SESSIONS );  
      ServletHolder ctxUIHolder= <font color="#1f3f81">**new**</font> ServletHolder();  
      ctxUIHolder.setInitParameter(<font color="#077807">"debug"</font>, <font color="#077807">"true"</font>);  
      ctxUIHolder.setInitParameter(<font color="#077807">"jsonpEnabled"</font>, <font color="#077807">"true"</font>);  
      ctxUIHolder.setInitParameter(<font color="#077807">"crossDomainSessionSecurity"</font>, <font color="#077807">"false"</font>);

      <font color="#786000">// Specify the classes (comma delimited fully qualified class names)</font>  
      <font color="#786000">// to be exposed to Web browser</font>  
      ctxUIHolder.setInitParameter(<font color="#077807">"classes"</font>, <font color="#077807">"com.company.app.UIController"</font>);  
      ctxUIHolder.setServlet(<font color="#1f3f81">**new**</font> DwrServlet());

      ctxUI.addServlet(ctxUIHolder, <font color="#077807">"/\*"</font>);  
      contexts.setHandlers(<font color="#1f3f81">**new**</font> Handler\[\]{ctxUI, ctxDocs});

      jettyServer.start();  
      jettyServer.join();

    } <font color="#1f3f81">**catch**</font> (Exception e) {  
      e.printStackTrace();  
    }  
}

We now need to bootstrap our application with JavaConfig by creating an application context.  

<font color="#912f11">**public**</font> <font color="#912f11">**class**</font> App {

  <font color="#912f11">**public**</font> <font color="#912f11">**static**</font> <font color="#912f11">**void**</font> main(String\[\] args) <font color="#912f11">**throws**</font> Exception {  
    JavaConfigApplicationContext ctx =  
      <font color="#1f3f81">**new**</font> JavaConfigApplicationContext(MidasConfig.<font color="#912f11">**class**</font>);

    <font color="#786000">// so DWR knows where to find classes</font>  
    SpringCreator.setOverrideBeanFactory(ctx);

    UIServer uiServer = ctx.getBean(UIServer.<font color="#912f11">**class**</font>);  
    uiServer.start();  
  }  
}

**DWR**

DWR allows javascript on browser to directly call Java methods on server. It's like a RPC thing, which is pretty convenient. It's my favirate ajax communication layer. Notice we have already covered most of the configurations needed for DWR in the code fragments above. Here's some explanations. The @RemoteProxy annotation basically says that "expose this class to javascript". Within such classes, @RemoteMethod annotation makes annotated methods visible for javascript to call. More details please see DWR documentation.  In addition to such annotations, we did two tricks here to make DWR configuration completely devoid of any xml files. First we passed DWR some configurations through jetty's servletholder. Second, we used SpringCreator of DWR, which basically ask Spring for objects.  

Well, it took me lots of googling to put this together. Hope it would be useful for someone.
