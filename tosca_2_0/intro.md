# Introduction

- The *Topology and Orchestration Specification for Cloud
  Applications* (TOSCA) is a *domain-specific language* (DSL) for
  automating the *Lifecycle Management* of large complex systems.

- a language for describing application components
  and their relationships by means of a service topology, and for
  specifying the lifecycle management procedures for creation or
  modification of services using orchestration processes. The
  combination of topology and orchestration enables not only the
  automation of deployment but also the automation of the complete
  service lifecycle management.

## Objectives

- Standard language that is not tied to specific technologies or
  specific vendors.

- Thus, the goal of the TOSCA TC is to define a language that is
  agnostic to specific technological and commercial ecosystems and
  that supports the design and operation of cloud applications.

- TOSCA was expressly designed to address the complexity associated
  with managing large systems

- The capabilities offered by TOSCA will facilitate higher service
  continuity, reduce service disruption and manual mitigation,
  increase interoperability, avoid lock-in, and achieve the intended
  orchestration.

- Ultimately, this will benefit the consumers, developers, and
  providers of more and more complex and heterogeneous cloud-native
  applications.

- Network operators typically build management systems based on
  vendor-specific tools, dedicated element management systems, and
  special-purpose controllers, each of which manages only a small
  subset of the network.

- To make matters worse, these tools often use incompatible interfaces
  or data schemas, resulting in integration nightmares. As the number
  of network elements grows—because the scale of the network increases
  and disaggregation becomes the norm—so will the number of required
  management tools.

- In this environment special-purpose management tools are no longer
  practical, since the size of the management system will grow in
  concert with the network, and the challenge of integrating the
  management components will grow exponentially.

- Uniform network management for all parts of the network and all
  layers of the technology stack.

- Software services and networks are becoming more complex because of the adoption of disaggregation between hardware and software, 

- Management of such systems can be greatly simplified if the creation
  and lifecycle management of application, infrastructure, and network
  services can be fully automated and supported across a variety of
  deployment environments.

- The core TOSCA specification provides a language for describing
  service components and their relationships using a service topology
  graph, and it provides for specifying the lifecycle management
  procedures that allow for creation or modification of services using
  orchestration processes.

- The combination of topology and orchestration in a Service Template
  describes what is needed in different environments to enable
  automated deployment of services and their management throughout the
  complete service lifecycle (e.g. scaling, patching, monitoring,
  etc.).

## TOSCA Features

### TOSCA is Model-Driven

TOSCA Uses model-driven approach:

- The TOSCA specification promotes a model-driven approach, whereby
  information embedded in the model structure (the dependencies,
  connections, compositions) drives the automated processes.

- TOSCA processors maintain service models (*digital twins*) for all
  service components—across all layers

- All management actions are performed on service models first and
  propagated to external real-world entities by the automation
  platform.

- Similarly, changes to external resources are reflected into models
  first and then handled by automationp platform.

### Model-Driven Enable all Lifecycle Management Phases

- Service models are used:

  - As starting point for Moves, Adds, Changes, and Deletions
    (MACDs)

  - As context for handling faults and events using Closed Loop
    Automation

- Can't do this without models.

### TOSCA Models are Graphs

- TOSCA models systems as graphs, where the vertices represent the
  components of the system and the edges represents relationships,
  dependencies, and other interactions between these components.

### Graphs are Domain-Independent

- Fundamental abstraction in TOSCA is graph, which makes it suitable
  for any application domain. Any domain where systems can be modeled
  as graphs.

### TOSCA Enables Declarative Orchestration

- Model-driven approach enables "declarative" orchestration, where
  system designers create descriptions ("models") of their systems,
  and it is the task of the orchestrator to translate descriptions
  into the commands to realize the systems being described.

- This is what delivers simplicity. Often referred to as desired state
  or intent-based orchestration.

# TOSCA Core Concepts

- Then we can get into explanation of the core concepts.

- Declarative orchestration expects that that models are created from
  templates.

- To make this possible, designers define reusable components ("Node
  Types") that define an externally visible façade of these components
  as well as the necessary implementations to interact with physical
  resources. These components are organized in profiles for reuse.

- TOSCA is perfect for multi-cloud orchestration you
  describe, since it has built-in support for abstractions. In fact,
  it has two separate features in support of abstraction: 1. Type
  derivation (where specialized node types derived from an abstract
  base type) 2. Substitution mapping (where substituting templates
  provide internal implementations for abstract types).

## 1.1 Changes from earlier Versions

<!-- Optional section -->
<!-- Describe significant changes from previous differently-numbered Versions, not changes between stages of the current Version -->

## 1.2 Glossary

<!-- Optional section with suggested subsections -->

### 1.2.1 Definitions of terms

The following terms are used throughout this specification and have the
following definitions when used in context of this document.

|Term|Definition|
|---|---|
|Representation Model|A deployed service is a running instance of a Service Template. The instance is typically derived by running a declarative workflow that is automatically generated based on the node templates and relationship templates defined in the service template.|
|Node Template| A *Node Template* specifies the occurrence of a component node as part of a service template. Each Node Template refers to a Node Type that defines the semantics of the node (e.g., properties, attributes, requirements, capabilities, interfaces). Node Types are defined separately for reuse purposes.                                                          |
|Relationship Template| A *Relationship Template* specifies the occurrence of a relationship between nodes in a service template. Each Relationship Template refers to a Relationship Type that defines the semantics of the relationship (e.g., properties, attributes, interfaces, etc.). Relationship Types are defined separately for reuse purposes.                                           |
|Service Template| A *Service Template* is used to specify the *topology* (or structure) and *orchestration* (or invocation of management behavior) of services so that they can be provisioned and managed in accordance with constraints and policies.                                                                                                                   |
|Topology Model| A Topology Model defines the structure of a service in the context of a Service Template. A Topology model consists of a set of Node Template and Relationship Template definitions that together define the topology of a service as a (not necessarily connected) directed graph.                                                                                  |
|Abstract Node Template | An abstract node template is a node template that doesn’t define any implementations for the TOSCA lifecycle management operations. Service designers explicitly mark node templates as abstract using the substitute directive. TOSCA orchestrators provide implementations for abstract node templates by finding substituting templates for those node templates. |

### 1.2.2 Acronyms and abbreviations

### 1.2.3 Document conventions

- Naming conventions
- Font colors and styles
- Typographic conventions

-------
