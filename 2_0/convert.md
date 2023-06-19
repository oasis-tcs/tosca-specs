|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
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

# Interface Definition

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|type|yes|string|The mandatory name of the Interface Type this interface definition is based upon.|
|description|no|string|The optional description for this interface definition.|
|inputs|no|map of parameter definitions and refinements|The optional map of input parameter refinements and new input parameter definitions available to all operations defined for this interface (the input parameters to be refined have been defined in the Interface Type definition).|
|operations|no|map of operation refinements|The optional map of operations refinements for this interface. The referred operations must have been defined in the Interface Type definition.|
|notifications|no|map of notification refinements|The optional map of notifications refinements for this interface. The referred operations must have been defined in the Interface Type definition.|

# Operation Definition

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|description|no|string|The optional description string for the associated operation.|
|implementation|no|operation implementation definition|The optional definition of the operation implementation. May not be used in an interface type definition (i.e. where an operation is initially defined), but only during refinements. |
|inputs|no|map of parameter definitions|The optional map of parameter definitions for operation input values.|
|outputs|no|map of parameter definitions|The optional map of parameter definitions for operation output values. Only as part of node and relationship type definitions, the output definitions may include mappings onto attributes of the node or relationship type that contains the definition.|

# Operation Assignment

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|implementation|no|operation implementation definition|The optional definition of the operation implementation. Overrides implementation provided at operation definition.|
|inputs|no|map of parameter value assignments|The optional map of parameter value assignments for assigning values to operation inputs. |
|outputs|no|map of parameter mapping assignments|The optional map of parameter mapping assignments that specify how operation outputs are mapped onto attributes of the node or relationship that contains the operation definition. |

# Notification Definition

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|description|no|string|The optional description string for the associated notification.|
|implementation|no|notification implementation definition|The optional definition of the notification implementation.|
|outputs|no|map of parameter definitions|The optional map of parameter definitions that specify notification output values.  Only as part of node and relationship type definitions, the output definitions may include their mappings onto attributes of the node type or relationship type that contains the definition. |

# Notification Assignment

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|implementation|no|notification implementation definition|The optional definition of the notification implementation. Overrides implementation provided at notification definition.|
|outputs|no|map of parameter mapping assignments|The optional map of parameter mapping assignments that specify how notification outputs values are mapped onto attributes of the node or relationship type that contains the notification definition.|
|||||

# Operation Implementation

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|primary|no|artifact definition|The optional implementation artifact (i.e., the primary script file within a TOSCA CSAR file).  |
|dependencies|no|list of  artifact definition|The optional list of one or more dependent or secondary implementation artifacts which are referenced by the primary implementation artifact (e.g., a library the script installs or a secondary script).  |
|timeout|no|integer|Timeout value in seconds. Has no meaning and should not be used within a notification implementation definition.|

# Artifact Type

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|mime_type|no|string|The optional mime type property for the Artifact Type.|
|file_ext|no|list of string|The optional file extension property for the Artifact Type.|
|properties|no|map of property definitions|An optional map of property definitions for the Artifact Type.|
|||||

# Artifact Definition

|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|type|yes|string|The mandatory artifact type for the artifact definition.|
|file|yes|string|The mandatory URI string (relative or absolute) which can be used to locate the artifact’s file.|
|repository|no|string|The optional name of the repository definition which contains the location of the external repository that contains the artifact.  The artifact is expected to be referenceable by its file URI within the repository.|
|description|no|string|The optional description for the artifact definition.|
|deploy_path|no|string|The file path the associated file will be deployed on within the target node’s container. |
|artifact_version|no|string|The version of this artifact. One use of this artifact_version is to declare the particular version of this artifact type, in addition to its mime_type (that is declared in the artifact type definition). Together with the mime_type it may be used to select a particular artifact processor for this artifact. For example, a python interpreter that can interpret python version 2.7.0.|
|checksum|no|string|The checksum used to validate the integrity of the artifact.|
|checksum_algorithm|no|string|Algorithm used to calculate the artifact checksum (e.g. MD5, SHA [Ref]). Shall be specified if checksum is specified for an artifact.|
|properties|no|map of property assignments|The optional map of property assignments associated with the artifact.|
