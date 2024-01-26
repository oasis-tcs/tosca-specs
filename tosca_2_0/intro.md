- Position TOSCA as a language for automation and lifecycle
  management.

- TOSCA Uses model-driven approach. Explain what that means.

- TOSCA models systems as graphs, where the vertices represent the
  components of the system and the edges represents relationships,
  dependencies, and other interactions between these components.

- Fundamental abstraction in TOSCA is graph, which makes it suitable
  for any application domain. Any domain where systems can be modeled
  as graphs.

- Model-driven approach enables "declarative" orchestration, where
  system designers create descriptions ("models") of their systems,
  and it is the task of the orchestrator to translate descriptions
  into the commands to realize the systems being described.

- Declarative approach is used for all phases of a service lifecycle.

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
