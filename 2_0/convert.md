|Keyname|Mandatory|Type|Description|
| ----- | ------- | ----- | ------- |
|tosca_definitions_version|yes|string|Defines the version of the TOSCA specification used in the TOSCA file |

## Schema Definition

Keyname|Mandatory|Type|Description
type|yes|string|The mandatory data type for the key or entry. If this schema definition is for a map key, then the referred type must be derived originally from string.
|||
description|no|string|The optional description for the schema.
validation|no|validation clauses\|The optional validation clause that must evaluate to True for the property.
key_schema|no (default: string)|schema definition|When the schema itself is of type map, the optional schema definition that is used to specify the type of the keys of that map’s entries (if key_schema is not defined it is assumed to be “string” by default). For other schema types, the key_schema must not be defined.
entry_schema|conditional|schema definition|When the schema itself is of type map or list, the schema definition is mandatory and is used to specify the type of the entries in that map or list. For other schema types, the entry_schema must not be defined.

## Property Definition

Keyname|Mandatory|Type|Description
type|yes|string|The mandatory data type for the property.
description|no|string|The optional description for the property.
required|No (default: true)|boolean|An optional key that declares a property as required (true) or not (false). Defaults to true.
|||
default|no|<must match property type>|An optional key that may provide a value to be used as a default if not provided by another means.  The default keyname SHALL NOT be defined when property is not required (i.e. the value of the required keyname is false).
|||
value|no|<see below>|An optional key that may provide a fixed value to be used. A property that has a fixed value provided (as part of a definition or refinement) cannot be subject to a further refinement or assignment. That is, a fixed value cannot be changed.
status|No (default: supported)|string|The optional status of the property relative to the specification or implementation. See table below for valid values. Defaults to supported.
|||
validation|no|validation clause|The optional validation clause for the property.
key_schema|conditional (default: string)|schema definition|The schema definition for the keys used to identify entries in properties of type TOSCA map (or types that derive from map). If not specified, the key_schema defaults to string. For properties of type other than map, the key_schema is not allowed. 
entry_schema|conditional|schema definition|The schema definition for the entries in properties of TOSCA collection types such as list, map, or types that derive from list or map) If the property type is a collection type, the entry schema is mandatory. For other types, the entry_schema is not allowed.
external-schema|no|string|The optional key that contains a schema definition that TOSCA Orchestrators MAY use for validation when the “type” key’s value indicates an External schema (e.g., “json”). See section “External schema” below for further explanation and usage.
|||
metadata|no|map of string|Defines a section used to declare additional metadata information. 

## Attribute Definition

Keyname|Mandatory|Type|Description
type|yes|string|The mandatory data type for the attribute.
description|no|string|The optional description for the attribute.
default|no|<any>|An optional key that may provide a value to be used as a default if not provided by another means.  This value SHALL be type compatible with the type declared by the attribute definition’s type keyname.
|||
|||
status|no|string|The optional status of the attribute relative to the specification or implementation.  See supported status values . Defaults to supported.
validation|no|validation clause|The optional validation clause for the attribute.
key_schema|conditional (default: string)|schema definition|The schema definition for the keys used to identify entries in attributes of type TOSCA map (or types that derive from map). If not specified, the key_schema defaults to string. For attributes of type other than map, the key_schema is not allowed. 
entry_schema|conditional|schema definition|The schema definition for the entries in attributes of TOSCA collection types such as list, map, or types that derive from list or map) If the attribute type is a collection type, the entry schema is mandatory. For other types, the entry_schema is not allowed.
metadata|no|map of string|Defines a section used to declare additional metadata information. 

## Parameter Definition

Keyname|Mandatory|Type|Description
type|no|string|The data type of the parameter. Note: This keyname is mandatory for a TOSCA Property definition but is not mandatory for a TOSCA Parameter definition.
|||
|||
value|no|<any>|The type-compatible value to assign to the parameter.  Parameter values may be provided as the result from the evaluation of an expression or a function. May only be defined for outgoing parameters. Mutually exclusive with the “mapping” keyname.
mapping|no|attribute selection format|A mapping that specifies the node or relationship attribute into which the returned output value must be stored. May only be defined for incoming parameters. Mutually exclusive with the “value” keyname.

## Attribute Selection Format

Parameter|Mandatory|Description
<tosca_traversal_path>|yes|Using the <tosca_traversal_path> we can traverse the representation graph to reach the attribute we need to store the output value into. The specification of the <tosca_traversal_path> is explicated in section 6.1.2 get_property. Note that while the <tosca_traversal_path> is very powerful, its usage should normally be restricted to reach attributes in the local node ore relationship (i.e. SELF) or in a local capability definition.
||
||
<attribute_name> |yes|The name of the attribute into which the output value must be stored.
<nested_attribute_name_or_index_or_key_*> |no|Some TOSCA attributes are complex (i.e., composed as nested structures).  These parameters are used to dereference into the names of these nested structures when needed.   Some attributes represent list or map types. In these cases, an index or key may be provided to reference a specific entry in the list or map (identified by the previous parameter). 
||

## Group Type

Keyname|Mandatory|Type|Description
properties|no|map of property definitions|An optional map of property definitions for the Group Type.
|||
attributes|no|map of attribute definitions|An optional map of attribute definitions for the Group Type.
|||
members |no|list of string|An optional list of one or more names of Node Types that are valid (allowed) as members of the Group Type.

## Group Definition

Keyname|Mandatory|Type|Description
type|yes|string|The mandatory name of the group type the group definition is based upon.
description|no|string|The optional description for the group definition.
metadata|no|map of string|Defines a section used to declare additional metadata information. 
properties|no|map of property assignments|An optional map of property value assignments for the group definition.
|||
attributes|no|map of attribute assignments|An optional map of attribute value assignments for the group definition.
|||
members|no|list of string|The optional list of one or more node template names that are members of this group definition.

## Policy Type
Keyname|Mandatory|Type|Description
properties|no|map of property definitions|An optional map of property definitions for the Policy Type.
|||
targets|no|list of string|An optional list of valid Node Types or Group Types the Policy Type can be applied to.
|||
triggers|no|map of trigger definitions |An optional map of policy triggers for the Policy Type.

## Policy Definition
Keyname|Mandatory|Type|Description
type|yes|string|The mandatory name of the policy type the policy definition is based upon.
description|no|string|The optional description for the policy definition.
metadata|no|map of string|Defines a section used to declare additional metadata information. 
properties|no|map of property assignments|An optional map of property value assignments for the policy definition.
|||
targets|no|list of string|An optional list of valid Node Templates or Groups the Policy can be applied to.
|||
triggers|no|map of trigger definitions|An optional map of trigger definitions to invoke when the policy is applied by an orchestrator against the associated TOSCA entity. These triggers apply in addition to the triggers defined in the policy type.

## Delegate Workflow Activity
Keyname|Mandatory|Type|Description
delegate|yes|string or empty  (see grammar below)|Defines the name of the delegate workflow and optional input assignments. This activity requires the target to be provided by the orchestrator (no-op node or relationship).
|||
workflow|no|string|The name of the delegate workflow. Mandatory in the extended notation.
inputs|no|map of parameter assignments|The optional map of input parameter assignments for the delegate workflow.

## Call operation Activity
Keyname|Mandatory|Type|Description
call_operation|yes|string or empty (see grammar below)|Defines the opration call. The operation name uses the <interface_name>.<operation_name> notation. Optionally, assignments for the operation inputs can also be provided. If provided, they will override for this operation call the operation inputs assignment in the node template.
|||
operation|no|string|The name of the operation to call, using the <interface_name>.<operation_name> notation.  Mandatory in the extended notation.
|||
inputs|no|map of parameter assignments|The optional map of input parameter assignments for the called operation. Any provided input assignments will override the operation input assignment in the target node template for this operation call.

## Inline Workflow Activity
Keyname|Mandatory|Type|Description
inline|yes|string or empty (see grammar below)|The definition includes the name of a workflow to be inlined and optional workflow input assignments.
|||
workflow|no|string|The name of the inlined workflow. Mandatory in the extended notation.
inputs|no|map of parameter assignments|The optional map of input parameter assignments for the inlined workflow.
|||

## Tosca Workflow Definition
Keyname|Mandatory|Type|Description
description|no|string|The optional description for the workflow definition.
metadata|no|map of string|Defines a section used to declare additional metadata information. 
inputs|no|map of parameter definitions|The optional map of input parameter definitions.
|||
precondition|no|condition clause|Condition clause that must evaluate to true before the workflow can be processed.
steps|no|map of step definitions|An optional map of valid imperative workflow step definitions.
|||
implementation|no|operation implementation definition|The optional definition of an external workflow definition. This keyname is mutually exclusive with the steps keyname above.
outputs|no|map of attribute mappings|The optional map of attribute mappings that specify workflow  output values and their mappings onto attributes of a node or relationship defined in the service.
|||

## Workflow Step
Keyname|Mandatory|Type|Description
target|yes|string|The target of the step (this can be a node template name, a group name)
target_relationship|no|string|The optional name of a requirement of the target in case the step refers to a relationship rather than a node or group. Note that this is applicable only if the target is a node.
operation_host|no|string|The node on which operations should be executed (for TOSCA call_operation activities). This element is mandatory only for relationships and groups target. If target is a relationship then operation_host is mandatory and valid_values are SOURCE or TARGET – referring to the relationship source or target node. If target is a group then operation_host is optional. If not specified the operation will be triggered on every node of the group. If specified the valid_value is a node_type or the name of a node template.
|||
|||
|||
|||
|||
|||
|||
filter|no|list of validation clauses|Filter is a list of validation clauses that allows to provide a filtering logic.
activities|yes|list of activity definition|The list of sequential activities to be performed in this step.
on_success|no|list of string|The optional list of step names to be performed after this one has been completed with success (all activities has been correctly processed).
on_failure|no|list of string|The optional list of step names to be called after this one in case one of the step activity failed.

# get_input arguments
Argument|Mandatory|Type|Description
<input_parameter_name>|yes|string|The name of the parameter as defined in the inputs section of the service template.
<nested_input_parameter_name_or_index_*>|no|"string| integer"|Some TOSCA input parameters are complex (i.e., composed as nested structures).  These parameters are used to dereference into the names of these nested structures when needed.  Some parameters represent list types. In these cases, an index may be provided to reference a specific entry in the list (as identified by the previous parameter) to return. 
|||
|||

# get_property arguments
Argument|Mandatory|Description
< tosca_traversal_path >|yes|Using the <tosca_traversal_path> we can traverse the representation graph to extract information from a certain node or relationship. We start from a specific node or relationship identified by its symbolic name (or by the SELF keyword representing the node or relationship containing the definition) and then we may further traverse the relationships and nodes of the representation graph (using a variable number of steps) until reaching the desired node or relationship. In the following subsection the specification of the <tosca_traversal_path> is explicated.
<property_name>|yes|The name of the property definition the function will return the value from.
<nested_property_name_or_index_*> |no|Some TOSCA properties are complex (i.e., composed as nested structures).  These parameters are used to dereference into the names of these nested structures when needed.  Some properties represent list types. In these cases, an index may be provided to reference a specific entry in the list (as identified by the previous parameter) to return. 
||
||

# get_attribute arguments
Argument|Mandatory|Description
<tosca_traversal_path>|yes|Using the <tosca_traversal_path> we can traverse the representation graph to extract information from a certain node or relationship. We start from a specific node or relationship identified by its symbolic name (or by the SELF keyword representing the node or relationship containing the definition) and then we may further traverse the relationships and nodes of the representation graph (using a variable number of steps) until reaching the desired node or relationship. The specification of the <tosca_traversal_path> is explicated in the get_property section.
<attribute_name> |yes|The name of the attribute definition the function will return the value from.
<nested_attribute_name_or_index_*> |no|Some TOSCA attributes are complex (i.e., composed as nested structures).  These parameters are used to dereference into the names of these nested structures when needed.    Some attributes represent list types. In these cases, an index may be provided to reference a specific entry in the list (as identified by the previous parameter) to return. 
||
||

# get_artifact arguments
Argument|Mandatory|Type|Description
"<modelable entity name> | SELF | SOURCE | TARGET | HOST"|yes|string|The mandatory name of a modelable entity (e.g., Node Template or Relationship Template name) as declared in the service template that contains the property definition the function will return the value from. See section B.1 for valid keywords.
<artifact_name>|yes|string|The name of the artifact definition the function will return the value from.
"<location> | LOCAL_FILE"|no|string|Location value must be either a valid path e.g. ‘/etc/var/my_file’ or ‘LOCAL_FILE’. If the value is LOCAL_FILE the orchestrator is responsible for providing a path as the result of the get_artifact call where the artifact file can be accessed. The orchestrator will also remove the artifact from this location at the end of the operation. If the location is a path specified by the user the orchestrator is responsible to copy the artifact to the specified location. The orchestrator will return the path as the value of the get_artifact function and leave the file here after the execution of the operation.
|||
|||
|||
|||
remove|no|boolean|Boolean flag to override the orchestrator default behavior so it will remove or not the artifact at the end of the operation execution. If not specified the removal will depends of the location e.g. removes it in case of ‘LOCAL_FILE’ and keeps it in case of a path. If true the artifact will be removed by the orchestrator at the end of the operation execution, if false it will not be removed.
|||
|||
|||
|||

# value arguments
Argument|Mandatory|Description
<nested_value_name_or_index> |no|Some TOSCA data are complex (i.e., composed as nested structures).  These parameters are used to dereference into the names of these nested structures when needed.    Some data represent lists. In these cases, an index may be provided to reference a specific entry in the list (as identified by the previous parameter) to return. 
||

# join arguments

Argument|Mandatory|Type|Description
<list of  strings>|yes|list of string or string value expressions|A list of one or more strings (or expressions that result in a list of string values) which can be joined together into a single string.
|||
|||
<delimiter>|no|string|An optional delimiter used to join the string in the provided list.


