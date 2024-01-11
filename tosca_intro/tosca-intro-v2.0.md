
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

### OASIS Committee Note
-------

# Introduction to TOSCA Version 2.0

## Committee Note 01

## 21 March 2023

&nbsp;

#### This stage:
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/cn01/tosca-intro-v2.0-cn01.md (Authoritative) \
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/cn01/tosca-intro-v2.0-cn01.html \
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/cn01/tosca-intro-v2.0-cn01.pdf

#### Previous stage:
N/A

#### Latest stage:
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/tosca-intro-v2.0.md (Authoritative) \
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/tosca-intro-v2.0.html \
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/tosca-intro-v2.0.pdf

#### Technical Committee:
[OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC](https://www.oasis-open.org/committees/tosca/)

#### Chair:

Chris Lauwers (lauwers@ubicity.com), Individual Member

#### Editors:

Chris Lauwers (lauwers@ubicity.com), Individual Member \
Calin Curescu (calin.curescu@ericsson.com), [Ericsson](http://ericsson.com/)

#### Related work:

This document provides an introduction to:
* _Topology and Orchestration Specification for Cloud Applications Version 2.0._ Edited by Chris Lauwers and Calin Curescu. Latest stage: https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.html.

#### Abstract:

This document provides an introduction to the TOSCA Version 2.0 standard and an overview of its features.

#### Status:

This is a Non-Standards Track Work Product. The patent provisions of the OASIS IPR Policy do not apply.

This document was last revised or approved by the OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca#technical.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/tosca/.

#### Citation format:
When referencing this document the following citation format should be used:

**[TOSCA-Intro-v2.0]**

_Introduction to TOSCA Version 2.0_.
Edited by Chris Lauwers and Calin Curescu.
21 March 2023.
OASIS Committee Note 01.
https://docs.oasis-open.org/tosca/tosca-intro/v2.0/cn01/tosca-intro-v2.0-cn01.html.
Latest stage: https://docs.oasis-open.org/tosca/tosca-intro/v2.0/tosca-intro-v2.0.html.

#### Notices
Copyright &copy; OASIS Open 2023. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in an Appendix below.

-------

# Table of Contents
[[TOC will be inserted here]]

-------

<!-- Insert a "line rule" (three or more hyphens alone on a new line, following a blank line) before each major section. This is used to generate a page break in the PDF format. -->

# 1 Introduction

## 1.1 Introductory Material

## 1.2 Glossary

<!-- Optional section with suggested subsections -->

### 1.2.1 Definitions of terms

### 1.2.2 Acronyms and abbreviations

### 1.2.3 Document conventions

- Naming conventions
- Font colors and styles
- Typographic conventions

# 2 TOSCA by example

This **non-normative** section contains several sections that show how
to model applications with TOSCA using YAML by example starting with a
“Hello World” template up through examples that show complex composition
modeling.

## A “hello world” template for TOSCA

As mentioned before, TOSCA assumes the existence of a small set of
pre-defined, normative set of node types (e.g., a ‘Compute’ node) along
with other types, which will be introduced through the course of this
document, for creating TOSCA Service Templates. It is envisioned that
many additional node types for building service templates will be
created by communities. Some may be published as profiles that build
upon the TOSCA specification. Using the normative TOSCA Compute node
type, a very basic “Hello World” TOSCA template for deploying just a
single server would look as follows:

Example 1 - TOSCA Simple "Hello World"
```
tosca_definitions_version: tosca_2_0
		
description: >-
  Template for deploying a single server with predefined properties.

topology_template:
  node_templates:
    db_server:
      type: tosca.nodes.Compute
      capabilities:
        # Host container properties
        host:
         properties:
           num_cpus: 1 
           disk_size: 10 GB
           mem_size: 4096 MB
        # Guest Operating System properties
        os:
          properties:
            # host Operating System image properties
            architecture: x86_64 
            type: linux  
            distribution: rhel  
            version: 6.5  
```

The template above contains a very simple topology template” with only a
single ‘Compute’ node template named “db_server that declares some basic
values for properties within two of the several capabilities that are
built into the Compute node type definition. All TOSCA Orchestrators are
expected to know how to instantiate a Compute node since it is normative
and expected to represent a well-known function that is portable across
TOSCA implementations. This expectation is true for all normative TOSCA
Node and Relationship types that are defined in the specification. This
means, with TOSCA’s approach, that the application developer does not
need to provide any deployment or implementation artifacts that contain
code or logic to orchestrate these common software components. TOSCA
orchestrators simply select or allocate the correct node (resource) type
that fulfills the application topologies requirements using the
properties declared in the node and its capabilities.

In the above example, the “host” capability contains properties that
allow application developers to optionally supply the number of CPUs,
memory size and disk size they believe they need when the Compute node
is instantiated in order to run their applications. Similarly, the “os”
capability is used to provide values to indicate what host operating
system the Compute node should have when it is instantiated.

The logical diagram of the “hello world” Compute node would look as
follows:

<img src="media/image1.png" style="width:2.05943in;height:3.01764in" />

As you can see, the Compute node also has attributes and other built-in
capabilities, such as Bindable and Endpoint, each with additional
properties that will be discussed in other examples later in this
document. Although the Compute node has no direct properties apart from
those in its capabilities, other TOSCA node type definitions may have
properties that are part of the node type itself in addition to having
Capabilities. TOSCA orchestration engines are expected to validate all
property values provided in a node template against the property
definitions in their respective node type definitions referenced in the
service template. The tosca_definitions_version keyname in the TOSCA
service template identifies the versioned set of normative TOSCA type
definitions to use for validating those types defined in TOSCA including
the Compute node type. Specifically, the value tosca_2_0 indicates TOSCA
v2.0.0 definitions would be used for validation. Other type definitions
may be imported from other service templates using the import keyword
discussed later.

## Requesting input parameters and providing output

Typically, one would want to allow users to customize deployments by
providing input parameters instead of using hardcoded values inside a
template. In addition, output values are provided to pass information
that perhaps describes the state of the deployed template to the user
who deployed it (such as the private IP address of the deployed server).
A refined service template with corresponding inputs and outputs
sections is shown below.

Example 2 - Template with input and output parameter sections
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a single server with predefined properties.

topology_template:
  inputs:
     db_server_num_cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]

  node_templates:
    db_server:
      type: tosca.nodes.Compute
      capabilities:
        # Host container properties
        host:
          properties:
            # Compute properties
            num_cpus: { get_input: db_server_num_cpus }
            mem_size: 2048  MB
            disk_size: 10 GB
            mem_size: 4096 MB
        # Guest Operating System properties
        os:
          # omitted for brevity 

  outputs:
    server_ip:
      description: The private IP address of the provisioned server.
      value: { get_attribute: [ db_server, private_address ] }
```

The inputs and outputs sections are contained in the topology_template
element of the TOSCA template, meaning that they are scoped to node
templates within the topology template. Input parameters defined in the
inputs section can be assigned to properties of node template within the
containing topology template; output parameters can be obtained from
attributes of node templates within the containing topology template.

Note that the inputs section of a TOSCA template allows for defining
optional constraints on each input parameter to restrict possible user
input. Further note that TOSCA provides for a set of intrinsic functions
like get_input, get_property or get_attribute to reference elements
within the template or to retrieve runtime values.

## TOSCA template for a simple software installation

Software installations can be modeled in TOSCA as node templates that
get related to the node template for a server on which the software
would be installed. With a number of existing software node types (e.g.
either created by the TOSCA work group or a community) template authors
can just use those node types for writing service templates as shown
below.

Example 3 - Simple (MySQL) software installation on a TOSCA Compute node
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a single server with MySQL software on top.

topology_template:
  inputs:
    mysql_rootpw:
      type: string
    mysql_port:
      type: integer
    # rest omitted here for brevity

  node_templates:
    db_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        root_password: { get_input: mysql_rootpw }
        port: { get_input: mysql_port }
      requirements:
        - host: db_server

  outputs:
    # omitted here for brevity
```

The example above makes use of a node type tosca.nodes.DBMS.MySQL for
the mysql node template to install MySQL on a server. This node type
allows for setting a property root_password to adapt the password of the
MySQL root user at deployment. The set of properties and their schema
has been defined in the node type definition. By means of the
**get_input** function, a value provided by the user at deployment time
is used as the value for the **root_password** property. The same is
true for the **port** property.

The **mysql** node template is related to the **db_server** node
template (of type tosca.nodes.Compute) via the **requirements** section
to indicate where MySQL is to be installed. In the TOSCA metamodel,
nodes get related to each other when one node has a requirement against
some capability provided by another node. What kinds of requirements
exist is defined by the respective node type. In case of MySQL, which is
software that needs to be installed or hosted on a compute resource, the
underlying node type named tosca.nodes.SoftwareComponent has a
predefined requirement called **host**, which needs to be fulfilled by
pointing to a node template of type tosca.nodes.Compute.

The logical relationship between the mysql node and its host db_server
node would appear as follows:

<img src="media/image2.png" style="width:2.44959in;height:3.83333in" />

Within the list of requirements, each list entry is a map that contains
a single key/value pair where the symbolic name of a requirement
definition is the *key* and the identifier of the fulfilling node is the
*value.* The value is essentially the symbolic name of the other node
template; specifically, or the example above, the **host** requirement
is fulfilled by referencing the db_server node template. The underlying
TOSCA DBMS node type already has a complete requirement definition for
the host requirement of type Compute and assures that a HostedOn TOSCA
relationship will automatically be created and will only allow a valid
target host node is of type Compute. This approach allows the template
author to simply provide the name of a valid Compute node (i.e.,
db_server) as the value for the mysql node’s host requirement and not
worry about defining anything more complex if they do not want to.

## Using YAML Macros to simplify templates

The YAML 1.2 specification allows for defining of
[aliases](http://yaml.org/spec/1.2/spec.html#id2786196), which allow for
authoring a block of YAML (or node) once and indicating it is an
“anchor” and then referencing it elsewhere in the same document as an
“alias”. Effectively, YAML parsers treat this as a “macro” and copy the
anchor block’s code to wherever it is referenced. Use of this feature is
especially helpful when authoring TOSCA Service Templates where similar
definitions and property settings may be repeated multiple times when
describing a multi-tier application.

For example, an application that has a web server and database (i.e., a
two-tier application) may be described using two Compute nodes (one to
host the web server and another to host the database). The author may
want both Compute nodes to be instantiated with similar properties such
as operating system, distribution, version, etc.

To accomplish this, the author would describe the reusable properties
using a named anchor in the “dsl_definitions” section of the TOSCA
Service Template and reference the anchor name as an alias in any
Compute node templates where these properties may need to be reused. For
example:

Example 22 - Using YAML anchors in TOSCA templates
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA template that just defines a YAML macro for commonly reused Compute
  properties.

dsl_definitions:
  my_compute_node_props: &my_compute_node_props
    disk_size: 10 GB
    num_cpus: 1
    mem_size: 2 GB

topology_template:
  node_templates:
    my_server:
      type: Compute
      capabilities:
        host:
          properties: *my_compute_node_props

    my_database:
      type: Compute
      capabilities:
        host:
          properties: *my_compute_node_props
```


# 3 TOSCA Base Profile

- Introduce node types and data types

- Introduce Profile as a collection of types

- Introduce Base Profile as collection of “built-in” types

- Explain automatic import of Base Profile

- Introduce Semantic versioning

# 4 Interfaces, Operations, and Artifacts

## Overriding behavior of predefined node types

Node types in TOSCA have associated implementations that provide the
automation (e.g. in the form of scripts such as Bash, Chef or Python)
for the normative lifecycle operations of a node. For example, the node
type implementation for a MySQL database would associate scripts to
TOSCA node operations like configure, start, or stop to manage the state
of MySQL at runtime.

Many node types may already come with a set of operational scripts that
contain basic commands that can manage the state of that specific node.
If it is desired, template authors can provide a custom script for one
or more of the operations defined by a node type in their node template
which will override the default implementation in the type. The
following example shows a mysql node template where the template author
provides their own configure script:

Example 4 - Node Template overriding its Node Type's "configure"
interface
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a single server with MySQL software on top.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    db_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        root_password: { get_input: mysql_rootpw }
        port: { get_input: mysql_port }
      requirements:
        - host: db_server
      interfaces:
        Standard:
          configure: scripts/my_own_configure.sh

  outputs:
    # omitted here for brevity
```


In the example above, the my_own_configure.sh script is provided for the
configure operation of the MySQL node type’s Standard lifecycle
interface. The path given in the example above (i.e., ‘scripts/’) is
interpreted relative to the template file, but it would also be possible
to provide an absolute URI to the location of the script.

In other words, operations defined by node types can be thought of as
“hooks” into which automation can be injected. Typically, node type
implementations provide the automation for those “hooks”. However,
within a template, custom automation can be injected to run in a hook in
the context of the one, specific node template (i.e. without changing
the node type).

## TOSCA template for database content deployment

In the Example 4, shown above, the deployment of the MySQL middleware
only, i.e. without actual database content was shown. The following
example shows how such a template can be extended to also contain the
definition of custom database content on-top of the MySQL DBMS software.

Example 5 - Template for deploying database content on-top of MySQL DBMS
middleware
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a single server with predefined properties. 

topology_template:
  inputs:
    wordpress_db_name:
      type: string
    wordpress_db_user:
      type: string
    wordpress_db_password:
      type: string
    # rest omitted here for brevity

  node_templates:
    db_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    mysql:
      type: tosca.nodes.DBMS.MySQL
      # rest omitted here for brevity

    wordpress_db:
      type: tosca.nodes.Database.MySQL
      properties:
        name: { get_input: wordpress_db_name }
        user: { get_input: wordpress_db_user }
        password: { get_input: wordpress_db_password }
      artifacts:
        db_content:
          file: files/wordpress_db_content.txt
          type: tosca.artifacts.File 
      requirements:
        - host: mysql
      interfaces:
        Standard:
          create:
            implementation: db_create.sh 
            inputs:
              # Copy DB file artifact to server’s staging area
              db_data: { get_artifact: [ SELF, db_content ] }

  outputs:
    # omitted here for brevity
```

In the example above, the wordpress_db node template of type
tosca.nodes.Database.MySQL represents an actual MySQL database instance
managed by a MySQL DBMS installation. The requirements section of the
wordpress_db node template expresses that the database it represents is
to be hosted on a MySQL DBMS node template named mysql which is also
declared in this template.

In the **artifacts** section of the wordpress_db the node template,
there is an artifact definition named db_content which represents a text
file wordpress_db_content.txt which in turn will be used to add content
to the SQL database as part of the create operation.

As you can see above, a script is associated with the create operation
with the name db_create.sh. The TOSCA Orchestrator sees that this is not
a named artifact declared in the node’s artifact section, but instead a
filename for a normative TOSCA implementation artifact script type
(i.e., tosca.artifacts.Implementation.Bash). Since this is an
implementation type for TOSCA, the orchestrator will execute the script
automatically to create the node on db_server, but first it will prepare
the local environment with the declared inputs for the operation. In
this case, the orchestrator would see that the db_data input is using
the get_artifact function to retrieve the file
(wordpress_db_content.txt) which is associated with the db_content
artifact name prior to executing the db_create.sh script.

The logical diagram for this example would appear as follows:

> <img src="media/image3.png" style="width:4.56667in;height:4.67287in" />

Note that while it would be possible to define one node type and
corresponding node templates that represent both the DBMS middleware and
actual database content as one entity, TOSCA normative node types
distinguish between middleware (container) and application (containee)
node types. This allows on one hand to have better re-use of generic
middleware node types without binding them to content running on top of
them, and on the other hand this allows for better substitutability of,
for example, middleware components like a DBMS during the deployment of
TOSCA models.

## TOSCA template for a two-tier application

The definition of multi-tier applications in TOSCA is quite similar to
the example shown in section 2.2, with the only difference that multiple
software node stacks (i.e., node templates for middleware and
application layer components), typically hosted on different servers,
are defined and related to each other. The example below defines a web
application stack hosted on the **web_server** “compute” resource, and a
database software stack similar to the one shown earlier in section 6
hosted on the **db_server** compute resource.

Example 6 - Basic two-tier application (web application and database
server tiers)
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a two-tier application servers on 2 servers.

topology_template:
  inputs:
    # Admin user name and password to use with the WordPress application
    wp_admin_username:
      type: string
    wp_admin_password:
      type: string
    mysql_root_password:
      type: string
    context_root:
      type: string
    # rest omitted here for brevity


  node_templates:
    db_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    mysql:
      type: tosca.nodes.DBMS.MySQL
      # rest omitted here for brevity

    wordpress_db:
      type: tosca.nodes.Database.MySQL
      # rest omitted here for brevity

    web_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    apache:
      type: tosca.nodes.WebServer.Apache
      requirements:
        - host: web_server
      # rest omitted here for brevity

    wordpress:
      type: tosca.nodes.WebApplication.WordPress
      properties:
        context_root: { get_input: context_root }
        admin_user: { get_input: wp_admin_username }
        admin_password: { get_input: wp_admin_password }
        db_host: { get_attribute: [ db_server, private_address ] }
      requirements:
        - host: apache
        - database_endpoint: wordpress_db
      interfaces:
        Standard:
          inputs:
            db_host: { get_attribute: [ db_server, private_address ] }
            db_port: { get_property: [ mysql, port ] }
            db_name: { get_property: [ wordpress_db, name ] }
            db_user: { get_property: [ wordpress_db, user ] }
            db_password: { get_property: [ wordpress_db, password ] }

  outputs:
    # omitted here for brevity
```



The web application stack consists of the **wordpress**
\[[WordPress](#REF_WORDPRESS)\], the **apache**
\[[Apache](#REF_APACHE)\] and the **web_server** node templates. The
**wordpress** node template represents a custom web application of type
**tosca.nodes.WebApplication.WordPress** which is hosted on an Apache
web server represented by the **apache** node template. This hosting
relationship is expressed via the **host** entry in the **requirements**
section of the **wordpress** node template. The **apache** node
template, finally, is hosted on the **web_server** compute node.

The database stack consists of the **wordpress_db**, the **mysql** and
the **db_server** node templates. The **wordpress_db** node represents a
custom database of type **tosca.nodes.Database.MySQL** which is hosted
on a MySQL DBMS represented by the **mysql** node template. This node,
in turn, is hosted on the **db_server** compute node.

The **wordpress** node requires a connection to the **wordpress_db**
node, since the WordPress application needs a database to store its data
in. This relationship is established through the **database**\_endpoint
entry in the **requirements** section of the **wordpress** node
template’s declared node type. For configuring the WordPress web
application, information about the database to connect to is required as
input to the **configure** operation. Therefore, the input parameters
are defined and values for them are retrieved from the properties and
attributes of the **wordpress_db** node via the **get_property** and
get_attribute functions. In the above example, these inputs are defined
at the interface-level and would be available to all operations of the
Standard interface (i.e., the tosca.interfaces.node.lifecycle.Standard
interface) within the wordpress node template and not just the configure
operation.

## Using a custom script to establish a relationship in a template

In previous examples, the template author did not have to think about
explicit relationship types to be used to link a requirement of a node
to another node of a model, nor did the template author have to think
about special logic to establish those links. For example, the **host**
requirement in previous examples just pointed to another node template
and based on metadata in the corresponding node type definition the
relationship type to be established is implicitly given.

In some cases, it might be necessary to provide special processing logic
to be executed when establishing relationships between nodes at runtime.
For example, when connecting the WordPress application from previous
examples to the MySQL database, it might be desired to apply custom
configuration logic in addition to that already implemented in the
application node type. In such a case, it is possible for the template
author to provide a custom script as implementation for an operation to
be executed at runtime as shown in the following example.

Example 7 - Providing a custom relationship script to establish a
connection
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a two-tier application on two servers.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    db_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    mysql:
      type: tosca.nodes.DBMS.MySQL
      # rest omitted here for brevity

    wordpress_db:
      type: tosca.nodes.Database.MySQL
      # rest omitted here for brevity

    web_server:
      type: tosca.nodes.Compute
      # rest omitted here for brevity

    apache:
      type: tosca.nodes.WebServer.Apache
      requirements:
        - host: web_server
      # rest omitted here for brevity

    wordpress:
      type: tosca.nodes.WebApplication.WordPress
      properties:
        # omitted here for brevity
      requirements:
        - host: apache
        - database_endpoint: 
            node: wordpress_db
            relationship: wp_db_connection
      # rest omitted here for brevity

    wordpress_db:
      type: tosca.nodes.Database.MySQL
      properties:
        # omitted here for the brevity
      requirements:
        - host: mysql

  relationship_templates:
    wp_db_connection:
      type: ConnectsTo
      interfaces:
        Configure:
          pre_configure_source: scripts/wp_db_configure.sh

  outputs:
    # omitted here for brevity
```

The node type definition for the wordpress node template is WordPress
which declares the complete **database_endpoint** requirement
definition. This database_endpoint declaration indicates it must be
fulfilled by any node template that provides an Endpoint.Database
Capability Type using a ConnectsTo relationship. The wordpress_db node
template’s underlying MySQL type definition indeed provides the
Endpoint.Database Capability type. In this example however, no explicit
relationship template is declared; therefore, TOSCA orchestrators would
automatically create a ConnectsTo relationship to establish the link
between the wordpress node and the wordpress_db node at runtime.

The ConnectsTo relationship (see 5.7.4) also provides a default
Configure interface with operations that optionally get executed when
the orchestrator establishes the relationship. In the above example, the
author has provided the custom script wp_db_configure.sh to be executed
for the operation called pre_configure_source. The script file is
assumed to be located relative to the referencing service template such
as a relative directory within the TOSCA Cloud Service Archive (CSAR)
packaging format. This approach allows for conveniently hooking in
custom behavior without having to define a completely new derived
relationship type.

## Using custom relationship types in a TOSCA template

In the previous section it was shown how custom behavior can be injected
by specifying scripts inline in the requirements section of node
templates. When the same custom behavior is required in many templates,
it does make sense to define a new relationship type that encapsulates
the custom behavior in a re-usable way instead of repeating the same
reference to a script (or even references to multiple scripts) in many
places.

Such a custom relationship type can then be used in templates as shown
in the following example.

Example 8 - A web application Node Template requiring a custom database
connection type
```
tosca_definitions_version: tosca_2_0

description: Template for deploying a two-tier application on two servers.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    wordpress:
      type: tosca.nodes.WebApplication.WordPress
      properties:
        # omitted here for brevity
      requirements:
        - host: apache
        - database_endpoint: 
            node: wordpress_db
            relationship: my.types.WordpressDbConnection

    wordpress_db:
      type: tosca.nodes.Database.MySQL
      properties:
        # omitted here for the brevity
      requirements:
        - host: mysql

   # other resources not shown here ...
```

In the example above, a special relationship type
**my.types.WordpressDbConnection** is specified for establishing the
link between the **wordpress** node and the **wordpress_db** node
through the use of the **relationship** keyword in the **database**
reference. It is assumed, that this special relationship type provides
some extra behavior (e.g., an operation with a script) in addition to
what a generic “connects to” relationship would provide. The definition
of this custom relationship type is shown in the following section.

### Definition of a custom relationship type

The following YAML snippet shows the definition of the custom
relationship type used in the previous section. This type derives from
the base “ConnectsTo” and overrides one operation defined by that base
relationship type. For the pre_configure_source operation defined in the
Configure interface of the ConnectsTo relationship type, a script
implementation is provided. It is again assumed that the custom
configure script is located at a location relative to the referencing
service template, perhaps provided in some application packaging format
(e.g., the TOSCA Cloud Service Archive (CSAR) format).

Example 9 - Defining a custom relationship type
```
tosca_definitions_version: tosca_2_0

description: Definition of custom WordpressDbConnection relationship type

relationship_types:
  my.types.WordpressDbConnection:
    derived_from: tosca.relationships.ConnectsTo
    interfaces:
      Configure:
        pre_configure_source: scripts/wp_db_configure.sh
```

## Defining generic dependencies between nodes in a template

In some cases, it can be necessary to define a generic dependency
between two nodes in a template to influence orchestration behavior,
i.e. to first have one node processed before another dependent node gets
processed. This can be done by using the generic dependency requirement
which is defined by the [TOSCA Root Node Type](#tosca.nodes.root) and
thus gets inherited by all other node types in TOSCA (see section
5.9.1).

Example 10 - Simple dependency relationship between two nodes
```

description: Template with a generic dependency between two nodes.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    my_app:
      type: my.types.MyApplication
      properties:
        # omitted here for brevity
      requirements:
        - dependency: some_service

    some_service:
      type: some.nodetype.SomeService
      properties:
        # omitted here for brevity
```



As in previous examples, the relation that one node depends on another
node is expressed in the requirements section using the built-in
requirement named dependency that exists for all node types in TOSCA.
Even if the creator of the MyApplication node type did not define a
specific requirement for SomeService (similar to the database
requirement in the example in section 2.6), the template author who
knows that there is a timing dependency and can use the generic
dependency requirement to express that constraint using the very same
syntax as used for all other references. Passing information as inputs
to Interfaces and Operations

It is possible for type and template authors to declare input variables
within an inputs block on interfaces to nodes or relationships in order
to pass along information needed by their operations (scripts). These
declarations can be scoped such as to make these variable values
available to all operations on a node or relationships interfaces or to
individual operations. TOSCA orchestrators will make these values
available using the appropriate mechanisms depending on the type of
implementation artifact used for each operation. For example, when using
script artifacts, input values are passed as environment variables
within the execution environments in which the scripts associated with
lifecycle operations are run.

### Example: declaring input variables for all operations on a single interface
```
node_templates:  
  wordpress:
    type: tosca.nodes.WebApplication.WordPress
    requirements:
      ...
      - database_endpoint: mysql_database
    interfaces:
      Standard:
        inputs:
          wp_db_port: { get_property: [ SELF, database_endpoint, port ] }
```



### Example: declaring input variables for a single operation
```
node_templates:  
  wordpress:
    type: tosca.nodes.WebApplication.WordPress
    requirements:
      ...
      - database_endpoint: mysql_database
    interfaces:
      Standard:
        create: wordpress_install.sh
        configure: 
          implementation: wordpress_configure.sh            
          inputs:
            wp_db_port: { get_property: [ SELF, database_endpoint, port ] }
```


In the case where an input variable name is defined at more than one
scope within the same interfaces section of a node or template
definition, the lowest (or innermost) scoped declaration would override
those declared at higher (or more outer) levels of the definition.

# 5 TOSCA workflows

TOSCA defines two different kinds of workflows that can be used to
deploy (instantiate and start), manage at runtime or undeploy (stop and
delete) a TOSCA topology: declarative workflows and imperative
workflows. Declarative workflows are automatically generated by the
TOSCA orchestrator based on the nodes, relationships, and groups defined
in the topology. Imperative workflows are manually specified by the
author of the topology and allows the specification of any use-case that
has not been planned in the definition of node and relationships types
or for advanced use-case (including reuse of existing scripts and
workflows).

Workflows can be triggered on deployment of a topology (deploy workflow)
on undeployment (undeploy workflow) or during runtime, manually, or
automatically based on policies defined for the topology.

**Note:** The TOSCA orchestrators will execute a single workflow at a
time on a topology to guarantee that the defined workflow can be
consistent and behave as expected.

## Normative workflows

TOSCA defines several normative workflows that are used to operate a
Topology. That is, reserved names of workflows that should be preserved
by TOSCA orchestrators and that, if specified in the topology will
override the workflow generated by the orchestrator :

- deploy: is the workflow used to instantiate and perform the initial
  deployment of the topology.

- undeploy: is the workflow used to remove all instances of a topology.

### Notes

Future versions of the specification will describe the normative naming
and declarative generation of additional workflows used to operate the
topology at runtime.

- scaling workflows: defined for every scalable nodes or based on
  scaling policies

- auto-healing workflows: defined in order to restart nodes that may
  have failed

## Declarative workflows

Declarative workflows are the result of the weaving of topology’s node,
relationships, and groups workflows.

The weaving process generates the workflow of every single node in the
topology, insert operations from the relationships and groups and
finally add ordering consideration. The weaving process will also take
care of the specific lifecycle of some nodes and the TOSCA orchestrator
is responsible to trigger errors or warnings in case the weaving cannot
be processed or lead to cycles for example.

This section aims to describe and explain how a TOSCA orchestrator will
generate a workflow based on the topology entities (nodes, relationships
and groups).

### Notes

This section details specific constraints and considerations that
applies during the weaving process.

#### Orchestrator provided nodes lifecycle and weaving

When a node is abstract the orchestrator is responsible for providing a
valid matching resources for the node in order to deploy the topology.
This consideration is also valid for dangling requirements (as they
represents a quick way to define an actual node).

The lifecycle of such nodes is the responsibility of the orchestrator
and they may not answer to the normative TOSCA lifecycle. Their workflow
is considered as "delegate" and acts as a black-box between the initial
and started state in the install workflow and the started to deleted
states in the uninstall workflow.

If a relationship to some of this node defines operations or lifecycle
dependency constraint that relies on intermediate states, the weaving
SHOULD fail and the orchestrator SHOULD raise an error.

### Relationship impacts on topology weaving

This section explains how relationships impacts the workflow generation
to enable the composition of complex topologies.

#### tosca.relationships.DependsOn

The depends on relationship is used to establish a dependency from a
node to another. A source node that depends on a target node will be
created only after the other entity has been started.

#### Note

DependsOn relationship SHOULD not be implemented. Even if the Configure
interface can be implemented this is not considered as a best-practice.
If you need specific implementation, please have a look at the
ConnectsTo relationship.

##### Example DependsOn

This example show the usage of a generic DependsOn relationship between
two custom software components.

<img src="media/image4.png" style="width:6.5in;height:3.58333in"
alt="../Capture%20d’écran%202016-05-19%20à%2016.15.03.png" />

In this example the relationship configure interface doesn’t define
operations so they don’t appear in the generated lifecycle.

#### tosca.relationships.ConnectsTo

The connects to relationship is similar to the DependsOn relationship
except that it is intended to provide an implementation. The difference
is more theoretical than practical but helps users to make an actual
distinction from a meaning perspective.

<img src="media/image5.png" style="width:6.5in;height:4.72222in"
alt="../Capture%20d’écran%202016-05-31%20à%2013.55.32.png" />

#### tosca.relationships.HostedOn

The hosted_on dependency relationship allows to define a hosting
relationship between an entity and another. The hosting relationship has
multiple impacts on the workflow and execution:

- The implementation artifacts of the source node is executed on the
  same host as the one of the target node.

- The create operation of the source node is executed only once the
  target node reach the started state.

- When multiple nodes are hosted on the same host node, the defined
  operations will not be executed concurrently even if the theoretical
  workflow could allow it (actual generated workflow will avoid
  concurrency).

##### Example Software Component HostedOn Compute

This example explain the TOSCA weaving operation of a custom
SoftwareComponent on a tosca.nodes.Compute instance. The compute node is
an orchestrator provided node meaning that it’s lifecycle is delegated
to the orchestrator. This is a black-box and we just expect a started
compute node to be provided by the orchestrator.

The software node lifecycle operations will be executed on the Compute
node (host) instance.

<img src="media/image6.png" style="width:6.49097in;height:3.61111in"
alt="../Capture%20d’écran%202016-05-19%20à%2011.00.22.png" />

##### Example Software Component HostedOn Software Component

Tosca allows some more complex hosting scenarios where a software
component could be hosted on another software component.

<img src="media/image7.png" style="width:6.49097in;height:3.26875in"
alt="../Capture%20d’écran%202016-05-19%20à%2013.40.41.png" />

In such scenarios the software create operation is triggered only once
the software_base node has reached the started state.

##### Example 2 Software Components HostedOn Compute

This example illustrate concurrency constraint introduced by the
management of multiple nodes on a single compute.

### Limitations

#### Hosted nodes concurrency

TOSCA implementation currently does not allow concurrent executions of
scripts implementation artifacts (shell, python, ansible, puppet, chef
etc.) on a given host. This limitation is not applied on multiple hosts.
This limitation is expressed through the HostedOn relationship
limitation expressing that when multiple components are hosted on a
given host node then their operations will not be performed concurrently
(generated workflow will ensure that operations are not concurrent).

#### Dependent nodes concurrency

When a node depends on another node no operations will be processed
concurrently. In some situations, especially when the two nodes lies on
different hosts we could expect the create operation to be executed
concurrently for performance optimization purpose. The current version
of the specification will allow to use imperative workflows to solve
this use-case. However, this scenario is one of the scenario that we
want to improve and handle in the future through declarative workflows.

#### Target operations and get_attribute on source

The current ConnectsTo workflow implies that the target node is started
before the source node is even created. This means that
pre_configure_target and post_configure_target operations cannot use any
input based on source attribute. It is however possible to refer to
get_property inputs based on source properties. For advanced
configurations the add_source operation should be used.

Note also that future plans on declarative workflows improvements aims
to solve this kind of issues while it is currently possible to use
imperative workflows.

## Imperative workflows

Imperative workflows are user defined and can define any really specific
constraints and ordering of activities. They are really flexible and
powerful and can be used for any complex use-case that cannot be solved
in declarative workflows. However, they provide less reusability as they
are defined for a specific topology rather than being dynamically
generated based on the topology content.

### Defining sequence of operations in an imperative workflow

Imperative workflow grammar defines two ways to define the sequence of
operations in an imperative workflow:

- Leverage the on_success definition to define the next steps that will
  be executed in parallel.

- Leverage a sequence of activity in a step.

#### Using on_success to define steps ordering

The graph of workflow steps is build based on the values of on_success
elements of the various defined steps. The graph is built based on the
following rules:

- All steps that defines an on_success operation must be executed before
  the next step can be executed. So if A and C defines an on_success
  operation to B, then B will be executed only when both A and C have
  been successfully executed.

- The multiple nodes defined by an on_success construct can be executed
  in parallel.

- Every step that doesn’t have any predecessor is considered as an
  initial step and can run in parallel.

- Every step that doesn’t define any successor is considered as final.
  When all the final nodes executions are completed then the workflow is
  considered as completed.

##### Example

The following example defines multiple steps and the on_success
relationship between them.
```
topology_template:
  workflows:
    deploy:
      description: Workflow to deploy the application
      steps:
        A:
          on_success:
            - B
            - C
        B:
          on_success:
            - D
        C:
          on_success:
            - D
        D:
        E: 
          on_success:
            - C
            - F
        F: 
```



The following schema is the visualization of the above definition in
term of sequencing of the steps.

<img src="media/image8.png" style="width:2.17076in;height:2.97037in"
alt="../Capture%20d’écran%202016-05-03%20à%2013.29.54.png" />

#### Define a sequence of activity on the same element

The step definition of a TOSCA imperative workflow allows multiple
activities to be defined :
```
  workflows:
    my_workflow:
      steps:
        create_my_node:
          target: my_node
          activities: 
            - set_state: creating
            - call_operation: tosca.interfaces.node.lifecycle.Standard.create
            - set_state: created
```


The sequence defined here defines three different activities that will
be performed in a sequential way. This is just equivalent to writing
multiple steps chained by an on_success together :
```
  workflows:
    my_workflow:
      steps:
        creating_my_node:
          target: my_node
          activities: 
            - set_state: creating
          on_success: create_my_node
        create_my_node:
          target: my_node
          activities: 
            - call_operation: tosca.interfaces.node.lifecycle.Standard.create
          on_success: created_my_node
        created_my_node:
          target: my_node
          activities: 
            - set_state: created
```
In both situations the resulting workflow is a sequence of activities:

<img src="media/image9.png" style="width:1.11128in;height:1.60926in"
alt="../Capture%20d’écran%202016-05-17%20à%2007.22.14.png" />

### Definition of a simple workflow

Imperative workflow allow user to define custom workflows allowing them
to add operations that are not normative, or for example, to execute
some operations in parallel when TOSCA would have performed sequential
execution.

As Imperative workflows are related to a topology, adding a workflow is
as simple as adding a workflows section to your topology template and
specifying the workflow and the steps that compose it.

#### Example: Adding a non-normative custom workflow

This sample topology add a very simple custom workflow to trigger the
mysql backup operation.
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup: backup.sh
  workflows:
    backup:
      description: Performs a snapshot of the MySQL data.
      steps:
        my_step:
          target: mysql
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
```

In such topology the TOSCA container will still use declarative workflow
to generate the deploy and undeploy workflows as they are not specified
and a backup workflow will be available for user to trigger.

#### Example: Creating two nodes hosted on the same compute in parallel

TOSCA declarative workflow generation constraint the workflow so that no
operations are called in parallel on the same host. Looking at the
following topology this means that the mysql and tomcat nodes will not
be created in parallel but sequentially. This is fine in most of the
situations as packet managers like apt or yum doesn’t not support
concurrency, however if both create operations performs a download of
zip package from a server most of people will hope to do that in
parallel in order to optimize throughput.

<img src="media/image10.png" style="width:2.13325in;height:2.83664in"
alt="../Capture%20d’écran%202016-05-03%20à%2013.09.26.png" />

Imperative workflows can help to solve this issue. Based on the above
topology we will design a workflow that will create tomcat and mysql in
parallel but we will also ensure that tomcat is started after mysql is
started even if no relationship is defined between the components:

<img src="media/image11.png" style="width:4.11289in;height:4.20648in"
alt="../Capture%20d’écran%202016-05-10%20à%2016.26.30.png" />

To achieve such workflow, the following topology will be defined:
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
    tomcat:
      type: tosca.nodes.WebServer.Tomcat
      requirements:
        - host: my_server
  workflows:
    deploy:
      description: Override the TOSCA declarative workflow with the following.
      steps:
        compute_install
          target: my_server
          activities:
            - delegate: deploy
          on_success:
            - mysql_install
            - tomcat_install
        tomcat_install:
          target: tomcat
          activities:
            - set_state: creating
            - call_operation: tosca.interfaces.node.lifecycle.Standard.create
            - set_state: created
          on_success:
            - tomcat_starting
        mysql_install:
          target: mysql
          activities:
            - set_state: creating
            - call_operation: tosca.interfaces.node.lifecycle.Standard.create
            - set_state: created
            - set_state: starting
            - call_operation: tosca.interfaces.node.lifecycle.Standard.start
            - set_state: started
          on_success:
            - tomcat_starting
        tomcat_starting:
          target: tomcat
          activities:
            - set_state: starting
            - call_operation: tosca.interfaces.node.lifecycle.Standard.start
            - set_state: started
```

### Specifying preconditions to a workflow

Pre conditions allows the TOSCA orchestrator to determine if a workflow
can be executed based on the states and attribute values of the
topology’s node. Preconditions must be added to the initial workflow.

#### Example : adding precondition to custom backup workflow

In this example we will use precondition so that we make sure that the
mysql node is in the correct state for a backup.
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup: backup.sh
  workflows:
    backup:
      description: Performs a snapshot of the MySQL data.
      preconditions:
        - target: my_server
          condition:
            - assert:
              - state: [{equal: available}]
        - target: mysql
          condition:
            - assert:
              - state: [{valid_values: [started, available]}]
              - my_attribute: [{equal: ready }]
      steps:
        my_step:
          target: mysql
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
```

When the backup workflow will be triggered (by user or policy) the TOSCA
engine will first check that preconditions are fulfilled. In this
situation the engine will check that *my_server* node is in *available*
state AND that *mysql* node is in *started* OR *available* states AND
that *mysql* *my_attribute* value is equal to *ready*.

### Workflow reusability

TOSCA allows the reusability of a workflow in other workflows. Such
concepts can be achieved thanks to the inline activity.

#### Reusing a workflow to build multiple workflows

The following example show how a workflow can inline an existing
workflow and reuse it.
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup: backup.sh
  workflows:
   start_mysql:
      steps:
        start_mysql:
          target: mysql
          activities :
            - set_state: starting
            - call_operation: tosca.interfaces.node.lifecycle.Standard.start
            - set_state: started
    stop_mysql:
      steps:
        stop_mysql:
          target: mysql
          activities:
            - set_state: stopping
            - call_operation: tosca.interfaces.node.lifecycle.Standard.stop
            - set_state: stopped

    backup: 
      description: Performs a snapshot of the MySQL data.
      preconditions: 
        - target: my_server
          condition:
            - assert:
              - state: [{equal: available}]
        - target: mysql
          condition:
            - assert:
              - state: [{valid_values: [started, available]}]
              - my_attribute: [{equal: ready }]
      steps:
        backup_step:
          activities:
            - inline: stop
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
            - inline: start
    restart: 
      steps:
        backup_step:
          activities:
            - inline: stop
            - inline: start      
```


The example above defines three workflows and show how the start_mysql
and stop_mysql workflows are reused in the backup and restart workflows.

Inlined workflows are inlined sequentially in the existing workflow for
example the backup workflow would look like this:

<img src="media/image12.png" style="width:1.10625in;height:2.96668in"
alt="../Capture%20d’écran%202016-05-17%20à%2009.45.23.png" />

#### Inlining a complex workflow

It is possible of course to inline more complex workflows. The following
example defines an inlined workflows with multiple steps including
concurrent steps:
```
topology_template:
  workflows:
   inlined_wf:
      steps: 
        A: 
          target: node_a
          activities:
            - call_operation: a
          on_success:
            - B
            - C
        B: 
          target: node_a
          activities:
            - call_operation: b
          on_success:
            - D
        C: 
          target: node_a
          activities:
            - call_operation: c
          on_success:
            - D
        D: 
          target: node_a
          activities:
            - call_operation: d
        E: 
          target: node_a
          activities:
            - call_operation: e
          on_success:
            - C
            - F
        F: 
          target: node_a
          activities:
            - call_operation: f
    main_workflow:
      steps:
        G: 
          target: node_a
          activities:
            - set_state: initial
            - inline: inlined_wf
            - set_state: available
```


To describe the following workflow:

<img src="media/image13.png" style="width:3.23125in;height:3.22622in"
alt="../Capture%20d’écran%202016-05-17%20à%2011.54.41.png" />

### Defining conditional logic on some part of the workflow

Preconditions are used to validate if the workflow should be executed
only for the initial workflow. If a workflow that is inlined defines
some preconditions theses preconditions will be used at the instance
level to define if the operations should be executed or not on the
defined instance.

This construct can be used to filter some steps on a specific instance
or under some specific circumstances or topology state.
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    cluster:
      type: tosca.nodes.DBMS.Cluster
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup: backup.sh
  workflows:
    backup: 
      description: Performs a snapshot of the MySQL data.
      preconditions: 
        - target: my_server
          condition:
            - assert:
              - state: [{equal: available}]
        - target: mysql
          condition:
            - assert:
              - state: [{valid_values: [started, available]}]
              - my_attribute: [{equal: ready }]
      steps:
        backup_step:
          target: cluster
          filter: # filter is a list of clauses. Matching between clauses is and.
            - or: # only one of sub-clauses must be true.
              - assert:
                - foo: [{equals: true}]
              - assert:
                - bar: [{greater_than: 2}, {less_than: 20}]
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
```


### Define inputs for a workflow

Inputs can be defined in a workflow and will be provided in the
execution context of the workflow. If an operation defines a get_input
function on one of its parameter the input will be retrieved from the
workflow input, and if not found from the topology inputs.

#### Example
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup:
              implementation: backup.sh
              inputs:
                storage_url: { get_input: storage_url }
  workflows:
    backup:
      description: Performs a snapshot of the MySQL data.
      preconditions:
        - target: my_server
          valid_states: [available]
        - target: mysql
          valid_states: [started, available]
          attributes:
            my_attribute: [ready]
      inputs:
        storage_url:
          type: string
      steps:
        my_step:
          target: mysql
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
```

To trigger such a workflow, the TOSCA engine must allow user to provide
inputs that match the given definitions.

### Handle operation failure

By default, failure of any activity of the workflow will result in the
failure of the workflow and will results in stopping the steps to be
executed.

Exception: uninstall workflow operation failure SHOULD not prevent the
other operations of the workflow to run (a failure in an uninstall
script SHOULD not prevent from releasing resources from the cloud).

For any workflow other than install and uninstall failures may leave the
topology in an unknown state. In such situation the TOSCA engine may not
be able to orchestrate the deployment. Implementation of on_failure
construct allows to execute rollback operations and reset the state of
the affected entities back to an orchestrator known state.

#### Example
```
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup:
              implementation: backup.sh
              inputs:
                storage_url: { get_input: storage_url }
  workflows:
    backup:
      steps:
        backup_step:
          target: mysql
          activities:
            - set_state: backing_up # this state is not a TOSCA known state
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
            - set_state: available # this state is known by TOSCA orchestrator
          on_failure:
            - rollback_step
        rollback_step:
          target: mysql
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
            - set_state: available # this state is known by TOSCA orchestrator
```


<img src="media/image14.png" style="width:4.91181in;height:2.55759in"
alt="../Capture%20d’écran%202016-05-17%20à%2015.40.04.png" />

<span id="_Toc5736864" class="anchor"></span>**7.3.8 Use a custom
workflow language**

TOSCA orchestrators may support additional workflow languages beyond the
one which has been described in this specification.

***7.3.8.1 Example***
```
topology_template:
  workflows:
    my_workflow:
      implementation: my_workflow.bpmn.xml
```

The **implementation** refers to the artifact **my_workflow.bpmn.xml**
containing the workflow definition written in BPMN (Business Process
Modeling Notation).

***7.3.8.2 Example***
```
topology_template:
  workflows:
    my_workflow:
      implementation: 
        description: workflow implemented in Mistral
        type: mycompany.artifacts.Implementation.Mistral
        file: my_workflow.workbook.mistral.yaml
```

The **implementation** refers to the artifact **my_workflow_script**
which is in fact a Mistral workbook written in the Mistral workflow
definition language.

## Making declarative more flexible and imperative more generic

TOSCA 1.1 version provides the genericity and reusability of declarative
workflows that is designed to address most of use-cases and the
flexibility of imperative workflows to address more complex or specific
use-cases.

Each approach has some pros and cons and we are working so that the next
versions of the specification can improve the workflow usages to try to
allow more flexibility in a more generic way. Two non-exclusive leads
are currently being discussed within the working group and may be
included in the future versions of the specification.

- Improvement of the declarative workflows in order to allow people to
  extend the weaving logic of TOSCA to fit some specific need.

- Improvement of the imperative workflows in order to allow partial
  imperative workflows to be automatically included in declarative
  workflows based on specific constraints on the topology elements.

Implementation of the improvements will be done by adding some elements
to the specification and will not break compatibility with the current
specification.

#### Notes

- The weaving improvement section is a Work in Progress and is not final
  in 2.0 version. The elements in this section are incomplete and may be
  subject to change in next specification version.

- Moreover, the weaving improvements is one of the track of
  improvements. As describe improving the reusability of imperative
  workflow is another track (that may both co-exists in next
  specifications).

### Weaving improvements

Making declarative better experimental option.

#### Node lifecycle definition

Node workflow is defined at the node type level. The node workflow
definition is used to generate the declarative workflow of a given node.

The tosca.nodes.Root type defines workflow steps for both the install
workflow (used to instantiate or deploy a topology) and the uninstall
workflow (used to destroy or undeploy a topology). The workflow is
defined as follows:
```
  tosca.nodes.Root:
    workflows:
      install:
        steps:
          install_sequence:
            activities:
              - set_state: creating
              - call_operation: tosca.interfaces.node.lifecycle.Standard.create
              - set_state: created
              - set_state: configuring
              - call_operation: tosca.interfaces.node.lifecycle.Standard.configure
              - set_state: configured
              - set_state: starting
              - call_operation: tosca.interfaces.node.lifecycle.Standard.start
              - set_state: started
      uninstall:
        steps:
          uninstall_sequence:
            activities:
              - set_state: stopping
              - call_operation: tosca.interfaces.node.lifecycle.Standard.stop
              - set_state: stopped
              - set_state: deleting
              - call_operation: tosca.interfaces.node.lifecycle.Standard.delete
              - set_state: deleted
```
#### Relationship lifecycle and weaving

While the workflow of a single node is quite simple the TOSCA weaving
process is the real key element of declarative workflows. The process of
weaving consist of the ability to create complex management workflows
including dependency management in execution order between node
operations, injection of operations to process specific instruction
related to the connection to other nodes based the relationships and
groups defined in a topology.

This section describes the relationship weaving and how the description
at a template level can be translated on an instance level.
```
relationship_types:
  tosca.relationships.ConnectsTo:
    workflow:
      install: # name of the workflow for wich the weaving has to be taken in account
        source_weaving: # Instruct how to weave some tasks on the source workflow (executed on SOURCE instance)
          - after: configuring # instruct that this operation should be weaved after the target reach configuring state
            wait_target: created # add a join from a state of the target
            activity: tosca.interfaces.relationships.Configure.pre_configure_source
          - before: configured # instruct that this operation should be weaved before the target reach configured state
            activity: tosca.interfaces.relationships.Configure.post_configure_source
          - before: starting
            wait_target: started # add a join from a state of the target
          - after: started
            activity: tosca.interfaces.relationships.Configure.add_target
        target_weaving: # Instruct how to weave some tasks on the target workflow (executed on TARGET instance)
          - after: configuring # instruct that this operation should be weaved after the target reach configuring state
            after_source: created # add a join from a state of the source
            activity: tosca.interfaces.relationships.Configure.pre_configure_target
          - before: configured # instruct that this operation should be weaved before the target reach configured state
            activity: tosca.interfaces.relationships.Configure.post_configure_target
          - after: started
            activity: tosca.interfaces.relationships.Configure.add_source
```
# 6 Instance Model

## Topology Template Model versus Instance Model

A TOSCA service template contains a **topology template,** which models
the components of an application, their relationships and dependencies
(a.k.a., a topology model) that get interpreted and instantiated by
TOSCA Orchestrators. The actual node and relationship instances that are
created represent a set of resources distinct from the template itself,
called a **topology instance (model)**. The direction of this
specification is to provide access to the instances of these resources
for management and operational control by external administrators. This
model can also be accessed by an orchestration engine during deployment
– i.e. during the actual process of instantiating the template in an
incremental fashion, That is, the orchestrator can choose the order of
resources to instantiate (i.e., establishing a partial set of node and
relationship instances) and have the ability, as they are being created,
to access them in order to facilitate instantiating the remaining
resources of the complete topology template.

## Using attributes implicitly reflected from properties

Most entity types in TOSCA (e.g., Node, Relationship, Capability Types,
etc.) have [property definitions](#DEFN_ELEMENT_PROPERTY_DEFN), which
allow template authors to set the values for as inputs when these
entities are instantiated by an orchestrator. These property values are
considered to reflect the desired state of the entity by the author.
Once instantiated, the actual values for these properties on the
realized (instantiated) entity are obtainable via attributes on the
entity with the same name as the corresponding property.

In other words, TOSCA orchestrators will automatically reflect (i.e.,
make available) any property defined on an entity as an attribute of the
entity with the same name as the property.

Use of this feature is shown in the example below where a source node
named my_client, of type ClientNode, requires a connection to another
node named my_server of type ServerNode. As you can see, the ServerNode
type defines a property named notification_port which defines a
dedicated port number which instances of my_client may use to post
asynchronous notifications to it during runtime. In this case, TOSCA
assures that the notification_port property is implicitly reflected as
an attribute in the my_server node (also with the name
notification_port) when its node template is instantiated.

Example 23 - Properties reflected as attributes
```
tosca_definitions_version: tosca_2_0
	
description: >
  TOSCA template that shows how the (notification_port) property is reflected as an attribute and can be referenced elsewhere.

node_types:
  ServerNode:
    derived_from: SoftwareComponent
    properties:
      notification_port:
        type: integer
    capabilities:
      # omitted here for brevity 

  ClientNode:
    derived_from: SoftwareComponent
    properties:
      # omitted here for brevity
    requirements:
      - server: 
          capability: Endpoint
          node: ServerNode  
          relationship: ConnectsTo

topology_template:           
  node_templates:

    my_server:
      type: ServerNode  
      properties:
        notification_port: 8000

    my_client:
      type: ClientNode
      requirements: 
        - server: 
            node: my_server
            relationship: my_connection

  relationship_templates:
    my_connection:
      type: ConnectsTo
      interfaces:
        Configure:
          inputs: 
            targ_notify_port: { get_attribute: [ TARGET, notification_port ] }
            # other operation definitions omitted here for brevity
```
Specifically, the above example shows that the ClientNode type needs the
notification_port value anytime a node of ServerType is connected to it
using the ConnectsTo relationship in order to make it available to its
Configure operations (scripts). It does this by using the get_attribute
function to retrieve the notification_port attribute from the TARGET
node of the ConnectsTo relationship (which is a node of type ServerNode)
and assigning it to an environment variable named targ_notify_port.

It should be noted that the actual port value of the notification_port
attribute may or may not be the value 8000 as requested on the property;
therefore, any node that is dependent on knowing its actual “runtime”
value would use the get_attribute function instead of the get_property
function.

## Returning output values from operations

Service template designers have the ability to define operation outputs
that specify named output values that are expected to be returned by
interface operations as well as the attributes on nodes or relationships
into which these output values must be stored.

### Example: setting output values to a node attribute

The service template below shows an example service template that is
used to create a compute node. The config operation of the Standard
lifecycle returns both the private and the public IP addresses of the
config node. The *attribute mappings grammar* is used to reflect these
addresses into the appropriate Compute node attributes:
```
tosca_definitions_version: tosca_2_0

description: Template for creating compute node 

topology_template:

  node_templates:

    node:
      type: tosca.nodes.Compute
      interfaces:
        Standard:
          configure:
            outputs:
              ip1: [ SELF, private_address ]
              ip2: [ SELF, public_address ]
```
### Example: setting output values to a capability attribute

Some operation outputs may need to be reflected into attributes of
capabilities of nodes, rather than in attributes of the nodes
themselves. The following example shows how an IP address returned by a
config operation is stored in the *ip_address* attribute of the
*endpoint* capability of a *Compute* node:
```
tosca_definitions_version: tosca_simple_yaml_1_2_0

description: Template for creating compute node

topology_template:

  node_templates:

    compute:
      type: tosca.nodes.Compute
      interfaces:
        Standard:
          config:
            outputs:
              ip1: [ SELF, endpoint, ip_address ]

```
## Receiving asynchronous notifications

As shown in the previous section, TOSCA allows service template
designers to reflect the results of executing interface operations into
node or relationship artifacts using output mappings. However, there are
many situations where components modeled by a node can change
independently as a result of external events (e.g. load changes,
failures, mode changes, etc.) rather than as a result of executing
lifecycle management operations. To support those situations, TOSCA
includes support for **notifications** that allow service template
designers to specify how to asynchronously receive external events and
how those events should result in node or relationship attribute
changes.

Just like operations, notifications are specified as part of interface
definitions. The major difference between notifications and operations
is that the former are called from the outside world to on the
orchestrator, and not the other way around. As a result, notifications
do not have inputs defined (since they are called asynchronously from
the outside). Information carried in notifications is pushed to the
orchestrator via notification outputs (similar to operation outputs).

The following example shows how a health monitoring interface is used to
allow the orchestrator to monitor the health of a database node by
listening for heartbeats as well as by waiting for asynchronous failure
alerts:
```
tosca_definitions_version: tosca_2_0

description: Template showing a health monitoring interface

topology_template:
  node_templates:
    db_1:
      type: org.ego.nodes.Database
      interfaces:
        HealthMonitor:
          notifications:
            heartbeat:
              outputs:
                tick: [ SELF, still_alive ]
            failure_report:
              outputs:
                level: [SELF, failure_level]
                time: [SELF, failure_time]
                environment: [SELF, failure_context]    

```
## Creating Multiple Node Instances from the Same Node Template

TOSCA service templates specify a set of nodes that need to be
instantiated at service deployment time. Some service templates may
include multiple nodes that perform the same role. For example, a
template that models an SD-WAN service might contain multiple VPN Site
nodes, one for each location that accesses the SD-WAN. Rather than
having to create a separate service template for each possible number of
VPN sites, it would be preferable to have a single service template that
allows the number of VPN sites to be specified as an input to the
template at deployment time. This section introduces ***experimental***
TOSCA language extensions in support of this functionality.It is
expected that these extensions will be formally standardized in a future
version of this specifications.

The discussion in this section uses an example SD-WAN deployment to
three sites as shown in the following figure:

VPN

San Jose

Austin

Boston

Example SD-WAN Service Deployment

The following code snippet shows a TOSCA service template from which
this service could have been deployed:

Example 24 – TOSCA SD-WAN Service Template
```
tosca_definitions_version: tosca_2_0

description: Template for deploying SD-WAN with three sites.

topology_template:
  inputs:
    location1:
      type: Location
    location2:
      type: Location
    location3:
      type: Location
  node_templates:
    sdwan:
      type: VPN
    site1:
      type: VPNSite
      properties:
        location: { get_input: location1 }
      requirements:
        - vpn: sdwan
    site2:
      type: VPNSite
      properties:
        location: { get_input: location2 }
      requirements:
        - vpn: sdwan
    site3:
      type: VPNSite
      properties:
        location: { get_input: location3 }
      requirements:
        - vpn: sdwan
 
```
Unfortunately, this template can only be used to deploy an SD-WAN with
three sites. To deploy a different number of sites, additional service
templates would have t be created, one for each number of possible
SD-WAN sites. This leads to template proliferation, which is
undesirable. The next section explores alternatives.

### Specifying Number of Occurrences

To avoid the need for multiple service templates, TOSCA must provide a
mechanism that allows all VPN Site nodes to be created from the same
Site node template in the topology, and allow the number of sites to be
specified at deployment time. Specifically, this functionality must:

- Allow service template designers to specify that multiple node
  instances can be created from a single node template

- Allow service template designers to constrain how many node instances
  can be created from a single node template

- Allow users to specify at deployment time the exact number of
  instances that need to be created from the single node template.

To provide this functionality, the TOSCA node template definition
grammar is extended with an **occurrences** keyword that specifies the
minimum and maximum number of instances that can be created from this
node template. If occurrences is not specified, only one single instance
can be created. In addition, an **instance_count** keyword is used to
specify the requested number of runtime instances of this node template.
It is expected that the value of the instance_count is provided as an
input to the topology template. These extensions enable the creation of
a simplified SD-WAN service template that contains only one single VPN
Site node as shown in the following code snippet:

Example 25 – TOSCA SD-WAN Service Template
```
tosca_definitions_version: tosca_2_0

description: Template for deploying SD-WAN with a variable number of sites.

topology_template:
  inputs:
    numberOfSites:
      type: integer
  
  node_templates:
    sdwan:
      type: VPN
    site:
      type: VPNSite
      occurrences: [1, UNBOUNDED]
      instance_count: { get_input: numberOfSites }
      requirements:
        - vpn: sdwan
```
### Specifying Inputs

The service template in the previous section conveniently ignores the
location property of the Site node. As shown earlier, the location
property is expected to be provided as an input value. If Site node
templates can be instantiated multiple times, then it follows that
multiple input values are required to initialize the location property
for each of the Site node instances.

To allow specific input values to be matched with specific node template
instances, a new reserved keyword called INDEX is introduced. A TOSCA
orchestrator will interpret this keyword as the runtime index in the
list of node instances created from a single node template.

The following service template shows how the INDEX keyword is used to
retrieve specific values from a list of input values in a service
template:

Example 26 – TOSCA SD-WAN Service Template
```
tosca_definitions_version: tosca_2_0

description: Template for deploying SD-WAN with a variable number of sites.

topology_template:
  inputs:
    numberOfSites:
      type: integer
    locations:
      type: list
      entry_schema: Location
  
  node_templates:
    sdwan:
      type: VPN
    site:
      type: VPNSite
      occurrences: [1, UNBOUNDED]
      instance_count: { get_input: numberOfSites }
      properties:
        location: { get_input: [ locations, INDEX ] }
      requirements:
        - vpn: sdwan
```
# Describing abstract requirements for nodes and capabilities in a TOSCA template

In TOSCA templates, nodes are either:

- **Concrete**: meaning that they have a deployment and/or one or more
  implementation artifacts that are declared on the “create” operation
  of the node’s Standard lifecycle interface, or they are

- **Abstract**: where the template describes only the node type along
  with its required capabilities and properties that must be satisfied.

TOSCA Orchestrators, by default, when finding an abstract node in TOSCA
Service Template during deployment will attempt to “select” a concrete
implementation for the abstract node type that best matches and fulfills
the requirements and property constraints the template author provided
for that abstract node. The concrete implementation of the node could be
provided by another TOSCA Service Template (perhaps located in a catalog
or repository known to the TOSCA Orchestrator) or by an existing
resource or service available within the target Cloud Provider’s
platform that the TOSCA Orchestrator already has knowledge of.

TOSCA supports two methods for template authors to express requirements
for an abstract node within a TOSCA service template.

1.  ***Using a target node_filter***: where a node template can describe
    a requirement (relationship) for another node without including it
    in the topology. Instead, the node provides a node_filter to
    describe the target node type along with its capabilities and
    property constrains

2.  ***Using an abstract node template***: that describes the abstract
    node’s type along with its property constraints and any requirements
    and capabilities it also exports. This first method you have already
    seen in examples from previous chapters where the Compute node is
    abstract and selectable by the TOSCA Orchestrator using the supplied
    Container and [OperatingSystem](#tosca.capabilities.operatingsystem)
    capabilities property constraints.

These approaches allow architects and developers to create TOSCA service
templates that are composable and can be reused by allowing flexible
matching of one template’s requirements to another’s capabilities.
Examples of both these approaches are shown below.

The following section describe how a user can define a requirement for
an orchestrator to select an implementation and replace a node. For more
details on how an orchestrator may perform matching and select a node
from it’s catalog(s) you may look at section 14 of the specification.

## Using a node_filter to define hosting infrastructure requirements for a software 

Using TOSCA, it is possible to define only the software components of an
application in a template and just express constrained requirements
against the hosting infrastructure. At deployment time, the provider can
then do a late binding and dynamically allocate or assign the required
hosting infrastructure and place software components on top.

This example shows how a single software component (i.e., the mysql node
template) can define its host requirements that the TOSCA Orchestrator
and provider will use to select or allocate an appropriate host Compute
node by using matching criteria provided on a node_filter.

Example 11 - An abstract "host" requirement using a node filter
```

description: Template with requirements against hosting infrastructure.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        # omitted here for brevity
      requirements:
        - host: 
            node_filter:
              capabilities:
                # Constraints for selecting “host” (Container Capability)
                - host:
                    properties:
                      - num_cpus: { in_range: [ 1, 4 ] }
                      - mem_size: { greater_or_equal: 2 GB }
                # Constraints for selecting “os” (OperatingSystem Capability)
                - os:
                    properties:
                      - architecture: { equal: x86_64 }
                      - type: linux
                      - distribution: ubuntu
```
In the example above, the **mysql** component contains a host
requirement for a node of type **Compute** which it inherits from its
parent DBMS node type definition; however, there is no declaration or
reference to any node template of type Compute. Instead, the mysql node
template augments the abstract “host” requirement with a node_filter
which contains additional selection criteria (in the form of property
constraints that the provider must use when selecting or allocating a
host Compute node.

Some of the constraints shown above narrow down the boundaries of
allowed values for certain properties such as mem_size or num_cpus for
the “host” capability by means of qualifier functions such as
**greater_or_equal**. Other constraints, express specific values such as
for the architecture or distribution properties of the “os” capability
which will require the provider to find a precise match.

Note that when no qualifier function is provided for a property
(filter), such as for the distribution property, it is interpreted to
mean the equal operator as shown on the architecture property.

## Using an abstract node template to define infrastructure requirements for software

This previous approach works well if no other component (i.e., another
node template) other than mysql node template wants to reference the
same Compute node the orchestrator would instantiate. However, perhaps
another component wants to also be deployed on the same host, yet still
allow the flexible matching achieved using a node-filter. The
alternative to the above approach is to create an abstract node template
that represents the Compute node in the topology as follows:

Example 12 - An abstract Compute node template with a node filter
```
tosca_definitions_version: tosca_2_0
	
description: Template with requirements against hosting infrastructure.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        # omitted here for brevity
      requirements:
        - host: mysql_compute

    # Abstract node template (placeholder) to be selected by provider
    mysql_compute:
      type: Compute
      directives: [ select ]
      node_filter:
        capabilities:
          - host:
              properties:
                num_cpus: { equal: 2 }
                mem_size: { greater_or_equal: 2 GB }
          - os:
              properties:
                architecture: { equal: x86_64 }
                type: linux
                distribution: ubuntu
```

In this node template, the **msql_compute** node template is marked as
abstract using the **select** directive. As you can see the resulting
mysql_compute node template looks very much like the “hello world”
template as shown in [Chapter
2.1](file:///C:\Users\Chris\Downloads\hello_world#_A_) but this one also
allows the TOSCA orchestrator more flexibility when “selecting” a host
Compute node by providing flexible constraints for properties like
mem_size.

As we proceed, you will see that TOSCA provides many normative node
types like Compute for commonly found services (e.g., BlockStorage,
WebServer, Network, etc.). When these TOSCA normative node types are
used in your application’s topology they are always assumed to be
“implementable” by TOSCA Orchestrators which work with target
infrastructure providers to find or allocate the best match for them
based upon your application’s requirements and constraints.

## Using a node_filter to define requirements on a database for an application

In the same way requirements can be defined on the hosting
infrastructure (as shown above) for an application, it is possible to
express requirements against application or middleware components such
as a database that is not defined in the same template. The provider may
then allocate a database by any means, (e.g. using a
database-as-a-service solution).

Example 13 - An abstract database requirement using a node filter
```
tosca_definitions_version: tosca_2_0

description: Template with a TOSCA Orchestrator selectable database requirement using a node_filter.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    my_app:
      type: my.types.MyApplication
      properties:
        admin_user: { get_input: admin_username }
        admin_password: { get_input: admin_password }
        db_endpoint_url: { get_property: [SELF, database_endpoint, url_path ] }         
      requirements:
        - database_endpoint:
            node: my.types.nodes.MyDatabase
            node_filter:
              properties:
                - db_version: { greater_or_equal: 5.5 }
```
In the example above, the application my_app requires a database node of
type MyDatabase which has a db_version property value of
greater_or_equal to the value 5.5.

This example also shows how the get_property intrinsic function can be
used to retrieve the url_path property from the database node that will
be selected by the provider and connected to my_app at runtime due to
fulfillment of the database_endpoint requirement. To locate the
property, the get_property’s first argument is set to the keyword SELF
which indicates the property is being referenced from something in the
node itself. The second parameter is the name of the requirement named
**database_endpoint** which contains the property we are looking for.
The last argument is the name of the property itself (i.e., url_path)
which contains the value we want to retrieve and assign to
db_endpoint_url.

The alternative representation, which includes a node template in the
topology for database that is still selectable by the TOSCA orchestrator
for the above example, is as follows:

Example 14 - An abstract database node template
```
tosca_definitions_version: tosca_2_0

description: Template with a TOSCA Orchestrator selectable database using node template.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    my_app:
      type: my.types.MyApplication
      properties:
        admin_user: { get_input: admin_username }
        admin_password: { get_input: admin_password }
        db_endpoint_url: { get_property: [SELF, database_endpoint, url_path ] }         
      requirements:
        - database_endpoint: my_abstract_database

    my_abstract_database:
      type: my.types.nodes.MyDatabase
      properties:
        - db_version: { greater_or_equal: 5.5 }
```
# 7 Substitution Mapping

## Using node template substitution for model composition

From an application perspective, it is often not necessary or desired to
dive into platform details, but the platform/runtime for an application
is abstracted. In such cases, the template for an application can use
generic representations of platform components. The details for such
platform components, such as the underlying hosting infrastructure and
its configuration, can then be defined in separate template files that
can be used for substituting the more abstract representations in the
application level template file. Service designers use the substitute
directive to declare node templates as abstract. At deployment time,
TOSCA orchestrators are expected to *substitute* abstract node templates
in a service template before service orchestration can be performed.

### Understanding node template instantiation through a TOSCA Orchestrator

When a topology template is instantiated by a TOSCA Orchestrator, the
orchestrator has to first look for abstract node templates in the
topology template. Abstract node templates are node templates that
include the substitute directive. These abstract node templates must
then be realized using *substituting service templates* that are
compatible with the node types specified for each abstract node
template. Such realizations can either be node types that include the
appropriate implementation artifacts and deployment artifacts that can
be used by the orchestrator to bring to life the real-world resource
modeled by a node template. Alternatively, separate topology templates
may be annotated as being suitable for realizing a node template in the
top-level topology template.

In the latter case, a TOSCA Orchestrator will use additional
substitution mapping information provided as part of the substituting
topology templates to derive how the substituted part gets “wired” into
the overall deployment, for example, how capabilities of a node template
in the top-level topology template get bound to capabilities of node
templates in the substituting topology template.

Thus, in cases where no “normal” node type implementation is available,
or the node type corresponds to a whole subsystem that cannot be
implemented as a single node, additional topology templates can be used
for filling in more abstract placeholders in top level application
templates.

### Definition of the top-level service template

The following sample defines a web application web_app connected to a
database db. In this example, the complete hosting stack for the
application is defined within the same topology template: the web
application is hosted on a web server web_server, which in turn is
installed (hosted) on a compute node server.

The hosting stack for the database db, in contrast, is not defined
within the same file but only the database is represented as a node
template of type tosca.nodes.Database. The underlying hosting stack for
the database is defined in a separate template file, which is shown
later in this section. Within the current template, only a number of
properties (user, password, name) are assigned to the database using
hardcoded values in this simple example.

<img src="media/image15.png" style="width:5.66809in;height:3.50263in" />

Figure 1: Using template substitution to implement a database tier

When a node template is to be substituted by another service template,
this has to be indicated to an orchestrator by marking he node template
as abstract using the **substitute** directive. Orchestrators can only
instantiate abstract node templates by substituting them with a service
template that consists entirely of concrete nodes. Note that abstract
node template substitution may need to happen recursively before a
service template is obtained that consists only of concrete nodes.

Note that in contrast to the use case described in section 2.9.2 (where
a database was abstractly referred to in the requirements section of a
node and the database itself was not represented as a node template),
the approach shown here allows for some additional modeling capabilities
in cases where this is required.

For example, if multiple components need to use the same database (or
any other sub-system of the overall service), this can be expressed by
means of normal relations between node templates, whereas such modeling
would not be possible in requirements sections of disjoint node
templates.

Example 15 - Referencing an abstract database node template
```
tosca_definitions_version: tosca_2_0

topology_template:
  description: Template of an application connecting to a database.

  node_templates:
    web_app:
      type: tosca.nodes.WebApplication.MyWebApp
      requirements:
        - host: web_server
        - database_endpoint: db

    web_server:
      type: tosca.nodes.WebServer
      requirements:
        - host: server

    server:
      type: tosca.nodes.Compute
      # details omitted for brevity

    db:
      # This node is abstract as specified by the substitute directive
      # and must be substituted with a topology provided by another template
      # that exports a Database type’s capabilities.
      type: tosca.nodes.Database
      directives:
        - substitute
      properties:
        user: my_db_user
        password: secret
        name: my_db_name 
```
### Definition of the database stack in a service template

The following sample defines a template for a database including its
complete hosting stack, i.e. the template includes a database node
template, a template for the database management system (dbms) hosting
the database, as well as a computer node server on which the DBMS is
installed.

This service template can be used standalone for deploying just a
database and its hosting stack. In the context of the current use case,
though, this template can also substitute the database node template in
the previous snippet and thus fill in the details of how to deploy the
database.

In order to enable such a substitution, an additional metadata section
substitution_mappings is added to the topology template to tell a TOSCA
Orchestrator how exactly the topology template will fit into the context
where it gets used. For example, requirements or capabilities of the
node that gets substituted by the topology template have to be mapped to
requirements or capabilities of internal node templates for allow for a
proper wiring of the resulting overall graph of node templates.

In short, the substitution_mappings section provides the following
information:

3.  It defines what node templates, i.e. node templates of which type,
    can be substituted by the topology template.

4.  It defines how capabilities of the substituted node (or the
    capabilities defined by the node type of the substituted node
    template, respectively) are bound to capabilities of node templates
    defined in the topology template.

5.  It defines how requirements of the substituted node (or the
    requirements defined by the node type of the substituted node
    template, respectively) are bound to requirements of node templates
    defined in the topology template.

<img src="media/image16.png" style="width:5.42175in;height:3.65in" />

Figure 2: Substitution mappings

The substitution_mappings section in the sample below denotes that this
topology template can be used for substituting node templates of type
tosca.nodes.Database. It further denotes that the database_endpoint
capability of the substituted node gets fulfilled by the
database_endpoint capability of the database node contained in the
topology template.

Example 16 - Using substitution mappings to export a database
implementation
```
tosca_definitions_version: tosca_2_0

topology_template:
  description: Template of a database including its hosting stack.

  inputs:
    db_user:
      type: string
    db_password:
      type: string
    # other inputs omitted for brevity

  substitution_mappings:
    node_type: tosca.nodes.Database
    capabilities:
      database_endpoint: [ database, database_endpoint ]

  node_templates:
    database:
      type: tosca.nodes.Database
      properties:
        user: { get_input: db_user }
        # other properties omitted for brevity
      requirements:
        - host: dbms

    dbms:
      type: tosca.nodes.DBMS
      # details omitted for brevity

    server:
      type: tosca.nodes.Compute
      # details omitted for brevity
```
Note that the substitution_mappings section does not define any mappings
for requirements of the Database node type, since all requirements are
fulfilled by other nodes templates in the current topology template. In
cases where a requirement of a substituted node is bound in the
top-level service template as well as in the substituting topology
template, a TOSCA Orchestrator should raise a validation error.

Further note that no mappings for properties or attributes of the
substituted node are defined. Instead, the inputs and outputs defined by
the topology template are mapped to the appropriate properties and
attributes or the substituted node. If there are more inputs than the
substituted node has properties, default values must be defined for
those inputs, since no values can be assigned through properties in a
substitution case.

## Using node template substitution for chaining subsystems

A common use case when providing an end-to-end service is to define a
chain of several subsystems that together implement the overall service.
Those subsystems are typically defined as separate service templates to
(1) keep the complexity of the end-to-end service template at a
manageable level and to (2) allow for the re-use of the respective
subsystem templates in many different contexts. The type of subsystems
may be specific to the targeted workload, application domain, or custom
use case. For example, a company or a certain industry might define a
subsystem type for company- or industry specific data processing and
then use that subsystem type for various end-user services. In addition,
there might be generic subsystem types like a database subsystem that
are applicable to a wide range of use cases.

### Defining the overall subsystem chain

Figure 3 shows the chaining of three subsystem types – a message queuing
subsystem, a transaction processing subsystem, and a databank subsystem
– that support, for example, an online booking application. On the front
end, this chain provides a capability of receiving messages for handling
in the message queuing subsystem. The message queuing subsystem in turn
requires a number of receivers, which in the current example are two
transaction processing subsystems. The two instances of the transaction
processing subsystem might be deployed on two different hosting
infrastructures or datacenters for high-availability reasons. The
transaction processing subsystems finally require a database subsystem
for accessing and storing application specific data. The database
subsystem in the backend does not require any further component and is
therefore the end of the chain in this example.

<img src="media/image17.png" style="width:6.25338in;height:2.01994in" />

Figure 3: Chaining of subsystems in a service template

All of the node templates in the service template shown above are
abstract and considered substitutable where each can be treated as their
own subsystem; therefore, when instantiating the overall service, the
orchestrator would realize each substitutable node template using other
TOSCA service templates. These service templates would include more
nodes and relationships that include the details for each subsystem. A
simplified version of a TOSCA service template for the overall service
is given in the following listing.

Example 17 - Declaring a transaction subsystem as a chain of
substitutable node templates
```
tosca_definitions_version: tosca_2_0

topology_template:
  description: Template of online transaction processing service.

  node_templates:
    mq:
      type: example.QueuingSubsystem
      directives:
        - substitute
      properties:
        # properties omitted for brevity
      capabilities:
        message_queue_endpoint:
          # details omitted for brevity
      requirements:
        - receiver: trans1
        - receiver: trans2

    trans1:
      type: example.TransactionSubsystem
      directives:
        - substitute
      properties:
        mq_service_ip: { get_attribute: [ mq, service_ip ] }
        receiver_port: 8080
      capabilities:
        message_receiver:
          # details omitted for brevity
      requirements:
        - database_endpoint: dbsys

    trans2:
      type: example.TransactionSubsystem
      directives:
        - substitute
      properties:
        mq_service_ip: { get_attribute: [ mq, service_ip ] }
        receiver_port: 8080
      capabilities:
        message_receiver:
          # details omitted for brevity
      requirements:
        - database_endpoint: dbsys

    dbsys:
      type: example.DatabaseSubsystem
      directives:
        - substitute
      properties:
        # properties omitted for brevity
      capabilities:
        database_endpoint:
          # details omitted for brevity
```
As can be seen in the example above, the subsystems are chained to each
other by binding requirements of one subsystem node template to other
subsystem node templates that provide the respective capabilities. For
example, the receiver requirement of the message queuing subsystem node
template mq is bound to transaction processing subsystem node templates
trans1 and trans2.

Subsystems can be parameterized by providing properties. In the listing
above, for example, the IP address of the message queuing server is
provided as property mq_service_ip to the transaction processing
subsystems and the desired port for receiving messages is specified by
means of the receiver_port property.

If attributes of the instantiated subsystems need to be obtained, this
would be possible by using the get_attribute intrinsic function on the
respective subsystem node templates.

### Defining a subsystem (node) type

The types of subsystems that are required for a certain end-to-end
service are defined as TOSCA node types as shown in the following
example. Node templates of those node types can then be used in the
end-to-end service template to define subsystems to be instantiated and
chained for establishing the end-to-end service.

The realization of the defined node type will be given in the form of a
whole separate service template as outlined in the following section.

Example 18 - Defining a TransactionSubsystem node type
```
tosca_definitions_version: tosca_2_0

node_types:
  example.TransactionSubsystem:
    properties:
      mq_service_ip:
        type: string
      receiver_port:
        type: integer
    attributes:
      receiver_ip:
        type: string
      receiver_port:
        type: integer
    capabilities:
      message_receiver: tosca.capabilities.Endpoint
    requirements:
      - database_endpoint: tosca.capabilities.Endpoint.Database
```
Configuration parameters that would be allowed for customizing the
instantiation of any subsystem are defined as properties of the node
type. In the current example, those are the properties mq_service_ip and
receiver_port that had been used in the end-to-end service template in
section 2.11.1.

Observable attributes of the resulting subsystem instances are defined
as attributes of the node type. In the current case, those are the IP
address of the message receiver as well as the actually allocated port
of the message receiver endpoint.

### Defining the details of a subsystem

The details of a subsystem, i.e. the software components and their
hosting infrastructure, are defined as node templates and relationships
in a service template. By means of substitution mappings that have been
introduced in section 2.10.2, the service template is annotated to
indicate to an orchestrator that it can be used as realization of a node
template of a certain type, as well as how characteristics of the node
type are mapped to internal elements of the service template.

<img src="media/image18.png" style="width:5.87076in;height:3.45956in" />

Figure 4: Defining subsystem details in a service template

Figure 1 illustrates how a transaction processing subsystem as outlined
in the previous section could be defined in a service template. In this
example, it simply consists of a custom application app of type SomeApp
that is hosted on a web server websrv, which in turn is running on a
compute node.

The application named app provides a capability to receive messages,
which is bound to the message_receiver capability of the substitutable
node type. It further requires access to a database, so the
application’s database_endpoint requirement is mapped to the
database_endpoint requirement of the TransactionSubsystem node type.

Properties of the TransactionSubsystem node type are used to customize
the instantiation of a subsystem. Those properties can be mapped to any
node template for which the author of the subsystem service template
wants to expose configurability. In the current example, the application
app and the web server middleware websrv get configured through
properties of the TransactionSubsystem node type. All properties of that
node type are defined as inputs of the service template. The input
parameters in turn get mapped to node templates by means of get_input
function calls in the respective sections of the service template.

Similarly, attributes of the whole subsystem can be obtained from
attributes of particular node templates. In the current example,
attributes of the web server and the hosting compute node will be
exposed as subsystem attributes. All exposed attributes that are defined
as attributes of the substitutable TransactionSubsystem node type are
defined as outputs of the subsystem service template.

An outline of the subsystem service template is shown in the listing
below. Note that this service template could be used for stand-alone
deployment of a transaction processing system as well, i.e. it is not
restricted just for use in substitution scenarios. Only the presence of
the substitution_mappings metadata section in the topology_template
enables the service template for substitution use cases.

Example 19 - Implementation of a TransactionSubsytem node type using
substitution mappings
```
tosca_definitions_version: tosca_2_0

topology_template:
  description: Template of a database including its hosting stack.

  inputs:
    mq_service_ip:
      type: string
      description: IP address of the message queuing server to receive messages from
    receiver_port:
      type: string
      description: Port to be used for receiving messages
    # other inputs omitted for brevity

  substitution_mappings:
    node_type: example.TransactionSubsystem
    capabilities:
      message_receiver: [ app, message_receiver ]
    requirements:
      database_endpoint: [ app, database ]

  node_templates:
    app:
      type: example.SomeApp
      properties:
        # properties omitted for brevity
      capabilities:
        message_receiver:
          properties:
            service_ip: { get_input: mq_service_ip }
            # other properties omitted for brevity
      requirements:
        - database:
            # details omitted for brevity
        - host: websrv

    websrv:
      type: tosca.nodes.WebServer
      properties:
        # properties omitted for brevity
      capabilities:
        data_endpoint:
          properties:
            port_name: { get_input: receiver_port }
            # other properties omitted for brevity
      requirements:
        - host: server

    server:
      type: tosca.nodes.Compute
      # details omitted for brevity

  outputs:
    receiver_ip:
      description: private IP address of the message receiver application
      value: { get_attribute: [ server, private_address ] }
    receiver_port:
      description: Port of the message receiver endpoint
      value: { get_attribute: [ app, app_endpoint, port ] }
```
## Using node template substitution to provide product choice

Some service templates might include abstract node templates that model
specific functionality without fully specifying the exact product or
technology that provides that functionality. The objective of such
service templates is to allow the end-user of the service to decide *at
service deployment time* which specific product component to use.

### Defining a service template with vendor-independent component

For example, let’s assume an abstract security service that includes a
firewall component where the choice of firewall product is left to the
end-user at service deployment time. The following template shows an
example of such a service: it includes an abstract firewall node
template that has a *vendor* property that represents the firewall
vendor. The value of this property is obtained from a topology input
variable that allows end-users to specify the desired firewall vendor at
deployment time.

Defining a security service with a vendor-independent firewall component
```
tosca_definitions_version: tosca_2_0

description: Service template for an abstract security service

topology_template:

  inputs:
    vendorInput:
      type: string
    rulesInput:
      type: list
      entry_schema: FirewallRules
    
  node_templates:
    firewall:
      type: abstract.Firewall
      directives:
        - substitute
      properties:
        vendor: { get_input: vendorInput }
        rules: { get_input: rulesInput }
```
The abstract firewall node type is defined in the following code
snippet. The abstract firewall node type defines a *rules* property to
hold the configured firewall rules. In addition, it also defines a
property for capturing the name of the vendor of the firewall.

Node type defining an abstract firewall component
```
tosca_definitions_version: tosca_2_0

description: Template defining an abstract firewall component

node_types:
  abstract.Firewall:
    derived_from: tosca.nodes.Root
    properties:
      vendor:
        type: string
      rules:
        type: list
        entry_schema: FirewallRules
```
### Defining vendor-specific component options

In the above example, the firewall node template is abstract, which
means that it needs to be substituted with a substituting firewall
template. Let’s assume we have two firewall vendors—ACME Firewalls and
Simple Firewalls—who each provide implementations for the abstract
firewall component. Their respective implementations are defined in
vendor-specific service templates. ACME Firewall’s service template
might look as follows:

Service template for an ACME firewall
```
tosca_definitions_version: tosca_2_0

description: Service template for an ACME firewall

topology_template:

  inputs:
    rulesInput:
      type: list
      entry_schema: FirewallRules
    
  substitution_mappings:
    node_type: abstract.Firewall
    properties:
      rules: [ rulesInput ]

  node_templates:
    acme:
      type: ACMEFirewall
      properties:
        rules: { get_input: rulesInput }
        acmeConfig: # any ACME-specific properties go here.
```


In this example the node type ACMEFirewall is an ACME-specific node type
that models the internals of the ACME firewall product. The ACMEFirewall
node type definition is omitted here for brevity since it is not
relevant for the example.

Similarly, Simple Firewall’s service template looks as follows:

Service template for a Simple Firewall
```
tosca_definitions_version: tosca_2_0

description: Service template for a Simple Corp. firewall

topology_template:

  inputs:
    rulesInput:
      type: list
      entry_schema: FirewallRules
    
  substitution_mappings:
    node_type: abstract.Firewall
    properties:
      rules: [ rulesInput ]

  node_templates:
    acme:
      type: SimpleFirewall
      properties:
        rules: { get_input: rulesInput }
```
As the substitution mappings section in the service templates show,
either firewall service template can be used to implement the abstract
firewall component defined above.

### Substitution matching using substitution filters

Since both the ACME Firewall and the Simple Firewall can substitute for
abstract node templates of type abstract.Firewall, either firewall is a
valid candidate to substitute the abstract firewall node template. When
multiple matching templates are available, the orchestrator must provide
mechanisms to allow the end-user to drive the decision about which
matching template must be selected.

TOSCA uses a **substitution_filter** in the substitution mappings
section of a service template to further constrain the abstract nodes
for which a service template can be a valid substitution. Using
substitution filters, a service template is a valid candidate to
substitute an abstract node template if the following two conditions are
met:

6.  The **type** advertised in the substitution_mappings section of the
    service template matches the type of the abstract node template.

7.  The property values of the abstract node template satisfy the
    constraints defined in the **substitution_filtter** of the
    substituting service template.

In the security service example used in this section, the value of the
*vendor* property of the abstract firewall node template is provide by
the end-user using a topology input parameter. Substituting templates
use a substitution_filter to match the appropriate vendor-specific
service templates with the abstract firewall node template based on the
value of the *vendor* property.

The following code snippet shows an updated version of the ACME Firewall
service template. This version includes a substitution_filter that
specifies that this service template only matches abstract firewall
nodes with a vendor property equal to ‘ACME’.

Service template for an ACME firewall with a substitution filter
```
tosca_definitions_version: tosca_2_0
description: Service template for an ACME firewall
topology_template:
  inputs:
    rulesInput:
      type: list
      entry_schema: FirewallRules
  
  substitution_mappings:
    node_type: abstract.Firewall
    substitution_filter:
      properties:
vendor: { equal: ACME }
    properties:
      rules: [ rulesInput ]

  node_templates:
    acme:
      type: ACMEFirewall
      properties:
        rules: { get_input: rulesInput }
        acmeConfig: # any ACME-specific properties go here.
```
Similarly, an updated service template for Simple Corp’s firewall looks
as follows:

Service template for a Simple firewall with a substitution filter
```
tosca_definitions_version: tosca_2_0

description: Service template for a Simple Corp. firewall

topology_template:

  inputs:
    rulesInput:
      type: list
      entry_schema: FirewallRules
    
  substitution_mappings:
    node_type: abstract.Firewall
    substitution_filter:
      properties:
vendor: { equal: Simple }
    properties:
      rules: [ rulesInput ]

  node_templates:
    acme:
      type: SimpleFirewall
      properties:
        rules: { get_input: rulesInput }
```

As specified in this example, only abstract firewall node templates that
have the *vendor* property set to ‘Simple’ can be substituted by this
service template.

## Abstract nodes and target node filters matching

This section details the matching or orchestrator’s node selection
mechanisms that is mentioned and explained from user point of view in
section 2.9 of the specification.

When a user defines a service template, some of the nodes within the
service templates are not implemented (abstract) and some requirements
may define some node filters target rather than actual abstract node
templates. In order to deploy such service templates, the orchestrator
has to find a valid fulfillment and implementation available on the
deployment target in order to be able to actually instantiate the
various elements of the template.

The goal of this **non-normative** chapter is to provide non-exclusive
insight into possible orchestrator behavior to provide fulfillment of
abstract nodes and dangling requirements within a TOSCA template.

### Reminder on types

TOSCA allows the definition of types that can later be used within
templates. Types can be of two nature on regard of the matching process:

- **Abstract types** that have no implementation specified and that can
  be used within a Topology template in order to request the
  orchestrator to find a valid implementation (for example an abstract
  tosca.nodes.Compute type can be used to define a template to request a
  VM from an orchestrator without any specific knowledge on the
  implementation, allowing that way portability).

- **Concrete types** that are implemented through TOSCA implementation
  artifacts (shell scripts, python scripts etc.) or through the mean of
  a Topology substitution.

Both abstract and concrete types define properties (and capabilities
properties) that can be used for two different means:

- **Configuration** of the node and of its behavior (most likely used in
  concrete types).

- **Matching** purpose (most likely used for abstract types).

This section will focus on the matching process while configuration
properties is mostly related to types design.

### Orchestrator catalogs

Most of orchestrators are likely to have internal catalogs of TOSCA
types, pre-defined templates, internal implementation of nodes (either
through concrete types, substitution mechanisms, potentially supported
by non-normative workflow definitions etc.) and maybe even running
instances (services).

Theses catalogs are not normative, and it is up to the TOSCA
implementation to support some or all of them. During matching the TOSCA
orchestrator may find a valid match for a template within any of it’s
internal catalogs or through any other mean.

This section will consider and provide examples based on the three
following catalogs (they may or may not be used in actual
implementations):

- **Type catalog:** Basic internal catalog but not the most intuitive
  candidate for node matching. It contains:

- abstract node types

- concrete node types implemented through implementation artifacts.

- concrete node types implemented through topology substitution.

- **Pre-defined node template catalog**: This is the catalog that is the
  most likely to be used for matching, it may contain:

- Orchestrator Provider pre-defined node templates offered to its user
  eventually backed up with orchestrator specific implementations (that
  may delegate to non-tosca internal components).

- User defined node templates implemented through implementation
  artifacts.

- User defined node templates implemented through topology substitution.

- **Running instance/Services catalog**: Catalog of already running
  services available for matching that contains some definition of TOSCA
  instances.

### Abstract node template matching

A TOSCA topology template as defined by a user will probably define some
abstract node templates. A node template is considered abstract if it is
based on an abstract type and does not provides implementation at the
template level. As instantiating an abstract node cannot be done by an
orchestrator, the orchestrator will have to perform internally the
replacement of the defined abstract node template's types by a matching
implementation of the type.

**A type** is considered as a valid matching implementation if it
fulfils all of the following conditions:

- The matching node derives from the type specified in the template

- Every property defined in the matching node is matching the constraint
  specified on the node template's properties or capability properties
  given the following rules:

- A property that is defined in the node template (either through a
  value at the template level or through a default property value at the
  type level) should be match the constraint defined on the matching
  node type property.

- A property that is not defined in the node template may have no or any
  value (matching the node type property definition constraints) in the
  orchestrator matched node.

**A pre-defined template** is considered as a valid matching
implementation if it fulfils all of the following conditions:

- The orchestrator pre-defined matching node derives from the type
  specified in the topology template's node

- Every property defined in the orchestrator pre-defined matching node
  is matching the constraint specified on the node template's properties
  or capability properties given the following rules:

- A property that is defined in the node template (either through a
  value at the template level or through a default property value at the
  type level) should be matched by an equality constraint

- A property that is not defined in the node template may have no or any
  value (matching the node type property definition constraints) in the
  orchestrator matched node.

**A running instance (service)** is considered as a valid matching
implementation if it fulfils all of the following conditions:

- The node instance has a type that equals or derives from the type
  specified in the topology template's node

- Every attribute defined in the orchestrator instance node is matching
  the constraint specified on the node template's properties or
  capability properties given the following rules:

- A property that is defined in the node template (either through a
  value at the template level or through a default property value at the
  type level) should be matched by an equality constraint against the
  attribute value.

- A property that is not defined in the node template may have no or any
  value (matching the node type property definition constraints) in
  instance node.

Note that the node instance that defines the running instance/service
can be actually a full topology that propose a node abstraction through
the topology substitution mechanism.

**Multiple valid matches:** If the orchestrator has more than one valid
match in its catalog(s) he is responsible for either choosing
automatically a node or providing a mean for users to specify the node
they want to select.

**No match:** If the orchestrator does not find any valid match, he
could propose alternative that he consider valid but should not
automatically deploy the topology without an explicit user approval.

Note: These rules are the basic matching rules of TOSCA, however if an
orchestrator has a UI and want to propose other matching nodes that does
not fulfil all of these constraints he can still do that even if he
should warn the user that the deployed template will not be the same
template as defined. For example, an orchestrator could propose a node
with greater than CPU rather than an equal match or propose an
equivalent node (with different type) that has the same capabilities as
the ones connected by the node in the topology.

Note: Support of instances matching may impact the TOSCA workflow and
lifecycle as their operations will not be included in the workflow
(instances are already created).

#### Examples

Let's consider a few examples of abstract node templates and how they
can be matched against an orchestrator catalog(s). Note that the type
catalog is not the only catalog in which to find implementation. Most
orchestrator will probably have an internal provider templates catalog
that includes pre-defined templates. None of the catalog is required to
be a valid TOSCA implementation and the following are just examples for
orchestrator implementers but is not required to be implemented.

##### Matching from a type catalog

Let's consider the following node types in an orchestrator internal type
catalog.
```
tosca_definitions_version: tosca_2_0

node_types:
  tosca.samples.nodes.MyAbstractNode:
    derived_from: tosca.nodes.Root
    properties:
      str_prop:
        type: string
      nbr_prop:
        type: integer
```
MyAbstractNode is an abstract type as Root does not define any
implementation and the defined node neither.
```
node_types:
  tosca.samples.nodes.MyNodeImpl1:
    derived_from: tosca.samples.nodes.MyAbstractNode
    properties:
      nbr_prop :
        constraints:
          - greater_or_equal: 1
    interfaces:
      standard:
        create: test.sh
```

MyNodeImpl1 is an implementation (through the test.sh script) of
MyAbstractNode that requires the nbr_prop property to be higher than 1.
```
tosca_definitions_version: tosca_2_0

node_types:
  tosca.samples.nodes.MyNodeImpl2:
    derived_from: tosca.samples.nodes.MyAbstractNode
    properties:
    nbr_prop :
      constraints:
          - greater_or_equal: 25
    interfaces:
      standard:
        create: test2.sh
```
MyNodeImpl2 is an implementation (through the test2.sh script) of
MyAbstractNode that requires the nbr_prop property to be higher than 25.

Let's consider the following topology template that a user wants to
deploy:
```
tosca_definitions_version: tosca_2_0

topology_template:
  node_templates:
    my_node:
      type: tosca.samples.MyAbstractNode
      properties:
        str_prop: standard
        nbr_prop: 10
```
The specified node template (my_node) is an abstract node template as
its type is abstract and it does not add any implementation. Before
being able to deploy this template, a TOSCA orchestrator will have to
find a valid match for this node. In order to do so it will look into
its catalog (in this example the type catalog) and try to find nodes
that matches the definition.

In this example while both MyNodeImpl1 and MyNodeImpl2 have a valid type
as they derive from MyAbstractNode only MyNodeImpl1 is a valid match as
the constraint defined on the nbr_prop property of the MyNodeImpl2 node
type (greater_or_equal: 25) is not matching the property value defined
in the requested node template (10).

##### Matching from a pre-defined template catalog

This example details how a tosca.nodes.Compute abstract node can be
matched to a specific pre-defined template that an orchestrator may
have. First of all, the orchestrator will probably define a concrete
implementation of the Compute node. So, let's consider the following
example type
```
tosca_definitions_version: tosca_2_0

node_types:
  tosca.samples.nodes.MyCloudCompute:
    derived_from: tosca.nodes.Compute
    properties:
      image_id:
        type: string
        required: true
      flavor_id:
        type: string
        required: true
    interfaces:
      standard:
        create: create.py
```
This type adds two properties to the Compute node so the orchestrator
knows which image_id and flavor_id are used to instantiate the VM.
Implementation is simplified here and just a single python script is
enough.

Note: an orchestrator provider can define internally some non-portable
implementations of types that will be supported only by the latter. As
the user defines an abstract node its template is portable even if the
execution is specific to the orchestrator.

Let's now consider that the orchestrator has defined some internal node
template in its own pre-defined templates or provider catalog (note that
this is orchestrator specific and this specification has no intent on
defining how the orchestrator should manage, import or support its
internal catalogs).
```
tosca_definitions_version: tosca_2_0

node_templates:
    small_ubuntu:
      type: tosca.samples.nodes.MyCloudCompute
      properties:
        image_id: ubuntu
        flavor_id: small
      capabilities:
        host:
	      num_cpus: 1
	      cpu_frequency: 1 GHz
	      disk_size: 15 GiB
	      mem_size: 2 GiB
        os:
          type: linux
          distribution: ubuntu
    large_ubuntu:
      type: tosca.samples.nodes.MyCloudCompute
      properties:
        image_id: ubuntu
        flavor_id: small
      capabilities:
        host:
	      num_cpus: 4
	      cpu_frequency: 2 GHz
	      disk_size: 15 GiB
	      mem_size: 8 GiB
        os:
          type: linux
          distribution: ubuntu
    large_windows:
      type: tosca.samples.nodes.MyCloudCompute
      properties:
        image_id: ubuntu
        flavor_id: small
      capabilities:
        host:
	      num_cpus: 4
	      cpu_frequency: 2 GHz
	      disk_size: 15 GiB
	      mem_size: 8 GiB
        os:
          type: windows
          distribution: server
```
If a user defines the following template:
```
tosca_definitions_version: tosca_2_0

topology_template:
  node_templates:
    my_node:
      type: tosca.nodes.Compute
      capabilities:
        host:
	      num_cpus: 1
	      mem_size: 2 GiB
        os:
          distribution: Ubuntu
```
The orchestrator will select the small_ubuntu pre-defined template as a
valid match. The image_id and flavor_id properties are internal to the
orchestrator.

### Target node filter matching

In addition to matching abstract nodes, an orchestrator also has to find
matches for dangling requirements. Target node filter (also referred as
dangling requirements) matching provides loose coupling as you may
specify a request on any node that provides a capability rather than a
specific node.

A dangling requirement is defined on the requirement section of a node
template, it instruct the orchestrator how to find a valid node template
to add and connect in the topology. The node added by the orchestrator
as a relationship target is matched based on the following rules.

**A type** is considered as a valid matching implementation if it
fulfils all of the following conditions:

- The selected node must define a capability with the same type as
  specified by the dangling requirement or with a type that derive from
  the specified type.

- If the *node* property is specified on the dangling requirement, then
  the type of the matched node must derive from the requested type

- The node filter constraints defined on the dangling requirement are
  compatible with the candidate node type properties constraints and
  default values.

- **A pre-defined template** is considered as a valid matching
  implementation if it fulfils all of the following conditions:

- The orchestrator pre-defined node defines a capability with the same
  type as specified by the dangling requirement or with a type that
  derive from the specified type.

- If the *node* property is specified on the dangling requirement, then
  the type of the orchestrator pre-defined node must derive from the
  requested type

- The node filter constraints defined on the dangling requirement are
  matched by the pre-defined template properties values.

**A running instance (service)** is considered as a valid matching
implementation if it fullfills all of the following conditions:

- The orchestrator pre-defined node defines a capability with the same
  type as specified by the dangling requirement or with a type that
  derive from the specified type.

- If the *node* property is specified on the dangling requirement, then
  the type of the node instance must derive from the requested type

- The node filter constraints defined on the dangling requirement are
  matched by the node instance current attribute values

A property that is not defined in the node template may have no or any
value (matching the node type property definition constraints) in
instance node.

#### Examples

##### Matching a node filter target against a type catalog

Let’s consider the following nodes in a type catalog:
```

capability_types:
  tosca.samples.capabilities.MyMessagingEndpoint :
    derived_from: tosca.capabilities.Endpoint
    properties:
      throughput :
        type: integer
        required: true
  tosca.samples.capabilities.MyLimitedMessagingEndpoint :
    derived_from: tosca.samples.capabilities.MyMessagingEndpoint 
    properties:
      throughput :
        type: integer
        required: true
        constraints:
          - lower_than: 5


node_types:
  tosca.samples.nodes.MyNode :
    derived_from: tosca.nodes.Root
    requirements: tosca.samples.capabilities.MyMessagingEndpoint
    interfaces:
      standard:
        create: install.sh
  tosca.samples.nodes.MyAbstractMessagingSystem:
    derived_from: tosca.nodes.Root
    properties:
      scaling:
        type: string
        required: true
        constraints:
          - valid_values: [ “auto”, ”manual”, “none” ]
      highly_available :
        type: boolean
        required: true
    capabilities:
      messaging: tosca.samples.capabilities.MyMessagingEndpoint
  tosca.samples.nodes.MyMessagingServiceSystem:
    derived_from: tosca.samples.nodes.MyAbstractMessagingSystem
    properties:
      scaling :
        type: string
        required: true
        constraints:
          - valid_values: [ “manual”]
      highly_available:
        constraints:
          - equal: true
    interfaces:
      standard:
        create: create.py
  tosca.samples.nodes.MyMessagingSystem:
    derived_from: tosca.samples.nodes.MyAbstractMessagingSystem
    properties:
      scaling :
        type: string
        required: true
        constraints:
          - valid_values: [ “none”]
      highly_available:
        constraints:
          - equal: false
    capabilities:
      messaging: tosca.samples.capabilities.MyLimitedMessagingEndpoint 
    interfaces:
      standard:
        create: install.sh
        start: start.sh
```
And the following user template to deploy:
```
tosca_definitions_version: tosca_2_0

topology_template:
  node_templates:
    my_node:
      type: tosca.samples.nodes.MyNode
      requirements:
        - messaging:
            node: tosca.samples.nodes.MyAbstractMessagingSystem
            node_filter:
              properties:
                - scaling: { valid_values: [manual, auto] }
                - highly_available: { equal: true }
              capabilities:
                - tosca.samples.capabilities.MyMessagingEndpoint:
                    properties:
                      - throughput: { greater_than: 10 } 
```
In order to fulfill the messaging endpoint target the orchestrator will
have to add a node template from a type that derives from
MyAbstractMessagingSystem (as specified within the node filter node
property) and that defines constraints that are compatible with the ones
specified on the node filter.

In the defined type catalog, the only type that fulfill all constraints
is the MyMessagingServiceSystem node.

##### Matching a node filter target against a type catalog with substitution

TOSCA allows the definition of a type implementation through a
substitution template. In this case the specified topology templates
becomes a type in the catalog. From this type an orchestrator may define
some pre-defined templates or even running services if instanciated. In
the following example we will consider the same user template as in the
previous example as well as the same abstract types. However, the
implemented type will be defined through the following topology
template:
```
tosca_definitions_version: tosca_2_0

topology_template:
  inputs:
    # Nodes in this topology can be configured to enable auto-scaling or not
    scaling_input :
        type: string
        required: true
        constraints:
          - valid_values: [ “auto”, “none” ]
 
  substitution_mappings:
    node_type: tosca.samples.nodes.MyAbstractMessagingSystem
    properties:
      scaling: [ scaling_input ]
      highly_available: true
    capabilities:
      messaging : [ my_load_balancer, load_balanced_messaging_endpoint]
  node_templates:
    my_load_balancer:
      type: tosca.samples.nodes.MyLoadBalancer
      capability:
        load_balanced_messaging_endpoint: tosca.samples.capabilities.MyMessagingEndpoint
    my_other_node_that_trigger_a_service_somewhere:
      type: org.custom.Type
      properties:
        my_scaling_info: get_input { scaling }
    my_other_node:
      type: org.something.Type:
      properties:
        my_other_scaled_prop: get_input { scaling }
        another_prop: value
… other nodes templates
```

This template from a substitution boundaries point of view would be
equivalent to the following node type:
```
tosca_definitions_version: tosca_2_0

node_type:
  my_node_resulting_from_topology
    # From topology_template -> substitution_mappings -> node_type
    derived_from: tosca.samples.nodes.MyAbstractMessagingSystem
    properties:
      scaling :
        constraints:
            - valid_values: [ “auto”, “none” ]
      highly_available:
        default: true
        constraints:
            - equal: true
      # Equivalent:
      # implementation: The topology specified above
```
In this example the orchestrator can select the topology template
specified above as a valid match for the requested target node filter.

### Post matching properties

It is possible that, even after matching, some properties have unset
values, moreover some properties may be added by the type that is
selected by the orchestrator and derives from the user requested type.
In any case an orchestrator should not deploy a node that has some
required properties undefined.

Based on the orchestrator capabilities it could be possible to assign
values to the properties (either required or not required) of the node
after the matching, including properties added by the selected
implementation node. Note that these capabilities are not mandatory and
that as properties depends from the actual result of the matching it is
not possible to ship them with the template. Therefore, there is no
standard for defining theses additional properties and the mean of
providing them will be specific to the orchestrator implementation.

# 8 TOSCA Policies

This section is **non-normative** and describes the approach TOSCA plans
to take for policy description with TOSCA Service Templates. In
addition, it explores how existing TOSCA Policy Types and definitions
might be applied in the future to express operational policy use cases.

## Grouping node templates

In designing applications composed of several interdependent software
components (or nodes) it is often desirable to manage these components
as a named group. This can provide an effective way of associating
policies (e.g., scaling, placement, security or other) that
orchestration tools can apply to all the components of group during
deployment or during other lifecycle stages.

In many realistic scenarios it is desirable to include scaling
capabilities into an application to be able to react on load variations
at runtime. The example below shows the definition of a scaling web
server stack, where a variable number of servers with apache installed
on them can exist, depending on the load on the servers.

Example 20 - Grouping Node Templates for possible policy application
```
tosca_definitions_version: tosca_2_0

description: Template for a scaling web server.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    apache:
      type: tosca.nodes.WebServer.Apache
      properties:
        # Details omitted for brevity
      requirements:
        - host: server

    server:
      type: tosca.nodes.Compute
        # details omitted for brevity

  groups:
    webserver_group:
      type: tosca.groups.Root
      members: [ apache, server ]
```

The example first of all uses the concept of grouping to express which
components (node templates) need to be scaled as a unit – i.e. the
compute nodes and the software on-top of each compute node. This is done
by defining the webserver_group in the groups section of the template
and by adding both the apache node template and the **server** node
template as a member to the group.

Furthermore, a scaling policy is defined for the group to express that
the group as a whole (i.e. pairs of **server** node and the **apache**
component installed on top) should scale up or down under certain
conditions.

In cases where no explicit binding between software components and their
hosting compute resources is defined in a template, but only
requirements are defined as has been shown in section 2.9, a provider
could decide to place software components on the same host if their
hosting requirements match, or to place them onto different hosts.

It is often desired, though, to influence placement at deployment time
to make sure components get collocation or anti-collocated. This can be
expressed via grouping and policies as shown in the example below.

Example 21 - Grouping nodes for anti-colocation policy application
```
tosca_definitions_version: tosca_2_0

description: Template hosting requirements and placement policy.

topology_template:
  inputs:
    # omitted here for brevity

  node_templates:
    wordpress_server:
      type: tosca.nodes.WebServer
      properties:
        # omitted here for brevity
      requirements:
        - host: 
            # Find a Compute node that fulfills these additional filter reqs.
            node_filter:
              capabilities:
                - host:
                    properties:
                      - mem_size: { greater_or_equal: 512 MB }
                      - disk_size: { greater_or_equal: 2 GB }
                - os:
                    properties:
                      - architecture: x86_64
                      - type: linux

    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        # omitted here for brevity
      requirements:
        - host: 
            node: tosca.nodes.Compute
            node_filter:
              capabilities:
                - host:
                    properties:
                      - disk_size: { greater_or_equal: 1 GB }
                - os:
                    properties:
                      - architecture: x86_64
                      - type: linux

  groups:
    my_co_location_group:
      type: tosca.groups.Root
      members: [ wordpress_server, mysql ]
  
  policies:
    - my_anti_collocation_policy:
        type: my.policies.anticolocateion
        targets: [ my_co_location_group ]
        # For this example, specific policy definitions are considered 
        # domain specific and are not included here
```
In the example above, both software components **wordpress_server** and
**mysql** have similar hosting requirements. Therefore, a provider could
decide to put both on the same server as long as both their respective
requirements can be fulfilled. By defining a group of the two components
and attaching an anti-collocation policy to the group it can be made
sure, though, that both components are put onto different hosts at
deployment time.

## A declarative approach

TOSCA Policies are a type of requirement that govern use or access to
resources which can be expressed independently from specific
applications (or their resources) and whose fulfillment is not
discretely expressed in the application’s topology (i.e., via TOSCA
Capabilities).

TOSCA deems it not desirable for a declarative model to encourage
external intervention for resolving policy issues (i.e., via imperative
mechanisms external to the Cloud). Instead, the Cloud provider is deemed
to be in the best position to detect when policy conditions are
triggered, analyze the affected resources and enforce the policy against
the allowable actions declared within the policy itself.

### Declarative considerations

- Natural language rules are not realistic, too much to represent in our
  specification; however, regular expressions can be used that include
  simple operations and operands that include symbolic names for TOSCA
  metamodel entities, properties and attributes.

- Complex rules can actually be directed to an external policy engine
  (to check for violation) returns true\|false then policy says what to
  do (trigger or action).

- Actions/Triggers could be:

- Autonomic/Platform corrects against user-supplied criteria

- External monitoring service could be utilized to monitor policy
  rules/conditions against metrics, the monitoring service could
  coordinate corrective actions with external services (perhaps Workflow
  engines that can analyze the application and interact with the TOSCA
  instance model).

## Consideration of Event, Condition and Action 

## Types of policies

Policies typically address two major areas of concern for customer
workloads:

**Access Control** – assures user and service access to controlled
resources are governed by rules which determine general access
permission (i.e., allow or deny) and conditional access dependent on
other considerations (e.g., organization role, time of day, geographic
location, etc.).

**Placement** – assures affinity (or anti-affinity) of deployed
applications and their resources; that is, what is allowed to be placed
where within a Cloud provider’s infrastructure.

- **Quality-of-Service** (and continuity) - assures performance of
  software components (perhaps captured as quantifiable, measure
  components within an SLA) along with consideration for scaling and
  failover.

### Access control policies

Although TOSCA Policy definitions could be used to express and convey
access control policies, definitions of policies in this area are out of
scope for this specification. At this time, TOSCA encourages
organizations that already have standards that express policy for access
control to provide their own guidance on how to use their standard with
TOSCA.

### Placement policies

- There must be control mechanisms in place that can be part of these
  patterns that accept governance policies that allow control
  expressions of what is allowed when placing, scaling and managing the
  applications that are enforceable and verifiable in Cloud.

- 

- These policies need to consider the following:

- Regulated industries need applications to control placement
  (deployment) of applications to different countries or regions (i.e.,
  different logical geographical boundaries).

#### Placement for governance concerns

In general, companies and individuals have security concerns along with
general “loss of control” issues when considering deploying and hosting
their highly valued application and data to the Cloud. They want to
control placement perhaps to ensure their applications are only placed
in datacenter they trust or assure that their applications and data are
not placed on shared resources (i.e., not co-tenanted).

In addition, companies that are related to highly regulated industries
where compliance with government, industry and corporate policies is
paramount. In these cases, having the ability to control placement of
applications is an especially significant consideration and a
prerequisite for automated orchestration.

#### Placement for failover

Companies realize that their day-to-day business must continue on
through unforeseen disasters that might disable instances of the
applications and data at or on specific data centers, networks or
servers. They need to be able to convey placement policies for their
software applications and data that mitigate risk of disaster by
assuring these cloud assets are deployed strategically in different
physical locations. Such policies need to consider placement across
geographic locations as wide as countries, regions, datacenters, as well
as granular placement on a network, server or device within the same
physical datacenter. Cloud providers must be able to not only enforce
these policies but provide robust and seamless failover such that a
disaster’s impact is never perceived by the end user.

### Quality-of-Service (QoS) policies

Quality-of-Service (apart from failover placement considerations)
typically assures that software applications and data are available and
performant to the end users. This is usually something that is
measurable in terms of end-user responsiveness (or response time) and
often qualified in SLAs established between the Cloud provider and
customer. These QoS aspects can be taken from SLAs and legal agreements
and further encoded as performance policies associated with the actual
applications and data when they are deployed. It is assumed that Cloud
provider is able to detect high utilization (or usage load) on these
applications and data that deviate from these performance policies and
is able to bring them back into compliance.

## Policy relationship considerations

- Performance policies can be related to scalability policies.
  Scalability policies tell the Cloud provider exactly **how** to scale
  applications and data when they detect an application’s performance
  policy is (or about to be) violated (or triggered).

- Scalability policies in turn are related to placement policies which
  govern **where** the application and data can be scaled to.

- There are general “tenant” considerations that restrict what resources
  are available to applications and data based upon the contract a
  customer has with the Cloud provider. This includes other constraints
  imposed by legal agreements or SLAs that are not encoded
  programmatically or associated directly with actual application or
  data..

## Use Cases

This section includes some initial operation policy use cases that we
wish to describe using the TOSCA metamodel. More policy work will be
done in future versions of the TOSCA specification.

### Placement

#### Use Case 1: Simple placement for failover

##### Description

This use case shows a failover policy to keep at least 3 copies running
in separate containers. In this simple case, the specific containers to
use (or name is not important; the Cloud provider must assure placement
separation (anti-affinity) in three physically separate containers.

##### Features

This use case introduces the following policy features:

- Simple separation on different “compute” nodes (up to discretion of
  provider).

- Simple separation by region (a logical container type) using an
  allowed list of region names relative to the provider.

- Also, shows that set of allowed “regions” (containers) can be greater
  than the number of containers requested.

##### Logical Diagram

Sample YAML: Compute separation
```
failover_policy_1:
  type: tosca.policy.placement.Antilocate
  description: My placement policy for Compute node separation
  properties:
    # 3 diff target containers
    container_type: Compute 
    container_number: 3 
```
##### Notes

- There may be availability (constraints) considerations especially if
  these policies are applied to “clusters”.

- There may be future considerations for controlling max \# of instances
  per container.

#### Use Case 2: Controlled placement by region

##### Description

This use case demonstrates the use of named “containers” which could
represent the following:

- Datacenter regions

- Geographic regions (e.g., cities, municipalities, states, countries,
  etc.)

- Commercial regions (e.g., North America, Eastern Europe, Asia Pacific,
  etc.)

##### Features

This use case introduces the following policy features:

- Separation of resources (i.e., TOSCA nodes) by logical regions, or
  zones.

##### Sample YAML: Region separation amongst named set of regions
```
failover_policy_2:
  type: tosca.policy.placement
  description: My failover policy with allowed target regions (logical containers)
  properties:
    container_type: region 
    container_number: 3 
    # If “containers” keyname is provided, they represent the allowed set 
    # of target containers to use for placement for .
    containers: [ region1, region2, region3, region4 ]
```
#### Use Case 3: Co-locate based upon Compute affinity

##### Description

Nodes that need to be co-located to achieve optimal performance based
upon access to similar Infrastructure (IaaS) resource types (i.e.,
Compute, Network and/or Storage).

This use case demonstrates the co-location based upon Compute resource
affinity; however, the same approach could be taken for Network as or
Storage affinity as well. :

##### Features

This use case introduces the following policy features:

- Node placement based upon Compute resource affinity.

#### Notes

- The concept of placement based upon IaaS resource utilization is not
  future-thinking, as Cloud should guarantee equivalent performance of
  application performance regardless of placement. That is, all network
  access between application nodes and underlying Compute or Storage
  should have equivalent performance (e.g., network bandwidth, network
  or storage access time, CPU speed, etc.).

##### Sample YAML: Region separation amongst named set of regions
```
keep_together_policy:
  type: tosca.policy.placement.Colocate
  description: Keep associated nodes (groups of nodes) based upon Compute
  properties:
    affinity: Compute
```

### Scaling

#### Use Case 1: Simple node autoscale

##### Description

Start with X nodes and scale up to Y nodes, capability to do this from a
dashboard for example.

##### Features

This use case introduces the following policy features:

- Basic autoscaling policy

##### Sample YAML
```
my_scaling_policy_1:
  type: tosca.policy.scaling
  description: Simple node autoscaling
  properties:
    min_instances: <integer>
    max_instances: <integer>
    default_instances: <integer>
    increment: <integer>
```
##### Notes

- Assume horizontal scaling for this use case

- Horizontal scaling, implies “stack-level” control using Compute nodes
  to define a “stack” (i.e., The Compute node’s entire HostedOn
  relationship dependency graph is considered part of its “stack”)

- Assume Compute node has a SoftwareComponent that represents a VM
  application.

- Availability Zones (and Regions if not same) need to be considered in
  further use cases.

- If metrics are introduced, there is a control-loop (that monitors).
  Autoscaling is a special concept that includes these considerations.

- Mixed placement and scaling use cases need to be considered:

- *Example*: Compute1 and Compute2 are 2 node templates. Compute1 has 10
  instances, 5 in one region 5 in other region.

# Component Modeling Use Cases

This section is **non-normative** and includes use cases that explore
how to model components and their relationships using TOSCA.

### Use Case: Exploring the HostedOn relationship using WebApplication and WebServer

This use case examines the ways TOSCA YAML can be used to express a
simple hosting relationship (i.e., HostedOn) using the normative TOSCA
WebServer and WebApplication node types defined in this specification.

#### WebServer declares its “host” capability

For convenience, relevant parts of the normative TOSCA Node Type for
WebServer are shown below:
```
tosca.nodes.WebServer
  derived_from: SoftwareComponent
  capabilities:
    ...
    host: 
      type: tosca.capabilities.Container
      valid_source_types: [ tosca.nodes.WebApplication ]
```
As can be seen, the WebServer Node Type declares its capability to
“contain” (i.e., host) other nodes using the symbolic name “host” and
providing the Capability Type tosca.capabilities.Container. It should be
noted that the symbolic name of “host” is not a reserved word, but one
assigned by the type designer that implies at or betokens the associated
capability. The Container capability definition also includes a required
list of valid Node Types that can be contained by this, the WebServer,
Node Type. This list is declared using the keyname of valid_source_types
and in this case it includes only allowed type WebApplication.

#### WebApplication declares its “host” requirement

The WebApplication node type needs to be able to describe the type of
capability a target node would have to provide in order to “host” it.
The normative TOSCA capability type tosca.capabilities.Container is used
to describe all normative TOSCA hosting (i.e., container-containee
pattern) relationships. As can be seen below, the WebApplication
accomplishes this by declaring a requirement with the symbolic name
“host” with the **capability** keyname set to
tosca.capabilities.Container.

Again, for convenience, the relevant parts of the normative
WebApplication Node Type are shown below:
```
tosca.nodes.WebApplication:
  derived_from: tosca.nodes.Root
  requirements:
    - host:        
        capability: tosca.capabilities.Container
        node: tosca.nodes.WebServer
        relationship: tosca.relationships.HostedOn
```

##### Notes

- The symbolic name “host” is not a keyword and was selected for
  consistent use in TOSCA normative node types to give the reader an
  indication of the type of requirement being referenced. A valid
  HostedOn relationship could still be established between WebApplicaton
  and WebServer in a TOSCA Service Template regardless of the symbolic
  name assigned to either the requirement or capability declaration.

### Use Case: Establishing a ConnectsTo relationship to WebServer

This use case examines the ways TOSCA YAML can be used to express a
simple connection relationship (i.e.,
[ConnectsTo](#tosca.relationships.connectsto-1)) between some service
derived from the [SoftwareComponent](#tosca.nodes.softwarecomponent)
Node Type, to the normative [WebServer](#tosca.nodes.webserver) node
type defined in this specification.

The service template that would establish a
[ConnectsTo](#tosca.relationships.connectsto-1) relationship as follows:
```
node_types:
  MyServiceType:
    derived_from: SoftwareComponent
    requirements:
      # This type of service requires a connection to a WebServer’s data_endpoint
      - connection1: 
          node: WebServer
          relationship: ConnectsTo
          capability: Endpoint

topology_template:
  node_templates:
    my_web_service:
      type: MyServiceType
      ...
      requirements:
        - connection1: 
            node: my_web_server

    my_web_server:
      # Note, the normative WebServer node type declares the “data_endpoint” 
      # capability of type tosca.capabilities.Endpoint.  
      type: WebServer
```
Since the normative WebServer Node Type only declares one capability of
type tosca.capabilties.Endpoint (or Endpoint, its shortname alias in
TOSCA) using the symbolic name data_endpoint, the my_web_service node
template does not need to declare that symbolic name on its requirement
declaration. If however, the my_web_server node was based upon some
other node type that declared more than one capability of type Endpoint,
then the capability keyname could be used to supply the desired symbolic
name if necessary.

#### Best practice

It should be noted that the best practice for designing Node Types in
TOSCA should not export two capabilities of the same type if they truly
offer different functionality (i.e., different capabilities) which
should be distinguished using different Capability Type definitions.

### Use Case: Attaching (local) BlockStorage to a Compute node 

This use case examines the ways TOSCA YAML can be used to express a
simple AttachesTo relationship between a Compute node and a locally
attached BlockStorage node.

The service template that would establish an
[AttachesTo](#tosca.relationships.attachesto) relationship follows:
```
node_templates:
  my_server:
    type: Compute
    ...
    requirements:
      # contextually this can only be a relationship type
      - local_storage: 
          # capability is provided by Compute Node Type
          node: my_block_storage            
          relationship: 
            type: AttachesTo
            properties:
              location: /path1/path2
          # This maps the local requirement name ‘local_storage’ to the
          # target node’s capability name ‘attachment’

  my_block_storage:
    type: BlockStorage
    properties:
      size: 10 GB
```
### Use Case: Reusing a BlockStorage Relationship using Relationship Type or Relationship Template

This builds upon the previous use case (10.1.3) to examine how a
template author could attach multiple Compute nodes (templates) to the
same BlockStorage node (template), but with slightly different property
values for the AttachesTo relationship.

Specifically, several notation options are shown (in this use case) that
achieve the same desired result.

####  Rationale

Referencing an explicitly declared Relationship Template is a
convenience of the that allows template authors an entity to set,
constrain or override the properties and operations as defined in its
declared (Relationship) Type much as allowed now for Node Templates. It
is especially useful when a complex Relationship Type (with many
configurable properties or operations) has several logical occurrences
in the same Service (Topology) Template; allowing the author to avoid
configuring these same properties and operations in multiple Node
Templates.

#### Notation Style \#1: Augment AttachesTo Relationship Type directly in each Node Template

This notation extends the methodology used for establishing a HostedOn
relationship, but allowing template author to supply (dynamic)
configuration and/or override of properties and operations.

**Note:** This option will remain valid for regardless of other notation
(copy or aliasing) options being discussed or adopted for future
versions.
```
node_templates:
  
  my_block_storage:
    type: BlockStorage
    properties:
      size: 10

  my_web_app_tier_1:
    type: Compute
    requirements:
      - local_storage: 
          node: my_block_storage
          relationship: MyAttachesTo
            # use default property settings in the Relationship Type definition

  my_web_app_tier_2:
    type: Compute
    requirements:
      - local_storage: 
          node: my_block_storage
          relationship:
            type: MyAttachesTo
            # Override default property setting for just the ‘location’ property
            properties:
              location: /some_other_data_location 

relationship_types:

  MyAttachesTo:
    derived_from: AttachesTo
    properties:
      location: /default_location
    interfaces:
      Configure:
        post_configure_target:
          implementation: default_script.sh
```
#### Notation Style \#2: Use the ‘template’ keyword on the Node Templates to specify which named Relationship Template to use

This option shows how to explicitly declare different named Relationship
Templates within the Service Template as part of a
relationship_templates section (which have different property values)
and can be referenced by different Compute typed Node Templates.
```
node_templates:
  
  my_block_storage:
    type: BlockStorage
    properties:
      size: 10

  my_web_app_tier_1:
    derived_from: Compute
    requirements:
      - local_storage:
          node: my_block_storage
          relationship: storage_attachesto_1

  my_web_app_tier_2:
    derived_from: Compute
    requirements:
      - local_storage: 
          node: my_block_storage
          relationship: storage_attachesto_2

relationship_templates:
  storage_attachesto_1:
    type: MyAttachesTo
    properties:
      location: /my_data_location

  storage_attachesto_2:
    type: MyAttachesTo
    properties:
      location: /some_other_data_location

relationship_types:

  MyAttachesTo:
    derived_from: AttachesTo
    interfaces:
      some_interface_name:
        some_operation:
          implementation: default_script.sh
```
#### Notation Style \#3: Using the “copy” keyname to define a similar Relationship Template

How does TOSCA make it easier to create a new relationship template that
is mostly the same as one that exists without manually copying all the
same information? TOSCA provides the copy keyname as a convenient way to
copy an existing template definition into a new template definition as a
starting point or basis for describing a new definition and avoid manual
copy. The end results are cleaner TOSCA Service Templates that allows
the description of only the changes (or deltas) between similar
templates.

The example below shows that the Relationship Template named
storage_attachesto_1 provides some overrides (conceptually a large set
of overrides) on its Type which the Relationship Template named
storage_attachesto_2 wants to “copy” before perhaps providing a smaller
number of overrides.
```
node_templates:
  
  my_block_storage:
    type: BlockStorage
    properties:
      size: 10

  my_web_app_tier_1:
    derived_from: Compute
    requirements:
      - attachment: 
          node: my_block_storage
          relationship: storage_attachesto_1

  my_web_app_tier_2:
    derived_from: Compute
    requirements:
      - attachment: 
          node: my_block_storage
          relationship: storage_attachesto_2

relationship_templates:
  storage_attachesto_1:
    type: MyAttachesTo
    properties:
      location: /my_data_location
    interfaces:
      some_interface_name:
        some_operation_name_1: my_script_1.sh
        some_operation_name_2: my_script_2.sh
        some_operation_name_3: my_script_3.sh

  storage_attachesto_2:
    # Copy the contents of the “storage_attachesto_1” template into this new one
    copy: storage_attachesto_1
    # Then change just the value of the location property
    properties:
      location: /some_other_data_location

relationship_types:

  MyAttachesTo:
    derived_from: AttachesTo
    interfaces:
      some_interface_name:
        some_operation:
          implementation: default_script.sh
```
# Application Modeling Use Cases

This section is **non-normative** and includes use cases that show how
to model Infrastructure-as-a-Service (IaaS), Platform-as-a-Service
(PaaS) and complete application uses cases using TOSCA.

## Use cases

Many of the use cases listed below can be found under the following
link:

<https://github.com/openstack/heat-translator/tree/master/translator/tests/data>

### Overview

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#USE_CASE_COMPUTE_1"><strong>Compute</strong></a>: Create a
single Compute instance with a host Operating System</td>
<td>Introduces a TOSCA Compute node type which is used to stand up a
single compute instance with a host Operating System Virtual Machine
(VM) image selected by the platform provider using the Compute node’s
properties.</td>
</tr>
<tr class="even">
<td><a href="#USE_CASE_SW_COMP_1"><strong>Software Component
1</strong></a>: Automatic deployment of a Virtual Machine (VM) image
artifact</td>
<td>Introduces the SoftwareComponent node type which declares software
that is hosted on a Compute instance. In this case, the
SoftwareComponent declares a VM image as a deployment artifact which
includes its own pre-packaged operating system and software. The TOSCA
Orchestrator detects this known deployment artifact type on the
SoftwareComponent node template and automatically deploys it to the
Compute node.</td>
</tr>
<tr class="odd">
<td><a
href="#USE_CASE_BLOCKSTORAGE_1"><strong>BlockStorage-1</strong></a>:
Attaching Block Storage to a single Compute instance</td>
<td>Demonstrates how to attach a TOSCA BlockStorage node to a Compute
node using the normative AttachesTo relationship.</td>
</tr>
<tr class="even">
<td><a
href="#USE_CASE_BLOCKSTORAGE_2"><strong>BlockStorage-2</strong></a>:
Attaching Block Storage using a custom Relationship Type</td>
<td>Demonstrates how to attach a TOSCA BlockStorage node to a Compute
node using a custom RelationshipType that derives from the normative
AttachesTo relationship.</td>
</tr>
<tr class="odd">
<td><a
href="#USE_CASE_BLOCKSTORAGE_3"><strong>BlockStorage-3</strong></a>:
Using a Relationship Template of type AttachesTo</td>
<td>Demonstrates how to attach a TOSCA BlockStorage node to a Compute
node using a TOSCA Relationship Template that is based upon the
normative AttachesTo Relationship Type.</td>
</tr>
<tr class="even">
<td><a
href="#USE_CASE_BLOCKSTORAGE_4"><strong>BlockStorage-4</strong></a>:
Single Block Storage shared by 2-Tier Application with custom AttachesTo
Type and implied relationships</td>
<td>This use case shows 2 Compute instances (2 tiers) with one
BlockStorage node, and also uses a custom AttachesTo Relationship that
provides a default mount point (i.e., location) which the 1<sup>st</sup>
tier uses, but the 2<sup>nd</sup> tier provides a different mount
point.</td>
</tr>
<tr class="odd">
<td><a
href="#USE_CASE_BLOCKSTORAGE_5"><strong>BlockStorage-5</strong></a>:
Single Block Storage shared by 2-Tier Application with custom AttachesTo
Type and explicit Relationship Templates</td>
<td>This use case is like the previous <a
href="#USE_CASE_BLOCKSTORAGE_4">BlockStorage-4</a> use case, but also
creates two relationship templates (one for each tier) each of which
provide a different mount point (i.e., location) which overrides the
default location defined in the custom Relationship Type.</td>
</tr>
<tr class="even">
<td><a
href="#USE_CASE_BLOCKSTORAGE_6"><strong>BlockStorage-6</strong></a>:
Multiple Block Storage attached to different Servers</td>
<td>This use case demonstrates how two different TOSCA BlockStorage
nodes can be attached to two different Compute nodes (i.e., servers)
each using the normative AttachesTo relationship.</td>
</tr>
<tr class="odd">
<td><a href="#USE_CASE_OBJECTSTORAGE_1"><strong>Object Storage
1</strong></a>: Creating an Object Storage service</td>
<td>Introduces the TOSCA ObjectStorage node type and shows how it can be
instantiated.</td>
</tr>
<tr class="even">
<td><a href="#USE_CASE_NETWORK_1"><strong>Network-1</strong></a>: Server
bound to a new network</td>
<td>Introduces the TOSCA Network and Port nodes used for modeling
logical networks using the LinksTo and BindsTo Relationship Types. In
this use case, the template is invoked without an existing network_name
as an input property so a new network is created using the properties
declared in the Network node.</td>
</tr>
<tr class="odd">
<td><a href="#USE_CASE_NETWORK_2"><strong>Network-2</strong></a>: Server
bound to an existing network</td>
<td>Shows how to use a network_name as an input parameter to the
template to allow a server to be associated with (i.e. bound to) an
existing Network.</td>
</tr>
<tr class="even">
<td><a href="#USE_CASE_NETWORK_3"><strong>Network-3</strong></a>: Two
servers bound to a single network</td>
<td>This use case shows how two servers (Compute nodes) can be
associated with the same Network node using two logical network
Ports.</td>
</tr>
<tr class="odd">
<td><a href="#USE_CASE_NETWORK_4"><strong>Network-4</strong></a>: Server
bound to three networks</td>
<td>This use case shows how three logical networks (Network nodes), each
with its own IP address range, can be associated with the same server
(Compute node).</td>
</tr>
<tr class="even">
<td><a
href="#USE_CASE_WEBSERVER_DBMS_1"><strong>WebServer-DBMS-1</strong></a>:
WordPress [<a href="#REF_WORDPRESS">WordPress</a>] + MySQL, single
instance</td>
<td>Shows how to host a TOSCA WebServer with a TOSCA WebApplication,
DBMS and Database Node Types along with their dependent HostedOn and
ConnectsTo relationships.</td>
</tr>
<tr class="odd">
<td><a
href="#USE_CASE_WEBSERVER_DBMS_2"><strong>WebServer-DBMS-2</strong></a>:
Nodejs with PayPal Sample App and MongoDB on separate instances</td>
<td>Instantiates a 2-tier application with Nodejs and its (PayPal
sample) WebApplication on one tier which connects a MongoDB database
(which stores its application data) using a ConnectsTo
relationship.</td>
</tr>
<tr class="even">
<td><a href="#USE_CASE_MULTI_TIER_1"><strong>Multi-Tier-1</strong></a>:
Elasticsearch, Logstash, Kibana (ELK)</td>
<td><p>Shows Elasticsearch, Logstash and Kibana (ELK) being used in a
typical manner to collect, search and monitor/visualize data from a
running application.</p>
<p>This use case builds upon the previous Nodejs/MongoDB 2-tier
application as the one being monitored. The collectd and rsyslog
components are added to both the WebServer and Database tiers which work
to collect data for Logstash.</p>
<p>In addition to the application tiers, a 3<sup>rd</sup> tier is
introduced with Logstash to collect data from the application tiers.
Finally a 4<sup>th</sup> tier is added to search the Logstash data with
Elasticsearch and visualize it using Kibana.</p>
<p><strong><u>Note</u></strong>: This use case also shows the
convenience of using a single YAML macro (declared in the
dsl_definitions section of the TOSCA Service Template) on multiple
Compute nodes.</p></td>
</tr>
<tr class="odd">
<td><a href="#USE_CASE_CONTAINERS_1"><strong>Container-1</strong></a>:
Containers using Docker single Compute instance (Containers only)</td>
<td><p>Minimalist TOSCA Service Template description of 2 Docker
containers linked to each other. Specifically, one container runs
<strong>wordpress</strong> and connects to second <strong>mysql</strong>
database container both on a single server (i.e., Compute instance). The
use case also demonstrates how TOSCA declares and references Docker
images from the Docker Hub repository.</p>
<p><strong><u>Variation 1</u></strong>: Docker Container nodes (only)
providing their Docker Requirements allowing platform (orchestrator) to
select/provide the underlying Docker implementation
(Capability).</p></td>
</tr>
<tr class="even">
<td>Artifacts: Compute Node with multiple artifacts</td>
<td>Illustrates how multiple artifacts for different lifecycle
operations (create, terminate, configure, etc.) can be associated with a
node.</td>
</tr>
</tbody>
</table>

### Compute: Create a single Compute instance with a host Operating System

#### Description

This use case demonstrates how the TOSCA specification can be used to
stand up a single Compute instance with a guest Operating System using a
normative TOSCA Compute node. The TOSCA Compute node is declarative in
that the service template describes both the processor and host
operating system platform characteristics (i.e., properties declared on
the capability named “os” sometimes called a “flavor”) that are desired
by the template author. The cloud provider would attempt to fulfill
these properties (to the best of its abilities) during orchestration.

#### Features

This use case introduces the following TOSCA features:

- A node template that uses the normative TOSCA Compute Node Type along
  with showing an exemplary set of its properties being configured.

- Use of the TOSCA Service Template inputs section to declare a
  configurable value the template user may supply at runtime. In this
  case, the “host” property named “num_cpus” (of type integer) is
  declared.

  - Use of a property constraint to limit the allowed integer values for
    the “num_cpus” property to a specific list supplied in the property
    declaration.

- Use of the TOSCA Service Template outputs section to declare a value
  the template user may request at runtime. In this case, the property
  named “instance_ip” is declared

  - The “instance_ip” output property is programmatically retrieved from
    the Compute node’s “public_address” attribute using the TOSCA
    Service Template-level get_attribute function.

#### Logical Diagram

<img src="media/image24.png" style="width:1.97513in;height:2.8in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA that just defines a single compute instance and selects a (guest) host Operating System from the Compute node’s properties. Note, this example does not include default values on inputs properties.

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]

  node_templates:
    my_server:
      type: Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: {  get_input: cpus  }
            mem_size: 1 GB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: ubuntu
            version: 12.04
  outputs:
    private_ip:
      description: The private IP address of the deployed server instance.
      value: { get_attribute: [my_server, private_address] }
```
#### Notes

- This use case uses a versioned, Linux Ubuntu distribution on the
  Compute node.

### Software Component 1: Automatic deployment of a Virtual Machine (VM) image artifact

#### Description

This use case demonstrates how the TOSCA SoftwareComponent node type can
be used to declare software that is packaged in a standard Virtual
Machine (VM) image file format (i.e., in this case QCOW2) and is hosted
on a TOSCA Compute node (instance). In this variation, the
SoftwareComponent declares a VM image as a deployment artifact that
includes its own pre-packaged operating system and software. The TOSCA
Orchestrator detects this known deployment artifact type on the
SoftwareComponent node template and automatically deploys it to the
Compute node.

#### Features

This use case introduces the following TOSCA features:

- A node template that uses the normative TOSCA SoftwareComponent Node
  Type along with showing an exemplary set of its properties being
  configured.

- Use of the TOSCA Service Template artifacts section to declare a
  Virtual Machine (VM) image artifact type which is referenced by the
  SoftwareComponent node template.

- The VM file format, in this case QCOW2, includes its own guest
  Operating System (OS) and therefore does **<u>not</u>** “require” a
  TOSCA OperatingSystem capability from the TOSCA Compute node.

#### Assumptions

This use case assumes the following:

- That the TOSCA Orchestrator (working with the Cloud provider’s
  underlying management services) is able to instantiate a Compute node
  that has a hypervisor that supports the Virtual Machine (VM) image
  format, in this case QCOW2, which should be compatible with many
  standard hypervisors such as XEN and KVM.

- This is not a “bare metal” use case and assumes the existence of a
  hypervisor on the machine that is allocated to “host” the Compute
  instance supports (e.g. has drivers, etc.) the VM image format in this
  example.

#### Logical Diagram

<img src="media/image25.png" style="width:4.22137in;height:4.00833in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with a SoftwareComponent node with a declared Virtual machine (VM) deployment artifact that automatically deploys to its host Compute node.

topology_template:
  
  node_templates:
    my_virtual_machine:
      type: SoftwareComponent
      artifacts:
        my_vm_image: 
          file: images/fedora-18-x86_64.qcow2
          type: tosca.artifacts.Deployment.Image.VM.QCOW2
          topology: my_VMs_topology.yaml
      requirements:
        - host: my_server
      # Automatically deploy the VM image referenced on the create operation
      interfaces:
        Standard: 
          create: my_vm_image

    # Compute instance with no Operating System guest host
    my_server:
      type: Compute
      capabilities:
        # Note: no guest OperatingSystem requirements as these are in the image.
        host:
          properties:
            disk_size: 10 GB
            num_cpus: {  get_input: cpus  }
            mem_size: 4 GB

  outputs:
    private_ip:
      description: The private IP address of the deployed server instance.
      value: { get_attribute: [my_server, private_address] }
```
#### Notes

- The use of the type keyname on the artifact definition (within the
  my_virtual_machine node template) to declare the ISO image deployment
  artifact type (i.e., tosca.artifacts.Deployment.Image.VM.ISO) is
  redundant since the file extension is “.iso” which associated with
  this known, declared artifact type.

- This use case references a filename on the my_vm_image artifact, which
  indicates a Linux, Fedora 18, x86 VM image, only as one possible
  example.

### Block Storage 1: Using the normative AttachesTo Relationship Type

#### Description

This use case demonstrates how to attach a TOSCA BlockStorage node to a
Compute node using the normative AttachesTo relationship.

#### Logical Diagram

<img src="media/image26.png" style="width:5.21144in;height:3.02413in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with server and attached block storage using the normative AttachesTo Relationship Type.

topology_template:

  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      description: Size of the storage to be created.
      default: 1 GB
    storage_snapshot_id:
      type: string
      description: >
        Optional identifier for an existing snapshot to use when creating storage.    
    storage_location:
      type: string
      description: Block storage mount point (filesystem path).

  node_templates:
    my_server:
      type: Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 1 GB
        os:
          properties:
            architecture: x86_64 
            type: linux  
            distribution: fedora  
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            relationship: 
              type: AttachesTo
              properties:
                location: { get_input: storage_location }

    my_storage:
      type: BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

  outputs:
    private_ip:
      description: The private IP address of the newly created compute instance.
      value: { get_attribute: [my_server, private_address] }
    volume_id:
      description: The volume id of the block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
```
### Block Storage 2: Using a custom AttachesTo Relationship Type

#### Description

This use case demonstrates how to attach a TOSCA BlockStorage node to a
Compute node using a custom RelationshipType that derives from the
normative AttachesTo relationship.

#### Logical Diagram

<img src="media/image27.png" style="width:5.37419in;height:2.8841in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with server and attached block storage using a custom AttachesTo Relationship Type.

relationship_types:
  MyCustomAttachesTo:
     derived_from: AttachesTo

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      description: Size of the storage to be created.
      default: 1 GB
    storage_snapshot_id:
      type: string
      description: >
        Optional identifier for an existing snapshot to use when creating storage.    
    storage_location:
      type: string
      description: Block storage mount point (filesystem path).

  node_templates:
    my_server:
      type: Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4 GB
        os:
          properties:
            architecture: x86_64 
            type: Linux  
            distribution: Fedora  
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            # Declare custom AttachesTo type using the ‘relationship’ keyword
            relationship: 
              type: MyCustomAttachesTo
              properties: 
                location: { get_input: storage_location }
    my_storage:
      type: BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

  outputs:
    private_ip:
      description: The private IP address of the newly created compute instance.
      value: { get_attribute: [my_server, private_address] }
    volume_id:
      description: The volume id of the block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
```
### Block Storage 3: Using a Relationship Template of type AttachesTo

#### Description

This use case demonstrates how to attach a TOSCA BlockStorage node to a
Compute node using a TOSCA Relationship Template that is based upon the
normative AttachesTo Relationship Type.

#### Logical Diagram

<img src="media/image28.png" style="width:5.15551in;height:2.70946in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with server and attached block storage using a named Relationship Template for the storage attachment.

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      description: Size of the storage to be created.
      default: 1 GB
    storage_location:
      type: string
      description: Block storage mount point (filesystem path).

  node_templates:
    my_server:
      type: Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4 GB
        os:
          properties:
            architecture: x86_64 
            type: Linux  
            distribution: Fedora  
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            # Declare template to use with ‘relationship’ keyword
            relationship: storage_attachment

    my_storage:
      type: BlockStorage
      properties:
        size: { get_input: storage_size }

  relationship_templates:
    storage_attachment:
      type: AttachesTo
      properties:
        location: { get_input: storage_location }

  outputs:
    private_ip:
      description: The private IP address of the newly created compute instance.
      value: { get_attribute: [my_server, private_address] }
    volume_id:
      description: The volume id of the block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
```
### Block Storage 4: Single Block Storage shared by 2-Tier Application with custom AttachesTo Type and implied relationships

#### Description

This use case shows 2 compute instances (2 tiers) with one BlockStorage
node, and also uses a custom AttachesTo Relationship that provides a
default mount point (i.e., location) which the 1<sup>st</sup> tier uses,
but the 2<sup>nd</sup> tier provides a different mount point.

Please note that this use case assumes both Compute nodes are accessing
different directories within the shared, block storage node to avoid
collisions.

#### Logical Diagram

<img src="media/image29.png" style="width:5.9474in;height:4.23704in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with a Single Block Storage node shared by 2-Tier Application with custom AttachesTo Type and implied relationships.

relationship_types:
  MyAttachesTo:
    derived_from: tosca.relationships.AttachesTo
    properties: 
      location:
        type: string
        default: /default_location

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      default: 1 GB
      description: Size of the storage to be created.
    storage_snapshot_id:
      type: string
      description: >
        Optional identifier for an existing snapshot to use when creating storage.    

  node_templates:
    my_web_app_tier_1:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            relationship: MyAttachesTo

    my_web_app_tier_2:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            relationship: 
              type: MyAttachesTo
              properties:
                location: /some_other_data_location

    my_storage:
      type: tosca.nodes.Storage.BlockStoragetosca.nodes.Storage.BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

  outputs:
    private_ip_1:
      description: The private IP address of the application’s first tier.
      value: { get_attribute: [my_web_app_tier_1, private_address] }
    private_ip_2:
      description: The private IP address of the application’s second tier.
      value: { get_attribute: [my_web_app_tier_2, private_address] }
    volume_id:
      description: The volume id of the block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
```
### Block Storage 5: Single Block Storage shared by 2-Tier Application with custom AttachesTo Type and explicit Relationship Templates

#### Description

This use case is like the Notation1 use case, but also creates two
relationship templates (one for each tier) each of which provide a
different mount point (i.e., location) which overrides the default
location defined in the custom Relationship Type.

Please note that this use case assumes both Compute nodes are accessing
different directories within the shared, block storage node to avoid
collisions.

#### Logical Diagram

<img src="media/image30.png" style="width:5.19659in;height:3.73611in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with a single Block Storage node shared by 2-Tier Application with custom AttachesTo Type and explicit Relationship Templates.

relationship_types:
  MyAttachesTo:
    derived_from: tosca.relationships.AttachesTo
    properties: 
      location:
        type: string
        default: /default_location

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      default: 1 GB
      description: Size of the storage to be created.
    storage_snapshot_id:
      type: string
      description: >
        Optional identifier for an existing snapshot to use when creating storage.
    storage_location:
      type: string
      description: >
        Block storage mount point (filesystem path).

  node_templates:

    my_web_app_tier_1:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
        - local_storage:
            node: my_storage
            relationship: storage_attachesto_1

    my_web_app_tier_2:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
        - local_storage: 
            node: my_storage
            relationship: storage_attachesto_2

    my_storage:
      type: tosca.nodes.Storage.BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

  relationship_templates:
    storage_attachesto_1:
      type: MyAttachesTo
      properties:
        location: /my_data_location

    storage_attachesto_2:
      type: MyAttachesTo
      properties:
        location: /some_other_data_location
  outputs:
    private_ip_1:
      description: The private IP address of the application’s first tier.
      value: { get_attribute: [my_web_app_tier_1, private_address] }
    private_ip_2:
      description: The private IP address of the application’s second tier.
      value: { get_attribute: [my_web_app_tier_2, private_address] }
    volume_id:
      description: The volume id of the block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
```
### Block Storage 6: Multiple Block Storage attached to different Servers

#### Description

This use case demonstrates how two different TOSCA BlockStorage nodes
can be attached to two different Compute nodes (i.e., servers) each
using the normative AttachesTo relationship.

#### Logical Diagram

<img src="media/image31.png" style="width:4.93864in;height:3.84195in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with 2 servers each with different attached block storage.

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    storage_size:
      type: scalar-unit.size
      default: 1 GB
      description: Size of the storage to be created.
    storage_snapshot_id:
      type: string
      description: >
        Optional identifier for an existing snapshot to use when creating storage.
    storage_location:
      type: string
      description: >
        Block storage mount point (filesystem path).

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
         - local_storage: 
             node: my_storage
             relationship: 
               type: AttachesTo
               properties:
                 location: { get_input: storage_location }
    my_storage:
      type: tosca.nodes.Storage.BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

    my_server2:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: Fedora
            version: 18.0
      requirements:
         - local_storage: 
             node: my_storage2
             relationship: 
               type: AttachesTo
               properties:
                 location: { get_input: storage_location }
    my_storage2:
      type: tosca.nodes.Storage.BlockStorage
      properties:
        size: { get_input: storage_size }
        snapshot_id: { get_input: storage_snapshot_id }

  outputs:
    server_ip_1:
      description: The private IP address of the application’s first server.
      value: { get_attribute: [my_server, private_address] }
    server_ip_2:
      description: The private IP address of the application’s second server.
      value: { get_attribute: [my_server2, private_address] }
    volume_id_1:
      description: The volume id of the first block storage instance.
      value: { get_attribute: [my_storage, volume_id] }
    volume_id_2:
      description: The volume id of the second block storage instance.
      value: { get_attribute: [my_storage2, volume_id] }
```
### Object Storage 1: Creating an Object Storage service

#### Description

#### Logical Diagram

<img src="media/image32.png" style="width:2.23276in;height:1.85in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
    Tosca template for creating an object storage service.

topology_template:
  inputs:
    objectstore_name:
      type: string

  node_templates:
    obj_store_server:
      type: tosca.nodes.Storage.ObjectStorage
      properties:
        name: { get_input: objectstore_name }
        size: 4096 MB
        maxsize: 20 GB
```

### Network 1: Server bound to a new network

#### Description

Introduces the TOSCA Network and Port nodes used for modeling logical
networks using the LinksTo and BindsTo Relationship Types. In this use
case, the template is invoked without an existing network_name as an
input property so a new network is created using the properties declared
in the Network node.

#### Logical Diagram

<img src="media/image33.png" style="width:5.35417in;height:2.97985in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with 1 server bound to a new network

topology_template:

  inputs:
    network_name:
      type: string
      description: Network name

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: 1
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: CirrOS
            version: 0.3.2

    my_network:
      type: tosca.nodes.network.Network
      properties:
        network_name: { get_input: network_name }
        ip_version: 4
        cidr: '192.168.0.0/24'
        start_ip: '192.168.0.50'
        end_ip: '192.168.0.200'
        gateway_ip: '192.168.0.1'

    my_port:
      type: tosca.nodes.network.Port
      requirements:
        - binding: my_server
        - link: my_network
```
### Network 2: Server bound to an existing network

#### Description

This use case shows how to use a network_name as an input parameter to
the template to allow a server to be associated with an existing
network.

#### Logical Diagram

<img src="media/image34.png" style="width:5.30538in;height:2.61111in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with 1 server bound to an existing network

topology_template:
  inputs:
    network_name:
      type: string
      description: Network name

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        host: 
          properties:
            disk_size: 10 GB
            num_cpus: 1
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: CirrOS
            version: 0.3.2

    my_network:
      type: tosca.nodes.network.Network
      properties:
        network_name: { get_input: network_name }

    my_port:
      type: tosca.nodes.network.Port
      requirements:
        - binding:
            node: my_server
        - link:
            node: my_network
```
### Network 3: Two servers bound to a single network

#### Description

This use case shows how two servers (Compute nodes) can be bound to the
same Network (node) using two logical network Ports.

#### Logical Diagram

<img src="media/image35.png" style="width:5.90278in;height:3.46613in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with 2 servers bound to the 1 network

topology_template:

  inputs:
    network_name:
      type: string
      description: Network name
    network_cidr:
      type: string
      default: 10.0.0.0/24
      description: CIDR for the network
    network_start_ip:
      type: string
      default: 10.0.0.100
      description: Start IP for the allocation pool
    network_end_ip:
      type: string
      default: 10.0.0.150
      description: End IP for the allocation pool

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: 1
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: CirrOS
            version: 0.3.2

    my_server2:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: 1
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: CirrOS
            version: 0.3.2

    my_network:
      type: tosca.nodes.network.Network
      properties:
        ip_version: 4
        cidr: { get_input: network_cidr }
        network_name: { get_input: network_name }
        start_ip: { get_input: network_start_ip }
        end_ip: { get_input: network_end_ip }

    my_port:
      type: tosca.nodes.network.Port
      requirements:
        - binding: my_server
        - link: my_network

    my_port2:
      type: tosca.nodes.network.Port
      requirements:
        - binding: my_server2
        - link: my_network
```
### Network 4: Server bound to three networks

#### Description

This use case shows how three logical networks (Network), each with its
own IP address range, can be bound to with the same server (Compute
node).

#### Logical Diagram

<img src="media/image36.png" style="width:5.83333in;height:4.00579in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with 1 server bound to 3 networks

topology_template:

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: 1
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64
            type: Linux
            distribution: CirrOS
            version: 0.3.2

    my_network1:
      type: tosca.nodes.network.Network
      properties:
        cidr: '192.168.1.0/24'
        network_name: net1

    my_network2:
      type: tosca.nodes.network.Network
      properties:
        cidr: '192.168.2.0/24'
        network_name: net2

    my_network3:
      type: tosca.nodes.network.Network
      properties:
        cidr: '192.168.3.0/24'
        network_name: net3

    my_port1:
      type: tosca.nodes.network.Port
      properties:
        order: 0
      requirements:
        - binding: my_server
        - link: my_network1

    my_port2:
      type: tosca.nodes.network.Port
      properties:
        order: 1
      requirements:
        - binding: my_server
        - link: my_network2

    my_port3:
      type: tosca.nodes.network.Port
      properties:
        order: 2
      requirements:
        - binding: my_server
        - link: my_network3
```
### WebServer-DBMS 1: WordPress + MySQL, single instance

#### Description

TOSCA service showing the WordPress web application with a MySQL
database hosted on a single server (instance).

#### Logical Diagram

<img src="media/image37.png" style="width:4.5242in;height:4.64525in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with WordPress, a web server, a MySQL DBMS hosting the application’s database content on the same server. Does not have input defaults or constraints.

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
    db_name:
      type: string
      description: The name of the database.
    db_user:
      type: string
      description: The username of the DB user.
    db_pwd:
      type: string
      description: The WordPress database admin account password.
    db_root_pwd:
      type: string
      description: Root password for MySQL.
    db_port:
      type: PortDef
      description: Port for the MySQL database

  node_templates:
    wordpress:
      type: tosca.nodes.WebApplication.WordPress
      properties: 
        context_root: { get_input: context_root }
      requirements:
        - host: webserver
        - database_endpoint: mysql_database
      interfaces:
        Standard:
          create: wordpress_install.sh
          configure: 
            implementation: wordpress_configure.sh            
            inputs:
              wp_db_name: { get_property: [ mysql_database, name ] }
              wp_db_user: { get_property: [ mysql_database, user ] }
              wp_db_password: { get_property: [ mysql_database, password ] }   
              # In my own template, find requirement/capability, find port property
              wp_db_port: { get_property: [ SELF, database_endpoint, port ] }

    mysql_database:
      type: Database
      properties:
        name: { get_input: db_name } 
        user: { get_input: db_user }
        password: { get_input: db_pwd }
        port: { get_input: db_port }
      capabilities:
        database_endpoint:
          properties:
            port: { get_input: db_port }
      requirements:
        - host: mysql_dbms
      interfaces:
        Standard:
          configure: mysql_database_configure.sh

    mysql_dbms:
      type: DBMS
      properties:
        root_password: { get_input: db_root_pwd }
        port: { get_input: db_port }
      requirements:
        - host: server
      interfaces:
        Standard:              
          inputs:
              db_root_password: { get_property: [ mysql_dbms, root_password ] }
          create: mysql_dbms_install.sh
          start: mysql_dbms_start.sh
          configure: mysql_dbms_configure.sh

    webserver:
      type: WebServer
      requirements:
        - host: server
      interfaces:
        Standard:
          create: webserver_install.sh
          start: webserver_start.sh
	  
    server:
      type: Compute
      capabilities:
        host:
          properties:
            disk_size: 10 GB
            num_cpus: { get_input: cpus }
            mem_size: 4096 MB
        os:
          properties:
            architecture: x86_64 
            type: linux  
            distribution: fedora  
            version: 17.0

  outputs:
    website_url:
      description: URL for Wordpress wiki.
      value: { get_attribute: [server, public_address] }
```
#### Sample scripts

Where the referenced implementation scripts in the example above would
have the following contents

##### wordpress_install.sh
```
yum -y install wordpress
```

##### wordpress_configure.sh
```
sed -i "/Deny from All/d" /etc/httpd/conf.d/wordpress.conf
sed -i "s/Require local/Require all granted/" /etc/httpd/conf.d/wordpress.conf
sed -i s/database_name_here/name/ /etc/wordpress/wp-config.php
sed -i s/username_here/user/ /etc/wordpress/wp-config.php
sed -i s/password_here/password/ /etc/wordpress/wp-config.php
systemctl restart httpd.service
```
##### mysql_database_configure.sh
```
# Setup MySQL root password and create user
cat << EOF | mysql -u root --password=db_root_password
CREATE DATABASE name;
GRANT ALL PRIVILEGES ON name.* TO "user"@"localhost"
IDENTIFIED BY "password";
FLUSH PRIVILEGES;
EXIT
EOF
```
##### mysql_dbms_install.sh
```
yum -y install mysql mysql-server
# Use systemd to start MySQL server at system boot time
systemctl enable mysqld.service
```

##### mysql_dbms_start.sh
```
# Start the MySQL service (NOTE: may already be started at image boot time)
systemctl start mysqld.service
```
##### mysql_dbms_configure
```
# Set the MySQL server root password 
mysqladmin -u root password db_root_password
```

##### webserver_install.sh
```
yum -y install httpd
systemctl enable httpd.service
```
##### webserver_start.sh
```
# Start the httpd service (NOTE: may already be started at image boot time)
systemctl start httpd.service
```
### WebServer-DBMS 2: Nodejs with PayPal Sample App and MongoDB on separate instances 

#### Description

This use case Instantiates a 2-tier application with Nodejs and its
(PayPal sample) WebApplication on one tier which connects a MongoDB
database (which stores its application data) using a ConnectsTo
relationship.

#### Logical Diagram

<img src="media/image38.png" style="width:5.54167in;height:4.46357in" />

#### Sample YAML
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with a nodejs web server hosting a PayPal sample application which connects to a mongodb database.

imports:
  - custom_types/paypalpizzastore_nodejs_app.yaml

dsl_definitions:
    ubuntu_node: &ubuntu_node
      disk_size: 10 GB
      num_cpus: { get_input: my_cpus }
      mem_size: 4096 MB
    os_capabilities: &os_capabilities
      architecture: x86_64
      type: Linux
      distribution: Ubuntu
      version: 14.04

topology_template:
  inputs:
    my_cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
      default: 1
    github_url:
       type: string
       description: The URL to download nodejs.
       default:  https://github.com/sample.git

  node_templates:

    paypal_pizzastore:
      type: tosca.nodes.WebApplication.PayPalPizzaStore
      properties:
          github_url: { get_input: github_url }
      requirements:
        - host:nodejs
        - database_connection: mongo_db
      interfaces:
        Standard:
           configure:
             implementation: scripts/nodejs/configure.sh
             inputs:
               github_url: { get_property: [ SELF, github_url ] }
               mongodb_ip: { get_attribute: [mongo_server, private_address] }
           start: scriptsscripts/nodejs/start.sh
  
    nodejs:
      type: tosca.nodes.WebServer.Nodejs
      requirements:
        - host: app_server
      interfaces:
        Standard:
          create: scripts/nodejs/create.sh

    mongo_db:
      type: tosca.nodes.Database
      requirements:
        - host: mongo_dbms
      interfaces:
        Standard:
         create: create_database.sh

    mongo_dbms:
      type: tosca.nodes.DBMS
      requirements:
        - host: mongo_server
      properties:
        port: 27017
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: mongodb/create.sh
          configure:
            implementation: mongodb/config.sh
            inputs:
              mongodb_ip: { get_attribute: [mongo_server, private_address] }
          start: mongodb/start.sh

    mongo_server:
      type: tosca.nodes.Compute
      capabilities:
        os:
          properties: *os_capabilities
        host:
          properties: *ubuntu_node

    app_server:
      type: tosca.nodes.Compute
      capabilities:
        os:
          properties: *os_capabilities
        host:
          properties: *ubuntu_node

  outputs:
    nodejs_url:
      description: URL for the nodejs server, http://<IP>:3000
      value: { get_attribute: [app_server, private_address] }
    mongodb_url:
      description: URL for the mongodb server.
      value: { get_attribute: [ mongo_server, private_address ] }
```
#### Notes:

- Scripts referenced in this example are assumed to be placed by the
  TOSCA orchestrator in the relative directory declared in TOSCA.meta of
  the TOSCA CSAR file.

### Multi-Tier-1: Elasticsearch, Logstash, Kibana (ELK) use case with multiple instances

#### Description

TOSCA service showing the Nodejs, MongoDB, Elasticsearch, Logstash,
Kibana, rsyslog and collectd installed on a different server (instance).

This use case also demonstrates:

- Use of TOSCA macros or dsl_definitions

- Multiple SoftwareComponents hosted on same Compute node

- Multiple tiers communicating to each other over ConnectsTo using
  Configure interface.

#### Logical Diagram

<img src="media/image39.png" style="width:6.5in;height:3.50417in" />

#### Sample YAML

##### Master Service Template application (Entry-Definitions)

TheThe following YAML is the primary template (i.e., the
Entry-Definition) for the overall use case. The imported YAML for the
various subcomponents are not shown here for brevity.
```
tosca_definitions_version: tosca_2_0

description: >
  This TOSCA deploys nodejs, mongodb, elasticsearch, logstash and kibana each on a separate server with monitoring enabled for nodejs server where a sample nodejs application is running. The syslog and collectd are installed on a nodejs server.

imports:
  - paypalpizzastore_nodejs_app.yaml
  - elasticsearch.yaml
  - logstash.yaml
  - kibana.yaml
  - collectd.yaml
  - rsyslog.yaml

dsl_definitions:
    host_capabilities: &host_capabilities
      # container properties (flavor)
      disk_size: 10 GB
      num_cpus: { get_input: my_cpus }
      mem_size: 4096 MB
    os_capabilities: &os_capabilities
      architecture: x86_64
      type: Linux
      distribution: Ubuntu
      version: 14.04

topology_template:
  inputs:
    my_cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]
    github_url:
       type: string
       description: The URL to download nodejs.
       default: https://github.com/sample.git
  
  node_templates:
    paypal_pizzastore:
      type: tosca.nodes.WebApplication.PayPalPizzaStore
      properties:
          github_url: { get_input: github_url }
      requirements:
        - host: nodejs
        - database_connection: mongo_db
      interfaces:
        Standard:
           configure:
             implementation: scripts/nodejs/configure.sh
             inputs:
               github_url: { get_property: [ SELF, github_url ] }
               mongodb_ip: { get_attribute: [mongo_server, private_address] }
           start: scripts/nodejs/start.sh
  
    nodejs:
      type: tosca.nodes.WebServer.Nodejs
      requirements:
        - host: app_server
      interfaces:
        Standard:
          create: scripts/nodejs/create.sh

    mongo_db:
      type: tosca.nodes.Database
      requirements:
        - host: mongo_dbms
      interfaces:
        Standard:
         create: create_database.sh

    mongo_dbms:
      type: tosca.nodes.DBMS
      requirements:
        - host: mongo_server
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/mongodb/create.sh
          configure: 
            implementation: scripts/mongodb/config.sh
            inputs: 
              mongodb_ip: { get_attribute: [mongo_server, ip_address] }
          start: scripts/mongodb/start.sh

    elasticsearch:
      type: tosca.nodes.SoftwareComponent.Elasticsearch
      requirements:
        - host: elasticsearch_server
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/elasticsearch/create.sh
          start: scripts/elasticsearch/start.sh
    logstash:
      type: tosca.nodes.SoftwareComponent.Logstash
      requirements:
        - host: logstash_server
        - search_endpoint: elasticsearch
          interfaces:
            tosca.interfaces.relationship.Configure:
              pre_configure_source:
                implementation: python/logstash/configure_elasticsearch.py
                input:
                  elasticsearch_ip: { get_attribute: [elasticsearch_server, ip_address] }
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/lostash/create.sh
          configure: scripts/logstash/config.sh
          start: scripts/logstash/start.sh

    kibana:
      type: tosca.nodes.SoftwareComponent.Kibana
      requirements:
        - host: kibana_server
        - search_endpoint: elasticsearch
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/kibana/create.sh
          configure:
            implementation: scripts/kibana/config.sh
            input:
              elasticsearch_ip: { get_attribute: [elasticsearch_server, ip_address] }
              kibana_ip: { get_attribute: [kibana_server, ip_address] }
          start: scripts/kibana/start.sh

    app_collectd:
      type: tosca.nodes.SoftwareComponent.Collectd
      requirements:
        - host: app_server
        - collectd_endpoint: logstash
          interfaces:
            tosca.interfaces.relationship.Configure:
              pre_configure_target:
                implementation: python/logstash/configure_collectd.py
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/collectd/create.sh
          configure:
            implementation: python/collectd/config.py
            input:
              logstash_ip: { get_attribute: [logstash_server, ip_address] }
          start: scripts/collectd/start.sh

    app_rsyslog:
      type: tosca.nodes.SoftwareComponent.Rsyslog
      requirements:
        - host: app_server
        - rsyslog_endpoint: logstash
          interfaces:
            tosca.interfaces.relationship.Configure:
              pre_configure_target:
                implementation: python/logstash/configure_rsyslog.py
      interfaces:
        tosca.interfaces.node.lifecycle.Standard:
          create: scripts/rsyslog/create.sh
          configure:
            implementation: scripts/rsyslog/config.sh
            input:
              logstash_ip: { get_attribute: [logstash_server, ip_address] }
          start: scripts/rsyslog/start.sh

    app_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties: *host_capabilities
        os:
          properties: *os_capabilities

    mongo_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties: *host_capabilities
        os:
          properties: *os_capabilities

    elasticsearch_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties: *host_capabilities
        os:
          properties: *os_capabilities

    logstash_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties: *host_capabilities
        os:
          properties: *os_capabilities

    kibana_server:
      type: tosca.nodes.Compute
      capabilities:
        host:
          properties: *host_capabilities
        os:
          properties: *os_capabilities

  outputs:
    nodejs_url:
      description: URL for the nodejs server.
      value: { get_attribute: [ app_server, private_address ] }
    mongodb_url:
      description: URL for the mongodb server.
      value: { get_attribute: [ mongo_server, private_address ] }
    elasticsearch_url:
      description: URL for the elasticsearch server.
      value: { get_attribute: [ elasticsearch_server, private_address ] }
    logstash_url:
      description: URL for the logstash server.
      value: { get_attribute: [ logstash_server, private_address ] }
    kibana_url:
      description: URL for the kibana server.
      value: { get_attribute: [ kibana_server, private_address ] }
```
#### Sample scripts

Where the referenced implementation scripts in the example above would
have the following contents

### Container-1: Containers using Docker single Compute instance (Containers only)

#### Description

This use case shows a minimal description of two Container nodes (only)
providing their Docker Requirements allowing platform (orchestrator) to
select/provide the underlying Docker implementation (Capability).
Specifically, wordpress and mysql Docker images are referenced from
Docker Hub.

This use case also demonstrates:

- Abstract description of Requirements (i.e., Container and Docker)
  allowing platform to dynamically select the appropriate runtime
  Capabilities that match.

- Use of external repository (Docker Hub) to reference image artifact.

#### Logical Diagram

<img src="media/image40.png" style="width:5.38958in;height:3.18958in" />

#### Sample YAML

#####  Two Docker “Container” nodes (Only) with Docker Requirements 
```
tosca_definitions_version: tosca_2_0

description: >
  TOSCA with wordpress, web server and mysql on the same server.

# Repositories to retrieve code artifacts from 
repositories:
  docker_hub: https://registry.hub.docker.com/

topology_template:

  inputs:
    wp_host_port:
      type: integer
      description: The host port that maps to port 80 of the WordPress container.
    db_root_pwd:
      type: string
      description: Root password for MySQL.

  node_templates:
    # The MYSQL container based on official MySQL image in Docker hub
    mysql_container:
      type: tosca.nodes.Container.Application.Docker
      capabilities:
        # This is a capability that would mimic the Docker –link feature
        database_link: tosca.capabilities.Docker.Link
      artifacts:
        my_image: 
          file: mysql
          type: tosca.artifacts.Deployment.Image.Container.Docker
          repository: docker_hub
      interfaces:
        Standard:
          create:
            implementation: my_image
            inputs:
              db_root_password: { get_input: db_root_pwd }

    # The WordPress container based on official WordPress image in Docker hub
    wordpress_container:
      type: tosca.nodes.Container.Application.Docker
      requirements:
        - database_link: mysql_container
      artifacts:
        my_image: 
          file: wordpress
          type: tosca.artifacts.Deployment.Image.Container.Docker
          repository: docker_hub
          <metadata-link> : <topology_artifact_name> # defined outside and linked to from here
      interfaces:
        Standard:
          create:
            implementation: my_image
            inputs:
              host_port: { get_input: wp_host_port }
```
### Artifacts: Compute Node with Multiple Artifacts

#### Description

This use case illustrates how multiple artifacts can be associated with
a node for different lifecycle operations of a node (create, terminate,
configure, etc.)

#### Sample YAML
```
tosca_definitions_version: tosca_2_0
description: Sample tosca archive to illustrate use of a node with multiple artifacts for different life cycle operations of the node

topology_template :

  node_templates :
    dbServer:
      type: tosca.nodes.Compute
      properties:
        name: dbServer
        description:  
        artifacts:
          - sw_image:
              type: tosca.artifacts.Deployment.SwImage
              file: http://1.1.1.1/images/ubuntu-14.04.qcow2
              name: ubuntu-14.04
              version: 14.04
              checksum: e5c1e205f62f3 

         - configuration:
             type: tosca.artifacts.Implementation.Ansible
             file: implementation/configuration/Ansible/configure.yml
             version: 2.0

        - terminate:
            type: tosca.artifacts.Implementation.scripts
            file: implementation/configuration/scripts/terminate.sh
            version: 6.2
```

# TOSCA networking use cases

Except for the examples, this section is **normative** and describes how
to express and control the application centric network semantics
available in TOSCA.

## Networking and Service Template Portability

TOSCA Service Templates are application centric in the sense that they
focus on describing application components in terms of their
requirements and interrelationships. In order to provide cloud
portability, it is important that a TOSCA Service Template avoid cloud
specific requirements and details. However, at the same time, TOSCA must
provide the expressiveness to control the mapping of software component
connectivity to the network constructs of the hosting cloud.

TOSCA Networking takes the following approach.

1.  The application component connectivity semantics and expressed in
    terms of Requirements and Capabilities and the relationships between
    these. Service Template authors are able to express the
    interconnectivity requirements of their software components in an
    abstract, declarative, and thus highly portable manner.

2.  The information provided in TOSCA is complete enough for a TOSCA
    implementation to fulfill the application component network
    requirements declaratively (i.e., it contains information such as
    communication initiation and layer 4 port specifications) so that
    the required network semantics can be realized on arbitrary network
    infrastructures.

3.  TOSCA Networking provides full control of the mapping of software
    component interconnectivity to the networking constructs of the
    hosting cloud network independently of the Service Template,
    providing the required separation between application and network
    semantics to preserve Service Template portability.

4.  Service Template authors have the choice of specifying application
    component networking requirements in the Service Template or
    completely separating the application component to network mapping
    into a separate document. This allows application components with
    explicit network requirements to express them while allowing users
    to control the complete mapping for all software components which
    may not have specific requirements. Usage of these two approaches is
    possible simultaneously and required to avoid having to re-write
    components network semantics as arbitrary sets of components are
    assembled into Service Templates.

5.  Defining a set of network semantics which are expressive enough to
    address the most common application connectivity requirements while
    avoiding dependencies on specific network technologies and
    constructs. Service Template authors and cloud providers are able to
    express unique/non-portable semantics by defining their own
    specialized network Requirements and Capabilities.

## Connectivity semantics

TOSCA’s application centric approach includes the modeling of network
connectivity semantics from an application component connectivity
perspective. The basic premise is that applications contain components
which need to communicate with other components using one or more
endpoints over a network stack such as TCP/IP, where connectivity
between two components is expressed as a \<source component, source
address, source port, target component, target address, target port\>
tuple. Note that source and target components are added to the
traditional 4 tuple to provide the application centric information,
mapping the network to the source or target component involved in the
connectivity.

Software components are expressed as Node Types in TOSCA which can
express virtually any kind of concept in a TOSCA model. Node Types
offering network based functions can model their connectivity using a
special Endpoint Capability,
[tosca.capabilities.Endpoint](#tosca.capabilities.endpoint), designed
for this purpose. Node Types which require an Endpoint can specify this
as a TOSCA requirement. A special Relationship Type,
tosca.relationships.ConnectsTo, is used to implicitly or explicitly
relate the source Node Type’s endpoint to the required endpoint in the
target node type. Since tosca.capabilities.Endpoint and
tosca.relationships.ConnectsTo are TOSCA types, they can be used in
templates and extended by subclassing in the usual ways, thus allowing
the expression of additional semantics as needed.

<img src="media/image41.png" style="width:6.06944in;height:2.60833in" />The
following diagram shows how the TOSCA node, capability and relationship
types enable modeling the application layer decoupled from the network
model intersecting at the Compute node using the
[Bindable](#tosca.capabilities.network.bindable) capability type.

As you can see, the Port node type effectively acts a broker node
between the Network node description and a host Compute node of an
application.

## Expressing connectivity semantics

This section describes how TOSCA supports the typical client/server and
group communication semantics found in application architectures.

### Connection initiation semantics

The tosca.relationships.ConnectsTo expresses that requirement that a
source application component needs to be able to communicate with a
target software component to consume the services of the target.
ConnectTo is a component interdependency semantic in the most general
sense and does not try imply how the communication between the source
and target components is physically realized.

Application component intercommunication typically has conventions
regarding which component(s) initiate the communication. Connection
initiation semantics are specified in
[tosca.capabilities.Endpoint](#tosca.capabilities.endpoint). Endpoints
at each end of the
[tosca.relationships.ConnectsTo](#tosca.relationships.connectsto-1) must
indicate identical connection initiation semantics.

The following sections describe the normative connection initiation
semantics for the tosca.relationships.ConnectsTo Relationship Type.

#### Source to Target

The Source to Target communication initiation semantic is the most
common case where the source component initiates communication with the
target component in order to fulfill an instance of the
tosca.relationships.ConnectsTo relationship. The typical case is a
“client” component connecting to a “server” component where the client
initiates a stream oriented connection to a pre-defined transport
specific port or set of ports.

It is the responsibility of the TOSCA implementation to ensure the
source component has a suitable network path to the target component and
that the ports specified in the respective
[tosca.capabilities.Endpoint](#tosca.capabilities.endpoint) are not
blocked. The TOSCA implementation may only represent state of the
tosca.relationships.ConnectsTo relationship as fulfilled after the
actual network communication is enabled and the source and target
components are in their operational states.

Note that the connection initiation semantic only impacts the
fulfillment of the actual connectivity and does not impact the node
traversal order implied by the tosca.relationships.ConnectsTo
Relationship Type.

#### Target to Source

The Target to Source communication initiation semantic is a less common
case where the target component initiates communication with the source
comment in order to fulfill an instance of the
tosca.relationships.ConnectsTo relationship. This “reverse” connection
initiation direction is typically required due to some technical
requirements of the components or protocols involved, such as the
requirement that SSH mush only be initiated from target component in
order to fulfill the services required by the source component.

It is the responsibility of the TOSCA implementation to ensure the
source component has a suitable network path to the target component and
that the ports specified in the respective tosca.capabilities.Endpoint
are not blocked. The TOSCA implementation may only represent state of
the tosca.relationships.ConnectsTo relationship as fulfilled after the
actual network communication is enabled and the source and target
components are in their operational states.

Note that the connection initiation semantic only impacts the
fulfillment of the actual connectivity and does not impact the node
traversal order implied by the tosca.relationships.ConnectsTo
Relationship Type.

#### Peer-to-Peer

The Peer-to-Peer communication initiation semantic allows any member of
a group to initiate communication with any other member of the same
group at any time. This semantic typically appears in clustering and
distributed services where there is redundancy of components or
services.

It is the responsibility of the TOSCA implementation to ensure the
source component has a suitable network path between all the member
component instances and that the ports specified in the respective
tosca.capabilities.Endpoint are not blocked, and the appropriate
multicast communication, if necessary, enabled. The TOSCA implementation
may only represent state of the tosca.relationships.ConnectsTo
relationship as fulfilled after the actual network communication is
enabled such that at least one-member component of the group may reach
any other member component of the group.

Endpoints specifying the Peer-to-Peer initiation semantic need not be
related with a tosca.relationships.ConnectsTo relationship for the
common case where the same set of component instances must communicate
with each other.

Note that the connection initiation semantic only impacts the
fulfillment of the actual connectivity and does not impact the node
traversal order implied by the tosca.relationships.ConnectsTo
Relationship Type.

### Specifying layer 4 ports

TOSCA Service Templates must express enough details about application
component intercommunication to enable TOSCA implementations to fulfill
these communication semantics in the network infrastructure. TOSCA
currently focuses on TCP/IP as this is the most pervasive in today’s
cloud infrastructures. The layer 4 ports required for application
component intercommunication are specified in
tosca.capabilities.Endpoint. The union of the port specifications of
both the source and target tosca.capabilities.Endpoint which are part of
the tosca.relationships.ConnectsTo Relationship Template are interpreted
as the effective set of ports which must be allowed in the network
communication.

The meaning of Source and Target port(s) corresponds to the direction of
the respective tosca.relationships.ConnectsTo.

## Network provisioning

### Declarative network provisioning

TOSCA orchestrators are responsible for the provisioning of the network
connectivity for declarative TOSCA Service Templates (Declarative TOSCA
Service Templates don’t contain explicit plans). This means that the
TOSCA orchestrator must be able to infer a suitable logical connectivity
model from the Service Template and then decide how to provision the
logical connectivity, referred to as “fulfillment”, on the available
underlying infrastructure. In order to enable fulfillment, sufficient
technical details still must be specified, such as the required
protocols, ports and QOS information. TOSCA connectivity types, such as
tosca.capabilities.Endpoint, provide well defined means to express these
details.

### Implicit network fulfillment

TOSCA Service Templates are by default network agnostic. TOSCA’s
application centric approach only requires that a TOSCA Service Template
contain enough information for a TOSCA orchestrator to infer suitable
network connectivity to meet the needs of the application components.
Thus Service Template designers are not required to be aware of or
provide specific requirements for underlying networks. This approach
yields the most portable Service Templates, allowing them to be deployed
into any infrastructure which can provide the necessary component
interconnectivity.

### Controlling network fulfillment

TOSCA provides mechanisms for providing control over network
fulfillment.

This mechanism allows the application network designer to express in
service template or network template how the networks should be
provisioned.

For the use cases described below let’s assume we have a typical 3-tier
application which is consisting of FE (frontend), BE (backend) and DB
(database) tiers. The simple application topology diagram can be shown
below:

<img src="media/image42.emf" style="width:1.92569in;height:3.39792in" />

<img src="media/image42.emf" style="width:1.92569in;height:3.39792in" />

Figure‑5: Typical 3-Tier Network

#### Use case: OAM Network

When deploying an application in service provider’s on-premise cloud,
it’s very common that one or more of the application’s services should
be accessible from an ad-hoc OAM (Operations, Administration and
Management) network which exists in the service provider backbone.

As an application network designer, I’d like to express in my TOSCA
network template (which corresponds to my TOSCA service template) the
network CIDR block, start ip, end ip and segmentation ID (e.g. VLAN id).

The diagram below depicts a typical 3-tiers application with specific
networking requirements for its FE tier server cluster:

<img src="media/image43.emf" style="width:4.44444in;height:4.98125in" />

#### Use case: Data Traffic network

The diagram below defines a set of networking requirements for the
backend and DB tiers of the 3-tier app mentioned above.

<img src="media/image44.emf" style="width:4.97222in;height:4.13889in" />

#### Use case: Bring my own DHCP

The same 3-tier app requires for its admin traffic network to manage the
IP allocation by its own DHCP which runs autonomously as part of
application domain.

For this purpose, the app network designer would like to express in
TOSCA that the underlying provisioned network will be set with
DHCP_ENABLED=false. See this illustrated in the figure below:

<img src="media/image45.emf" style="width:5.86111in;height:4.88889in" />



## Network modeling approaches

### Option 1: Specifying a network outside the application’s Service Template

This approach allows someone who understands the application’s
networking requirements, mapping the details of the underlying network
to the appropriate node templates in the application.

The motivation for this approach is providing the application network
designer a fine-grained control on how networks are provisioned and
stitched to its application by the TOSCA orchestrator and underlying
cloud infrastructure while still preserving the portability of his
service template. Preserving the portability means here not doing any
modification in service template but just “plug-in” the desired network
modeling. The network modeling can reside in the same service template
file but the best practice should be placing it in a separated
self-contained network template file.

This “pluggable” network template approach introduces a new normative
node type called Port, capability called
[tosca.capabilities.network.Linkable](#DEFN_TYPE_CAPABILITIES_NETWORK_LINKABLE)
and relationship type called
[tosca.relationships.network.LinksTo](#DEFN_TYPE_RELATIONSHIPS_NETWORK_LINKSTO).

The idea of the Port is to elegantly associate the desired compute nodes
with the desired network nodes while not “touching” the compute itself.

The following diagram series demonstrate the plug-ability strength of
this approach.

Let’s assume an application designer has modeled a service template as
shown in Figure 1 that describes the application topology nodes
(compute, storage, software components, etc.) with their relationships.
The designer ideally wants to preserve this service template and use it
in any cloud provider environment without any change.

Figure‑6: Generic Service Template

When the application designer comes to consider its application
networking requirement they typically call the network
architect/designer from their company (who has the correct expertise).

The network designer, after understanding the application connectivity
requirements and optionally the target cloud provider environment, is
able to model the network template and plug it to the service template
as shown in Figure 2:

Figure‑7: Service template with network template A

When there’s a new target cloud environment to run the application on,
the network designer is simply creates a new network template B that
corresponds to the new environmental conditions and provide it to the
application designer which packs it into the application CSAR.

Figure‑8: Service template with network template B

The node templates for these three networks would be defined as follows:
```
node_templates:
  frontend:
    type: tosca.nodes.Compute
    properties: # omitted for brevity

  backend:
    type: tosca.nodes.Compute
    properties: # omitted for brevity

  database:
    type: tosca.nodes.Compute
    properties: # omitted for brevity

  oam_network:
    type: tosca.nodes.network.Network
    properties: # omitted for brevity 

  admin_network:
    type: tosca.nodes.network.Network
    properties: # omitted for brevity  

  data_network:
    type: tosca.nodes.network.Network
    properties: # omitted for brevity 
  
  # ports definition
  fe_oam_net_port:
    type: tosca.nodes.network.Port
    properties:
      is_default: true
      ip_range_start: { get_input: fe_oam_net_ip_range_start }
      ip_range_end: { get_input: fe_oam_net_ip_range_end } 
    requirements:
      - link: oam_network 
      - binding: frontend
      
  fe_admin_net_port:
    type: tosca.nodes.network.Port
    requirements:
      - link: admin_network 
      - binding: frontend
      
  be_admin_net_port:
    type: tosca.nodes.network.Port
    properties:
       order: 0
    requirements:
      - link: admin_network 
      - binding: backend
      
  be_data_net_port:
    type: tosca.nodes.network.Port
    properties:
       order: 1
    requirements:
      - link: data_network 
      - binding: backend

  db_data_net_port:
    type: tosca.nodes.network.Port
    requirements:      
      - link: data_network
      - binding: database
```
### Option 2: Specifying network requirements within the application’s Service Template

This approach allows the Service Template designer to map an endpoint to
a logical network.

The use case shown below examines a way to express in the TOSCA YAML
service template a typical 3-tier application with their required
networking modeling:
```
node_templates:
  frontend:
    type: tosca.nodes.Compute
    properties: # omitted for brevity
    requirements:
      - network_oam: oam_network
      - network_admin: admin_network
  backend:
    type: tosca.nodes.Compute
    properties: # omitted for brevity
    requirements:
      - network_admin: admin_network 
      - network_data: data_network

  database:
    type: tosca.nodes.Compute
    properties: # omitted for brevity
    requirements:
      - network_data: data_network 

  oam_network:
    type: tosca.nodes.network.Network
    properties:
      ip_version:  { get_input: oam_network_ip_version } 
      cidr: { get_input: oam_network_cidr }
      start_ip: { get_input: oam_network_start_ip }
      end_ip: { get_input: oam_network_end_ip }

  admin_network:
    type: tosca.nodes.network.Network
    properties:
      ip_version:  { get_input: admin_network_ip_version } 
      dhcp_enabled: { get_input: admin_network_dhcp_enabled }  

  data_network:
    type: tosca.nodes.network.Network
    properties:
	ip_version:  { get_input: data_network_ip_version } 
       cidr: { get_input: data_network_cidr } 
```
# TOSCA Orchestrators

Discuss the following:

- Orchestrator components

- Service template catalog

- Inventory

<!-- -->

- o Available (for “onboarded resources”)

- o Active (for “instance model”)

<!-- -->

- Workflow engine

- Policy engine

- Artifact processors

- Onboarding service templates

- Orchestration steps

- Portable artifact processing

- Orchestrator APIs/Interfaces

- Which workflows to invoke?

## Artifact Processing and creating Portable Service Templates

TOSCA’s declarative modelling includes features that allow service
designers to model abstract components without having to specify
concrete implementations for these components. Declarative modeling is
made possible through the use of standardized TOSCA types. Any
TOSCA-compliant orchestrator is expected to know how to deploy these
standard types. Declarative modeling ensures optimal portability of
service templates, since any cloud-specific or technology specific
implementation logic is provided by the TOSCA orchestrator, not by the
service template.

The examples in the previous chapter also demonstrate how TOSCA allows
service designers to extend built-in orchestrator behavior in a number
of ways:

- Service designers can override or extend behavior of built-in types by
  supplying service-specific implementations of lifecycle interface
  operations in their node templates.

- Service designers can create entirely new types that define custom
  implementations of standard lifecycle interfaces.

Implementations of Interface operations are provided through artifacts.
The examples in the previous chapter showed shell script artifacts, but
many other types of artifacts can be used as well. The use of artifacts
in TOSCA service templates breaks pure declarative behavior since
artifacts effectively contain “imperative logic” that is opaque to the
orchestrator. This introduces the risk of non-portable templates. Since
some artifacts may have dependencies on specific technologies or
infrastructure component, the use of artifacts could result in service
templates that cannot be used on all cloud infrastructures.

The goal of this **non-normative** chapter is to ensure portable and
interoperable use of artifacts by providing a detailed description of
how TOSCA orchestrators process artifacts, by illustrating how a number
of standard TOSCA artifact types are expected to be processed, and by
describing TOSCA language features that allow artifact to provide
metadata containing artifact-specific processing instructions. These
metadata around the artifact allow the orchestrator to make descisions
on the correct Artifact Processor and runtime(s) needed to execute. The
sole purpose of this chapter is to show TOSCA template designers how to
best leverage built-in TOSCA capabilities. It is not intended to
recommend specific orchestrator implementations.

### CSAR Onboarding 

This section is **non-normative** and outlines various options to
distribute artifacts to artifact processors as a part of CSAR
on-boarding.

CSAR On-boarding refers to the process of

- Creating a CSAR and its contents

- Submitting the CSAR to the Orchestrator to be included in the
  catalogue

- Uploading CSAR to Orchestrator

- Processing of CSAR by the Orchestrator

#### How is on-boarding done

<img src="media/image58.png" style="width:6.5in;height:2.33472in" />

CSAR on-boarding is achieved through the following steps:

8.  Request for uploading a CSAR is received by the Orchestrator

9.  Orchestrator verifies integrity of package

10. Orchestrator re-directs request with CSAR to Catalogue

11. Catalogue receives CSAR and reads the Package content

12. Catalogue validates the CSAR

The orchestrator distributes artifacts to artifact processors from
Catalogue

#### Artifact Distribution

Artifacts can be distributed to artifact processors through the
following mechanisms:

1.  *Synchronous on-*boarding: During onboarding, Orchestrator
    forcefully pushes artifacts to artifacts processor and waits for
    success response, marks onboarding operation as successful only
    after a success response is received from artifact processor.

<!-- -->

13. *Asynchronous on-boarding*: Orchestrator notifies artifact
    processors and lets artifact processors pull artifacts

14. Do not distribute artifacts during onboarding, let artifact
    processors pull them from CSAR catalogue when they are called to
    execute the artifact

***Note***: Disabling artifact validation during onboarding opens up
possibilities of failures during deployment of CSAR in to the cloud

#### Why is on-boarding needed

On-boarding eases deployment and reduces the first time instantiation of
cloud applications. It helps validation and detection of errors early,
prior to deployment.

### Artifacts Processing

Artifacts represent the content needed to realize a deployment or
implement a specific management action.

Artifacts can be of many different types. Artifacts could be executables
(such as scripts or executable program files) or pieces of data required
by those executables (e.g. configuration files, software libraries,
license keys, etc). Implementations for some operations may require the
use of multiple artifacts.

Different types of artifacts may require different mechanisms for
processing the artifact. However, the sequence of steps taken by an
orchestrator to process an artifcat is generally the same for all types
of artifacts:

#### Identify Artifact Processor

The first step is to identify an appropriate processor for the specified
artifact. A processor is any executable that knows how to process the
artifact in order to achieve the intended management operation. This
processor could be an interpreter for executable shell scripts or
scripts written in Python. It could be a tool such as Ansible, Puppet,
or Chef for playbook, manifest, or recipe artifacts, or it could be a
container management or cloud management system for image artifacts such
as container images or virtual machine images.

TOSCA includes a number of standard artifact types. Standard-compliant
TOSCA orchestrators are expected to include processors for each of these
types. For each type, there is a correspondent Artifact Processor that
is responsible for processing artifacts of that type.

Note that aside from selecting the proper artifact processor, it may
also be important to use the proper version of the processor. For
example, some python scripts may require Python 2.7 whereas other
scripts may require Python 3.4. TOSCA provides metadata to describe
service template-specific parameters for the Artifact Processor. In
addition to specifying specific versions, those metadata could also
identify repositories from which to retrieve the artifact processor.

Some templates may require the use of custom Artifact Processors, for
example to process non-standard artifacts or to provide a custom
Artifact Processor for standard artifact types. For such cases, TOSCA
allows service template designers to define Application Processors in
service templates as a top-level entity. Alternatively, service template
designers can also provide their own artifact processor by providing
wrapper artifacts of a supported type. These wrapper artifacts could be
shell scripts, python scripts, or artifacts of any other standard type
that know how process or invoke the custom artifact.

#### Establish an Execution Environment

The second step is to identify or create a proper execution environment
within which to run the artifact processor. There are generally three
options for where to run artifact processors :

1.  One option is to execute the artifact processor in the topology that
    is being orchestrated, for example on a Compute node created by the
    orchestrator.

- A second option is to process the artifact in the same environment in
  which the orchestrator is running (although for security reasons,
  orchestrators may create sandboxes that shield the orchestrator from
  faulty or malicious artifacts).

- The third option is to process the script in a management environment
  that is external to both the orchestrator and the topology being
  orchestrated. This might be the preferred option for scenarios where
  the environment already exists, but it is also possible for
  orchestrators to create external execution environments.

It is often possible for the orchestrator to determine the intended
execution environment based on the type of the artifact as well as on
the topology context in which the the artifact was specified. For
example, shell script artifacts associated with software components
typically contain the install script that needs to be executed on the
software component’s host node in order to install that software
component. However, other scripts may not need to be run inside the
topology being orchestrated. For example, a script that creates a
database on a database management system could run on the compute node
that hosts the database management system, or it could run in the
orchestrator environment and communicate with the DBMS across a
management network connection.

Similarly, there may be multiple options for other types of artifacts as
well. For example, puppet artifacts could get processed locally by a
puppet agent running on a compute node in the topology, or they could
get passed to a puppet master that is external to both the orchestrator
and the topology.

Different orchestrators could make different decisions about the
execution environments for various combinations of node types and
artifact types. However, service template designers must have the
ability to specify explicitly where artifacts are intended to be
processed in those scneario where correct operation depends on using a
specific execution environment.

Need discussion on how this is done.

#### Configure Artifact Processor User Account

An artifact processor may need to run using a specific user account in
the execution environment to ensure that the processor has the proper
permissions to execute the required actions. Depending on the artifact,
existing user accounts might get used, or the orchestrator might have to
create a new user account specifically for the artifact processor. If
new user accounts are needed, the orchestrator may also have to create a
home directory for those users.

Depending on the security mechanisms used in the execution environment,
it may also be necessary to add user accounts to specific groups, or to
assign specific roles to the user account.

#### Deploy Artifact Processor

Once the orchestrator has identified the artifact processor as well as
the execution environment, it must make sure that the artifact processor
is deployed in the execution environment:

If the orchestrator’s own environment acts as the execution environment
for the artifact processor, orchestrator implementors can make sure that
a standard set of artifact processors is pre-installed in that
environment, and nothing further may need to be done.

When a Compute node in the orchestrated topology is selected as the
execution environment, typically only the most basic processors (such as
bash shells) are pre-installed on that compute node. All other execution
processors need to be installed on that compute node by the
orchestrator.

When an external execution environment is specified, the orchestrator
must at the very least be able to verify that the proper artifact
processor is present in the external execution environment and generate
an error if it isn’t. Ideally, the orchestrator should be able to
install the processor if necessary.

The orchestrator may also take the necessary steps to make sure the
processor is run as a specific user in the execution environment.

#### Deploy Dependencies

The imperative logic contained in artifacts may in turn install or
configure software components that are not part of the service topology,
and as a result are opaque to the orchestrator. This means that the
orchestrator cannot reflect these components in an instance model, which
also means they cannot be managed by the orchestrator.

It is best practice to avoid this situation by explicitly modeling any
dependent components that are required by an artifact processor. When
deploying the artifact processor, the orchestrator can then deploy or
configure these dependencies in the execution environment and reflect
them in an instance model as appropriate.

For artifacts that require dependencies to to be installed, TOSCA
provides a generic way in which to describe those dependencies, which
will avoid the use of monolithic scripts.

Examples of dependent components include the following :

Some executables may have dependencies on software libraries. For tools
like Python, required libraries might be specified in a requirements.txt
file and deployed into a virtual environment.

Environment variables may need to be set.

Configuration files may need to be created with proper settings for the
artifact processor. For example, configuration settings could include
DNS names (or IP addresses) for contacting a Puppet Master or Chef
Server.

Artifact processors may require valid software licenses in order to run.

Other artifacts specified in the template may need to be deposited into
the execution environment.

#### Identify Target

Orchestrators must pass information to the artifact processor that
properly identifies the target for each artifact being processed.

In many cases, the target is the Compute node that acts as the host for
the node being created or configured. If that Compute node also acts as
the execution environment for the artifact processor, the target for the
artifacts being processed is the Compute node itself. If that scenario,
there is no need for the orchestrator to pass additional target
information aside from specifying that all actions are intended to be
applied locally.

When artifact processors run externally to the topology being deployed,
they must establish a connection across a management network to the
target. In TOSCA, such targets are identified using Endpoint
capabilities that contain the necessary addressing information. This
addressing information must be passed to the artifact processor

Note that in addition to endpoint information about the target,
orchestrators may also need to pass information about the protocol that
must be used to connect to the target. For example, some networking
devices only accept CLI commands across a SSH connection, but others
could also accept REST API calls. Different python scripts could be used
to configure such devices: one that uses the CLI, and one that executes
REST calls. The artifact must include metadata about which connection
mechanism is intended to be used, and orchestrators must pass on this
information to the artifact processor.

Finally, artifact processor may need proper credentials to connect to
target endpoints. Orchestrators must pass those credentials to the
artifact processor before the artifact can be processed.

#### Pass Inputs and Retrieve Results or Errors

Orchestrators must pass any required inputs to the artifact processor.
Some processors could take inputs through environment variables, but
others may prefer command line arguments. Named or positional command
line arguments could be used. TOSCA must be very specific about the
mechanism for passing input data to processors for each type of
artifact.

Similarly, artifact processors must also pass results from operations
back to orchestrators so that results values can be reflected as
appropriate in node properties and attributes. If the operation fails,
error codes may need to be returned as well. TOSCA must be very specific
about the mechanism for returning results and error codes for each type
of artifact.

#### Cleanup

After the artifact has been processed by the artifact processor, the
orchestrator could perform optional cleanup:

If an artifact processor was deployed within the topology that is being
orchestrated, the orchestrator could decide to remove the artifact
processor (and all its deployed dependencies) from the topology with the
goal of not leaving behind any components that are not explicitly
modeled in the service template.

Alternatively, the orchestrator MAY be able to reflect the additional
components/resources associated with the Artifact Processor as part of
the instance model (post deployment).

Artifact Processors that do not use the service template topology as
their execution environment do not impact the deployed topology. It is
up to each orchestrator implementation to decide if these artifact
processors need to be removed.

### Dynamic Artifacts

Detailed Artifacts may be generated on-the-fly as orchestration happens.
May be propagated to other nodes in the topology. How do we describe
those?

### Discussion of Examples

This section shows how orchestrators might execute the steps listed
above for a few common artifact types, in particular:

1.  Shell scripts

- Python scripts

- Package artifacts

- VM images

- Container images

- API artifacts

- Non-standard artifacts

By illustrating how different types of artifacts are intended to be
processed, we identify the information needed by artifact processors to
properly process the artifacts, and we will also identify the components
in the topology from which this information is intended to be obtained.

#### Shell Scripts

Many artifacts are simple bash scripts that provide implementations for
operations in a Node’s Lifecycle Interfaces. Bash scripts are typically
intended to be executed on Compute nodes that host the node with which
these scripts are associated.

We use the following example to illustrate the steps taken by TOSCA
orchestrators to process shell script artifacts.
```
tosca_definitions_version: tosca_2_0
description: Sample tosca archive to illustrate simple shell script usage.
template_name: tosca-samples-shell
template_version: 1.0.0-SNAPSHOT
template_author: TOSCA TC

node_types:
  tosca.nodes.samples.LogIp:
    derived_from: tosca.nodes.SoftwareComponent
    description: Simple linux cross platform create script.
    attributes:
      log_attr: { get_operation_output: [SELF, Standard, create, LOG_OUT] }
    interfaces:
      Standard:
        create:
          inputs:
            SELF_IP: { get_attribute: [HOST, ip_address] }
          implementation: scripts/create.sh

topology_template:
  node_templates:
    log_ip:
      type: tosca.nodes.samples.LogIp
      requirements:
        - host:
            node: compute
            capability: tosca.capabilities.Container
            relationship: tosca.relationships.HostedOn
    # Any linux compute.
    compute:
      type: tosca.nodes.Compute
      capabilities:
        os:
          properties:
            type: linux
```
This example uses the following script to install the LogIP software :
```
#!/bin/bash

# This is exported so available to fetch as output using the get_operation_output function
export LOG_OUT="Create script : $SELF_IP"

# Just a simple example of create operation, of course software installation is better
echo "$LOG_OUT" >> /tmp/tosca_create.log
```
For this simple example, the artifact processing steps outlined above
are as follows:

1.  ***Identify Artifact Processor***: The artifact processor for bash
    shell scripts is the “bash” program.

2.  ***Establish Execution Environment***: The typical execution
    environment for bash scripts is the Compute node respresenting the
    Host of the node containing the artifact.

3.  ***Configure User Account***: The bash user account is the default
    user account created when instantiating the Compute node. It is
    assumed that this account has been configured with sudo privileges.

4.  ***Deploy Artifact Processor***: TOSCA orchestrators can assume that
    bash is pre-installed on all Compute nodes they orchestrate, and
    nothing further needs to be done.

5.  ***Deploy Dependencies***: Orchestrators should copy all provided
    artifacts using a directory structure that mimics the directory
    structure in the original CSAR file containing the artifacts. Since
    no dependencies are specified in the example above, nothing further
    needs to be done.

6.  ***Identify Target***: The target for bash is the Compute node
    itself.

7.  ***Pass Inputs and Retrieve Outputs***: Inputs are passed to bash as
    environment variables. In the example above, there is a single input
    declared for the create operation called SELF_IP. Before processing
    the script, the Orchestrator creates a corresponding environment
    variable in the execution environment. Similarly, the script creates
    a single output that is passed back to the orchestrator as an
    environment variable. This environment variable can be accessed
    elsewhere in the service template using the get_operation_output
    function.

##### Progression of Examples

The following examples show a number of potential use case variations
(not exhaustive) :

###### Simple install script that can run on all flavors for Unix.

For example, a Bash script called “create.sh” that is used to install
some software for a TOSCA Node; that this introduces imperative logic
points (all scripts perhaps) which MAY lead to the creation of “opaque
software” or topologies within the node

####### Notes

- Initial examples used would be independent of the specific flavor of
  Linux.

- The “create” operation, as part of the normative Standard node
  lifecycle, has special meaning in TOSCA in relation to a corresponding
  deployment artifact; that is, the node is not longer “abstract” if it
  either has an impl. Artifact on the create operation or a deployment
  artifact (provided on the node).

“create.sh” prepares/configures environment/host/container for other
software (see below for VM image use case variants).

####### Variants

1.  “create.sh” followed by a “configure.sh” (or “stop.sh”, “start.sh”
    or a similar variant).

2.  in Compute node (i.e., within a widely-used, normative, abstract
    Node Type).

3.  In non-compute node like WebServer (is this the hello world)?

    - Container vs. Containee “hello worlds”; create is “special”;
      speaks to where (target) the script is run at! i.e., Compute node
      does not have a host.

    - What is BEST PRACTICE for compute? Should “create.sh” even be
      allowed?

    - Luc: customer wanted to use an non-AWS cloud, used shell scripts
      to cloud API.

      1.  Should have specific Node type subclass for Compute for that
          other Cloud (OR) a capability that represents that specific
          target Cloud.

###### Script that needs to be run as specific user

For example, a Postgres user

###### Simple script with dependencies

For example, using example from the meeting where script depends on AWS
CLI being installed.

- How do you decide whether to install an RPM or python package for the
  AWS dependency?

- How do we decide whether to install python packages in virtualenv vs.
  system-wide?

###### Different scripts for different Linux flavors

For example. run apt-get vs. yum

- The same operation can be implemented by different artifacts depending
  on the flavor of Linux on which the script needs to be run. We need
  the ability to specify which artifacts to use based on the target.

- How do we extend the “operation” grammar to allow for the selection of
  one specific artifact out of a number of options?

- How do we annotate the artifacts to indicate that they require a
  specific flavor and/or version of Linux?

####### Variants

- A variant would be to use different subclasses of abstract nodes, one
  for each flavor of Linux on which the node is supposed to be deployed.
  This would eliminate the need for different artifacts in the same
  node. Of course, this significantly reduces the amount of
  “abstraction” in service templates.

###### Scripts with environment variables

- Environment variables that may not correspond to input parameters

- For example, OpenStack-specific environment variables

- How do we specify that these environment variables need to be set?

###### Scripts that require certain configuration files

For example, containing AWS credentials

- This configuration file may need to be created dynamically (rather
  than statically inside a CSAR file). How do we specify that these
  files may need to be created?

- Or does this require template files (e.g. Jinja2)?

#### Python Scripts

A second important class of artifacts are Python scripts. Unlike Bash
script artifacts, Python scripts are more commonly executed within the
context of the Orchestrator, but service template designers must also be
able to provide Python scripts artifacts that are intened to be
excecuted within the topology being orchestrated,

##### Python Scripts Executed in Orchestrator

Need a simple example of a Python script executed in the Orchestrator
context.

##### Python Scripts Executed in Topology

Need a simple example of a Python script executed in the topology being
orchestrated.

The following grammar is provided to allow service providers to specify
the execution environment within which the artifact is intended to be
processed :

Need to decide on grammar. Likely an additional keyword to the
“operation” section of lifecycle interface definitions.

##### Specifying Python Version

Some python scripts conform to Python version 2, whereas others may
require version 3. Artifact designers use the following grammar to
specify the required version of Python:

TODO

####### Assumptions/Questions

- Need to decide on grammar. Is artifact processer version associated
  with the processor, with the artifact, the artifact type, or the
  operation implementation?

##### Deploying Dependencies

Most Python scripts rely on external packages that must be installed in
the execution environment. Typically, python packages are installed
using the ‘pip’ command. To provide isolation between different
environments, is is considered best practice to create virtual
environments. A virtual environment is a tool to keep the dependencies
required by different python scripts or projects in separate places, by
creating virtual Python environments for each of them.

The following example shows a Python script that has dependencies on a
number of external packages:

TODO

####### Assumptions/Questions

- Python scripts often have dependencies on a number of external
  packages (that are referenced by some package artifcat). How would
  these be handled?

- How do we account for the fact that most python packages are available
  as Linux packages as well as pip packages?

- Does the template designer need to specify the use of virtual
  environments, or is this up to the orchestrator implementation? Must
  names be provided for virtual environments?

####### Notes

- Typically, dependent artifacts must be processed in a specific order.
  TOSCA grammar must provide a way to define orders and groups (perhaps
  by extending groups grammar by allowing indented sub-lists).

#### Package Artifacts

Most software components are distributed as software packages that
include an archive of files and information about the software, such as
its name, the specific version and a description. These packages are
processed by a package management system (PMS), such as rpm or YUM, that
automates the software installation process.

Linux packages are maintained in Software Repositories, databases of
available application installation packages and upgrade packages for a
number of Linux distributions. Linux installations come pre-configured
with a default Repository from which additional software components can
be installed.

While it is possible to install software packages using Bash script
artifacts that invoke the appropriate package installation commands
(e.g. using apt or yum), TOSCA provides improved portability by allowing
template designers to specify software package artifacts and leaving it
up to the orchestrator to invoke the appropriate package management
system.

##### RPM Packages

The following example shows a software component with an RPM package
artifact.

Need a simple example

#### Debian Packages 

The following example shows a software component with Debian package
artifact.

Need a simple example

####### Notes

- In this scenario, the host on which the software component is deployed
  must support RPM packages. This must be reflected in the software
  component’s host requirement for a target container.

- In this scenario, the host on which the software component is deployed
  must support Debian packages. This must be reflected in the software
  component’s host requirement for a target container.

##### Distro-Independent Service Templates

Some template designers may want to specify a generic application
software topology that can be deployed on a variety of Linux
distributions. Such templates may include software components that
include multiple package artifacts, one for each of the supported types
of container platforms. It is up to the orchestrator to pick the
appropriate package depending on the type of container chosed at
deployment time.

Supporting this use case requires the following:

- Allow multiple artifacts to be expressed for a given lifecycle
  operation.

- Associate the required target platform for which each of those
  artfiacts was meant.

####### Assumptions/Questions

How do we specify multiple artifacts for the same operation?

How we we specify which platforms are support for each artifact? In the
artifact itself? In the artifact type?

#### VM Images

####### Premises

- VM Images is a popular opaque deployment artifact that may deploy an
  entire topology that is not declared itself within the service
  template.

####### Notes

- The “create” operation, as part of the normative Standard node
  lifecycle, has special meaning in TOSCA in relation to a corresponding
  deployment artifact; that is, the node is not longer “abstract” if it
  either has an impl. Artifact on the create operation or a deployment
  artifact (provided on the node).

####### Assumptions/Questions

- In the future, the image itself could contain TOSCA topological
  information either in its metadata or externally as an associated
  file.

- Can these embedded or external descriptions be brought into the TOSCA
  Service Template or be reflected in an instance model for management
  purposes?

- Consider create.sh in conjunction with a VM image deployment artifact

- VM image only (see below)

- Create.sh and VM image, both. (Need to address argument that they
  belong in different nodes).

- Configure.sh with a VM image.? (see below)

- Create.sh only (no VM image)

- Implementation Artifact (on TOSCA Operations):

- Operations that have an artifact (implementation).

- Deployment Artifacts:

- Today: it must appear in the node under “artifacts” key (grammar)

- In the Future, should it:

<!-- -->

- Appear directly in “create” operation, distinguish by “type” (which
  indicates processor)?

- \<or\> by artifact name (by reference) to artifact declared in service
  template.

- What happens if on create and in node (same artifact=ok?
  Different=what happens? Error?)

- What is best practice? And why? Which way is clearer (to user?)?

- Processing order (use case variant) if config file and VM image appear
  on same node?

##### Image Onboarding – Uploading image to image repository

In the case of onboarding of images, the cloud management platform plays
the role of artifact processor. Different cloud management platforms
have different image characteristics.

For example :.

- **Openstack (Glance) -** disk_format, container_format, min_disk,
  min_ram etc.

- **Vmware** - vmware_disktype, vmware_ostype etc.

- **OpenshiftContainer** - name, namespace, selfLink ,resourceVersion
  etc.

These are described as artifact properties. They are not processed by
the Orchestrator, but passed on to the cloud management platform for
further processing.

#### Container Images

#### API Artifacts

Some implementations may need to be implemented by invoking an API on a
remote endpoint. While such implementations could be provided by shell
or python scripts that invoke API client software or use
language-specific bindings for the API, it might be preferred to use
generic API artifacts that leave decisions about the tools and/or
language bindings to invoke the API to the orchestrator.

To support generic API artifacts, the following is required:

- A format in which to express the target endpoint and the required
  parameters for the API call

- A mechanism for binding input parameters in the operation to the
  appropriate parameters in the API call.

- A mechanism for specifying the results and/or errors that will be
  returned by the API call

Moreover, some operations may need to be implemented by making more than
one API call. Flexible API support requires a mechanism for expressing
the control logic that runs those API calls.

It should be possible to use a generic interface to describe these
various API attributes without being forced into using specific software
packages or API tooling. Of course, in order to “invoke” the API an
orchestrator must launch an API client (e.g. a python script, a Java
program, etc.) that uses the appropriate API language bindings. However,
using generic API Artifact types, the decision about which API clients
and language bindings to use can be left to the orchestrator. It is up
to the API Artifact Processor provided by the Orchestrator to create an
execution environment within which to deploy API language bindings and
associated API clients based on Orchestrator preferences. The API
Artifact Processor then uses these API clients to “process” the API
artifact.

##### Examples

- REST

- SOAP

- OpenAPI

- IoT

- Serverless

#### Non-Standard Artifacts with Execution Wrappers

TODO

### Artifact Types and Metadata

To unambiguously describe how artifacts need to be processed, TOSCA
provides:

1.  Artifact types that define standard ways to process artifacts.

<!-- -->

15. Keywords such as checksum, version etc. that enable identification
    of suitable artifact processor and transfer of artifact to artifact
    processor.

16. Artifact Properties that enable the artifact processor to process
    the artifact

17. Descriptive metadata that provide additional information needed to
    properly process the artifact.

# Acknowledgments

The following individuals have participated in the creation of this
specification and are gratefully acknowledged:

Participants:

Alex Vul (<alex.vul@intel.com>), Intel

Anatoly Katzman (<anatoly.katzman@att.com>), AT&T

Arturo Martin De Nicolas (<arturo.martin-de-nicolas@ericsson.com>),
Ericsson

Avi Vachnis (<avi.vachnis@alcatel-lucent.com>), Alcatel-Lucent

Calin Curescu (<calin.curescu@ericsson.com>), Ericsson

Chris Lauwers (<lauwers@ubicity.com)>

Claude Noshpitz (<claude.noshpitz@att.com>), AT&T

Derek Palma (<dpalma@vnomic.com>), Vnomic

Dmytro Gassanov (<dmytro.gassanov@netcracker.com>), NetCracker

Frank Leymann
([Frank.Leymann@informatik.uni-stuttgart.de](file:///C:\Users\IBM_ADMIN\Documents\IBM\SWG\Standards\SDOs\OASIS\TOSCA\Interop%20SC\YAML\Frank.Leymann@informatik.uni-stuttgart.de)),
Univ. of Stuttgart

Gábor Marton (<gabor.marton@nokia.com>), Nokia

Gerd Breiter (<gbreiter@de.ibm.com>), IBM

Hemal Surti (<hsurti@cisco.com>), Cisco

Ifat Afek (<ifat.afek@alcatel-lucent.com>), Alcatel-Lucent

Idan Moyal, (<idan@gigaspaces.com>), Gigaspaces

Jacques Durand (<jdurand@us.fujitsu.com>), Fujitsu

Jin Qin, (<chin.qinjin@huawei.com>), Huawei

Jeremy Hess, (<jeremy@gigaspaces.com>) , Gigaspaces

John Crandall,
([mailto:jcrandal@brocade.com](mailto:jcrandal@brocade.com)), Brocade

Juergen Meynert (<juergen.meynert@ts.fujitsu.com>), Fujitsu

Kapil Thangavelu
([kapil.thangavelu@canonical.com](file:///C:\Users\IBM_ADMIN\Documents\IBM\SWG\Standards\SDOs\OASIS\TOSCA\Interop%20SC\YAML\kapil.thangavelu@canonical.com)),
Canonical

Karsten Beins (<karsten.beins@ts.fujitsu.com>), Fujitsu

Kevin Wilson (<kevin.l.wilson@hp.com>), HP

Krishna Raman
([kraman@redhat.com](file:///C:\Users\IBM_ADMIN\Documents\IBM\SWG\Standards\SDOs\OASIS\TOSCA\Interop%20SC\YAML\kraman@redhat.com)),
Red Hat

Luc Boutier (<luc.boutier@fastconnect.fr>), FastConnect

Luca Gioppo, (<luca.gioppo@csi.it>), CSI-Piemonte

Matej Artač, (<matej.artac@xlab.si>), XLAB

Matt Rutkowski (<mrutkows@us.ibm.com>), IBM

Moshe Elisha (<moshe.elisha@alcatel-lucent.com>), Alcatel-Lucent

Nate Finch (<nate.finch@canonical.com>), Canonical

Nikunj Nemani
([nnemani@vmware.com](file:///C:\Users\IBM_ADMIN\Documents\IBM\SWG\Standards\SDOs\OASIS\TOSCA\Interop%20SC\YAML\nnemani@vmware.com)),
Wmware

Priya TG (<priya.g@netcracker.com)> NetCracker

Richard Probst
([richard.probst@sap.com](file:///C:\Users\IBM_ADMIN\Documents\IBM\SWG\Standards\SDOs\OASIS\TOSCA\Interop%20SC\YAML\richard.probst@sap.com)),
SAP AG

Sahdev Zala (<spzala@us.ibm.com>), IBM

Shitao li (<lishitao@huawei.com>), Huawei

Simeon Monov (<sdmonov@us.ibm.com>), IBM

Sivan Barzily, (<sivan@gigaspaces.com>), Gigaspaces

Sridhar Ramaswamy (<sramasw@brocade.com>), Brocade

Stephane Maes (<stephane.maes@hp.com>), HP

Steve Baillargeon (<steve.baillargeon@ericsson.com>), Ericsson

Thinh Nguyenphu (<thinh.nguyenphu@nokia.com>), Nokia

Thomas Spatzier (<thomas.spatzier@de.ibm.com>), IBM

Ton Ngo (<ton@us.ibm.com>), IBM

Travis Tripp (<travis.tripp@hp.com>), HP

Vahid Hashemian (<vahidhashemian@us.ibm.com>), IBM

Wayne Witzel (<wayne.witzel@canonical.com>), Canonical

Yaron Parasol (<yaronpa@gigaspaces.com>), Gigaspaces

# Some Section

Text.

## Subsidiary Appendix Section

Text.

### Sub-subsidiary Appendix Section

text.

# Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Revision</strong></th>
<th><strong>Date</strong></th>
<th><strong>Editor</strong></th>
<th><strong>Changes Made</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WD01, Rev01</td>
<td>2019-04-22</td>
<td>Chris Lauwers</td>
<td>Initial WD01, Revision 01. Split off from <em>TOSCA Version 2.0</em>
document.</td>
</tr>
<tr class="even">
<td>WD01, Rev02</td>
<td>2019-04-23</td>
<td>Calin Curescu</td>
<td><p>Revision 02 changes to the “TOSCA Cloud Service Archive (CSAR)
format” chapter:</p>
<ul>
<li><p>The CSAR and TOSCA.meta structure specification is self-contained
and is not defined anymore as a modification of the definitions of XML
TOSCA 1.0 specification</p></li>
<li><p>The TOSCA.meta file may be placed in the root of the CSAR
archive, in addition to its historic location in TOSCA-Metadata
directory (thus, existing CSAR structures where the TOSCA.meta is
located in the TOSCA-Metadata directory are still valid). This
eliminates any kind of necessary directory structure in the
CSAR.</p></li>
<li><p>We have deprecated the usage of TOSCA-Meta-File-Version keyname.
Previously (up to v1.3) we had two keynames for more or less the same
thing. The CSAR-Version starting with “2.0” covers both the CSAR
structure and the TOSCA metafile structure (overriding any value of
TOSCA-Meta-File-Version in this context)</p></li>
<li><p>We have deprecated the meaning of any block beyond block_0 in the
TOSCA.meta file (as defined in XML TOSCA 1.0 specification and
optionally used up to the v1.3 of the TOSCA specification). Additional
blocks (to block_0) can be used to define custom keynames that have
meanings outside of the TOSCA specification.</p></li>
<li><p>We have deprecated the required use of the metadata section
(where template_name and template_version metadata are also required) in
the service definition yaml file for the case where where we have no
TOSCA.meta file (and the yaml file in the root of the CSAR is the
service definition file). Moreover, the previous specification (up to
v1.3) of using the template-version to denote the CSAR-version is
inconsistent with the definition of template-version. In the current
specification, for the case with no TOSCA.meta file we infer the
CSAR-Version from the tosca_definitions_version keyword in the
Entry-Definitions file.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD01, Rev03</td>
<td>2019-05-13</td>
<td>Chris Lauwers</td>
<td>Fix formatting</td>
</tr>
<tr class="even">
<td>WD01, Rev04</td>
<td>2019-08-30</td>
<td>Chris Lauwers</td>
<td>Minor template changes</td>
</tr>
<tr class="odd">
<td>WD01, Rev05</td>
<td>2020-02-20</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Move normative type definitions from the “TOSCA v2.0
Specification” into this document</p></li>
<li><p>Move non-normative type definitions from the “TOSCA v2.0
Specification” into this document</p></li>
<li><p>Move CSAR specification into “TOSCA v2.0 Specification”
document.</p></li>
</ul></td>
</tr>
</tbody>
</table>

-------

# Appendix A. Informative References

<!-- Required section -->

This appendix contains the informative references that are used in this document.

While any hyperlinks included in this appendix were valid at the time of publication, OASIS cannot guarantee their long-term validity.

(Reference sources:
For references to IETF RFCs, use the approved citation formats at: \
https://docs.oasis-open.org/templates/ietf-rfc-list/ietf-rfc-list.html. \
For references to W3C Recommendations, use the approved citation formats at: \
https://docs.oasis-open.org/templates/w3c-recommendations-list/w3c-recommendations-list.html. \
Remove this note before submitting for publication.)

###### [TOSCA-v2.0]
 _Topology and Orchestration Specification for Cloud Applications Version 2.0._ Edited by Chris Lauwers and Calin Curescu. Latest stage: https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.html.

-------

# Appendix B. Acknowledgments

(Note: A Work Product approved by the TC must include a list of people who participated in the development of the Work Product. This is generally done by collecting the list of names in this appendix. This list shall be initially compiled by the Chair, and any Member of the TC may add or remove their names from the list by request.  
Remove this note before submitting for publication.)

## B.1 Special Thanks

<!-- This is an optional subsection to call out contributions from TC members. If a TC wants to thank non-TC members then they should avoid using the term "contribution" and instead thank them for their "expertise" or "assistance". -->

Substantial contributions to this document from the following individuals are gratefully acknowledged:

Participant Name, Affiliation or "Individual Member"

## B.2 Participants

<!-- A TC can determine who they list here, however, TC Observers must not be listed. It is common practice for TCs to list everyone that was part of the TC during the creation of the document, but this is ultimately a TC decision on who they want to list and not list, and in what order. -->

The following individuals have participated in the creation of this document and are gratefully acknowledged:

**TOSCA TC Members:**

| First Name | Last Name | Company |
| :--- | :--- | :--- |
Philippe | Alcon | Marvelous Networks
Alex | Amir | Viacat
Kris | Anders | Trend Mission
Darren | Anysteel | Macro Networks

-------

# Appendix C. Revision History
| Revision | Date | Editor | Changes Made |
| :--- | :--- | :--- | :--- |
| filename-v1.0-wd01 | yyyy-mm-dd | Editor Name | Initial working draft |

------

# Appendix D. Notices

Copyright &copy; OASIS Open 2023. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.
