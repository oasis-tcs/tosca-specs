# Model-Driven Management

TOSCA supports a *Model-Driven Management* paradigm:

- A TOSCA orchestrator keeps a model of each instantiated service in
  its service instance repository. This service (instance) model
  provides an abstract representation of the underlying running
  system.

- All service lifecycle management actions are performed fist on the
  service instance model in the repository rather than directly on the
  managed entities.

- Any changes resulting from management operations on the model first
  are then propagated into the managed entities by running workflows
  that invoke a set of standard interface operations supported by the
  nodes in the topology.

To date, TOSCA has primarily been used for (Day 1) service
orchestration. This means there are currently two lifecycle management
operations that must be supported by a TOSCA v1.3 orchestrator API.

1.  ***Create***: combine a TOSCA service template with
    deployment-specific input values (*service characteristics*) to
    create a deployed service instance model, and to deploy a service
    into the external systems based on this model.

2.  ***Delete***: remove a deployed service and delete its service
    instance model from the service instance repository.

Our intent is to also use TOSCA to support ongoing (Day 2) management
of deployed services. Ongoing service lifecycle management could
involve a variety of lifecycle management operations. For example,
ETSI NFV includes the following lifecycle management operations that
must be supported by a VNFM:

- Operate VNF

- Modify VNF Information

- Scale VNF

- Change VNF Flavor

- Heal VNF

- Change External VNF connectivity

This document discusses how such lifecycle management operations can
be supported by introducing a general-purpose mechanism to allow
external systems to modify deployed services.

# Modifying a Deployed TOSCA Service Instance

The model-driven management paradigm states that modifying a deployed
service is done by updating the service instance model first, and then
reflecting the updated service instance model into the external systems
by running workflows that invoke interface operations on individual
service components.

The question, then, is how external systems (we will refer to such
systems as *north-bound* systems) interact with a TOSCA orchestrator
to modify a service instance model in the service instance repository.

One obvious approach might be to use a REST-based paradigm where
north-bound systems POST updated representations of some or all of the
service components. However, this is not the TOSCA approach. Since
TOSCA service templates may encode complex dependencies between
components in a topology, between service components and resources in
inventory, and between service components and their substituting
topologies. It is not realistic to expect north-bound systems to
modify service components while simultaneously maintaining the
integrity of the service topology.  In fact, automated management of
these dependencies is exactly what a TOSCA orchestrator is intended
for.

The TOSCA paradigm for modifying deployed services, therefore, is
different from REST and is an extension of the mechanism used for
initial service creation. As explained earlier, when issuing a request
to create a service instance, a north-bound system is expected to
provide two sets of information:

1.  The *service template* from which the service must be created.

2.  Deployment-specific *input values* (also called *service
    characteristics*) as defined in the service template.

No other information is required. Specifically, neither the service
topology nor any internal details of the service components need to be
visible to the north-bound system. Only the schema for the input values
(the input definitions in the TOSCA service template) must be known.

From this observation, it follows that in order to modify a deployed
service instance, only the externally visible aspects of that service
instance should be modifiable. Specifically, this means that a service
modification could involve modifying service input values, modifying
the service template, or both. This leads to the following two service
modification operations:

1.  ***Service Update***: A north-bound system *supplies new input
    values* to a running service topology without requesting any
    changes to the service topology.

2.  ***Service Upgrade***: A north-bound system *changes the service
    topology* of a running service by providing a new service template
    with an updated topology that needs to be applied to the service.

The next sections will explain how an orchestrator is expected to
handle service update and service upgrade requests, and how most (if
not all) service lifecycle management operations can be implemented
using service updates and service upgrades.

# Service Update

This section introduces orchestration functionality required to
support modifying deployed services and how this functionality can be
expressed in TOSCA service templates.

## Modify Interface Operation

As discussed above, one option for modifying services is for the
north-bound system to *supply updated input values* to a running
service.

Consider use example service shown in the following figure.

> ***\<\< Include a figure \>\>***

The service shown in the example consists of a single component
represented by a single TOSCA node. The service is updated as follows:

1.  A north-bound system sends a request to the orchestrator to update a
    service. The request includes a set of updated input values for the
    service.
2.  In response to the request, the orchestrator retrieves the service
    instance that needs to be modified from the service instance
    repository.
3.  The orchestrator also retrieves the service template from which this
    service instance was created from the service catalog.
4.  The orchestrator propagates the new input values to property values
    in nodes in the service (as specified by the **get_input** intrinsic
    function). This results in an updated service instance model.
5.  At this point, the orchestrator must reflect changes into the
    external systems. TOSCA orchestrators do this by comparing the new
    updated service instance model with the previous model of the
    running system to determine which node properties have changed and
    applying those changes to the corresponding external system
    component by calling the appropriate interface operation on the
    node.

Applying configuration changes to a running service component requires
the addition of a **modify** operation to the standard lifecycle
management interface. The updated interface type definition is shown
here:

```yaml
interface_types:
  LifeCycleManagement:
    derived_from: tosca.interfaces.node.lifecycle.Standard
    operations:
      modify:
        description: Standard lifecycle modify operation.
```

Node types that define the standard lifecycle management interface
must also define input parameters for the **modify** operation. Note
that in general, these input parameters will be defined as optional,
since the orchestrator will only supply those parameters that reflect
properties that have changed in the corresponding node instance.

## Declarative Update Workflows

In a model-driven orchestration system, orchestrators propagate
changes to a service instance model by running workflows that call
interface operations on nodes and relationships in the service
topology. Ideally, these workflows are declarative, meaning they are
automatically generated by the orchestrator, based on dependencies
reflected in the service topology. Just like a TOSCA orchestrator is
expected to create declarative **deploy** workflows that call
**create**, **configure**, and **start** operations on nodes in the
service topology, the orchestrator is also expected to create
declarative **update** workflows that call **modify** operations on
affected nodes. Orchestrators use the same logic for ordering steps in
**update** workflows as for ordering steps in **deploy** workflows.

# Service Upgrade

A second set of modifications consists of applying a new service
template to a running service instance. The common use case for this
type of modification is to upgrade a service to a newer version.

Service upgrades may change the service topology by adding or removing
nodes, by adding or removing relationships, or both. In addition,
properties may be added to or removed from previously existing nodes.

To explore service upgrades in more detail, let’s start from the example
in the previous section. Let’s assume that as part of a version upgrade,
a new service template is applied to the running service that adds a new
node in the service topology as shown in the following figure:

\<\< Include a figure \>\>

An orchestrator handles service modification resulting from service
upgrades as follows:

1.  A north-bound system sends a request to the orchestrator to modify
    the topology of a running service instance. The request includes a
    reference to an updated service template that needs to be applied to
    the running service. It also includes any input values that may be
    needed by nodes or relationships that were added to the topology.
2.  In response to the request, the orchestrator retrieves the service
    instance that needs to be modified from its service instance
    repository.
3.  The orchestrator also retrieves (from the service catalog) the
    service template from which this service instance was created.
4.  The orchestrator creates an updated service instance model that
    reflects the upgraded service topology.
5.  The orchestrator then creates a **diff** between the updated
    service instance model and the service instance model of the
    running service. This diff could include:

    - a set of nodes that need to be added to the service topology
    - a set of nodes that need to be removed from the service topology
    - a set of relationships that need to be added to the service topology
    - a set of relationships that need to be removed from the service
      topology
    - a set of nodes that are in both the old as well as in the new service
      topology, but that have updated property values
    - a set of relationships that are in both the old as well as in the new
      service topology, but that have updated property values

6.  Based on this diff, the orchestrator creates an **upgrade** workflow
    that will be used to achieve the desired service topology
    modifications. This workflow could call:

    - create, config, and start operations for the nodes that need to be
      added
    - stop and delete operations for the nodes that need to be removed
    - configuration operations for the relationships that need to be added
    - modify operations for the nodes that need to be changed
    - modify operation for the relationships that need to be changed

7.  The orchestrator then runs the **upgrade** workflow by invoking
    these operations. Assuming the workflow returns successfully, the
    orchestrator stores the upgraded service instance model in its
    service instance repository.

Note that the **upgrade** workflow is similar to the **update** workflow
introduced in the previous section, since it only calls operations on
nodes and relationships that have changed. However, it is also more
complex than the **update** workflow, since rather than just modifying
nodes it may also have to create and delete nodes.

# Complex Scenarios

The examples shown in the previous sections resulted in simple update
and upgrade workflows. In practice, however, the actual modification
functionality that may need to be implemented can be much more complex
because of cascading modifications. For example:

1.  Property modifications in one node may result in property changes in
    other nodes in the topology that have a relationship with the
    modified node and use **get_property** functions to propagate
    property values across the topology. The orchestrator must check all
    nodes that have a relationship to the modified node for cascading
    property value changes.
2.  Updated input values may require the orchestrator to reestablish
    relationships when these input values are used in node filters and
    when the resources that were initially used to fulfill the
    requirement no longer satisfy the constraints specified in the
    updated node filter
3.  Property modifications in a node of an abstract service result in
    new input values in a substituting service.
4.  Property modifications in a node of an abstract service may require
    the orchestrator to select a different substituting service template
    when the modified property values no longer satisfy the substitution
    filter of the substituting template.

As this example shows, modifying property values of a single node may
impact the entire service topology, since updated input values can
result in:

- New configuration values for a service component
- Different decomposition of a service component
- New resource requirements
- New service topology

As a result, simple modifications to property values of a single node
may require the orchestrator to re-calculate the entire service topology
as follows:

1.  Update the properties with the new input values (as specified using
    **get_input** intrinsic functions).
2.  If necessary, re-do substitution mapping (since substitution filters
    may no longer be satisfied).
3.  If necessary, re-do requirement fulfillment (since new
    sub-topologies may have been created or since node filters may no
    longer be satisfied).

What this means is that in practice, there will not be a distinction
between **update** and **upgrade** actions, since service update and
service upgrade actions can both result in updated service topologies.
As a result, only one single update/upgrade action must be supported in
the orchestrator API, and only one single associated update/upgrade
implementation is required to handle both service update and service
upgrade scenarios. In the remainder of this document, we will simply
refer to service **update** actions rather than update/upgrade actions.

\<\< More detailed examples to be provided\>\>

# Mapping Lifecycle Management Operations to Service Update

What this means, then, is that an orchestrator that provides
model-driven lifecycle management must support an API that includes the
following three *standard* lifecycle management operations:

1.  Create

2.  Update

3.  Delete

As stated earlier, most if not all other lifecycle management operations
can ultimately be implemented using a combination of these canonical
update operation. The following examples show how a canonical update
action can be used to implement the various lifecycle management actions
defined by ETSI NFV:

## Operate VNF

The Operate VNF action is designed to stop or restart a running service.
This can be implemented by a generic update action as follows:

- Define an **operating_state** property on VNFs with the following two
  possible values:

  - Running
  - Stopped

  The value for this **operating_state** property is retrieved using a
  **get_input** function

- Define a corresponding **operating_state** input that can be changed
  by administrators using the update action. When the
  **operating_state** is modified, the modify operation on the VNF node
  will stop and/or restart the VNF.

## Modify VNF Information

This operation allows updating configuration information about a VNF
instance. It maps most closely onto the update action, since it is
designed to provide changes to configuration values of the various VNF
components.

## Scale VNF

This operation allows an external system or user to request that the
orchestrator perform a scaling procedure. This can be implemented by a
generic update action as follows:

- Define a **number_of_instances** property that reflects how many
  instances of the various VNF components are intended to be running.
  The value of this property is retrieved using a **get_input**
  function.

- Define a corresponding **number_of_instances** input that can be
  changed by administrators using the update action. When the
  **number_of_instances** is modified, the modify operation on the VNF
  node will add or remove running instances.

## Change VNF Flavor

This operation changes the *Deployment Flavor* of a VNF instance. ETSI
NFV supports multiple deployment flavors using the TOSCA substitution
mapping feature.

Changing deployment flavors can be implemented using a generic update
action as follows:

- Define a **flavor_id** property that reflects which deployment flavor
  is intended to be selected. The value of this property is retrieved
  using a **get_input** function.
- Define a corresponding **flavor_id** input that can be changed by
  administrators using the update action.
- Each of the various deployment flavor templates for the VNF must—in
  its **substitution_mappings** section—define a **substitution_filter**
  that specifies the value of the **flavor_id** property for which it is
  a valid substitution.
- When the **flavor_id** of a running VNF is changed by an external
  user, the orchestrator must check if the selected deployment flavor
  template is still a valid substitution and, if not, redo the
  substitution mapping with an updated deployment flavor template.

## Heal VNF

This operation allows and external administrator to request that an
orchestrator perform a VNF healing procedure. This can be implemented
using a generic update action as follows:

- Define a **vnf_health** property that reflects the health of a VNF.
  The value of this property is retrieved using a **get_input**
  function.
- Define a corresponding **flavor_id** input that can be changed by
  administrators using the update action.
- Various health monitoring operations can be provided (using TOSCA
  Interface Notifications) that update this **vnf_health** property (or
  more accurately, the corresponding **vnf_health** attribute) in
  response to external failures.
- Whenever the **vnf_health** reflects a failure state, external users
  can attempt to heal the VNF by resetting the **vnf_health** property
  value to active. When the **vnf_health** is modified, the modify
  operation on the VNF node will attempt the heal the VNF (e.g. by
  rebooting some or all of its components).

## Change External VNF connectivity

This operation enables changing the external connectivity of a VNF
instance. This operation is used to disconnect the external Connection
Points that are connected to a particular external Virtual Link and
connect them to a different external Virtual Link. This can be
implemented using a generic update action as follows:

- Using TOSCA, the need to connect a VNF to a (presumable
  already-existing) external Virtual Link is modeled using dangling
  requirements on VNF nodes that must be fulfilled by the orchestrator
  at VNF deployment time. VNF designers use node filters in these
  dangling requirements to specify information about the Virtual Links
  to which the VNF must be connected.
- To allow dynamic reconfiguration of external connectivity, the
  constraints specified in node filters must use dynamic information
  that can be provided by external administrators using input values.
- To change external connectivity, administrator provide updated input
  values that reflect information about the new Virtual Link to which
  the VNF must be connected. In response to these updated values, the
  orchestrator reevaluates the node filters in the dangling requirements
  to check if selected external Virtual Links still satisfy the
  constraints specified in the node filter. If not, the orchestrator
  must disconnect from the previously selected Virtual Link and
  reconnect using the newly selected Virtual Link.

# Orchestration Support for Service Update

This section provides more detail about the orchestration functionality
required to support service updates. As the discussion above
illustrates, service updates cannot be performed by simply running
workflows since one or more of the following orchestration tasks may
need to be performed as well:

- Deletion of nodes
- Creation of nodes
- Deallocation of existing resources
- Allocation of new resources
- Removing existing substitutions
- Establishing new substitutions.

When updating a service, the orchestrator must first determine which of
these actions need to be performed on which nodes and in which order.
This requires a separate planning phase during which the orchestrator
marks for each node in the topology the proper actions to be taken.

After the planning phase, the orchestrator performs the following:

1.  Run the **undeploy** workflow that calls the **stop** and **delete**
    actions for all the nodes that are marked for deleting.
2.  Deallocate the necessary resources for those nodes that are marked
    for resource deallocation.
3.  Remove substitutions for those abstract nodes that are marked for
    resubstituting.
4.  Substitute abstract nodes that are marked for resubstituting.
5.  Allocate resources for nodes that were marked for resource
    deallocation.
6.  Run the **update** workflow that calls the **modify** operation on
    nodes that are marked for modification as well as the **create**,
    **configure**, and **start** operations on any newly created nodes.
