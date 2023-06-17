|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|tosca_definitions_version|yes|string|Defines the version of the TOSCA specification used in the TOSCA file |
|profile|no|string|The profile name that can be used by other TOSCA files to import the type definitions in this document.|
|metadata|no|map of YAML values|Defines a section used to declare additional metadata information.  Domain-specific TOSCA profile specifications may define keynames that are mandatory for their implementations. |
|description|no|string|Declares a description for this TOSCA file and its contents.|
|dsl_definitions|no |N/A|Defines reusable YAML macros (i.e., YAML alias anchors) for use throughout the TOSCA file.|
|repositories|no|map of Repository definitions|Declares the map of external repositories that contain artifacts that are referenced in the TOSCA file along with the addresses used to connect to them in order to retrieve the artifacts.|
|imports|no|list of Import definitions|Declares a list of import statements pointing to external TOSCA files or well-known profiles. For example, these may be file locations or URIs relative to the TOSCA file within the same TOSCA CSAR file.|
|artifact_types|no|map of Artifact Types|This section contains amap of artifact type definitions for use in the TOSCA file and/or external TOSCA files.|
|data_types|no|map of Data Types|Declares a map of TOSCA Data Type definitions for use in the TOSCA file and/or external TOSCA files.|
|capability_types|no|map of Capability Types|This section contains amap of capability type definitions for use in the TOSCA file and/or external TOSCA files.|
|interface_types|no|map of Interface Types|This section contains amap of interface type definitions for use in the TOSCA file and/or external TOSCA files.|
|relationship_types|no|map of Relationship Types|This section contains a map of relationship type definitions for use in the TOSCA file and/or external TOSCA files.|
|node_types|no|map of Node Types|This section contains a map of node type definitions for use in the TOSCA file and/or external TOSCA files.|
|group_types|no|map of Group Types|This section contains a map of group type definitions for use in the TOSCA file and/or external TOSCA files.|
|policy_types|no|map of Policy Types|This section contains a map of policy type definitions for use in the TOSCA file and/or external TOSCA files.|
|service_template|no|service template definition|Defines a template from which to create a mode/representation of an application or service. Service templates consist of node templates that represent the application's or service's components, as well as relationship templates representing relations between these components.|
|functions|no|map of function definitions|This section contains a map of function definitions for use in the TOSCA file and/or external TOSCA files.|

# TOSCA Service Template

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|tosca_definitions_version|yes|string|Defines the version of the TOSCA specification used in the TOSCA file |
|profile|no|string|The profile name that can be used by other TOSCA files to import the type definitions in this document.|
|metadata|no|map of YAML values|Defines a section used to declare additional metadata information.  Domain-specific TOSCA profile specifications may define keynames that are mandatory for their implementations. |
|description|no|string|Declares a description for this TOSCA file and its contents.|
|dsl_definitions|no |N/A|Defines reusable YAML macros (i.e., YAML alias anchors) for use throughout the TOSCA file.|
|repositories|no|map of Repository definitions|Declares the map of external repositories that contain artifacts that are referenced in the TOSCA file along with the addresses used to connect to them in order to retrieve the artifacts.|
|imports|no|list of Import definitions|Declares a list of import statements pointing to external TOSCA files or well-known profiles. For example, these may be file locations or URIs relative to the TOSCA file within the same TOSCA CSAR file.|
|artifact_types|no|map of Artifact Types|This section contains amap of artifact type definitions for use in the TOSCA file and/or external TOSCA files.|
|data_types|no|map of Data Types|Declares a map of TOSCA Data Type definitions for use in the TOSCA file and/or external TOSCA files.|
|capability_types|no|map of Capability Types|This section contains amap of capability type definitions for use in the TOSCA file and/or external TOSCA files.|
|interface_types|no|map of Interface Types|This section contains amap of interface type definitions for use in the TOSCA file and/or external TOSCA files.|
|relationship_types|no|map of Relationship Types|This section contains a map of relationship type definitions for use in the TOSCA file and/or external TOSCA files.|
|node_types|no|map of Node Types|This section contains a map of node type definitions for use in the TOSCA file and/or external TOSCA files.|
|group_types|no|map of Group Types|This section contains a map of group type definitions for use in the TOSCA file and/or external TOSCA files.|
|policy_types|no|map of Policy Types|This section contains a map of policy type definitions for use in the TOSCA file and/or external TOSCA files.|
|service_template|no|service template definition|Defines a template from which to create a mode/representation of an application or service. Service templates consist of node templates that represent the application’s or service’s components, as well as relationship templates representing relations between these components.|
|Functions|no|map of function definitions|This section contains a map of function definitions for use in the TOSCA file and/or external TOSCA files.|


# Node Type

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|properties|no|map of property definitions|An optional map of property definitions for the Node Type.|
|attributes|no|map of attribute definitions|An optional map of attribute definitions for the Node Type.|
|capabilities|no|map of capability definitions|An optional map of capability definitions for the Node Type.|
|requirements|no|list of requirement definitions|An optional list of requirement definitions for the Node Type.|
|interfaces|no|map of interface definitions|An optional map of interface definitions supported by the Node Type.|
|artifacts|no|map of artifact definitions|An optional map of artifact definitions for the Node Type.|

# Node Template

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|type|yes|string|The mandatory name of the Node Type the Node Template is based upon.|
|description|no|string|An optional description for the Node Template.|
|metadata|no|map of string|Defines a section used to declare additional metadata information. |
|directives|no|list of string|An optional list of directive values to provide processing instructions to orchestrators and tooling.|
|properties|no|map of property assignments|An optional map of property value assignments for the Node Template.|
|attributes|no|map of attribute assignments|An optional map of attribute value assignments for the Node Template.|
|requirements|no|list of requirement assignments|An optional list of requirement assignments for the Node Template.|
|capabilities|no|map of capability assignments|An optional map of capability assignments for the Node Template.|
|interfaces|no|map of interface assignments|An optional map of interface assignments for the Node Template.|
|artifacts|no|map of  artifact definitions|An optional map of artifact definitions for the Node Template.|
|node_filter|no|node filter|The optional filter definition that TOSCA orchestrators will use to select the correct target node.  |
|copy|no|string|The optional (symbolic) name of another node template to copy into (all keynames and values) and use as a basis for this node template.|

# relationship type

|Keyname|Mandatory|Definition/Type|Description|
| :---- | :------ | :---- | :------ |
|properties|no|map of property definitions|An optional map of property definitions for the Relationship Type.|
|attributes|no|map of attribute definitions|An optional map of attribute definitions for the Relationship Type.|
|interfaces|no|map of interface definitions|An optional map of interface definitions supported by the Relationship Type.|
|valid_capability_types|no|list of string|An optional list of one or more names of Capability Types that are valid targets for this relationship. If undefined, all Capability Types are valid.|
|valid_target_node_types|no|list of string|An optional list of one or more names of Node Types that are valid targets for this relationship. If undefined, all Node Types are valid targets.|
|valid_source_node_types|no|list of string|An optional list of one or more names of Node Types that are valid sources for this relationship. If undefined, all Node Types are valid sources.|

# Relationship template

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|type|yes|string|The mandatory name of the Relationship Type the Relationship Template is based upon.|
|description|no|string|An optional description for the Relationship Template.|
|metadata|no|map of string|Defines a section used to declare additional metadata information. |
|properties|no|map of property assignments|An optional map of property assignments for the Relationship Template.|
|attributes|no|map of attribute assignments|An optional map of attribute assignments for the Relationship Template.|
|interfaces|no|map of interface assignments|An optional map of interface assignments for the relationship template.|
|copy|no|string|The optional (symbolic) name of another relationship template to copy into (all keynames and values) and use as a basis for this relationship template.|

# Capability Type

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|properties|no|map of property definitions|An optional map of property definitions for the Capability Type.|
|attributes|no|map of attribute definitions|An optional map of attribute definitions for the Capability Type.|
|valid_source_node_types|no|list of string|An optional list of one or more valid names of Node Types that are supported as valid sources of any relationship established to the declared Capability Type. If undefined, all Node Types are valid sources.|
|valid_relationship_types|no|list of string|An optional list of one or more valid names of Relationship Types that are supported as valid types of any relationship established to the declared Capability Type. If undefined, all Relationship Types are valid.|

# Capability Definition

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|type|yes|string|The mandatory name of the Capability Type this capability definition is based upon.|
|description|no|string|The optional description of the Capability definition.|
|properties|no|map of property refinements|An optional map of property refinements for the Capability definition. The referred properties must have been defined in the Capability Type definition referred by the type keyword. New properties may not be added.|
|attributes|no|map of attribute refinements|An optional map of attribute refinements for the Capability definition. The referred attributes must have been defined in the Capability Type definition referred by the type keyword. New attributes may not be added.|
|valid_source_node_types|no|list of string|An optional list of one or more valid names of Node Types that are supported as valid sources of any relationship established to the declared Capability Type. If undefined, all node types are valid sources. If valid_source_node_types is defined in the Capability Type, each element in this list must either be or derived from an element in the list defined in the type.|
|valid_relationship_types|no|list of string|An optional list of one or more valid names of Relationship Types that are supported as valid types of any relationship established to the declared Capability Type. If undefined, all Relationship Types are valid. If valid_relationship_types is defined in the Capability Type, each element in this list must either be or derived from an element in the list defined in the type.|

# Capability assignment

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|properties|no|map of  property assignments|An optional map of property assignments for the Capability definition.|
|attributes|no|map of attribute assignments|An optional map of attribute assignments for the Capability definition.|
|directives|no default: [internal, external] |list of string valid string values: “internal”, “external”|"Describes if the fulfillment of this capability assignment should use relationships with source nodes created within this template (“internal”) or should use source nodes created outside this template as available to the TOSCA environment (""external”) or if it should use a combination of the above. If so, the order of the strings in the list defines which scope should be attempted first. If no scope is defined, the default value is [internal, external]. If no directives are defined, the default value is left to the particular implementation."|

# Requirement definition

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|description|no|string|The optional description of the Requirement definition.|
|capability|yes|string|The mandatory keyname used to provide either the: ·         symbolic name of a Capability definition within a target Node Type that can fulfill the requirement. ·         name of a Capability Type that the TOSCA orchestrator will use to select a type-compatible target node to fulfill the requirement at runtime. |
|node|conditional|string|The optional keyname used to provide the name of a valid Node Type that contains the capability definition that can be used to fulfill the requirement.  If a symbolic name of a Capability definition has been used for the capability keyname, then the node keyname is mandatory.|
|relationship|conditional|string|The optional keyname used to provide the name of a valid Relationship Type to construct a relationship when fulfilling the requirement.  The relationship definition is mandatory either in the requirement definition of in the requirement assignment.|
|node_filter|no|node filter|The optional filter definition that TOSCA orchestrators will use to select a type-compatible target node that can fulfill the associated abstract requirement at runtime.|
|count_range|no|range of integer|The optional minimum required and maximum allowed number of relationships created by the requirement. If this key is not specified, the implied default of [0, UNBOUNDED] will be used. Note: the keyword UNBOUNDED is also supported to represent any positive integer.|

# Requirement Assignment

|Keyname|Mandatory|Type|Description|
| :---- | :------ | :---- | :------ |
|capability|no|string|The optional keyname used to provide either the: ·         symbolic name of a Capability definition within a target node that can fulfill the requirement. ·         name of a Capability Type that the TOSCA orchestrator will use to select a type-compatible target node to fulfill the requirement at runtime. |
|node|no|string|The optional keyname used to identify the target node of a relationship; specifically, it is used to provide either the: ·         name of a Node Template that can fulfill the target node requirement. ·         name of a Node Type that the TOSCA orchestrator will use to select a type-compatible target node to fulfill the requirement at runtime.|
|relationship|conditional|string|The conditional keyname used to provide either the: ·         name of a Relationship Template to use to relate this node to the target node when fulfilling the requirement. ·         name of a Relationship Type that the TOSCA orchestrator will use to create a relationship to relate this node to the target node when fulfilling the requirement. ·         Details of a Relationship Type and its property and interface assignments that the TOSCA orchestrator will use to create a relationship to relate this node to the target node when fulfilling the requirement. The relationship definition is mandatory either in the requirement definition of in the requirement assignment.|
|allocation|no|allocation block|The optional keyname that allows the inclusion of an allocation block. The allocation block contains a map of property assignments that semantically represent “allocations” from the property with the same name in the target capability.  ·         The allocation acts as a “capacity filter” for the target capability in the target node. When the requirement is resolved, a capability in a node is a valid target for the requirement relationship if for each property of the target capability, the sum of all existing allocations plus the current allocation is less_or_equal to the property value.|
|node_filter|no|node filter|The optional filter definition that TOSCA orchestrators will use to select a type-compatible target node that can fulfill the requirement at runtime.|
|count|no|non-negative integer|An optional keyname that sets the cardinality of the requirement assignment, that is how many relationships to be established from this requirement assignment specification. If not defined, the assumed count for an assignment is 1. Note that there can be multiple requirement assignments for a requirement with a specific symbolic name.  ·         The sum of all count values of assignments for a requirement with a specific symbolic name must be within the count_range defined in the requirement definition. ·         Moreover, the sum of all count values of non-optional assignments for a requirement with a specific symbolic name must also be within the count_range defined in the requirement definition.|
|directives|no|list of string valid string values: “internal”, “external”|"Describes if the fulfillment of this requirement assignment should use relationships with target nodes created within this template (“internal”) or should use target nodes created outside this template as available to the TOSCA environment (""external”) or if it should use a combination of the above. If so, the order of the strings in the list defines which directive should be attempted first. If no directives are defined, the default value is left to the particular implementation."|
|optional|no. default: FALSE|boolean|Describes if the fulfillment of this requirement assignment is optional (true) or not (false).  If not specified, the requirement assignment must be fulfilled, i.e. the default value is false.  Note also, that non-optional requirements have precedence, thus during a service deployment, the optional requirements for all nodes should be resolved only after the non-optional requirements for all nodes have been resolved.|

# Requirement Assignment Extra

Keyname|Mandatory|Type|Description
type|no|string|The optional keyname used to provide the name of the Relationship Type for the Requirement assignment’s relationship.
properties|no|map of property assignments|An optional keyname providing property assignments for the relationship.
|||
interfaces|no|map of interface assignments|The optional keyname providing Interface assignments for the corresponding Interface definitions in the Relationship Type.
|||
