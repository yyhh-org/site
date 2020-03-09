Title: Create Multiple Modules Maven Project in Eclipse
Date: 2008-02-14 04:49
Author: Huahai
Category: notebook
Tags: Programming, Java
Slug: create-multiple-modules-maven-project-in-eclipse
Alias: /blog/2008/02/create-multiple-modules-maven-project-eclipse
Lang: en

Modularized software system design is often a good idea. Maven is the new software build system that is purported to be better than ant. For my new project, I want to create a maven build consisting of multiple modules. To do this, and let Eclipse treats these modules as parts of a single Eclipse project, I used the following procedure.

First create the top level maven project, which will be the container of the modules. Our top level maven project is called "cool".

`mvn archetype:create -DgroupId=org.yyhh -DartifactId=cool -Dversion=0.0.1-SNAPSHOT`

By default, newly created maven projects has "jar" packaging type, so it cannot have sub-modules. To let our *cool* project become a container project, we need to edit its *pom.xml*, changing "jar" to "pom" for the " packaging " tag. Also, the *src* folder just created by maven is not necessary, and can be deleted.

Now we are ready to create module projects with maven. Change current directory (cd) to the newly created "cool" directory. For each module desired, create a maven project

`mvn archetype:create -DgroupId=org.yyhh.cool.module-name -DartifactId=module-name -Dversion=0.0.1-SNAPSHOT`

Maven is smart enough to figure out that these new projects are actually modules of the *cool* project, and will do appropriate modifications on all of the *pom.xml* files automatically.

Now we need to let Eclipse know about these maven project. Issue

`mvn eclipse:eclipse`

Finally, launch Eclipse, and create a generic project that uses *cool* directory as the project directory, and mission accomplished!

P.S. To install third-party jars in local maven repository, use  

`mvn install:install-file -Dfile= -DgroupId= \ -DartifactId= -Dversion= -Dpackaging=`

P.P.S. For some reason my default central maven repository is not very up-to-date, I have to rsync what I want manually from an up-to-date mirror. For example, I had to do this to get the latest batik library.  

`cd ~/.m2/repository/org/apache rsync -v -t -l -r mirrors.ibiblio.org::pub/mirrors/maven2/org/apache/xmlgraphics .`
