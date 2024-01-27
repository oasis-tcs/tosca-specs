# From the Charter

The Topology and Orchestration Specification for Cloud Applications
(TOSCA) provides a language for describing application components and
their relationships by means of a service topology, and for specifying
the lifecycle management procedures for creation or modification of
services using orchestration processes. The combination of topology
and orchestration enables not only the automation of deployment but
also the automation of the complete service lifecycle management. The
TOSCA specification promotes a model-driven approach, whereby
information embedded in the model structure (the dependencies,
connections, compositions) drives the automated processes.

The goal of the TOSCA TC is to promote and enhance the adoption and
portability of such model-driven concepts for orchestration and
management of complex systems.

The diversity of cloud applications has increased tremendously, and
TOSCA aims to address these different domains such as
Infrastructure-as-a-Service Clouds, Cloud-native Applications, Network
Functions Virtualization, Software Defined Networking,
Functions-as-a-Service, IoT and Edge Computing, Process Automation,
Embedded Systems Automation, and other paradigms as they may emerge.

Thus, the goal of the TOSCA TC is to define a language that is
agnostic to specific technological and commercial ecosystems and that
supports the design and operation of cloud applications.

The TOSCA TC also aims to make the TOSCA language easy to use and to
foster community-building around orchestration and cloud ecosystems.

The capabilities offered by TOSCA will facilitate higher service
continuity, reduce service disruption and manual mitigation, increase
interoperability, avoid lock-in, and achieve the intended
orchestration. Ultimately, this will benefit the consumers,
developers, and providers of more and more complex and heterogeneous
cloud-native applications.

# Introduction

- TOSCA is a *domain-specific language* (DSL) for automating the
  *Lifecycle Management* of large complex systems.

- TOSCA Goals

## TOSCA is Model-Driven

TOSCA Uses model-driven approach:

- TOSCA processors maintain service models (*digital twins*) for all
  service components—across all layers

- All management actions are performed on service models first and
  propagated to external real-world entities by the automation
  platform.

- Similarly, changes to external resources are reflected into models
  first and then handled by automationp platform.

## TOSCA Models are Graphs

- TOSCA models systems as graphs, where the vertices represent the
  components of the system and the edges represents relationships,
  dependencies, and other interactions between these components.

## Graphs are Domain-Independent

- Fundamental abstraction in TOSCA is graph, which makes it suitable
  for any application domain. Any domain where systems can be modeled
  as graphs.

## TOSCA Enables Declarative Orchestration

- Model-driven approach enables "declarative" orchestration, where
  system designers create descriptions ("models") of their systems,
  and it is the task of the orchestrator to translate descriptions
  into the commands to realize the systems being described.

## Models Enable all Lifecycle Management Phases

- Service models are used:

  - As starting point for Moves, Adds, Changes, and Deletions
    (MACDs)

  - As context for handling faults and events using Closed Loop
    Automation

- Declarative approach is used for all phases of a service lifecycle.

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
