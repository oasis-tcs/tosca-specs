# Unified Event Handling

One of the main differentiating features of TOSCA is that it supports
declarative service lifecycle management based on graph-based service
models. Declarative automation is supported by *declarative workflows*
that are created automatically by the orchestrator based on
dependencies encoded in the service topology graph combined with the
semantics of the standard interface types defined in the Simple
Profile. In addition, TOSCA supports *imperative workflows* for
defining lifecycle management actions as well. And finally, TOSCA
supports *policy triggers* intended to support closed-loop
automation. Each of these pieces of functionality uses different
grammar elements that are someone overlapping. TOSCA v2.0 introduces a
unified framework that harmonizes these various pieces of TOSCA
functionality and broadens the scope of supported lifecycle management
actions in the process.

## Motivation

The lifecycle management framework introduced in TOSCA v2.0 is
motivated by a number of obervations. 

- TOSCA Simple Profile in YAML v1.x supports automatically-generated
  *declarative workflows* based on operation sequencing and
  interleaving rules associated with the *normative interface types*
  defined in the standard. TOSCA v2.0 no longer includes these
  normative types definitions. This has a number of implications:
  - The Orchestrator no longer has built-in knowledge of the state
    machines associated with interfaces defined in
    TOSCA. Specifically, it does not know how operations in an
    interface must be sequenced to achieve a desired ("intended")
    outcome. New grammar is required to allow profile designers to
    define state machines associated with their interface types.
  - The Orchestrator no longer has built-in knowledge of how to
    interleave operations on one node with operations on relationships
    in and out of that node, or with operations of other nodes with
    which that node has relationships. New grammar is requied to allow
    component designers to specify these local sequencing behaviors
    based on intented outcomes.

  When service designers combine nodes and relationships into a
  service topology graph, end-to-end service lifecycle management
  behavior *emerges* by combining the various localized behaviors
  defined in node and relationship types.
- Lifecycle management in TOSCA v1.x focuses almost exclusively on Day
  0 service design and Day 1 service orchestration. The TOSCA 1.x
  standard makes an implicit assumption that service templates are
  designed only for the purpose of deploying (and potentially
  undeploying) services only as follows:
  - *Deploying* a service involves instantiating a *service
    representation* from a service template, fulfilling requirements
    if necessary, performing substitutions if necessary, and then
    running the `deploy` workflow (which ideally should be created
    automatically).
  - *Removing* a service involves running the `undeploy` workflow
    (which ideally should be created automatically). The Version 1.3
    spec doesn't state whether substituting services should be
    removed, or whether requirements fulfilled by the orchestrator
    should be *undone*.

  This list is completely inadequate. For example:
  - In practice, operators may want to perform *dry-runs* before
    deploying services. This means that the orchestrator may want to
    separate out a *provisioning* phase from an *activation* phase or
    perform *activation* phases using `noop` operations. How are these
    two different phases invoked and/or executed?
  - There is no discussion about updating or upgrading a running
    service.
  - Version 1.3 includes a `Scalable` capability type but provides no
    mechanism to invoke scaling of components.
  - There is no accommodation for administratively taking components
    out of service.
  
  TOSCA does not provide a formal way for service designers to define
  which other *lifecycle management actions* can be performed on an
  entire service. While some management actions can be provided by
  defining imperative workflows, these workflows provide only limited
  functionality, since they are not able to manipulate the topology
  representation graph. In addition, imperative workflows are defined
  in the context of service templates and thus cannot be packaged as
  reusable components.

  TOSCA v2.0 explicitly broadens its scope to include Day 2 service
  management actions such as modifying, updating, ugrading, moving,
  and scaling of services. This requires mechanisms that allow service
  designers to specify the set of supported service lifecycle
  management actions and for defining the associated implementations.
- While TOSCA v1.x supports *policy triggers*, this functionality
  provides only limited usefulness since the main objective of these
  triggers is to provide closed-loop automation to make sure deployed
  services satisfy desired service objectives. Service assurance is by
  definition a Day 2 service management task, but as explained in the
  previous bullet item, TOSCA v1.x provides little or no grammar for
  defining Day 2 service lifecycle management operations. This
  severely limits the usefulness of closed loop automation.

## Unified Event Handling Framework

The new Service Lifecycle Management framework introduced in TOSCA
v2.0 is based on a *unified event handling* approach that harmonizes
syntax for interface and interface type definitions, for workflow
definitions, and for policy definitions.

The basic pattern for unified event handling is shown in the following
figure:

```mermaid
flowchart TB
    A[[receive event]]
    A --> S0
    subgraph S0 [handle event]
      direction TB
      B{precondition<br>satisfied ?}
      B --> |Yes| D(update attributes)
      D --> E(execute handlers)
      B --> |No| C(ignore)
    end
    S0 --> S00((o))
    S00 --> S1
    S00 --> S2
    S00 --> S3
    subgraph S1 [trigger]
      direction TB
      F1{condition<br>satisfied ?}
      F1 --> |Yes| G1[[send event]]
      F1 --> |No| H1(done)
    end
    subgraph S2 [trigger]
      direction TB
      F2{condition<br>satisfied ?}
      F2 --> |Yes| G2[[send event]]
      F2 --> |No| H2(done)
    end
    subgraph S3 [trigger]
      direction TB
      F3{condition<br>satisfied ?}
      F3 --> |Yes| G3[[send event]]
      F3 --> |No| H3(done)
    end
```
The figure illustrates the following pattern:
- Entities in a TOSCA service topology advertize the ability to
  receive `events`. Events can reflect a requested management
  operation on the associated entity or signal a change in the state
  of entity. Events replace and generalize *interface operations* and
  *interface notifications* supported in the TOSCA v1.x
  standard. Events can be defined on nodes, on relationships, and on
  entire service topologies.
- Each event can optionally define an associated `precondition` that
  is evaluated when the event is received. Preconditions are evaluated
  within the context of the entity that defines the event. The
  precondition must evaluate to `true` for the event to be handled. If
  it evaluates to `false`, the event is ignored. TOSCA does not
  *defer* events for handling at a later point in time. Event
  preconditions generalize the `preconditions` concept associated with
  TOSCA v1.x workflow definitions.
- Receiving an event can result in updating attribute values that are
  accessible in the context within which the event is defined. For
  example, if events are defined within an interface, setting
  interface attributes allows events to drive a state machine
  associated with that interface.
- Each event can also define zero or more more event `handlers` that
  are executed in response to the event if the preconditions evaluates
  to true. Handlers can run scripts or other artifacts. Event handlers
  are a generalization of the `implementation artifacts` supported in
  TOSCA v1.x. Whereas TOSCA v1.x defines `primary` and `dependent`
  implementation artifacts, TOSCA v2.0 defines a single list of
  handles. TOSCA v2.0 also supports per-handler input and output
  definitions.
- After all event handlers have been executed, a set of `triggers` are
  run. Triggers conditionally send new events along the service
  topology graph. Triggers are a generalization of the `on_success`
  and `on_failure` keywords in the TOSCA v1.x workflow step
  grammar. Rather than conditially *triggering* follow-up actions
  based on the return values of the handlers, arbitrary conditions can
  be used to determine which follow-up actions should be taken next.

In this model, events are the common construct for delegating control
between entities, similar to how objects in an object-oriented system
interact. Events provide a shared *mechanism* that can be used to
harmonize different pieces of TOSCA functionality. The *event
mechanism* can be used at a *high level* as well as a *low level*, and
it can be used for defining *global* behavior as well as for *local*
behavior.
- The event mechanism can be used to describe interface state machines
  (i.e., the various interface states, the `events` that cause
  transitions between these events, and the `conditions` that must be
  satisfied before events can be handled or before events can be
  propagated across the topology graph.
- Events enable the creation of reusable components, where the logic
  for managing the lifecycle of a component can largely be defined
  locally within that component based on knowledge (defined in the
  node type) about possible incoming and outgoing relationships of
  that component.
- The *high-level* event handling statements can dictate how these
  low-level mechanisms are used to accomplish *intended* behavior
  (i.e., **intent statements**).
- Global service management behavior emerges as a result of combining
  localized event handling defined in reusable components (i.e. node
  types and relationship types) and as directed by the intent
  statements into complete service topology graphs. In addition,
  triggers can be used as *hooks* for defining additional end-to-end
  logic at the service template level if necessary.

The distributed event handling concept is a generalization of
declarative workflows that provides superior functionality.  The
following sections illustrate in more detail how this is done.

## Defining Interface State Machines

The *unified event handling* mechanism can be used to define the state
machines associated with arbitrary interface types, and to define how
events result in interface state transitions. Interface definitions
define a state machine by defining the following:
- The set of `events` supported by the interface.
- One or more `attributes` that track the current state of the
  interface (as opposed to the state of a node or relationship with
  which the interface is associated).
- For each event, the interface type defines `preconditions` that
  check whether the interface is in a state in which the event can be
  processed. The `precondition` statement must evaluate to `true` in
  order for the event to be handled.
- For each event, the state machine defines the attribute values that
  need to be set to track the state into which the interface
  transitions after receiving the event.
- Interfaces also support the ability to express *intent* using
  additional interface attributes that track the `desired_state` into
  which the interface needs to be transitioned.
- Interface types define triggers that post subsequent events to the
  interface that force it to transition through its state machine
  towards the desired state. The `state` and `desired_state`
  attributes are used in the *trigger conditions* to select the
  necessary events to drive the interface towards its intended state.
  State transitions are triggered whenever the `desired_state`
  attribute value changes or whenever the `state` attribute value
  changes.

The following example shows how the `Standard` interface in the Simple
Profile could be described using this grammar:
```yaml
data_types:
  State:
    derived_from: string
    validation:
      $valid_values:
        - $value: []
        - - initial
          - created
          - configured
          - started
    
interface_types:
  Standard:
    attributes:
      state:
        type: State
      desired_state:
        type: State
    operations:
      create:
        preconditions:
          $equal:
            - $get_attribute: [ INTERFACE, state ]
            - initial
        set_attribute: [ INTERFACE, state, created ]
        triggers:
          - condition: 
              $valid_values:
                - $get_attribute: [ INTERFACE, desired_state ]
                - [ configured, started ]
            target: SELF
            event: Standard.configure
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - initial
            target: SELF
            event: Standard.delete
      configure:
        preconditions:
          $equal:
            - $get_attribute: [ INTERFACE, state ]
            - created
        set_attribute: [ INTERFACE, state, configured ]
        triggers:
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - started
            target: SELF
            event: Standard.start
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - initial
            target: SELF
            event: Standard.delete
      start:
        preconditions:
          $equal:
            - $get_attribute: [ INTERFACE, state ]
            - configured
        set_attribute: [ INTERFACE, state, started ]
        triggers:
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - configured
            target: SELF
            event: Standard.stop
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - initial
            target: SELF
            event: Standard.delete
      stop:
        preconditions:
          $equal:
            - $get_attribute: [ INTERFACE, state ]
            - started
        set_attribute: [ INTERFACE, state, configured]
        triggers:
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - started
            target: SELF
            event: Standard.start
          - condition: 
              $equal:
                - $get_attribute: [ INTERFACE, desired_state ]
                - initial
            target: SELF
            event: Standard.delete
      delete:
        preconditions:
          $valid_values:
            - $get_attribute: [ INTERFACE, state ]
            - [ created, configured ]
        $set_attribute: [ INTERFACE, state, initial ]
        triggers:
          - condition: 
              $valid_values:
                - $get_attribute: [ INTERFACE, desired_state ]
                - [ created, configured, started ]
            target: SELF
            event: Standard.create
```
## Defining Reusable Localized Component Behavior

Interface types define state machines for individual interfaces. However:

- Node and relationship types can define multiple interfaces. The
  state machines of these interfaces need to be coordinated.
- The state machines of interfaces of a node need to be coordinated
  with the state machines of the incoming and outgoing relationships
  of that node.
- State machines of interfaces of a node may need to be coordinated
  with that state machines of other nodes with which the node has
  relationships.

The interface definitions in node types and relationship types are
responsible for this coordination by *refining* the preconditions
associated with interface events and by adding additional event
triggers. As a result, interface definitions create *localized*
component behaviors that are effectively *fine grained*
workflows. These mini-workflows specify local behaviors (in node type
definitions) for interleaving events defined in the node's interface
types with relationship operations defined in the interface types
associated with the incoming and outgoing relationships.  When nodes
and relationships are organized in a service topology graph, these
fine grained workflows propagate events across tge graph which causes
end-to-end behavior to emerge. This *emergent behavior* is an
generalization of the automatically created declarative workflows of
TOSCA v1.x.

Unlike *imperative workflows*, the localized *mine workflows*
specified in interface definitions have the following characteristics:
- The apply to all nodes of a specific type, rather that to specific
  nodes in a service template.
- Events can be propagated based on the types used in requirement
  definitions and capability definitions without needing to identify
  specific target nodes by name.

## Defining Service Lifecycle Management Actions

Events definitions are supported not just in interfaces but also at
the service template level. Service template events provide the
mechanism for service designer to express which lifecycle management
actions can be performed by external management systems or external
operators. Events defined at the service template level provide the
*intent* paradigm in TOSCA: they allow external systems to signal
changes in intended behavior to the Orchestrator.  The event/trigger
pattern is then used to translate *global* service-level intent into
*local* component-level operations by triggering lower-level events on
the nodes and relationships in the service topology.

Service level events formalize a number of implicit assumptions in the
TOSCA v1.x specification. For example:

- The Version 1.3 spec suggests that an operation to *deploy* a
  service returns a set of values as defined in the `outputs` section
  of a service template. This should be formally specified by
  triggering *output* events.
- It should be possible for orchestrators to *asynchronously* generate
  service-related events to external systems. This could support
  *escalation* scenarios where policies defined for a service first
  attempt to recover from failures automatically but escalate to an
  external system (or operator) if the recovery process is
  unsuccesful.
- How should partial failure scnenarios be handled? Retry? Rollback?
  Since there is likely no single approach that works best for all
  application domains, TOSCA should support defining the selected
  approach.

# Event Handling Grammar

## Event Definition
The grammar for defining events is shown in the following table:
|Keyname|Mandatory|Type|Description|
|---|---|---|---|
|precondition|no|boolean |A boolean function that must evaluate to `true` for the event to be handled. If the precondition is `false` the event is ignored.|
|set_attribute|no|map of values|Interface attribute values to set when the event is received. Keys in the map identify the attribute values. Values in the map are assigned to the attributes.|
|handlers|no|list of Event Handler Definitions|A list of handlers that are conditionally executed when the event is received.|
|triggers|no|list of Event Trigger Definitions|A list of triggers that can send new events after this event has been handled.|

## Event Handler Definition
The grammar for defining event handlers in event definitions is shown
in the following table:

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|execute|yes|Artifact definition or string|Defines the `artifact` to be executed. The artifact can either be specified using an inline artifact definition or it can be referenced using a string name that references an artifact definition in the node type or node template that includes the Event Handler definition|
|inputs|no|map of parameter assignments|The map of input parameter assignments for the event handler.|
|outputs|no|map of output mappings|The map of output value mappings for the event. Ouput values returned by the event handler are mapped to attributes that are accessible in the context within which the event is defined.|

## Event Trigger Definition

> To be provided

## Comparison with Version 1.x

The following table compares TOSCA v2.0 *unified event handling*
grammar with what's currently in Version 1.3.

|Version 1.x|Version 2.0|Discussion|
|---|---|---|
||interface properties and attributes|Version 1.x interfaces define `operations` and `notifications` only. V2.0 adds support for `properties` and `attributes` in interfaces to allow for interface-specific state variables.|
||INTERFACE|Interface properties or artifacts are identified using the `INTERFACE` keyword in ToscaPath expressions.|
|operations and notifications|events|Operations were intended to be API calls, whereas notifications were intended to be callbacks. Events do away with this distinction since it was never clearly specified how these were intended to be implemented. **TODO**: decide whether to adopt the `events` keyword, revert back to supporting `operations` only, or pick something else entirely such as `actions`|
|operation implementations|handlers|In Version 1.x, implementations of operations and notifications are specified using `artifacts` (that are expected to be processed by a corresponding *artifact processor*). Version 2.0 `handlers` allow implementations to be defined using artifacts, and also using other mechanisms (e.g. by setting attribute values)|
|primary and dependent implementations||v1.3 supports a single `primary` implementation artifact and an ordered list of `dependent` artifacts. Version 2.0 eliminates this distinction and defines a single list of handlers.|
|artifact type|event handler type|Event handler types are a generalization of artifact types. In v1.3, artifact types uniquely identify the artifact processor used to *execute* the artifact. How does an orchestrator know how to *execute* a handler based on handler type?|
|on_success and on_failure|triggers|Version 2.0 `triggers` generalize the `on_success` and `on_failure` keywords of the V1.x policy grammar. They define the events that must (conditionally) be sent after an event has been *handled*. Triggers can be specified in interface types or in interface definitions.|
|actions|handlers and triggers|V1.x workflows and policies can define `actions` that need to be taken after an operation has been executed. Version 2.x splits separates actions into `handlers` that are part of operation implementations (such as setting attribute values) and `triggers` that define how events can be propagated to other nodes in the topology.|
|preconditions|trigger conditions|Version 1.x `preconditions` are evaluated in the context of executing workflow steps. It is unclear what should happen if the precondition evaluates to False. Version 2.0 associates `conditions` with triggers only. Conditions are evaluated after an event has been handled rather than before, and they specify whether execution of an event should result in other events being triggered.|
||service-level events and triggers|Version 2.0 allows events and triggers to be defined at the service (template) level. This addresses a gap in the v1.x specification where no mechanism exists to specify the types of actions that can be taken on a service as a whole.|
 
