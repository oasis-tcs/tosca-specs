<img src="media/image1.png" style="width:3.21in;height:0.66in" />

TOSCA Version 2.0
<!----
{"id": "0", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T17:56:00Z", "comment": "I have\nprovided a number of comments. Some of these are pure editorial, e.g\nspelling, wording and cut and paste error correction. Other comments\nfall into these themes:  \nYAML is the only language  \nFolded comment style and double quotes  \nPolicy definition in general and period in particular  \nNode states  \nNormative types in examples  \nEnvironment variables and artefact arguments  \nGet_node_type and node filters  \nDocumentation of optional and required\nelements", "target": "0"}-->


Working Draft 06, Revision 02

19 February 2023

(URIs removed)

Technical Committee:

[OASIS Topology and Orchestration Specification for Cloud Applications
(TOSCA) TC](https://www.oasis-open.org/committees/tosca/)

Chairs:

Chris Lauwers (<lauwers@ubicity.com>), Individual Member

Editors:

Chris Lauwers (<lauwers@ubicity.com>), Individual Member

Calin Curescu (<calin.curescu@ericsson.com>),
[Ericsson](http://ericsson.com/)

Additional artifacts:

This prose specification is one component of a Work Product that also
includes:

- TBD - schemas?

- <span class="mark">(**Note:** Any normative computer language
  definitions that are part of the Work Product, such as XML instances,
  schemas and Java(TM) code, including fragments of such, must be (a)
  well-formed and valid, (b) provided in separate plain text files, (c)
  referenced from the Work Product; and (d) where any definition in
  these separate files disagrees with the definition found in the
  specification, the definition in the separate file prevails. Remove
  this note before submitting for publication.)</span>

Related work:

This specification replaces or supersedes:

- *Topology and Orchestration Specification for Cloud Applications
  Version 1.0*. Edited by Derek Palma and Thomas Spatzier. OASIS
  Standard. Latest version:
  <http://docs.oasis-open.org/tosca/TOSCA/v1.0/TOSCA-v1.0.html>.

- *TOSCA Simple Profile in YAML Version 1.3*. Edited by Matt Rutkowski,
  Chris Lauwers, Claude Noshpitz, and Calin Curescu. Latest version:
  <https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/TOSCA-Simple-Profile-YAML-v1.3.html>.

This specification is related to:

- *Introduction to TOSCA Version 2.0.* Edited by Chris Lauwers and Calin
  Curescu. Work in progress.

Declared XML namespaces:

- <http://docs.oasis-open.org/tosca/ns/2.0>

Abstract:

The OASIS TOSCA TC works to enhance the portability of cloud
applications and services across their entire lifecycle. TOSCA will
enable the interoperable description of application and infrastructure
cloud services, the relationships between parts of the service, and the
operational behavior of these services (e.g., deploy, patch, shutdown)
independent of the supplier creating the service or of any particular
cloud provider or hosting technology. TOSCA will also make it possible
for higher-level operational behavior to be associated with cloud
infrastructure management.

By increasing service and application portability in a vendor-neutral
ecosystem, TOSCA will enable:

- Portable deployment to any compliant cloud

- Smoother migration of existing applications to the cloud

- Flexible bursting (consumer choice)

- Dynamic, multi-cloud provider applications

Status:

This document was last revised or approved by the OASIS Topology and
Orchestration Specification for Cloud Applications (TOSCA) TC on the
above date. The level of approval is also listed above. Check the
“Latest stage” location noted above for possible later revisions of this
document. Any other numbered Versions and other technical work produced
by the Technical Committee (TC) are listed at
<https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca#technical>.

TC members should send comments on this specification to the TC’s email
list. Others should send comments to the TC’s public comment list, after
subscribing to it by following the instructions at the “[Send A
Comment](https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=tosca)”
button on the TC’s web page at
<https://www.oasis-open.org/committees/tosca/>.

This specification is provided under the [RF on Limited
Terms](https://www.oasis-open.org/policies-guidelines/ipr#RF-on-Limited-Mode)
Mode of the [OASIS IPR
Policy](https://www.oasis-open.org/policies-guidelines/ipr), the mode
chosen when the Technical Committee was established. For information on
whether any patents have been disclosed that may be essential to
implementing this specification, and any offers of patent licensing
terms, please refer to the Intellectual Property Rights section of the
TC’s web page (<https://www.oasis-open.org/committees/tosca/ipr.php>).

Note that any machine-readable content ([Computer Language
Definitions](https://www.oasis-open.org/policies-guidelines/tc-process#wpComponentsCompLang))
declared Normative for this Work Product is provided in separate plain
text files. In the event of a discrepancy between any such plain text
file and display content in the Work Product's prose narrative
document(s), the content in the separate plain text file prevails.

Citation format:

(removed)

Notices

Copyright © OASIS Open 2023. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned
to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR
Policy"). The full
[Policy](https://www.oasis-open.org/policies-guidelines/ipr) may be
found at the OASIS website.

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it or
assist in its implementation may be prepared, copied, published, and
distributed, in whole or in part, without restriction of any kind,
provided that the above copyright notice and this section are included
on all such copies and derivative works. However, this document itself
may not be modified in any way, including by removing the copyright
notice or references to OASIS, except as needed for the purpose of
developing any document or deliverable produced by an OASIS Technical
Committee (in which case the rules applicable to copyrights, as set
forth in the OASIS IPR Policy, must be followed) or as required to
translate it into languages other than English.

The limited permissions granted above are perpetual and will not be
revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS
IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE
INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

OASIS requests that any OASIS Party or any other party that believes it
has patent claims that would necessarily be infringed by implementations
of this OASIS Committee Specification or OASIS Standard, to notify OASIS
TC Administrator and provide an indication of its willingness to grant
patent licenses to such patent claims in a manner consistent with the
IPR Mode of the OASIS Technical Committee that produced this
specification.

OASIS invites any party to contact the OASIS TC Administrator if it is
aware of a claim of ownership of any patent claims that would
necessarily be infringed by implementations of this specification by a
patent holder that is not willing to provide a license to such patent
claims in a manner consistent with the IPR Mode of the OASIS Technical
Committee that produced this specification. OASIS may include such
claims on its website, but disclaims any obligation to do so.

OASIS takes no position regarding the validity or scope of any
intellectual property or other rights that might be claimed to pertain
to the implementation or use of the technology described in this
document or the extent to which any license under such rights might or
might not be available; neither does it represent that it has made any
effort to identify any such rights. Information on OASIS' procedures
with respect to rights in any document or deliverable produced by an
OASIS Technical Committee can be found on the OASIS website. Copies of
claims of rights made available for publication and any assurances of
licenses to be made available, or the result of an attempt made to
obtain a general license or permission for the use of such proprietary
rights by implementers or users of this OASIS Committee Specification or
OASIS Standard, can be obtained from the OASIS TC Administrator. OASIS
makes no representation that any information or list of intellectual
property rights will at any time be complete, or that any claims in such
list are, in fact, Essential Claims.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/),
the owner and developer of this specification, and should be used only
to refer to the organization and its official outputs. OASIS welcomes
reference to, and implementation and use of, specifications, while
reserving the right to enforce its marks against misleading uses. Please
see <https://www.oasis-open.org/policies-guidelines/trademark> for above
guidance.

Table of Contents

[1 Introduction [17](#introduction)](#introduction)

[1.1 IPR Policy [17](#ipr-policy)](#ipr-policy)

[1.2 Terminology [17](#terminology)](#terminology)

[1.3 Normative References
[17](#normative-references)](#normative-references)

[1.4 Non-Normative References
[17](#non-normative-references)](#non-normative-references)

[2 Overview [19](#overview)](#overview)

[2.1 Objective [19](#objective)](#objective)

[2.2 TOSCA Scope
[19](#tosca-this-section-has-been-moved-here-from-the-operational-model-chapter-in-the-previous-draft.-it-may-need-to-be-consolidated-with-the-objective-section-to-create-a-new-what-is-tosca-subsection.scope)](#tosca-this-section-has-been-moved-here-from-the-operational-model-chapter-in-the-previous-draft.-it-may-need-to-be-consolidated-with-the-objective-section-to-create-a-new-what-is-tosca-subsection.scope)

[2.3 Application Domains
[19](#application-domains)](#application-domains)

[2.4 Implementations [20](#implementations)](#implementations)

[2.5 Glossary [20](#glossary)](#glossary)

[3 TOSCA core concepts [21](#tosca-core-concepts)](#tosca-core-concepts)

[3.1 Service Templates, Node Templates, and Relationships
[21](#service-templates-node-templates-and-relationships)](#service-templates-node-templates-and-relationships)

[3.2 Interfaces, Operations, and Artifacts
[23](#interfaces-operations-and-artifacts)](#interfaces-operations-and-artifacts)

[3.3 Workflows [23](#workflows)](#workflows)

[3.4 Requirements and Capabilities
[23](#requirements-and-capabilities)](#requirements-and-capabilities)

[3.5 Decomposition of Service Templates
[24](#decomposition-of-service-templates)](#decomposition-of-service-templates)

[3.6 Policies in TOSCA [25](#policies-in-tosca)](#policies-in-tosca)

[3.7 Archive Format for Cloud Applications
[25](#archive-format-for-cloud-applications)](#archive-format-for-cloud-applications)

[3.8 TOSCA Entities
[26](#tosca-this-subsection-has-been-moved-here-from-the-operational-model-chapter.-we-need-to-revisit-where-exactly-it-belongs-to-make-sure-the-document-flows-correctly.alternatively-we-could-also-move-this-section-into-chapter-5entities)](#tosca-this-subsection-has-been-moved-here-from-the-operational-model-chapter.-we-need-to-revisit-where-exactly-it-belongs-to-make-sure-the-document-flows-correctly.alternatively-we-could-also-move-this-section-into-chapter-5entities)

[4 TOSCA Operational Model
[27](#tosca-operational-model)](#tosca-operational-model)

[4.1 TOSCA Processor [27](#tosca-processor)](#tosca-processor)

[4.1.1 Parser [27](#parser)](#parser)

[4.1.2 Resolver [27](#resolver)](#resolver)

[4.1.2.1 Creating Service Representations
[28](#creating-service-representations)](#creating-service-representations)

[4.1.2.2 Requirement Fulfillment
[28](#requirement-fulfillment)](#requirement-fulfillment)

[4.1.2.3 Substitution Mapping
[28](#substitution-mapping)](#substitution-mapping)

[4.2 Orchestrator [28](#orchestrator)](#orchestrator)

[5 TOSCA definitions [29](#tosca-definitions)](#tosca-definitions)

[5.1 TOSCA Metamodel
[29](#tosca-inconsistent-capitalizationthis-section-should-be-moved-into-the-previous-chapterwhat-is-a-metamodelmetamodel)](#tosca-inconsistent-capitalizationthis-section-should-be-moved-into-the-previous-chapterwhat-is-a-metamodelmetamodel)

[5.1.1 Modeling concepts and goals
[29](#this-section-needs-completion-before-submitting-the-tosca-2.0.modeling-concepts-and-goals)](#this-section-needs-completion-before-submitting-the-tosca-2.0.modeling-concepts-and-goals)

[5.1.2 Modeling definitions and reuse
[29](#modeling-definitions-and-reuse)](#modeling-definitions-and-reuse)

[5.1.3 Goal of the derivation and refinement rules
[30](#goal-of-the-derivation-and-refinement-rules)](#goal-of-the-derivation-and-refinement-rules)

[5.1.4 Mandatory Keynames
[30](#mandatory-keynames)](#mandatory-keynames)

[5.2 TOSCA Service
[30](#tbd.-here-comes-some-intro-and-generic-description-of-the-different-specification-blocks-that-will-build-the-following-sections.tosca-service)](#tbd.-here-comes-some-intro-and-generic-description-of-the-different-specification-blocks-that-will-build-the-following-sections.tosca-service)

[5.2.1 TOSCA file definition
[30](#update-to-reflect-new-namingtosca-file-definition)](#update-to-reflect-new-namingtosca-file-definition)

[5.2.1.1 Keynames [30](#keynames)](#keynames)

[5.2.1.2 Grammar
[31](#tal-do-we-even-need-these-grammar-sections-often-grammar-section-is-out-of-sync-with-keynames-section-and-notes-section-has-most-of-the-relevant-info.grammar)](#tal-do-we-even-need-these-grammar-sections-often-grammar-section-is-out-of-sync-with-keynames-section-and-notes-section-has-most-of-the-relevant-info.grammar)

[5.2.1.2.1 Requirements [32](#requirements)](#requirements)

[5.2.1.2.2 Notes
[32](#tosca-246-comments-captured-perhaps-need-an-advanced-concept-to-define-features-that-are-not-necessarily-attached-to-a-particular-node.-like-things-you-might-include-in-a-manifest.-like-the-requirement-for-a-global-time-sync.-how-do-we-reference-that-feature-where-is-that-feature-attached-to-some-node.-perhaps-add-a-new-keyword-like-cloud-that-can-hold-all-these-features-that-have-no-immediate-node-to-attach-them-to.-perhaps-a-syntax-convention-where-we-might-just-list-the-names-of-the-features-in-some-precedent-order-sequence.-need-to-answer--who-requires-it-who-fulfills-it-and-how-do-u-maintain-the-relationship-luc-environmental-requirements.-e.g.-python-or-something-similar.notes)](#tosca-246-comments-captured-perhaps-need-an-advanced-concept-to-define-features-that-are-not-necessarily-attached-to-a-particular-node.-like-things-you-might-include-in-a-manifest.-like-the-requirement-for-a-global-time-sync.-how-do-we-reference-that-feature-where-is-that-feature-attached-to-some-node.-perhaps-add-a-new-keyword-like-cloud-that-can-hold-all-these-features-that-have-no-immediate-node-to-attach-them-to.-perhaps-a-syntax-convention-where-we-might-just-list-the-names-of-the-features-in-some-precedent-order-sequence.-need-to-answer--who-requires-it-who-fulfills-it-and-how-do-u-maintain-the-relationship-luc-environmental-requirements.-e.g.-python-or-something-similar.notes)

[5.2.1.3 Top-level keyname definitions
[33](#top-level-keyname-definitions)](#top-level-keyname-definitions)

[5.2.1.3.1 tosca_definitions_version
[33](#tosca_definitions_version)](#tosca_definitions_version)

[5.2.1.3.1.1 Keyname [33](#keyname)](#keyname)

[5.2.1.3.1.2 Grammar [33](#grammar)](#grammar)

[5.2.1.3.1.3 Examples: [33](#examples)](#examples)

[5.2.1.3.2 profile
[33](#perhaps-this-should-be-its-own-sectionwhat-happens-if-files-imported-by-a-profile-file-also-defines-a-profileprofile)](#perhaps-this-should-be-its-own-sectionwhat-happens-if-files-imported-by-a-profile-file-also-defines-a-profileprofile)

[5.2.1.3.2.1 Keyname [33](#keyname-1)](#keyname-1)

[5.2.1.3.2.2 Grammar [33](#grammar-1)](#grammar-1)

[5.2.1.3.2.3 Examples [34](#examples-1)](#examples-1)

[5.2.1.3.3 metadata [34](#metadata)](#metadata)

[5.2.1.3.3.1 Keyname [34](#keyname-2)](#keyname-2)

[5.2.1.3.3.2 Grammar [34](#grammar-2)](#grammar-2)

[5.2.1.3.3.3 Example [34](#example)](#example)

[5.2.1.3.4 description [34](#description)](#description)

[5.2.1.3.4.1 Keyname [34](#keyname-3)](#keyname-3)

[5.2.1.3.4.2 Grammar [34](#grammar-3)](#grammar-3)

[5.2.1.3.4.3 Example [35](#example-1)](#example-1)

[5.2.1.3.5 dsl_definitions [35](#dsl_definitions)](#dsl_definitions)

[5.2.1.3.5.1 Keyname [35](#keyname-4)](#keyname-4)

[5.2.1.3.5.2 Grammar [35](#grammar-4)](#grammar-4)

[5.2.1.3.5.3 Example
[35](#there-should-also-be-an-example-of-how-to-use-the-macro-once-defined.example)](#there-should-also-be-an-example-of-how-to-use-the-macro-once-defined.example)

[5.2.1.3.6 repositories [35](#repositories)](#repositories)

[5.2.1.3.6.1 Keyname [35](#keyname-5)](#keyname-5)

[5.2.1.3.6.2 Grammar [35](#grammar-5)](#grammar-5)

[5.2.1.3.6.3 Example
[36](#this-example-is-repeated-in-4.2.3.2.3.-it-would-be-better-to-have-an-example-which-showed-multiple-repo-definitions-probably-using-a-mix-of-syntax-the-single-line-syntax.example)](#this-example-is-repeated-in-4.2.3.2.3.-it-would-be-better-to-have-an-example-which-showed-multiple-repo-definitions-probably-using-a-mix-of-syntax-the-single-line-syntax.example)

[5.2.1.3.7 imports [36](#imports)](#imports)

[5.2.1.3.7.1 Keyname [36](#keyname-6)](#keyname-6)

[5.2.1.3.7.2 Grammar [36](#grammar-6)](#grammar-6)

[5.2.1.3.7.3 Example [36](#example-2)](#example-2)

[5.2.1.3.8 artifact_types [36](#artifact_types)](#artifact_types)

[5.2.1.3.8.1 Keyname [36](#keyname-7)](#keyname-7)

[5.2.1.3.8.2 Grammar [36](#grammar-7)](#grammar-7)

[5.2.1.3.8.3 Example [36](#example-3)](#example-3)

[5.2.1.3.9 data_types [37](#data_types)](#data_types)

[5.2.1.3.9.1 Keyname [37](#keyname-8)](#keyname-8)

[5.2.1.3.9.2 Grammar [37](#grammar-8)](#grammar-8)

[5.2.1.3.9.3 Example [37](#example-4)](#example-4)

[5.2.1.3.10 capability_types [37](#capability_types)](#capability_types)

[5.2.1.3.10.1 Keyname [37](#keyname-9)](#keyname-9)

[5.2.1.3.10.2 Grammar [37](#grammar-9)](#grammar-9)

[5.2.1.3.10.3 Example [38](#example-5)](#example-5)

[5.2.1.3.11 interface_types [38](#interface_types)](#interface_types)

[5.2.1.3.11.1 Keyname [38](#keyname-10)](#keyname-10)

[5.2.1.3.11.2 Grammar [38](#grammar-10)](#grammar-10)

[5.2.1.3.11.3 Example [38](#example-6)](#example-6)

[5.2.1.3.12 relationship_types
[38](#relationship_types)](#relationship_types)

[5.2.1.3.12.1 Keyname [38](#keyname-11)](#keyname-11)

[5.2.1.3.12.2 Grammar [38](#grammar-11)](#grammar-11)

[5.2.1.3.12.3 Example [38](#example-7)](#example-7)

[5.2.1.3.13 node_types [39](#node_types)](#node_types)

[5.2.1.3.13.1 Keyname [39](#keyname-12)](#keyname-12)

[5.2.1.3.13.2 Grammar [39](#grammar-12)](#grammar-12)

[5.2.1.3.13.3 Example [39](#example-8)](#example-8)

[5.2.1.3.14 group_types [39](#group_types)](#group_types)

[5.2.1.3.14.1 Keyname [39](#keyname-13)](#keyname-13)

[5.2.1.3.14.2 Grammar [39](#grammar-13)](#grammar-13)

[5.2.1.3.14.3 Example
[39](#there-should-be-a-second-group-definition-in-the-example-or-it-is-just-a-repeat-of-the-group-type-def-exampleexample)](#there-should-be-a-second-group-definition-in-the-example-or-it-is-just-a-repeat-of-the-group-type-def-exampleexample)

[5.2.1.3.15 policy_types [40](#policy_types)](#policy_types)

[5.2.1.3.15.1 Keyname [40](#keyname-14)](#keyname-14)

[5.2.1.3.15.2 Grammar [40](#grammar-14)](#grammar-14)

[5.2.1.3.15.3 Example
[40](#there-should-be-a-second-policy-definition-in-the-example-or-it-is-just-a-repeat-of-the-policy-type-definition-exampleexample)](#there-should-be-a-second-policy-definition-in-the-example-or-it-is-just-a-repeat-of-the-policy-type-definition-exampleexample)

[5.2.2 Profiles [40](#profiles)](#profiles)

[5.2.2.1 Examples [40](#examples-2)](#examples-2)

[5.2.2.2 Defining Profiles [41](#defining-profiles)](#defining-profiles)

[5.2.2.3 Profile Versions [41](#profile-versions)](#profile-versions)

[5.2.3 Imports and Namespaces
[43](#i-dont-know-what-is-meant-by-references.imports-and-namespaces)](#i-dont-know-what-is-meant-by-references.imports-and-namespaces)

[5.2.3.1 Import definition
[43](#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition)](#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition)

[5.2.3.1.1 Keynames [43](#keynames-1)](#keynames-1)

[5.2.3.1.2 Grammar [43](#grammar-15)](#grammar-15)

[5.2.3.1.2.1 Single-line grammar:
[43](#single-line-grammar)](#single-line-grammar)

[5.2.3.1.2.2 Multi-line grammar
[43](#multi-line-grammar)](#multi-line-grammar)

[5.2.3.1.3 Import processing rules
[44](#import-processing-rules)](#import-processing-rules)

[5.2.3.1.3.1 Importing profiles
[44](#importing-profiles)](#importing-profiles)

[5.2.3.1.3.2 Importing service templates
[44](#importing-service-templates)](#importing-service-templates)

[5.2.3.1.4 Examples [45](#examples-3)](#examples-3)

[5.2.3.2 Namespaces
[45](#i-recommend-removing-this-entire-section-and-rewriting-any-parts-that-are-still-relevant-inside-the-imports-section.namespaces)](#i-recommend-removing-this-entire-section-and-rewriting-any-parts-that-are-still-relevant-inside-the-imports-section.namespaces)

[5.2.3.2.1 Additional Requirements
[48](#additional-requirements)](#additional-requirements)

[5.2.3.3 Repository definition
[48](#repository-definition)](#repository-definition)

[5.2.3.3.1 Keynames [48](#keynames-2)](#keynames-2)

[5.2.3.3.2 Grammar [49](#grammar-16)](#grammar-16)

[5.2.3.3.2.1 Single-line grammar:
[49](#single-line-grammar-1)](#single-line-grammar-1)

[5.2.3.3.2.2 Multi-line grammar
[49](#multi-line-grammar-1)](#multi-line-grammar-1)

[5.2.3.3.3 Example [49](#example-9)](#example-9)

[5.2.4 Additional information definitions
[49](#additional-information-definitions)](#additional-information-definitions)

[5.2.4.1 Description definition
[49](#description-is-already-described-in-4.2.1.3.6description-definition)](#description-is-already-described-in-4.2.1.3.6description-definition)

[5.2.4.1.1 Keyname [49](#keyname-15)](#keyname-15)

[5.2.4.1.2 Grammar [49](#grammar-17)](#grammar-17)

[5.2.4.1.3 Examples [49](#examples-4)](#examples-4)

[5.2.4.1.4 Notes [50](#notes)](#notes)

[5.2.4.2 Metadata
[50](#also-covered-by-4.2.1.3.2metadata)](#also-covered-by-4.2.1.3.2metadata)

[5.2.4.2.1 Keyname [50](#keyname-16)](#keyname-16)

[5.2.4.2.2 Grammar [50](#grammar-18)](#grammar-18)

[5.2.4.2.3 Examples [50](#examples-5)](#examples-5)

[5.2.4.2.4 Notes [50](#notes-1)](#notes-1)

[5.2.4.3 DSL Definitions
[50](#already-in-4.2.1.3.7dsl-definitions)](#already-in-4.2.1.3.7dsl-definitions)

[5.2.5 Type definitions [50](#type-definitions)](#type-definitions)

[5.2.5.1 General derivation and refinement rules
[51](#general-derivation-and-refinement-rules)](#general-derivation-and-refinement-rules)

[5.2.5.2 Common keynames in type definitions
[51](#common-keynames-in-type-definitions)](#common-keynames-in-type-definitions)

[5.2.5.2.1 Keynames [51](#keynames-3)](#keynames-3)

[5.2.5.2.2 Grammar [52](#grammar-19)](#grammar-19)

[5.2.5.2.3 Derivation rules [52](#derivation-rules)](#derivation-rules)

[5.2.6 Service template definition
[52](#service-template-definition)](#service-template-definition)

[5.2.6.1 Keynames [52](#keynames-4)](#keynames-4)

[5.2.6.2 Grammar [53](#grammar-20)](#grammar-20)

[5.2.6.2.1 inputs [54](#inputs)](#inputs)

[5.2.6.2.1.1 Grammar [54](#grammar-21)](#grammar-21)

[5.2.6.2.1.2 Examples [54](#examples-6)](#examples-6)

[5.2.6.2.2 node_templates [54](#node_templates)](#node_templates)

[5.2.6.2.2.1 grammar [55](#grammar-22)](#grammar-22)

[5.2.6.2.2.2 Example [55](#example-10)](#example-10)

[5.2.6.2.3 relationship_templates
[55](#relationship_templates)](#relationship_templates)

[5.2.6.2.3.1 Grammar [55](#grammar-23)](#grammar-23)

[5.2.6.2.3.2 Example [55](#example-11)](#example-11)

[5.2.6.2.4 outputs [55](#outputs)](#outputs)

[5.2.6.2.4.1 Grammar [55](#grammar-24)](#grammar-24)

[5.2.6.2.4.2 Example [56](#example-12)](#example-12)

[5.2.6.2.5 groups [56](#groups)](#groups)

[5.2.6.2.5.1 Grammar [56](#grammar-25)](#grammar-25)

[5.2.6.2.5.2 Example [56](#example-13)](#example-13)

[5.2.6.2.6 policies [56](#policies)](#policies)

[5.2.6.2.6.1 Grammar [56](#grammar-26)](#grammar-26)

[5.2.6.2.6.2 Example [56](#example-14)](#example-14)

[5.2.6.2.7 substitution_mapping
[57](#substitution_mapping)](#substitution_mapping)

[5.2.6.2.7.1 requirement_mapping
[57](#requirement_mapping)](#requirement_mapping)

[5.2.6.2.7.2 Example
[57](#need-to-revisit-this.-example-is-wrong-example)](#need-to-revisit-this.-example-is-wrong-example)

[5.3 Nodes and Relationships
[58](#nodes-and-relationships)](#nodes-and-relationships)

[5.3.1 Node Type [58](#node-type)](#node-type)

[5.3.1.1 Keynames [58](#keynames-5)](#keynames-5)

[5.3.1.2 Grammar [58](#grammar-27)](#grammar-27)

[5.3.1.3 Derivation rules
[59](#derivation-rules-1)](#derivation-rules-1)

[5.3.1.4 Additional Requirements
[59](#additional-requirements-1)](#additional-requirements-1)

[5.3.1.5 Example [60](#example-15)](#example-15)

[5.3.2 Node Template [60](#node-template)](#node-template)

[5.3.2.1 Keynames [60](#keynames-6)](#keynames-6)

[5.3.2.2 Grammar [61](#grammar-28)](#grammar-28)

[5.3.2.3 Additional requirements
[62](#additional-requirements-2)](#additional-requirements-2)

[5.3.2.4 Example [62](#example-16)](#example-16)

[5.3.3 Relationship Type
[62](#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type)](#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type)

[5.3.3.1 Keynames [62](#keynames-7)](#keynames-7)

[5.3.3.2 Grammar [63](#grammar-29)](#grammar-29)

[5.3.3.3 Derivation rules
[63](#derivation-rules-2)](#derivation-rules-2)

[5.3.3.4 Examples [64](#examples-7)](#examples-7)

[5.3.4 Relationship Template
[64](#relationship-template)](#relationship-template)

[5.3.4.1 Keynames [64](#keynames-8)](#keynames-8)

[5.3.4.2 Grammar [65](#grammar-30)](#grammar-30)

[5.3.4.3 Additional requirements
[65](#additional-requirements-3)](#additional-requirements-3)

[5.3.4.4 Example [65](#example-17)](#example-17)

[5.3.5 Capabilities and Requirements
[65](#capabilities-and-requirements)](#capabilities-and-requirements)

[5.3.5.1 Capability Type [65](#capability-type)](#capability-type)

[5.3.5.1.1 Keynames [66](#keynames-9)](#keynames-9)

[5.3.5.1.2 Grammar [66](#grammar-31)](#grammar-31)

[5.3.5.1.3 Derivation rules
[67](#derivation-rules-3)](#derivation-rules-3)

[5.3.5.1.4 Example [67](#example-18)](#example-18)

[5.3.5.2 Capability definition
[67](#capability-definition)](#capability-definition)

[5.3.5.2.1 Keynames [67](#keynames-10)](#keynames-10)

[5.3.5.2.2 Grammar [68](#grammar-32)](#grammar-32)

[5.3.5.2.2.1 Short notation [68](#short-notation)](#short-notation)

[5.3.5.2.2.2 Extended notation
[68](#extended-notation)](#extended-notation)

[5.3.5.2.3 Refinement rules [69](#refinement-rules)](#refinement-rules)

[5.3.5.2.4 Examples [69](#examples-8)](#examples-8)

[5.3.5.2.4.1 Simple notation example
[69](#simple-notation-example)](#simple-notation-example)

[5.3.5.2.4.2 Full notation example
[69](#full-notation-example)](#full-notation-example)

[5.3.5.2.5 Additional requirements
[69](#additional-requirements-4)](#additional-requirements-4)

[5.3.5.2.6 Note [70](#note)](#note)

[5.3.5.3 Capability assignment
[70](#capability-assignment)](#capability-assignment)

[5.3.5.3.1 Keynames [70](#keynames-11)](#keynames-11)

[5.3.5.3.2 Grammar [70](#grammar-33)](#grammar-33)

[5.3.5.3.3 Example [71](#example-19)](#example-19)

[5.3.5.3.3.1 Notation example
[71](#notation-example)](#notation-example)

[5.3.5.3.4 Note [71](#note-1)](#note-1)

[5.3.5.4 Requirement Type
[71](#it-seems-to-me-that-the-only-reason-this-section-is-here-is-to-point-out-a-difference-with-the-xml-spec.-i-recommend-removing-it.requirement-type)](#it-seems-to-me-that-the-only-reason-this-section-is-here-is-to-point-out-a-difference-with-the-xml-spec.-i-recommend-removing-it.requirement-type)

[5.3.5.5 Requirement definition
[71](#requirement-definition)](#requirement-definition)

[5.3.5.5.1 Keynames [71](#keynames-12)](#keynames-12)

[5.3.5.5.1.1 Additional keynames for multi-line relationship grammar
[72](#additional-keynames-for-multi-line-relationship-grammar)](#additional-keynames-for-multi-line-relationship-grammar)

[5.3.5.5.2 Grammar [72](#grammar-34)](#grammar-34)

[5.3.5.5.2.1 Simple grammar (Capability Type only)
[72](#simple-grammar-capability-type-only)](#simple-grammar-capability-type-only)

[5.3.5.5.2.2 Extended grammar (with Node and Relationship Types)
[72](#extended-grammar-with-node-and-relationship-types)](#extended-grammar-with-node-and-relationship-types)

[5.3.5.5.2.3 Extended grammar for declaring Parameter Definitions on the
relationship’s Interfaces
[73](#extended-grammar-for-declaring-parameter-definitions-on-the-relationships-interfaces)](#extended-grammar-for-declaring-parameter-definitions-on-the-relationships-interfaces)

[5.3.5.5.3 Refinement rules
[73](#refinement-rules-1)](#refinement-rules-1)

[5.3.5.5.4 Additional requirements
[74](#additional-requirements-5)](#additional-requirements-5)

[5.3.5.5.5 Notes [74](#notes-2)](#notes-2)

[5.3.5.5.6 Requirement definition is a tuple with a filter
[74](#requirement-definition-is-a-tuple-with-a-filter)](#requirement-definition-is-a-tuple-with-a-filter)

[5.3.5.6 Requirement assignment
[74](#requirement-assignment)](#requirement-assignment)

[5.3.5.6.1 Keynames [75](#keynames-13)](#keynames-13)

[5.3.5.6.2 Grammar [76](#grammar-35)](#grammar-35)

[5.3.5.6.2.1 Short notation: [76](#short-notation-1)](#short-notation-1)

[5.3.5.6.2.2 Extended notation:
[77](#extended-notation-1)](#extended-notation-1)

[5.3.5.6.2.3 Extended grammar with Property Assignments and Interface
Assignments for the relationship
[77](#extended-grammar-with-property-assignments-and-interface-assignments-for-the-relationship)](#extended-grammar-with-property-assignments-and-interface-assignments-for-the-relationship)

[5.3.5.6.2.4 Extended grammar with capacity allocation
[77](#extended-grammar-with-capacity-allocation)](#extended-grammar-with-capacity-allocation)

[5.3.5.6.3 Notes [79](#notes-3)](#notes-3)

[5.3.5.6.4 Examples [80](#examples-9)](#examples-9)

[5.3.5.6.4.1 Example 1 – Hosting requirement on a Node Type
[80](#example-1-hosting-requirement-on-a-node-type)](#example-1-hosting-requirement-on-a-node-type)

[5.3.5.6.4.2 Example 2 - Requirement with Node Template and a custom
Relationship Type
[80](#example-2---requirement-with-node-template-and-a-custom-relationship-type)](#example-2---requirement-with-node-template-and-a-custom-relationship-type)

[5.3.5.6.4.3 Example 3 - Requirement for a Compute node with additional
selection criteria (filter)
[80](#example-3---requirement-for-a-compute-node-with-additional-selection-criteria-filter)](#example-3---requirement-for-a-compute-node-with-additional-selection-criteria-filter)

[5.3.5.6.4.4 Example 4 - Requirement assignment for definition with
count_range: \[2,2\]
[81](#example-4---requirement-assignment-for-definition-with-count_range-22)](#example-4---requirement-assignment-for-definition-with-count_range-22)

[5.3.5.6.4.5 Example 5 - Requirement assignment for definition with
capacity allocation
[81](#example-5---requirement-assignment-for-definition-with-capacity-allocation)](#example-5---requirement-assignment-for-definition-with-capacity-allocation)

[5.3.5.7 Node Filter definition
[82](#node-filter-definition)](#node-filter-definition)

[5.3.5.7.1 Grammar [82](#grammar-36)](#grammar-36)

[5.3.5.7.2 Example [82](#example-20)](#example-20)

[5.3.6 Interfaces [82](#interfaces)](#interfaces)

[5.3.6.1 Interface Type [82](#interface-type)](#interface-type)

[5.3.6.1.1 Keynames [82](#keynames-14)](#keynames-14)

[5.3.6.1.2 Grammar [83](#grammar-37)](#grammar-37)

[5.3.6.1.3 Derivation rules
[83](#derivation-rules-4)](#derivation-rules-4)

[5.3.6.1.4 Example [83](#example-21)](#example-21)

[5.3.6.1.5 Additional Requirements
[84](#additional-requirements-6)](#additional-requirements-6)

[5.3.6.2 Interface definition
[84](#interface-definition)](#interface-definition)

[5.3.6.2.1 Keynames [84](#keynames-15)](#keynames-15)

[5.3.6.2.2 Grammar [84](#grammar-38)](#grammar-38)

[5.3.6.2.3 Refinement rules
[85](#refinement-rules-2)](#refinement-rules-2)

[5.3.6.3 Interface assignment
[85](#interface-assignment)](#interface-assignment)

[5.3.6.3.1 Keynames [85](#keynames-16)](#keynames-16)

[5.3.6.3.2 Grammar [86](#grammar-39)](#grammar-39)

[5.3.6.4 Operation definition
[86](#operation-definition)](#operation-definition)

[5.3.6.4.1 Keynames [86](#keynames-17)](#keynames-17)

[5.3.6.4.2 Grammar [87](#grammar-40)](#grammar-40)

[5.3.6.4.2.1 Short notation [87](#short-notation-2)](#short-notation-2)

[5.3.6.4.2.2 Extended notation
[87](#extended-notation-2)](#extended-notation-2)

[5.3.6.4.3 Refinement rules
[87](#refinement-rules-3)](#refinement-rules-3)

[5.3.6.4.4 Additional requirements
[88](#additional-requirements-7)](#additional-requirements-7)

[5.3.6.4.5 Examples [88](#examples-10)](#examples-10)

[5.3.6.4.5.1 Single-line example
[88](#single-line-example)](#single-line-example)

[5.3.6.4.5.2 Multi-line example with shorthand implementation
definitions
[88](#multi-line-example-with-shorthand-implementation-definitions)](#multi-line-example-with-shorthand-implementation-definitions)

[5.3.6.4.5.3 Multi-line example with extended implementation definitions
[88](#multi-line-example-with-extended-implementation-definitions)](#multi-line-example-with-extended-implementation-definitions)

[5.3.6.5 Operation assignment
[89](#operation-assignment)](#operation-assignment)

[5.3.6.5.1 Keynames [89](#keynames-18)](#keynames-18)

[5.3.6.5.2 Grammar [89](#grammar-41)](#grammar-41)

[5.3.6.5.2.1 Short notation [89](#short-notation-3)](#short-notation-3)

[5.3.6.5.2.2 Extended notation
[89](#extended-notation-3)](#extended-notation-3)

[5.3.6.5.3 Additional requirements
[90](#additional-requirements-8)](#additional-requirements-8)

[5.3.6.5.4 Examples [90](#examples-11)](#examples-11)

[5.3.6.6 Notification definition
[90](#notification-definition)](#notification-definition)

[5.3.6.6.1 Keynames [90](#keynames-19)](#keynames-19)

[5.3.6.6.2 Grammar [91](#grammar-42)](#grammar-42)

[5.3.6.6.2.1 Short notation [91](#short-notation-4)](#short-notation-4)

[5.3.6.6.2.2 Extended notation
[91](#extended-notation-4)](#extended-notation-4)

[5.3.6.6.3 Refinement rules
[91](#refinement-rules-4)](#refinement-rules-4)

[5.3.6.6.4 Additional requirements
[92](#additional-requirements-9)](#additional-requirements-9)

[5.3.6.6.5 Examples [92](#examples-12)](#examples-12)

[5.3.6.7 Notification assignment
[92](#notification-assignment)](#notification-assignment)

[5.3.6.7.1 Keynames [92](#keynames-20)](#keynames-20)

[5.3.6.7.2 Grammar [92](#grammar-43)](#grammar-43)

[5.3.6.7.2.1 Short notation [93](#short-notation-5)](#short-notation-5)

[5.3.6.7.2.2 Extended notation
[93](#extended-notation-5)](#extended-notation-5)

[5.3.6.7.3 Additional requirements
[93](#additional-requirements-10)](#additional-requirements-10)

[5.3.6.7.4 Examples [93](#examples-13)](#examples-13)

[5.3.6.8 Operation and notification implementation definition
[93](#operation-and-notification-implementation-definition)](#operation-and-notification-implementation-definition)

[5.3.6.8.1 Keynames [94](#keynames-21)](#keynames-21)

[5.3.6.8.2 Grammar [94](#grammar-44)](#grammar-44)

[5.3.6.8.2.1 Short notation for use with single artifact
[94](#short-notation-for-use-with-single-artifact)](#short-notation-for-use-with-single-artifact)

[5.3.6.8.2.2 Short notation for use with multiple artifacts
[94](#short-notation-for-use-with-multiple-artifacts)](#short-notation-for-use-with-multiple-artifacts)

[5.3.6.8.2.3 Extended notation for use with single artifact
[94](#extended-notation-for-use-with-single-artifact)](#extended-notation-for-use-with-single-artifact)

[5.3.6.8.2.4 Extended notation for use with multiple artifacts
[94](#extended-notation-for-use-with-multiple-artifacts)](#extended-notation-for-use-with-multiple-artifacts)

[5.3.7 Artifacts [95](#artifacts)](#artifacts)

[5.3.7.1 Artifact Type [95](#artifact-type)](#artifact-type)

[5.3.7.1.1 Keynames [95](#keynames-22)](#keynames-22)

[5.3.7.1.2 Grammar [95](#grammar-45)](#grammar-45)

[5.3.7.1.3 Derivation rules
[96](#derivation-rules-5)](#derivation-rules-5)

[5.3.7.1.4 Examples [96](#examples-14)](#examples-14)

[5.3.7.1.5 Additional Requirements
[96](#additional-requirements-11)](#additional-requirements-11)

[5.3.7.1.6 Notes [96](#notes-4)](#notes-4)

[5.3.7.2 Artifact definition
[97](#artifact-definition)](#artifact-definition)

[5.3.7.2.1 Keynames [97](#keynames-23)](#keynames-23)

[5.3.7.2.2 Grammar [97](#grammar-46)](#grammar-46)

[5.3.7.2.2.1 Short notation [97](#short-notation-6)](#short-notation-6)

[5.3.7.2.2.2 Extended notation:
[97](#extended-notation-6)](#extended-notation-6)

[5.3.7.2.3 Refinement rules
[98](#refinement-rules-5)](#refinement-rules-5)

[5.3.7.2.4 Examples [98](#examples-15)](#examples-15)

[5.4 Properties, Attributes, and Parameters
[99](#properties-attributes-and-parameters)](#properties-attributes-and-parameters)

[5.4.1 Primitive Types [99](#primitive-types)](#primitive-types)

[5.4.1.1 string [99](#string)](#string)

[5.4.1.1.1 Notes:
[100](#from-tal-do-we-want-the-comparison-constraints-to-work-for-strings-e.g.-should-greater_than-do-a-sorting-based-comparison-ill-just-point-that-it-is-non-trivial-to-sort-unicode-strings.-the-most-common-way-is-to-use-the-unicode-collation-algorithm-which-involves-a-database-of-information.-there-is-a-reference-implementation-in-icu.-good-and-proper-unicode-libraries-will-support-it-e.g.-here-is-gos-but-i-do-imagine-it-may-be-a-burden-for-some-implementations.-i-suggest-we-discuss-this-in-the-ad-hoc-and-consider-the-pros-and-cons.notes)](#from-tal-do-we-want-the-comparison-constraints-to-work-for-strings-e.g.-should-greater_than-do-a-sorting-based-comparison-ill-just-point-that-it-is-non-trivial-to-sort-unicode-strings.-the-most-common-way-is-to-use-the-unicode-collation-algorithm-which-involves-a-database-of-information.-there-is-a-reference-implementation-in-icu.-good-and-proper-unicode-libraries-will-support-it-e.g.-here-is-gos-but-i-do-imagine-it-may-be-a-burden-for-some-implementations.-i-suggest-we-discuss-this-in-the-ad-hoc-and-consider-the-pros-and-cons.notes)

[5.4.1.2 integer [100](#integer)](#integer)

[5.4.1.2.1 Notes [101](#notes-5)](#notes-5)

[5.4.1.3 float [101](#float)](#float)

[5.4.1.3.1 Notes [101](#notes-6)](#notes-6)

[5.4.1.4 boolean [101](#boolean)](#boolean)

[5.4.1.5 bytes [102](#bytes)](#bytes)

[5.4.1.5.1 Notes [102](#notes-7)](#notes-7)

[5.4.1.6 nil [102](#nil)](#nil)

[5.4.2 Special Types
[103](#need-to-add-timestamp-typespecial-types)](#need-to-add-timestamp-typespecial-types)

[5.4.2.1 TOSCA version
[103](#tosca-tal-suggests-removing-this.version)](#tosca-tal-suggests-removing-this.version)

[5.4.2.1.1 Grammar [103](#grammar-47)](#grammar-47)

[5.4.2.1.2 Version Comparison
[103](#version-comparison)](#version-comparison)

[5.4.2.1.3 Examples [104](#examples-16)](#examples-16)

[5.4.2.1.4 Notes [104](#notes-8)](#notes-8)

[5.4.2.1.5 Additional Requirements
[104](#additional-requirements-12)](#additional-requirements-12)

[5.4.2.2 TOSCA range type [104](#_Toc119950472)](#_Toc119950472)

[5.4.2.2.1 Grammar [104](#_Toc119950473)](#_Toc119950473)

[5.4.2.2.2 Keywords [104](#_Toc119950474)](#_Toc119950474)

[5.4.2.2.3 Examples [104](#_Toc119950475)](#_Toc119950475)

[5.4.2.3 TOSCA timestamp type
[105](#tosca-timestamp-type)](#tosca-timestamp-type)

[5.4.2.3.1 Notes [105](#notes-9)](#notes-9)

[5.4.2.4 TOSCA scalar-unit type
[105](#tosca-scalar-unit-type)](#tosca-scalar-unit-type)

[5.4.2.4.1 Grammar [105](#grammar-48)](#grammar-48)

[5.4.2.4.2 Additional requirements
[105](#additional-requirements-13)](#additional-requirements-13)

[5.4.2.4.3 Concrete Types [106](#concrete-types)](#concrete-types)

[5.4.2.4.4 scalar-unit.size
[106](#scalar-unit.what-dont-we-allow-multiples-of-bitssize)](#scalar-unit.what-dont-we-allow-multiples-of-bitssize)

[5.4.2.4.4.1 Recognized Units
[106](#recognized-units)](#recognized-units)

[5.4.2.4.4.2 Examples [106](#examples-17)](#examples-17)

[5.4.2.4.4.3 Notes [107](#notes-10)](#notes-10)

[5.4.2.4.5 scalar-unit.time [107](#scalar-unit.time)](#scalar-unit.time)

[5.4.2.4.5.1 Recognized Units
[107](#recognized-units-1)](#recognized-units-1)

[5.4.2.4.5.2 Examples [107](#examples-18)](#examples-18)

[5.4.2.4.5.3 Notes [107](#notes-11)](#notes-11)

[5.4.2.4.6 scalar-unit.frequency
[107](#scalar-unit.frequency)](#scalar-unit.frequency)

[5.4.2.4.6.1 Recognized Units
[107](#recognized-units-2)](#recognized-units-2)

[5.4.2.4.6.2 Examples [108](#examples-19)](#examples-19)

[5.4.2.4.6.3 Notes [108](#notes-12)](#notes-12)

[5.4.2.4.7 scalar-unit.bitrate
[108](#scalar-unit.bitrate)](#scalar-unit.bitrate)

[5.4.2.4.7.1 Recognized Units
[108](#recognized-units-3)](#recognized-units-3)

[5.4.2.4.7.2 Examples [108](#examples-20)](#examples-20)

[5.4.3 Collection Types [109](#collection-types)](#collection-types)

[5.4.3.1 TOSCA list type [109](#tosca-list-type)](#tosca-list-type)

[5.4.3.1.1 Grammar [109](#grammar-49)](#grammar-49)

[5.4.3.1.1.1 Square bracket notation
[109](#square-bracket-notation)](#square-bracket-notation)

[5.4.3.1.1.2 Bulleted list notation
[109](#bulleted-list-notation)](#bulleted-list-notation)

[5.4.3.1.2 Declaration Examples
[109](#declaration-examples)](#declaration-examples)

[5.4.3.1.2.1 List declaration using a simple type
[109](#list-declaration-using-a-simple-type)](#list-declaration-using-a-simple-type)

[5.4.3.1.2.2 List declaration using a complex type
[109](#list-declaration-using-a-complex-type)](#list-declaration-using-a-complex-type)

[5.4.3.1.3 Definition Examples
[110](#definition-examples)](#definition-examples)

[5.4.3.1.3.1 Square bracket notation
[110](#square-bracket-notation-1)](#square-bracket-notation-1)

[5.4.3.1.3.2 Bulleted list notation
[110](#bulleted-list-notation-1)](#bulleted-list-notation-1)

[5.4.3.2 TOSCA map type [110](#tosca-map-type)](#tosca-map-type)

[5.4.3.2.1 Grammar [110](#grammar-50)](#grammar-50)

[5.4.3.2.1.1 Single-line grammar
[110](#single-line-grammar-2)](#single-line-grammar-2)

[5.4.3.2.1.2 Multi-line grammar
[110](#multi-line-grammar-2)](#multi-line-grammar-2)

[5.4.3.2.2 Declaration Examples
[110](#declaration-examples-1)](#declaration-examples-1)

[5.4.3.2.2.1 Map declaration using a simple type
[110](#map-declaration-using-a-simple-type)](#map-declaration-using-a-simple-type)

[5.4.3.2.2.2 Map declaration using a complex type
[111](#map-declaration-using-a-complex-type)](#map-declaration-using-a-complex-type)

[5.4.3.2.3 Definition Examples
[111](#definition-examples-1)](#definition-examples-1)

[5.4.3.2.3.1 Single-line notation
[111](#single-line-notation)](#single-line-notation)

[5.4.3.2.3.2 Multi-line notation
[111](#multi-line-notation)](#multi-line-notation)

[5.4.4 Data Type [111](#data-type)](#data-type)

[5.4.4.1 Keynames [111](#keynames-24)](#keynames-24)

[5.4.4.2 Grammar [112](#grammar-51)](#grammar-51)

[5.4.4.3 Derivation rules
[112](#derivation-rules-6)](#derivation-rules-6)

[5.4.4.4 Additional Requirements
[113](#additional-requirements-14)](#additional-requirements-14)

[5.4.4.5 Examples [113](#examples-21)](#examples-21)

[5.4.4.5.1 Defining a complex datatype
[113](#defining-a-complex-datatype)](#defining-a-complex-datatype)

[5.4.4.5.2 Defining a datatype derived from an existing datatype
[113](#defining-a-datatype-derived-from-an-existing-datatype)](#defining-a-datatype-derived-from-an-existing-datatype)

[5.4.5 Schema definition [113](#schema-definition)](#schema-definition)

[5.4.5.1 Keynames [113](#keynames-25)](#keynames-25)

[5.4.5.2 Grammar [114](#grammar-52)](#grammar-52)

[5.4.5.2.1 Short notation [114](#short-notation-7)](#short-notation-7)

[5.4.5.2.2 Extended Notation
[114](#extended-notation-7)](#extended-notation-7)

[5.4.5.3 Refinement rules
[114](#refinement-rules-6)](#refinement-rules-6)

[5.4.6 Validation clause definition
[115](#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition)](#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition)

[5.4.6.1 Operator keynames [115](#_Toc119950533)](#_Toc119950533)

[5.4.6.1.1 Comparable value types [116](#_Toc119950534)](#_Toc119950534)

[5.4.6.2 Schema Constraint purpose
[116](#_Toc119950535)](#_Toc119950535)

[5.4.6.3 Additional Requirements [116](#_Toc119950536)](#_Toc119950536)

[5.4.6.4 Grammar [116](#_Toc119950537)](#_Toc119950537)

[5.4.6.5 Examples [117](#examples-22)](#examples-22)

[5.4.7 Property definition
[117](#_Schema_Definition)](#_Schema_Definition)

[5.4.7.1 Attribute and Property reflection
[117](#attribute-and-property-reflection)](#attribute-and-property-reflection)

[5.4.7.2 Keynames [117](#keynames-26)](#keynames-26)

[5.4.7.3 Status values
[118](#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values)](#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values)

[5.4.7.4 Grammar [119](#grammar-54)](#grammar-54)

[5.4.7.5 Refinement rules
[120](#refinement-rules-7)](#refinement-rules-7)

[5.4.7.6 Additional Requirements
[120](#additional-requirements-15)](#additional-requirements-15)

[5.4.7.7 Examples [120](#examples-23)](#examples-23)

[5.4.8 Property assignment
[121](#property-assignment)](#property-assignment)

[5.4.8.1 Keynames [121](#keynames-27)](#keynames-27)

[5.4.8.2 Grammar [121](#grammar-55)](#grammar-55)

[5.4.8.2.1 Short notation: [121](#short-notation-8)](#short-notation-8)

[5.4.8.3 Additional Requirements
[122](#additional-requirements-16)](#additional-requirements-16)

[5.4.9 Attribute definition
[122](#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition)](#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition)

[5.4.9.1 Attribute and Property reflection
[122](#attribute-and-property-reflection-1)](#attribute-and-property-reflection-1)

[5.4.9.2 Keynames [122](#keynames-28)](#keynames-28)

[5.4.9.3 Grammar [123](#grammar-56)](#grammar-56)

[5.4.9.4 Refinement rules
[123](#refinement-rules-8)](#refinement-rules-8)

[5.4.9.5 Additional Requirements
[124](#additional-requirements-17)](#additional-requirements-17)

[5.4.9.6 Notes [124](#notes-13)](#notes-13)

[5.4.9.7 Example [124](#example-22)](#example-22)

[5.4.10 Attribute assignment
[124](#attribute-assignment)](#attribute-assignment)

[5.4.10.1 Keynames [124](#keynames-29)](#keynames-29)

[5.4.10.2 Grammar [124](#grammar-57)](#grammar-57)

[5.4.10.2.1 Short notation: [124](#short-notation-9)](#short-notation-9)

[5.4.10.3 Additional requirements
[125](#additional-requirements-18)](#additional-requirements-18)

[5.4.11 Parameter definition
[125](#parameter-definition)](#parameter-definition)

[5.4.11.1 Keynames [125](#keynames-30)](#keynames-30)

[5.4.11.2 Grammar [126](#grammar-58)](#grammar-58)

[5.4.11.3 Refinement rules
[127](#refinement-rules-9)](#refinement-rules-9)

[5.4.11.4 Additional requirements
[128](#additional-requirements-19)](#additional-requirements-19)

[5.4.11.5 Example [128](#example-23)](#example-23)

[5.4.12 Parameter value assignment
[128](#parameter-value-assignment)](#parameter-value-assignment)

[5.4.12.1 Keynames [128](#keynames-31)](#keynames-31)

[5.4.12.2 Grammar [128](#grammar-59)](#grammar-59)

[5.4.12.3 Additional requirements
[128](#additional-requirements-20)](#additional-requirements-20)

[5.4.13 Parameter mapping assignment
[129](#parameter-mapping-assignment)](#parameter-mapping-assignment)

[5.4.13.1 Keynames [129](#keynames-32)](#keynames-32)

[5.4.13.2 Grammar [129](#grammar-60)](#grammar-60)

[5.4.13.3 Attribute selection format
[129](#attribute-selection-format)](#attribute-selection-format)

[5.4.13.4 Additional requirements
[130](#additional-requirements-21)](#additional-requirements-21)

[5.4.14 Function syntax [130](#function-syntax)](#function-syntax)

[5.4.14.1 Parsing rule [131](#_Toc119950581)](#_Toc119950581)

[5.4.15 Function definitions [131](#_Toc119950582)](#_Toc119950582)

[5.4.15.1 Grammar [131](#_Toc119950583)](#_Toc119950583)

[5.4.15.2 Examples [133](#_Toc119950584)](#_Toc119950584)

[5.4.15.2.1 Square root function with several signatures
[133](#_Toc119950585)](#_Toc119950585)

[5.4.15.2.2 Function with list of arguments
[134](#_Toc119950586)](#_Toc119950586)

[5.4.15.2.3 Function with no arguments
[134](#_Toc119950587)](#_Toc119950587)

[5.4.15.2.4 Function with polymorphic arguments/result inside of lists
[134](#_Toc119950588)](#_Toc119950588)

[5.4.15.2.5 Defining a list in a map argument
[135](#_Toc119950589)](#_Toc119950589)

[5.4.15.2.6 User-defined function usage
[135](#_Toc119950590)](#_Toc119950590)

[5.5 Substitution [135](#substitution)](#substitution)

[5.5.1 Substitution mapping
[135](#substitution-mapping-1)](#substitution-mapping-1)

[5.5.1.1 Keynames [135](#keynames-34)](#keynames-34)

[5.5.1.2 Grammar [136](#grammar-62)](#grammar-62)

[5.5.1.3 Examples [136](#examples-25)](#examples-25)

[5.5.1.4 Additional requirements
[136](#additional-requirements-22)](#additional-requirements-22)

[5.5.1.5 Notes [136](#notes-14)](#notes-14)

[5.5.2 Property mapping [137](#property-mapping)](#property-mapping)

[5.5.2.1 Keynames [137](#keynames-35)](#keynames-35)

[5.5.2.2 Grammar [137](#grammar-63)](#grammar-63)

[5.5.2.3 Notes [137](#notes-15)](#notes-15)

[5.5.2.4 Additional constraints
[137](#additional-constraints)](#additional-constraints)

[5.5.3 Attribute mapping [138](#attribute-mapping)](#attribute-mapping)

[5.5.3.1 Keynames [138](#keynames-36)](#keynames-36)

[5.5.3.2 Grammar [138](#grammar-64)](#grammar-64)

[5.5.4 Capability mapping
[138](#capability-mapping)](#capability-mapping)

[5.5.4.1 Keynames
[138](#here-at-the-end-we-should-add-also-the-occurences-keyname-that-should-allow-assignement-as-for-properties-and-attributes-see-capability-assignment-changes-to-be-madekeynames)](#here-at-the-end-we-should-add-also-the-occurences-keyname-that-should-allow-assignement-as-for-properties-and-attributes-see-capability-assignment-changes-to-be-madekeynames)

[5.5.4.2 Grammar [138](#grammar-65)](#grammar-65)

[5.5.5 Requirement mapping
[139](#requirement-mapping)](#requirement-mapping)

[5.5.5.1 Keynames
[139](#the-properties-and-attributes-are-totally-wrong-here-as-a-requirement-does-not-have-them.-one-should-not-be-able-to-assign-a-requirement-without-having-a-real-dependency-to-match.-the-last-two-rows-should-be-deletedkeynames)](#the-properties-and-attributes-are-totally-wrong-here-as-a-requirement-does-not-have-them.-one-should-not-be-able-to-assign-a-requirement-without-having-a-real-dependency-to-match.-the-last-two-rows-should-be-deletedkeynames)

[5.5.5.2 Grammar [139](#grammar-66)](#grammar-66)

[5.5.6 Interface mapping [140](#interface-mapping)](#interface-mapping)

[5.5.6.1 Grammar
[140](#this-could-change-if-we-introduce-the-operations-keyname-in-the-interface-definitionsgrammar)](#this-could-change-if-we-introduce-the-operations-keyname-in-the-interface-definitionsgrammar)

[5.5.6.2 Notes [140](#notes-16)](#notes-16)

[5.6 Groups and Policies
[140](#groups-and-language-suggested-by-paul-jordan-in-tosca-policy-is-used-to-affect-or-govern-an-application-or-services-topology-at-some-stage-of-its-lifecycle-but-is-not-explicitly-part-of-the-topology-itself.-the-policy-scope-can-be-limited-to-a-collection-of-nodes-or-node-types-by-using-groups-and-group-types.policies)](#groups-and-language-suggested-by-paul-jordan-in-tosca-policy-is-used-to-affect-or-govern-an-application-or-services-topology-at-some-stage-of-its-lifecycle-but-is-not-explicitly-part-of-the-topology-itself.-the-policy-scope-can-be-limited-to-a-collection-of-nodes-or-node-types-by-using-groups-and-group-types.policies)

[5.6.1 Group Type [140](#group-type)](#group-type)

[5.6.1.1 Keynames [140](#keynames-37)](#keynames-37)

[5.6.1.2 Grammar [141](#grammar-67)](#grammar-67)

[5.6.1.3 Derivation rules
[141](#derivation-rules-7)](#derivation-rules-7)

[5.6.1.4 Example [141](#example-24)](#example-24)

[5.6.2 Group definition [142](#group-definition)](#group-definition)

[5.6.2.1 Keynames [142](#keynames-38)](#keynames-38)

[5.6.2.2 Grammar [142](#grammar-68)](#grammar-68)

[5.6.2.3 Example [143](#example-25)](#example-25)

[5.6.3 Policy Type [143](#policy-type)](#policy-type)

[5.6.3.1 Keynames [143](#keynames-39)](#keynames-39)

[5.6.3.2 Grammar [143](#grammar-69)](#grammar-69)

[5.6.3.3 Derivation rules
[144](#derivation-rules-8)](#derivation-rules-8)

[5.6.3.4 Example [144](#example-26)](#example-26)

[5.6.4 Policy definition
[144](#i-know-that-tmf-have-a-branch-of-their-information-model-to-describe-policy-but-that-it-is-not-used-much-and-that-mef-have-recently-been-more-active-in-specializing-policy-for-access-control-and-for-ip-forwarding-rules.-it-is-possible-that-tosca-could-draw-on-this-work-to-make-tosca-policy-framework-more-useful.policy-definition)](#i-know-that-tmf-have-a-branch-of-their-information-model-to-describe-policy-but-that-it-is-not-used-much-and-that-mef-have-recently-been-more-active-in-specializing-policy-for-access-control-and-for-ip-forwarding-rules.-it-is-possible-that-tosca-could-draw-on-this-work-to-make-tosca-policy-framework-more-useful.policy-definition)

[5.6.4.1 Keynames [144](#keynames-40)](#keynames-40)

[5.6.4.2 Grammar [144](#grammar-70)](#grammar-70)

[5.6.4.3 Example [145](#example-27)](#example-27)

[5.6.5 Trigger definition
[145](#trigger-definition)](#trigger-definition)

[5.6.5.1 Keynames
[145](#recall-policy-type-defn-were-to-be-consumed-by-a-policy-engine-that-would-create-events-on-a-known-event-monitoring-service.-we-need-to-create-diagram-and-explain-the-event-condition-action-flow-of-policy-defn.keynames)](#recall-policy-type-defn-were-to-be-consumed-by-a-policy-engine-that-would-create-events-on-a-known-event-monitoring-service.-we-need-to-create-diagram-and-explain-the-event-condition-action-flow-of-policy-defn.keynames)

[5.6.5.2 Grammar
[146](#this-does-not-make-any-sense.-needs-to-be-deleted.grammar)](#this-does-not-make-any-sense.-needs-to-be-deleted.grammar)

[5.6.6 Activity definitions
[146](#activity-definitions)](#activity-definitions)

[5.6.6.1 Delegate workflow activity definition
[146](#delegate-workflow-activity-definition)](#delegate-workflow-activity-definition)

[5.6.6.1.1 Keynames [146](#keynames-41)](#keynames-41)

[5.6.6.1.2 Grammar [147](#grammar-71)](#grammar-71)

[5.6.6.1.2.1 Short notation
[147](#short-notation-10)](#short-notation-10)

[5.6.6.1.2.2 Extended notation
[147](#extended-notation-8)](#extended-notation-8)

[5.6.6.2 Set state activity definition
[147](#set-state-activity-definition)](#set-state-activity-definition)

[5.6.6.2.1 Keynames [147](#keynames-42)](#keynames-42)

[5.6.6.2.2 Grammar [147](#grammar-72)](#grammar-72)

[5.6.6.3 Call operation activity definition
[148](#call-operation-activity-definition)](#call-operation-activity-definition)

[5.6.6.3.1 Keynames [148](#keynames-43)](#keynames-43)

[5.6.6.3.2 Grammar [148](#grammar-73)](#grammar-73)

[5.6.6.3.2.1 Short notation
[148](#short-notation-11)](#short-notation-11)

[5.6.6.3.2.2 Extended notation
[148](#extended-notation-9)](#extended-notation-9)

[5.6.6.4 Inline workflow activity definition
[149](#inline-workflow-activity-definition)](#inline-workflow-activity-definition)

[5.6.6.4.1 Keynames [149](#keynames-44)](#keynames-44)

[5.6.6.4.2 Grammar [149](#grammar-74)](#grammar-74)

[5.6.6.4.2.1 Short notation
[149](#short-notation-12)](#short-notation-12)

[5.6.6.4.2.2 Extended notation
[149](#extended-notation-10)](#extended-notation-10)

[5.6.6.5 Example [149](#example-28)](#example-28)

[5.7 Workflows [150](#workflows-1)](#workflows-1)

[5.7.1 Imperative Workflow definition
[150](#imperative-workflow-definition)](#imperative-workflow-definition)

[5.7.1.1 Keynames [150](#keynames-45)](#keynames-45)

[5.7.1.2 Grammar [150](#grammar-75)](#grammar-75)

[5.7.2 Workflow precondition definition
[151](#workflow-precondition-definition)](#workflow-precondition-definition)

[5.7.2.1 Examples [151](#examples-26)](#examples-26)

[5.7.3 Workflow step definition
[151](#workflow-step-definition)](#workflow-step-definition)

[5.7.3.1 Keynames [151](#keynames-46)](#keynames-46)

[5.7.3.2 Grammar [152](#grammar-76)](#grammar-76)

[6 TOSCA built-in functions [153](#_Toc119950666)](#_Toc119950666)

[6.1 Representation graph query functions
[153](#_Toc119950667)](#_Toc119950667)

[6.1.1 get_input [153](#_Toc119950668)](#_Toc119950668)

[6.1.1.1 Grammar [153](#_Toc119950669)](#_Toc119950669)

[6.1.1.2 Arguments [153](#_Toc119950670)](#_Toc119950670)

[6.1.1.3 Examples [153](#_Toc119950671)](#_Toc119950671)

[6.1.2 get_property [154](#_Toc119950672)](#_Toc119950672)

[6.1.2.1 Grammar [154](#_Toc119950673)](#_Toc119950673)

[6.1.2.2 Arguments [154](#_Toc119950674)](#_Toc119950674)

[6.1.2.2.1 The simplified TOSCA_PATH definition in BNF format
[155](#_Toc119950675)](#_Toc119950675)

[6.1.2.3 Note [156](#_Toc119950676)](#_Toc119950676)

[6.1.2.4 Examples [156](#_Toc119950677)](#_Toc119950677)

[6.1.3 get_attribute [158](#_Toc119950678)](#_Toc119950678)

[6.1.3.1 Grammar [158](#_Toc119950679)](#_Toc119950679)

[6.1.3.2 Arguments [158](#_Toc119950680)](#_Toc119950680)

[6.1.3.3 Examples: [158](#_Toc119950681)](#_Toc119950681)

[6.1.4 get_artifact [158](#_Toc119950682)](#_Toc119950682)

[6.1.4.1 Grammar [159](#_Toc119950683)](#_Toc119950683)

[6.1.4.2 Arguments [159](#_Toc119950684)](#_Toc119950684)

[6.1.4.3 Examples [159](#_Toc119950685)](#_Toc119950685)

[6.1.4.3.1 Example: Retrieving artifact without specified location
[159](#_Toc119950686)](#_Toc119950686)

[6.1.4.3.2 Example: Retrieving artifact as a local path
[160](#_Toc119950687)](#_Toc119950687)

[6.1.4.3.3 Example: Retrieving artifact in a specified location
[160](#_Toc119950688)](#_Toc119950688)

[6.2 Condition Functions [160](#_Toc119950689)](#_Toc119950689)

[6.2.1 and [160](#_Toc119950690)](#_Toc119950690)

[6.2.1.1 Grammar [161](#_Toc119950691)](#_Toc119950691)

[6.2.2 or [161](#_Toc119950692)](#_Toc119950692)

[6.2.2.1 Grammar [161](#_Toc119950693)](#_Toc119950693)

[6.2.3 not [161](#_Toc119950694)](#_Toc119950694)

[6.2.3.1 Grammar [161](#_Toc119950695)](#_Toc119950695)

[6.2.4 equal [161](#_Toc119950696)](#_Toc119950696)

[6.2.5 greater_than [161](#_Toc119950697)](#_Toc119950697)

[6.2.6 greater_or_equal [161](#_Toc119950698)](#_Toc119950698)

[6.2.7 less_than [161](#_Toc119950699)](#_Toc119950699)

[6.2.8 less_or_equal [161](#_Toc119950700)](#_Toc119950700)

[6.2.9 in_range [161](#_Toc119950701)](#_Toc119950701)

[6.2.10 valid_values [161](#_Toc119950702)](#_Toc119950702)

[6.2.11 length [161](#_Toc119950703)](#_Toc119950703)

[6.2.12 min_length [161](#_Toc119950704)](#_Toc119950704)

[6.2.13 max_length [161](#_Toc119950705)](#_Toc119950705)

[6.2.14 pattern [161](#_Toc119950706)](#_Toc119950706)

[6.3 String manipulation functions
[161](#_Toc119950707)](#_Toc119950707)

[6.3.1 concat [161](#_Toc119950708)](#_Toc119950708)

[6.3.1.1 Grammar [162](#_Toc119950709)](#_Toc119950709)

[6.3.1.2 Arguments [162](#_Toc119950710)](#_Toc119950710)

[6.3.1.3 Examples [162](#_Toc119950711)](#_Toc119950711)

[6.3.2 join [162](#_Toc119950712)](#_Toc119950712)

[6.3.2.1 Grammar [162](#_Toc119950713)](#_Toc119950713)

[6.3.2.2 Arguments [162](#_Toc119950714)](#_Toc119950714)

[6.3.2.3 Examples [162](#_Toc119950715)](#_Toc119950715)

[6.3.3 token [162](#_Toc119950716)](#_Toc119950716)

[6.3.3.1 Grammar [163](#_Toc119950717)](#_Toc119950717)

[6.3.3.2 Arguments [163](#_Toc119950718)](#_Toc119950718)

[6.3.3.3 Examples [163](#_Toc119950719)](#_Toc119950719)

[7 TOSCA Cloud Service Archive (CSAR) format
[164](#tosca-cloud-service-archive-csar-format)](#tosca-cloud-service-archive-csar-format)

[7.1 Overall Structure of a CSAR
[164](#overall-structure-of-a-csar)](#overall-structure-of-a-csar)

[7.2 TOSCA Meta File [164](#tosca-meta-file)](#tosca-meta-file)

[7.2.1 Custom keynames in the TOSCA.meta file
[165](#custom-keynames-in-the-tosca.meta-file)](#custom-keynames-in-the-tosca.meta-file)

[7.2.2 Example [165](#example-29)](#example-29)

[7.3 Archive without TOSCA-Metadata
[165](#archive-without-tosca-metadata)](#archive-without-tosca-metadata)

[7.3.1 Example [165](#example-30)](#example-30)

[8 Security Considerations
[166](#security-considerations)](#security-considerations)

[9 Conformance [167](#conformance)](#conformance)

[9.1 Conformance Targets
[167](#conformance-targets)](#conformance-targets)

[9.2 Conformance Clause 1: TOSCA YAML service template
[167](#conformance-clause-1-tosca-yaml-service-template)](#conformance-clause-1-tosca-yaml-service-template)

[9.3 Conformance Clause 2: TOSCA processor
[167](#conformance-clause-2-tosca-processor)](#conformance-clause-2-tosca-processor)

[9.4 Conformance Clause 3: TOSCA orchestrator
[167](#conformance-clause-3-tosca-orchestrator)](#conformance-clause-3-tosca-orchestrator)

[9.5 Conformance Clause 4: TOSCA generator
[168](#conformance-clause-4-tosca-generator)](#conformance-clause-4-tosca-generator)

[9.6 Conformance Clause 5: TOSCA archive
[168](#conformance-clause-5-tosca-archive)](#conformance-clause-5-tosca-archive)

[Appendix A. Acknowledgments [169](#acknowledgments)](#acknowledgments)

[Appendix B. Example Title [171](#example-title)](#example-title)

[B.1 Subsidiary section [171](#subsidiary-section)](#subsidiary-section)

[B.1.1 Sub-subsidiary section
[171](#sub-subsidiary-section)](#sub-subsidiary-section)

[B.1.1.1 Sub-sub-subsidiary section
[171](#sub-sub-subsidiary-section)](#sub-sub-subsidiary-section)

[B.1.1.1.1 Sub-sub-sub-subsidiary section
[171](#sub-sub-sub-subsidiary-section)](#sub-sub-sub-subsidiary-section)

[Appendix C. Revision History
[172](#revision-history)](#revision-history)

Introduction
============

\[All text is normative unless otherwise labeled\]

IPR Policy
----------

This specification is provided under the [RF on Limited
Terms](https://www.oasis-open.org/policies-guidelines/ipr#RF-on-Limited-Mode)
Mode of the [OASIS IPR
Policy](https://www.oasis-open.org/policies-guidelines/ipr), the mode
chosen when the Technical Committee was established. For information on
whether any patents have been disclosed that may be essential to
implementing this specification, and any offers of patent licensing
terms, please refer to the Intellectual Property Rights section of the
TC’s web page (<https://www.oasis-open.org/committees/tosca/ipr.php>).

Terminology
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in BCP 14
\[[RFC2119](#RFC2119)\] and \[[RFC8174](#RFC8174)\] when, and only when,
they appear in all capitals, as shown here.

Normative References
--------------------

\[RFC2119\] Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997,
\<<http://www.rfc-editor.org/info/rfc2119>\>.

**\[**RFC8174\] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC
2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017,
\<<http://www.rfc-editor.org/info/rfc8174>\>.

\[YAML-1.2\] YAML, Version 1.2, 3rd Edition, Patched at 2009-10-01, Oren
Ben-Kiki, Clark Evans, Ingy döt Net
<http://www.yaml.org/spec/1.2/spec.html>

\[YAML-TS-1.1\] Timestamp Language-Independent Type for YAML Version
1.1, Working Draft 2005-01-18, <http://yaml.org/type/timestamp.html>

\[<span id="CIT_ISO_IEC_21320_1" class="anchor"></span>ISO-IEC-21320-1\]
ISO/IEC 21320-1 "Document Container File — Part 1: Core",
<https://www.iso.org/standard/60101.html> 

Non-Normative References
------------------------

\[Apache\] Apache Server, https://httpd.apache.org/

\[Chef\] Chef, https://wiki.opscode.com/display/chef/Home

\[NodeJS\] Node.js, https://nodejs.org/

\[Puppet\] Puppet, http://puppetlabs.com/

\[<span id="CIT_WORDPRESS" class="anchor"></span>WordPress\] WordPress,
https://wordpress.org/

\[<span id="CIT_MAVEN_VERSION" class="anchor"></span>Maven-Version\]
Apache Maven version policy draft:
https://cwiki.apache.org/confluence/display/MAVEN/Version+number+policy

\[JSON-Spec\] The JSON Data Interchange Format (ECMA and IETF versions):

- <http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf>

- https://tools.ietf.org/html/rfc7158

\[JSON-Schema\] JSON Schema specification:

- <http://json-schema.org/documentation.html>

\[XMLSpec\] XML Specification, W3C Recommendation, February 1998,
http://www.w3.org/TR/1998/REC-xml-19980210

\[XML Schema Part 1\] XML Schema Part 1: Structures, W3C Recommendation,
October 2004, <http://www.w3.org/TR/xmlschema-1/>

\[XML Schema Part 2\] XML Schema Part 2: Datatypes, W3C Recommendation,
October 2004, http://www.w3.org/TR/xmlschema-2/

\[IANA register for Hash Function Textual Names\]
https://www.iana.org/assignments/hash-function-text-names/hash-function-text-names.xhtml

\[Jinja2\] Jinja2, jinja.pocoo.org/

\[Twig\] Twig, https://twig.symfony.com

<span class="mark">(**Note**: Each reference to a separate document or
artifact in this work must be listed here and must be identified as
either a Normative or a Non-Normative Reference.</span>

*<span class="mark">For all References – Normative and
Non-Normative:</span>*

<span class="mark">Recommended approach: Set up \[Reference\] label
elements as "Bookmarks", then create hyperlinks to them within the
document. (**Here's how:** Insert hyperlinkPlace in this documentscroll
down to Bookmarks, select appropriate one.)</span>

<span class="mark">Use the "Ref" paragraph style to format
references.</span>

*<span class="mark">The proper format for citation of technical work
produced by an OASIS TC (whether Standards Track or Non-Standards Track)
is:</span>*

<span class="mark">\[Citation Label\] Work Product
[title](http://docs.oasis-open.org/specGuidelines/ndr/namingDirectives.html#workProductName)
(italicized). Edited by Albert Alston, Bob Ballston, and Calvin Carlson.
Approval date (DD Month YYYY). OASIS
[Stage](http://docs.oasis-open.org/specGuidelines/ndr/namingDirectives.html#stage)
Identifier and
[Revision](http://docs.oasis-open.org/specGuidelines/ndr/namingDirectives.html#revision)
Number (*e.g.*, OASIS Committee Specification Draft 01). Principal URI
([version-specific
URI](http://docs.oasis-open.org/specGuidelines/ndr/namingDirectives.html#this-version),
*e.g*., with stage component: somespec-v1.0-csd01.html). Latest version:
([latest version
URI](http://docs.oasis-open.org/specGuidelines/ndr/namingDirectives.html#latest-version),
without stage identifiers).</span>

<span class="mark">For example:</span>

<span class="mark">**\[OpenDoc-1.2\]** *Open Document Format for Office
Applications (OpenDocument) Version 1.2*. Edited by Patrick Durusau and
Michael Brauer. 19 January 2011. OASIS Committee Specification Draft 07.
<http://docs.oasis-open.org/office/v1.2/csd07/OpenDocument-v1.2-csd07.html>.
Latest version:
<http://docs.oasis-open.org/office/v1.2/OpenDocument-v1.2.html>.</span>

*<span class="mark">Reference sources:</span>*

<span class="mark">For references to **IETF RFCs**, use the approved
citation formats at:  
<http://docs.oasis-open.org/templates/ietf-rfc-list/ietf-rfc-list.html>.</span>

<span class="mark">For references to **W3C Recommendations**, use the
approved citation formats at:  
<http://docs.oasis-open.org/templates/w3c-recommendations-list/w3c-recommendations-list.html>.</span>

<span class="mark">Remove this note before submitting for
publication.)</span>

Overview
========

Objective
---------

Cloud computing
can become more valuable if the creation and lifecycle management of
application, infrastructure, and network services can be fully automated
and supported across a variety of deployment environments. The core
TOSCA specification provides a language for describing service
components and their relationships using a service topology, and it
provides for specifying the lifecycle management procedures that allow
for creation or modification of services using orchestration processes.
The combination of topology and orchestration in a Service Template
describes what is needed in different environments to enable automated
deployment of services and their management throughout the complete
service lifecycle (e.g. scaling, patching, monitoring,
etc.).
<!----
{"id": "45", "author": "Chris Lauwers", "date": "2020-05-31T00:44:00Z", "comment": "This prose has been copied from the TOSCA\nVersion 1.0 document and needs further editing.", "target": "Cloud computing\ncan become more valuable if the creation and lifecycle management of\napplication, infrastructure, and network services can be fully automated\nand supported across a variety of deployment environments. The core\nTOSCA specification provides a language for describing service\ncomponents and their relationships using a service topology, and it\nprovides for specifying the lifecycle management procedures that allow\nfor creation or modification of services using orchestration processes.\nThe combination of topology and orchestration in a Service Template\ndescribes what is needed in different environments to enable automated\ndeployment of services and their management throughout the complete\nservice lifecycle (e.g. scaling, patching, monitoring,\netc.)."}-->


TOSCA Scope
<!----
{"id": "47", "author": "Chris Lauwers", "date": "2021-06-28T23:04:00Z", "comment": "This section has been moved here from the Operational Model chapter in the previous draft. It may need to be consolidated with the \"Objective\" section to create a new \"What is TOSCA\" subsection.", "target": "Scope"}-->

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TOSCA is a domain-specific language for designing services and for
defining the deployment and run-time management aspects of these
services with the goal of enabling fully automated service management.
As such, TOSCA is designed to support all three phases of the service
lifecycle:

1.  **Day 0—Service Design**: Service designers use TOSCA to model
    services as topology graphs that consist of nodes and relationships.
    Nodes model the components of which a service is composed, and
    relationships model dependencies between these service components.

2.  ***Day 1—*Service *Deployment***: TOSCA can also be used to define
    mechanisms for deploying TOSCA service topologies on external
    platforms.

<!-- -->

1.  **Day 2—Service Management**: TOSCA can enable run-time management
    of services by providing support for updating and/or upgrading
    deployed services and by providing service assurance functionality.

Note that it is not mandatory for compliant TOSCA implementations to
support all three service lifecycle phases. Some implementations may use
TOSCA only for service design and delegate orchestration and ongoing
lifecycle management functionality to external (non-TOSCA)
orchestrators. Other implementations may decide to use TOSCA for all
three phases of the service lifecycle.

Application Domains
-------------------

TOSCA can be used to specify automated lifecycle management of the
following:

- Infrastructure-as-a-Service Clouds: automate the deployment and
  management of workloads in IaaS clouds such as OpenStack, Amazon Web
  Services, Microsoft Azure, and others.

- Cloud-native applications: deploy containerized applications and
  micro-services, for example by interfacing to orchestration platforms
  such as Kubernetes.

- Network Functions Virtualization: define the management of Virtual
  Network Functions and their composition into complex network services.

- Software Defined Networking: support on-demand creation of network
  services (for example SD-WAN).

- Functions-as-a-Service: define abstract software applications without
  any deployment or operational considerations.

- IoT and Edge computing: deploy services at the network edge with the
  goal of minimizing latency.

- Process automation: support open and interoperable process control
  architectures.

This list is by no means intended to be exhaustive and only serves to
demonstrate the breadth of application domains that can benefit from
TOSCA’s automated lifecycle management capabilities.

Implementations
---------------

Different kinds of processors and artifacts qualify as implementations
of TOSCA. Those that this specification is explicitly mentioning or
referring to fall into the following categories:

- TOSCA processor (or “processor”): An engine or tool that is capable of
  parsing and interpreting a TOSCA service template for a particular
  purpose. For example, the purpose could be validation, translation or
  visual rendering.

- TOSCA orchestrator (also called orchestration engine): A TOSCA
  processor that interprets a TOSCA file or a TOSCA CSAR in order to
  instantiate, deploy, and manage the described application in a Cloud.

- TOSCA translator: A tool that translates TOSCA files into documents
  that use another language, such as Kubernetes Helm charts or Amazon
  CloudFormation templates.

- TOSCA template generator: A tool that generates a TOSCA file. An
  example of generator is a modeling tool capable of generating or
  editing a TOSCA file (often such a tool would also be a TOSCA
  processor).

The above list is not exclusive. The above definitions should be
understood as referring to and implementing TOSCA as described in this
document.

Glossary
--------

The following terms are used throughout this specification and have the
following definitions when used in context of this document.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Instance Model</td>
<td>application
<!----
{"id": "67\" data-author=\"Calin Curescu\"\ndata-date=\"2020-06-22T17:48:00Z\">Needs to be updated to not confuse it\nwith real-life model</span>A deployed service is a running instance of a\nService Template. The instance is typically derived by running a\ndeclarative workflow that is automatically generated based on the node\ntemplates and relationship templates defined in the service\ntemplate.<span class=\"comment-end\" id=\"67\"></span></td>\n</tr>\n<tr class=\"even\">\n<td>Node Template</td>\n<td>A <em>Node Template</em> specifies the occurrence of a component\nnode as part of a service template. Each Node Template refers to a Node\nType that defines the semantics of the node (e.g., properties,\nattributes, requirements, capabilities, interfaces). Node Types are\ndefined separately for reuse purposes.</td>\n</tr>\n<tr class=\"odd\">\n<td>Relationship Template</td>\n<td>A <em>Relationship Template</em> specifies the occurrence of a\nrelationship between nodes in a service template. Each Relationship\nTemplate refers to a Relationship Type that defines the semantics\nrelationship (e.g., properties, attributes, interfaces, etc.).\nRelationship Types are defined separately for reuse purposes.</td>\n</tr>\n<tr class=\"even\">\n<td>Service Template</td>\n<td>A <em>Service Template</em> is typically used to specify the\n\u201ctopology\u201d (or structure) and \u201corchestration\u201d (or invocation of\nmanagement behavior) of IT services so that they can be provisioned and\nmanaged in accordance with constraints and policies.</td>\n</tr>\n<tr class=\"odd\">\n<td>Topology Model</td>\n<td>A Topology Model defines the structure of a service in the context\nof a Service Template. A Topology model consists of a set of Node\nTemplate and Relationship Template definitions that together define the\ntopology of a service as a (not necessarily connected) directed\ngraph.</td>\n</tr>\n<tr class=\"even\">\n<td>Abstract Node Template</td>\n<td><span class=\"comment-start\" id=\"70\" data-author=\"Calin Curescu\"\ndata-date=\"2019-02-06T18:10:00Z\">I think the latest understanding is\nthat a node is either \u201cregular\u201d or \u201cselected\u201d or \u201csubstituted\u201d, we don\u2019t\nneed the concept of an abstract node anymore.<br />\nTo be replaced with a definition of a node that is substituted or\nselected.<br />\nAlso check the <strong>concrete</strong> node definition, e.g. \u201cnode\ndefinition that are not substituted or selected may be referred more\nspecifically as regular nodes\u201d.</span>An abstract node template is a\nnode template that doesn\u2019t define any implementations for the TOSCA\nlifecycle management operations<span class=\"comment-end\"\nid=\"70\"></span>. Service designers explicitly mark node templates as\nabstract using the substitute directive. TOSCA orchestrators provide\nimplementations for abstract node templates by finding substituting\ntemplates for those node templates.</td>\n</tr>\n</tbody>\n</table>\n\nTOSCA core concepts\n===================\n\nThe TOSCA language introduces a YAML-based grammar for creating service\ntemplates that define the lifecycle management of\n<span class=\"comment-start\" id=\"91", "author": "Calin Curescu", "date": "2020-06-22T17:51:00Z", "comment": "digital services (i.e. infrastructure,\n\u2026)", "target": "application"}-->
,
infrastructure, and network services. The language defines a *metamodel*
for specifying both the structure of a service as well as its management
aspects. Within a TOSCA file, a *Service Template* defines the
*structure* of a service. *Interfaces, Operations, and Workflows* define
how service elements can be created and terminated as well as how they
can be managed during their whole lifetimes. Policies specify
operational behavior of the service such as quality-of-service
objectives, performance objectives, and security constraints, and allow
for closed-loop automation. The major elements defining a service are
depicted in Figure 1.

Service Templates, Node Templates, and Relationships
----------------------------------------------------

Within a TOSCA file, a Service Template defines the topology model of a
service as a directed acyclic graph. Each node in this graph is
represented by a *Node Template*. A Node Template specifies the presence
of an entity of a specific *Node Type* as a component of a service. A
Node Type defines the properties of such a component (via *Node Type
Properties*) and the operations (via *Interfaces*) available to
manipulate the component. Node Types are defined separately for reuse
purposes. In a service template a Node Template assigns values to the
properties defined in the Node Type.

<img src="media/image2.png" style="width:6.58577in;height:3.41667in" /><img src="media/image3.png" style="width:6in;height:3.11in" />

Figure : Structural Elements of a Service Template and their Relations

For
example
<!----
{"id": "94", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-04T16:20:00Z", "comment": "A diagram of the example would help", "target": "\nexample"}-->
, consider a service
that consists of an application server, a process engine, and a process
model. A Service Template defining that service would include one Node
Template of Node Type “application server”, another Node Template of
Node Type “process engine”, and a third Node Template of Node Type
“process model”. The application server Node Type defines properties
like the IP address of an instance of this type, an operation for
installing the application server with the corresponding IP address, and
an operation for shutting down an instance of this application server. A
constraint in the Node Template can specify a range of IP addresses
available when making a concrete application server available.

Node templates may include one or more
<span class="comment-start" id="96" author="Chris Lauwers"
date="2021-01-18T18:20:00Z">Mike Rehder suggested to use the general
term “relations” to avoid reference to “relationship templates” or
types.</span>*relationships* 
<!----
{"id": "95", "author": "Calin Curescu", "date": "2020-06-22T17:58:00Z", "comment": "Will this be understood correctly, since\nthis is part of the node requirement and not relationship template as\nsuch.", "target": "Node templates may include one or more\n<span class=\"comment-start\" id=\"96\" author=\"Chris Lauwers\"\ndate=\"2021-01-18T18:20:00Z\">Mike Rehder suggested to use the general\nterm \u201crelations\u201d to avoid reference to \u201crelationship templates\u201d or\ntypes.</span>*relationships* "}-->
to
other node templates in the Service Template. Relationships represent
the edges in the service topology
graph
<!----
{"id": "97", "author": "Michael Rehder", "date": "2020-12-15T08:49:00Z", "comment": "New term! It\u2019s\nconfusing to have \u201cService Template\u201d and \u201cService Topology Graph\u201d and\n\u201cTopology Template\u201d.", "target": "service topology\ngraph"}-->
.
The
<!----
{"id": "98", "author": "Chris Lauwers", "date": "2021-01-18T18:17:00Z", "comment": "Should we introduce \u201cservice topology graph\u201d\nwhen what we mean is really the \u201cinstance\nmodel\u201d.", "target": "The"}-->
 node template
that includes the relationship definition is implicitly defined as the
source node of the relationship and the target node is explicitly
specified as part of the relationship definition. Each relationship
definition refers to a Relationship Type that defines the semantics and
any properties of the relationship. Relationship Types are defined
separately for reuse purposes. <span class="comment-end" id="95"></span>

In the example above, a relationship can be established from the process
engine Node Template to the application server Node Template with the
meaning “hosted by”, and from the process model Node Template to the
process engine Node Template with meaning “deployed on”.

Interfaces, Operations, and Artifacts
-------------------------------------

Both node and relationship types may define lifecycle *operations* that
implement the behavior an orchestration engine can invoke when
instantiating a service template. For example, a node type for some
software product might provide a ‘create’ operation to handle the
creation of an instance of a component at runtime, or a ‘start’ or
‘stop’ operation to handle a start or stop event triggered by an
orchestration engine.

Operations that are related to the same management mission (e.g.
lifecycle management) are grouped together in *Interfaces* that are
defined by node and relationship types. Just like other TOSCA entities,
interfaces refer to their corresponding *Interface Type* that defines
the group of operations that are part of the interface. Interface Types
can also define *notifications* that represent external events that are
generated by the outside world and received by the orchestrator.

The implementations of interface operations can be provided as TOSCA
*artifacts*. An artifact represents the content needed to provide an
implementation for an interface operation. A TOSCA artifact could be an
executable (e.g. a script, an executable program, an image), a
configuration file or data file, or something that might be needed so
that another executable can run (e.g. a library). Artifacts can be of
different types, for example EJBs or python scripts. The content of an
artifact depends on its type. Typically, descriptive metadata (such as
properties) will also be provided along with the artifact. This metadata
might be needed to properly process the artifact, for example by
describing the appropriate execution environment.

Workflows
---------

A deployed service is an instance of a service
template
<!----
{"id": "101", "author": "Michael Rehder", "date": "2020-12-15T08:46:00Z", "comment": "This isn\u2019t correct as this document says\nthat a \u201cService Template\u201d is merely a TOSCA document and so could just\nhave type definitions within it.", "target": ""}-->
. More precisely, the instance is created by
instantiating the Service Template of its TOSCA file by running
workflows that are most often automatically created by the orchestrator
and that invoke the interface operations of the Node Types or the Node
Templates. Orchestrators can automatically generate workflows by using
the relationship between components to derive the order of component
instantiation. For example, during the instantiation of a two-tier
application that includes a web application that depends on a database,
an orchestration engine would first invoke the ‘create’ operation on the
database component to install and configure the database, and it would
then invoke the ‘create’ operation of the web application to install and
configure the application (which includes configuration of the database
connection).

Interface operations invoked by workflows must use actual values for the
various properties of the various Node Templates and Relationship
Templates of the Service Template. These values can come from input
passed in by users as triggered by human interactions with the
orchestrator or the templates can specify default values for some
properties. For example, the application server Node Template will be
instantiated by installing an actual application server at a concrete IP
address considering the specified range of IP addresses. Next, the
process engine Node Template will be instantiated by installing a
concrete process engine on that application server (as indicated by the
“hosted by” relationship template). Finally, the process model Node
Template will be instantiated by deploying the process model on that
process engine (as indicated by the “deployed on” relationship
template).

Requirements and Capabilities
-----------------------------

We discussed earlier how relationships are used to link node templates
together into a service topology graph. However, it may not always be
possible to define all node templates for a given
service topology within a single service
template
<!----
{"id": "107", "author": "Michael Rehder", "date": "2020-12-15T09:11:00Z", "comment": "Confusing \u2013 \u201cservice topology\u201d is a new\nterm. It\u2019s a \u201ctopology template\u201d but not all \u201cservice template\u201d are a\n\u201ctopology template\u201d.", "target": "service topology within a single service\ntemplate"}-->
. For example, modular
design practices may dictate that different service subcomponents be
modeled using separate service templates. This may result in
relationships that need to be established across multiple service
templates. Additionally, relationships may need to target components
that already exist and do not need to be instantiated by an
orchestrator. For example, relationships may reference physical
resources that are managed in a resource inventory. Service templates
may not include node templates for these resources.

TOSCA accommodates these scenarios using *requirements* and
*capabilities* of node templates. A requirement expresses that one
component depends on (requires) a feature provided by another component,
or that a component has certain requirements against the hosting
environment such as for the allocation of certain resources or the
enablement of a specific mode of operation. Capabilities represent
features exposed by components that can be used to fulfill requirements
of other components.

Relationships are the result of fulfilling a requirement in one node
template using a capability of a different node template. If both source
and target node templates are defined in the same service template,
service designers typically define the relationship between these node
templates explicitly. Requirements that do not explicitly specify a
target node must be fulfilled by the orchestrator at service deployment
time. Orchestrators can take multiple service templates into account
when fulfilling requirements, or they can attempt to use resources
managed in an inventory, which will result in relationships that are
established across service template boundaries.

Requirements and capabilities are modeled by annotating Node Types with
*Requirement Definitions* and *Capability Definitions*. *Capability
Types* are defined as reusable entities so that those definitions can be
used in the context of several Node Types. Requirement definitions can
specify the relationship type that will be used when creating the
relationship that fulfills the requirement.

<img src="media/image4.png" style="width:3.35in;height:2.1in" />

Figure : Requirements and Capabilities

Node Templates which have corresponding Node Types with Requirement
Definitions or Capability Definitions will include representations of
the respective *Requirements* and *Capabilities* with content specific
to the respective Node Template.

Requirements can be matched in two ways as briefly indicated above: (1)
requirements of a Node Template can be matched by capabilities of
another Node Template in the same Service Template by connecting the
respective requirement-capability-pairs via relationships; (2)
requirements of a Node Template can be matched by the orchestrator, for
example by allocating needed resources for a Node Template during
instantiation.
<!----
{"id": "108", "author": "Michael Rehder", "date": "2020-12-15T16:33:00Z", "comment": "There should be some\ndiscussion about this issue \u2013 how are the relations defined in the\ntopology template related to the relations of the substituted node\ntype?", "target": ""}-->


Decomposition of Service Templates
----------------------------------

TOSCA provides support for decomposing service components using the
Substitution Mapping feature. For example, a Service Template

<!----
{"id": "114", "author": "Michael Rehder", "date": "2020-12-15T16:17:00Z", "comment": "Another\nplace where I find the use of the term \u201cService Template\u201d overly\nconfusing. It should say \u201cTopology Template\u201d as that is the construct in\nthe end that is supporting the substitution.  \nSection 4.5.1 says \u201ctopology template\u201d so I think this change is in line\nwith the practical definitions in the document.", "target": "Service Template\n"}-->
for a business application
that is hosted on an application server tier might focus on defining the
structure and manageability behavior of the business application itself.
The structure of the application server tier hosting the application can
be provided in a separate Service Template built by another vendor
specialized in deploying and managing application servers. This approach
enables separation of concerns and re-use of common infrastructure
templates.

<img src="media/image5.png" style="width:3.75in;height:2.77in" />

Figure : Service Template Decomposition

From the point of view of a Service Template (e.g. the business
application Service Template from the example above) that uses another
Service Template, the other Service Template (e.g. the application
server tier) “looks” like just a Node Template. During deployment,
however, this Node Template can be substituted by the second Service
Template if it exposes the same external *façade* (i.e. properties,
capabilities, etc.) as the Node Template. Thus, a substitution with any
Service Template that has the same *facade* as a certain Node Template
in one Service Template becomes possible, allowing for a flexible
composition of different Service Templates. This concept also allows for
providing substitutable alternatives in the form of Service Templates.
For example, a Service Template for a single node application server
tier and a Service Template for a clustered application server tier
might exist, and the appropriate option can be selected per deployment.

Policies in TOSCA
-----------------

Non-functional behavior or quality-of-services are defined in TOSCA by
means of policies. A Policy can express such diverse things like
monitoring behavior, payment conditions, scalability, or continuous
availability, for example.

A Node Template can be associated with a set of Policies collectively
expressing the non-functional behavior or quality-of-services that each
instance of the Node Template will expose. Each Policy specifies the
actual properties of the non-functional behavior, like the concrete
payment information (payment period, currency, amount etc.) about the
individual instances of the Node Template.

These properties are defined by a Policy Type. Policy Types might be
defined in hierarchies to properly reflect the structure of
non-functional behavior or quality-of-services in particular domains.
Furthermore, a Policy Type might be associated with a set of Node Types
the non-functional behavior or quality-of-service it describes.

Policy Templates provide actual values of properties of the types
defined by Policy Types. For example, a Policy Template for monthly
payments for US customers will set the “payment period” property to
“monthly” and the “currency” property to “US\$”, leaving the “amount”
property open. The “amount” property will be set when the corresponding
Policy Template is used for a Policy within a Node Template. Thus, a
Policy Template defines the invariant properties of a Policy, while the
Policy sets the variant properties resulting from the actual usage of a
Policy Template in a Node Template.

Archive Format for Cloud Applications
-------------------------------------

In order to support in a certain environment for the execution and
management of the lifecycle of a cloud application, all corresponding
artifacts have to be available in that environment. This means that
beside the service template of the cloud application, the deployment
artifacts and implementation artifacts have to be available in that
environment. To ease the task of ensuring the availability of all of
these, this specification defines a corresponding archive format called
CSAR (Cloud Service ARchive).

A CSAR is a container file, i.e. it contains multiple files of possibly
different file types. These files are typically organized in several
subdirectories, each of which contains related files (and possibly other
subdirectories etc.). The organization into subdirectories and their
content is specific for a particular cloud application. CSARs are zip
files, typically compressed. A CSAR may contain a file called TOSCA.meta
that describes the organization of the CSAR.

TOSCA <span class="comment-start" id="130" author="Chris Lauwers" date="2021-06-28T23:14:00Z">Alternatively, we could also move this section into Chapter 5</span>Entities
<!----
{"id": "129", "author": "Chris Lauwers", "date": "2021-06-28T23:14:00Z", "comment": "This subsection has been moved here from the Operational Model chapter. We need to revisit where exactly it belongs to make sure the document flows correctly.", "target": "<span class=\"comment-start\" id=\"130\" author=\"Chris Lauwers\" date=\"2021-06-28T23:14:00Z\">Alternatively, we could also move this section into Chapter 5</span>Entities"}-->
</span>
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When defining services using TOSCA, we must distinguish between four
kinds of entities:

1.  **TOSCA Types**: TOSCA types define re-usable building blocks that
    can be used during service design. For example, TOSCA Node Types
    define reusable service components, including their configurable
    properties.

<!-- -->

2.  **TOSCA Templates**: TOSCA templates define (typed) components of a
    service. For example, service templates include node templates that
    assign specific values (often using TOSCA intrinsic functions) to
    the configurable properties defined in the corresponding node types.
    It is not uncommon to have multiple node templates of the same node
    type in a service template.

3.  **Representations**: At deployment time, TOSCA implementations
    combine TOSCA service templates with deployment-specific input
    values to create run-time representations of the service that is to
    be deployed and managed. Note that TOSCA does not standardize an
    object model for representations. Instead, such models are
    implementation specific.

4.  **External Implementations**: These are the actual entities in the
    external world that correspond to the representations managed by the
    orchestrator. TOSCA implementations that provide runtime service
    management must keep their internal service representations in sync
    with the actual state of the external implementations.

TOSCA Operational Model
=======================

This section presents a TOSCA Functional Architecture and an associated
operational model that supports the three service lifecycle phases
outline above. Note that this functional architecture is not intended to
prescribe how TOSCA must be implemented. Instead, it aims to provide
users of TOSCA with a mental model of how TOSCA implementations are
expected to process TOSCA files.

While TOSCA does not mandate that compatible implementations must
support all three lifecycle phases, a complete architecture must
anticipate all three and must include support for all four kinds of
TOSCA entities. The TOSCA architecture defined here illustrates how the
various TOSCA entities are used and how they are related.

<img src="media/image6.png" style="width:6.45in;height:1.8in"
alt="Timeline Description automatically generated with medium confidence" />

Figure : TOSCA Functional Architecture

The functional architecture defines the following three blocks:

1.  **TOSCA Processor**: This functional block defines functionality
    that must be provided by all TOSCA implementations. TOSCA processors
    convert TOSCA-based service definitions into service
    representations 
<!----
{"id": "132", "author": "Chris Lauwers", "date": "2021-06-28T23:19:00Z", "comment": "We need to better define the concept of\n    \"representations\"", "target": "representations "}-->
that can be processed by an Orchestrator.

<!-- -->

3.  **Orchestrator**: This functional block creates external
    implementations on various resource platforms based on the service
    representations created by a TOSCA processor. The orchestration
    functionality can itself be defined using TOSCA or can be provided
    by external (non-TOSCA) orchestration platforms.

4.  **Platform**: In the context of a TOSCA architecture, platforms
    represent external cloud, networking, or other infrastructure
    resources on top of which service entities can be created.

The remainder of this section describes each of these functional blocks
in more detail.

TOSCA Processor
---------------

At the core of a compliant TOSCA implementation is a TOSCA Processor
that can create service representations from TOSCA service templates. A
TOSCA Processor contains the following functional blocks:

### Parser

- Accepts a single TOSCA file plus imported TOSCA files (files without a
  “service_template”)

- Can (optionally) import these units from one or more repositories,
  either individually or as complete profiles

- Outputs valid normalized node templates and <u>unresolved</u>
  requirements (one-to-one equivalency)

### Resolver

A resolver performs the following functions

#### Creating Service Representations

- Applies service inputs.

- Converts normalized node templates to node representations (one-to-one
  equivalency *\[cardinality?\]*) *\[a full TOSCA orchestrator can
  manage these instead of the external orchestrator/platform\]*

- Calls intrinsic functions (on demand for all the above) using the
  graph of node representations.

#### Requirement Fulfillment

- Satisfies all requirements and creates the relationship graph (an
  unsatisfied requirement results in an error)

#### Substitution Mapping

Orchestrator
------------

An orchestrator performs the following actions:

- (Continuously) turns node representations into zero or more node
  implementations (one-to-any)

- (Continuously) updates node representation attribute values (error if
  they do not adhere to TOSCA type validation clauses or property
  definition validation clauses) *\[we still don’t know how to handle
  multiplicity\]*

- (Continuously) reactivates the resolver: outputs and even satisfaction
  of requirements may change.

- (Optionally) changes the node representations themselves for day 2
  transformations.

TOSCA definitions
=================

Except for the examples, this section is **normative** and describes the
YAML grammar, definitions, and semantics for all keynames that are
defined in the TOSCA Version 2.0 specification.

TOSCA <span class="comment-start" id="158" author="Chris Lauwers" date="2022-06-25T17:36:00Z">This section should be moved into the previous chapter</span><span class="comment-start" id="159" author="Chris Lauwers" date="2022-12-05T18:42:00Z">What is a metamodel?</span>Metamodel
<!----
{"id": "157", "author": "Chris Lauwers", "date": "2022-06-25T17:36:00Z", "comment": "Inconsistent capitalization", "target": "<span class=\"comment-start\" id=\"158\" author=\"Chris Lauwers\" date=\"2022-06-25T17:36:00Z\">This section should be moved into the previous chapter</span><span class=\"comment-start\" id=\"159\" author=\"Chris Lauwers\" date=\"2022-12-05T18:42:00Z\">What is a metamodel?</span>Metamodel"}-->
</span></span>
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section defines the models and the modeling goals that comprise the
TOSCA Version 2.0 specification.

### Modeling concepts and goals

TBD. Here we should have selected core concepts of TOSCA 1.0 from
section “[3   Core Concepts and Usage
Pattern](http://docs.oasis-open.org/tosca/TOSCA/v1.0/os/TOSCA-v1.0-os.html#_Toc356403643)”
and this section should be a more in-depth section than section 2.1 in
this document.
<!----
{"id": "161", "author": "Calin Curescu", "date": "2020-04-16T12:53:00Z", "comment": "This section needs completion before submitting the TOSCA 2.0.", "target": "Modeling concepts and goals\n\nTBD. Here we should have selected core concepts of TOSCA 1.0 from\nsection \u201c[3\u00a0\u00a0\u00a0Core Concepts and Usage\nPattern](http://docs.oasis-open.org/tosca/TOSCA/v1.0/os/TOSCA-v1.0-os.html#_Toc356403643)\u201d\nand this section should be a more in-depth section than section 2.1 in\nthis document."}-->


Add a metamodel picture

Explain separation of concerns and different roles. Refer to email from
Peter.

### Modeling definitions and reuse

The TOSCA metamodel includes complex definitions used in types and
templates. Reuse concepts simplify the design of TOSCA templates by
allowing relevant TOSCA entities to use and/or modify definitions
already specified during entity type design. The following four concepts
are clarified next:

- **Definition**:

<!-- -->

- The TOSCA specification is based on defining modeling entities.

- Entity definitions are based on different sets of keynames (with
  specific syntax and semantics) that are associated with values (of a
  specific format
<!----
{"id": "163", "author": "Chris Lauwers", "date": "2021-01-17T00:51:00Z", "comment": "Alternative language proposed by PJ:\n  Entity definitions comprise pairs of keynames and values. Each entity\n  has it own syntax, semantics and set of\n  keynames.", "target": "format"}-->
).

<!-- -->

- **Derivation**:

<!-- -->

- Specific TOSCA entities support a type definition.

- When defining a type, it can be derived from a parent type and inherit
  all the definitions of the parent type.

- The derivation rules describe what (keyname) definitions are inherited
  from the parent type and further if and how they can be expanded or
  
<!----
{"id": "164", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-04T16:42:00Z", "comment": "Expansion and modification is part of\n  Refinement not Derivation. This bullet point should be\n  removed", "target": ""}-->
modified. Note
  that some definitions (for example, “version”) and intrinsic to the
  type declaration and so are not inherited.

- A parent type can in turn be derived from a parent type. There is no
  limit to the depth of a chain of derivations.

<!-- -->

- **Refinement**:

<!-- -->

- Definitions within a type definition consist of the definition of
  keynames and other TOSCA entities (e.g. properties, requirements,
  capabilities, etc.). 
<!----
{"id": "165", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-04T16:43:00Z", "comment": "Type\n  definition is part of Definition not\n  Refinement", "target": ""}-->

  Definitions within a parent type can be refined (adjusted) to better
  suit the needs of the referencing type.

- The refinement rules pertaining to an entity describe how such entity
  definitions that are inherited from the parent type during a type
  derivation can be expanded or modified.

<!-- -->

- **Augmentation**
<!----
{"id": "166", "author": "Mike Rehder", "date": "2020-04-30T11:10:00Z", "comment": "I think separating augmentation is helpful\n  (as YANG has done). I think it makes it easier to understand the rules\n  that apply for the refining or augmenting\n  scenario", "target": "**Augmentation**"}-->
:

<!-- -->

- Definitions within a parent type can be expanded, which is the
  addition of properties, to better suit the requirements of the
  referencing type.

- The augmentation rules pertaining to an entity describe how the
  inherited parent type during a type derivation can be added to.

<!-- -->

- **Assignment**:

<!-- -->

- When creating a service template, we specify several entities that are
  part of the template (e.g., nodes, relationships, groups, etc.).

- When adding such an entity in the service template, for some
  definitions that appear in the corresponding entity type (e.g.,
  properties, operations, requirements, etc.) we may (or must) assign a
  certain specification (or value).

### Goal of the derivation and refinement rules

The main reason for derivation and refinement rules is to create a
framework useful for a consistent TOSCA type profile creation. The
intuitive idea is that a derived type follows to a large extent the
structure and behavior of a parent type, otherwise it would be better to
define a new "not derived" type.

The guideline regarding the derivation rules is that a node of a derived
type should be usable instead of a node of the parent type during the
selection and substitution mechanisms. These two mechanisms are used by
TOSCA templates to connect to TOSCA nodes and services defined by other
TOSCA templates:

- The selection mechanism allows a node instance created a-priori by
  another service template to be selected for usage (i.e., building
  relationships) to the current TOSCA template.

- The substitution mechanism allows a node instance to be represented by
  a service created simultaneously via a substitution template.

It is relevant to emphasize the cross-template usage, as only in this
case we deal with templates defined at different design time-points,
with potentially different editing and maintenance restrictions.

### Mandatory Keynames

The TOSCA metamodel includes complex definitions used in types (e.g.,
Node Types, Relationship Types, Capability Types, Data Types, etc.),
definitions and refinements (e.g., Requirement Definitions, Capability
Definitions, Property and Parameter Definitions, etc.) and templates
(e.g., Service Template, Node Template, etc.) all of which include their
own list of reserved keynames that are sometimes marked as
**mandatory**. If a keyname is marked as mandatory it **MUST** be
defined in that particular definition context. In some definitions,
certain keywords may be mandatory depending on the value of other
keywords in the definition. In that case, the keyword will be marked as
**conditional** and the condition will be explained in the description
column. Note that in the context of type definitions, types may be used
to derive other types, and keyname definitions **MAY** be inherited from
parent types (according to the derivation rules of that type entity). If
a keyname definition is inherited, the derived type does not have to
provide such definition.

TOSCA Service
<!----
{"id": "172", "author": "Calin Curescu", "date": "2020-04-20T18:49:00Z", "comment": "TBD. Here comes some intro and generic description of the different specification blocks that will build the following sections.", "target": "TOSCA Service"}-->

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A TOSCA Service is
specified by a TOSCA Service <span class="comment-start" id="174"
author="Chris Lauwers" date="2022-12-05T18:44:00Z">We haven't defined
service template yet.</span>Template
<!----
{"id": "173", "author": "Michael Rehder", "date": "2020-12-15T08:38:00Z", "comment": "This isn\u2019t true \u2013 if a \u201cService Template\u201d\ncan contain just supporting parts like type definitions then it won\u2019t\ncontain a \u201cTOSCA Service\u201d.  \nIn the end, I think that the term \u201cService Template\u201d is very confusing\nas it is never used as a \u201ctemplate\u201d, as an object. It\u2019s a collection of\ndefinitions, some of which are supporting and one of which is the\nworking code definition for the service to be realized.  \n\u201cService Definition\u201d is a more practical term.", "target": "A TOSCA Service is\nspecified by a TOSCA Service <span class=\"comment-start\" id=\"174\"\nauthor=\"Chris Lauwers\" date=\"2022-12-05T18:44:00Z\">We haven't defined\nservice template yet.</span>Template"}-->
.<span class="comment-end" id="173"></span>

### TOSCA file definition
<!----
{"id": "178", "author": "Chris Lauwers", "date": "2022-06-22T14:26:00Z", "comment": "Update to reflect new naming", "target": "TOSCA file definition"}-->


A TOSCA file contains definitions of building blocks for use in cloud
applications or complete models of cloud applications. This section
describes the top-level TOSCA keynames—along with their grammars—that
are allowed to appear in a TOSCA file.

#### Keynames

The following is the list of recognized keynames for a TOSCA file:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Grammar
<!----
{"id": "181\"\ndata-author=\"Jordan,PM,Paul,TNK6 R\" data-date=\"2020-11-05T10:17:00Z\">The\nuse of the word \u2018optional\u2019 in the descriptions is inconsistent. In some\nrows it occurs before the work \u2018map\u2019- in those cases it is repeating the\ninformation in the \u2018Required\u2019 column. In other rows it occurs after the\nwork \u2018map\u2019 and so operates on the elements of the map. In these rows I\nthink it is stating that the element can be declared but not used. Yet\nother rows do not included the word optional which could be taken to\nmean they have some third status of optionality.</span>Description<span\nclass=\"comment-end\" id=\"181\"></span></th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>tosca_definitions_version</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Defines the version of the TOSCA specification used in the TOSCA\nfile</td>\n</tr>\n<tr class=\"even\">\n<td>profile</td>\n<td>no</td>\n<td>string</td>\n<td>The profile name that can be used by other TOSCA files to import the\ntype definitions in this document.</td>\n</tr>\n<tr class=\"odd\">\n<td>metadata</td>\n<td>no</td>\n<td><a href=\"#tosca-map-type\">map</a> of YAML values</td>\n<td>Defines a section used to declare additional metadata information.\nDomain-specific TOSCA profile specifications may define keynames that\nare mandatory for their implementations.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Declares a description for this TOSCA file and its contents.</td>\n</tr>\n<tr class=\"odd\">\n<td>dsl_definitions</td>\n<td>no</td>\n<td>N/A</td>\n<td>Defines reusable YAML macros (i.e., YAML alias anchors) for use\nthroughout the TOSCA file.</td>\n</tr>\n<tr class=\"even\">\n<td>repositories</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a\nhref=\"#i-recommend-removing-this-entire-section-and-rewriting-any-parts-that-are-still-relevant-inside-the-imports-section.namespaces\">Repository\ndefinitions</a></p></td>\n<td>Declares the map of external repositories that contain artifacts\nthat are referenced in the TOSCA file along with the addresses used to\nconnect to them in order to retrieve the artifacts.</td>\n</tr>\n<tr class=\"odd\">\n<td>imports</td>\n<td>no</td>\n<td><p>list of</p>\n<p><a\nhref=\"#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition\">Import\ndefinitions</a></p></td>\n<td>Declares a list of import statements pointing to external TOSCA\nfiles or well-known profiles. For example, these may be file locations\nor URIs relative to the TOSCA file within the same TOSCA CSAR file.</td>\n</tr>\n<tr class=\"even\">\n<td>artifact_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#artifact-type\">Artifact Types</a></p></td>\n<td>This section contains amap of artifact type definitions for use in\nthe TOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"odd\">\n<td>data_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#data-type\">Data Types</a></p></td>\n<td>Declares a map of TOSCA Data Type definitions for use in the TOSCA\nfile and/or external TOSCA files.</td>\n</tr>\n<tr class=\"even\">\n<td>capability_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#capability-type\">Capability Types</a></p></td>\n<td>This section contains amap of capability type definitions for use in\n<span class=\"comment-start\" id=\"182\" data-author=\"Chris Lauwers\"\ndata-date=\"2021-01-17T00:56:00Z\">Paul Jordan suggest \u201cfor use in a\nservice template\u201d (as opposed to \u201cfor use in the service\ntemplate\u201d)</span>the<span class=\"comment-end\" id=\"182\"></span> TOSCA\nfile and/or external TOSCA files.</td>\n</tr>\n<tr class=\"odd\">\n<td>interface_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#interface-type\">Interface Types</a></p></td>\n<td>This section contains amap of interface type definitions for use in\nthe TOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"even\">\n<td>relationship_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a\nhref=\"#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type\">Relationship\nTypes</a></p></td>\n<td>This section contains a map of relationship type definitions for use\nin the TOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"odd\">\n<td>node_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#node-type\">Node Types</a></p></td>\n<td>This section contains a map of node type definitions for use in the\nTOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"even\">\n<td>group_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#group-type\">Group Types</a></p></td>\n<td>This section contains a map of group type definitions for use in the\nTOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"odd\">\n<td>policy_types</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#policy-type\">Policy Types</a></p></td>\n<td>This section contains a map of policy type definitions for use in\nthe TOSCA file and/or external TOSCA files.</td>\n</tr>\n<tr class=\"even\">\n<td>service_template</td>\n<td>no</td>\n<td><a href=\"#service-template-definition\">service template\ndefinition</a></td>\n<td>Defines a template from which to create a mode/representation of an\napplication or service. Service templates consist of node templates that\nrepresent the application\u2019s or service\u2019s components, as well as\nrelationship templates representing relations between these\ncomponents.</td>\n</tr>\n<tr class=\"odd\">\n<td>Functions</td>\n<td>no</td>\n<td>map of function definitions</td>\n<td>This section contains a map of function definitions for use in the\nTOSCA file and/or external TOSCA files.</td>\n</tr>\n</tbody>\n</table>\n\n#### <span class=\"comment-start\" id=\"185", "author": "Chris Lauwers", "date": "2020-09-01T16:14:00Z", "comment": "Tal: do we even need these grammar sections? Often grammar section is out of sync with keynames section, and \u201cnotes\u201d section has most of the relevant info.", "target": "Grammar"}-->


The overall structure of a TOSCA file and its top-level keynames is
shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Mandatory TOSCA version string</p>
<p>tosca_definitions_version: &lt;value&gt; # Mandatory, see section

<!----
{"id": "186\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-08-31T23:39:00Z\">Update cross references later when\ndocument outline is final.</span><span class=\"comment-start\" id=\"187\"\ndata-author=\"Chris Lauwers\" data-date=\"2020-09-01T16:16:00Z\"></span>3.1\n<span class=\"comment-end\" id=\"186\"><span class=\"comment-end\"\nid=\"187\"></span></span>for usage</p>\n<p>profile: &lt;string&gt; # Optional, see section 3.2 for usage</p>\n<p># Optional metadata keyname: value pairs</p>\n<p>metadata:</p>\n<p># map of YAML values</p>\n<p># Optional description of the definitions inside the file.</p>\n<p>description: &lt;<a href=\"#TYPE_YAML_STRING\">template_\ndescription</a>&gt;</p>\n<p><span class=\"comment-start\" id=\"188\" data-author=\"Matt Rutkowski\"\ndata-date=\"2015-08-25T21:52:00Z\">Should this appear after imports to\nassure anchors do not overwrite each other (from imported defn.\nfiles)?</span>dsl_definitions:</p>\n<p># map of YAML alias anchors (or macros)<span class=\"comment-end\"\nid=\"188\"></span></p>\n<p>repositories:</p>\n<p># map of external repository definitions which host TOSCA\nartifacts</p>\n<p>imports:</p>\n<p># ordered list of <a\nhref=\"#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition\">import\ndefinitions</a></p>\n<p>artifact_types:</p>\n<p># map of <a href=\"#artifact-type\">artifact type</a> definitions</p>\n<p>data_types:</p>\n<p># map of <a href=\"#data-type\">datatype</a> definitions</p>\n<p>capability_types:</p>\n<p># map of <a href=\"#capability-type\">capability type</a>\ndefinitions</p>\n<p>interface_types</p>\n<p># map of <a href=\"#interface-type\">interface type</a> definitions</p>\n<p>relationship_types:</p>\n<p># map of <a\nhref=\"#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type\">relationship\ntype</a> definitions</p>\n<p>node_types:</p>\n<p># map of <a href=\"#node-type\">node type</a> definitions</p>\n<p>group_types:</p>\n<p># map of <a href=\"#group-type\">group type</a> definitions</p>\n<p>policy_types:</p>\n<p># map of <a href=\"#policy-type\">policy type</a> definitions</p>\n<p>functions:</p>\n<p># map of function definitions`</p>\n<p>service_template:</p>\n<p># service template definition of the cloud application or\nservice</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### Requirements\n\n- The key \u201ctosca_definitions_version\u201d<span class=\"comment-start\"\n  id=\"191", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T10:30:00Z", "comment": "The document does not state any other\n  requirement on the order of the top-level collations. This clause\n  infers that they can be in any order but I suspect many\n  implementations would expect types to be defined before they are\n  referenced. I suggest the order in 4.2.1.2 is made mandatory\n  explicitly in which case this clause is not required.  \n  In addition this clause uses SHOULD while 4.2.2.1.2 uses\n  MUST", "target": ""}-->
 MUSTbe the first
  line of each TOSCA file..

##### Notes
<!----
{"id": "194", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "**[TOSCA-246](../customXml/item1.xml): Comments captured**: Perhaps need an advanced concept to define \u201cfeatures\u201d that are not necessarily attached to a particular node. (like things you might include in a manifest). Like the requirement for a global time sync. How do we reference that feature, where is that feature attached to (some node?). perhaps add a new keyword like \u201ccloud\u201d that can hold all these Features that have no immediate Node to attach them to. Perhaps a syntax convention, where we might just list the names of the features (in some precedent order (sequence). Need to answer: -Who requires, it who fulfills it and how do u maintain the relationship? Luc: Environmental requirements. e.g., Python or something similar.", "target": "Notes"}-->


- TOSCA files do not have to contain a service_template and MAY contain
  simply type definitions (e.g., Artifact, Interface, Capability, Node,
  Relationship Types, etc.), repository definitions, function
  definitions, or other import statements and be imported for use in
  other TOSCA files.

#### Top-level keyname definitions

##### tosca_definitions_version

This mandatory element provides a means to specify the TOSCA version
used within the TOSCA file. It is an indicator for the version of the
TOSCA grammar that should be used to parse the remainder of the TOSCA
file.

###### Keyname

| tosca_definitions_version |
|---------------------------|

###### Grammar

| tosca_definitions_version: \<tosca\_ version\> |
|------------------------------------------------|

TOSCA uses the following version strings for the various revisions of
the TOSCA specification:

| Version String        | TOSCA Specification                      |
|-----------------------|------------------------------------------|
| tosca_2_0             | TOSCA Version 2.0                        |
| tosca_simple_yaml_1_3 | TOSCA Simple Profile in YAML Version 1.3 |
| tosca_simple_yaml_1_2 | TOSCA Simple Profile in YAML Version 1.2 |
| tosca_simple_yaml_1_1 | TOSCA Simple Profile in YAML Version 1.1 |
| tosca_simple_yaml_1_0 | TOSCA Simple Profile in YAML Version 1.0 |

The version for this specification is tosca_2_0.

Note that it is not mandatory for TOSCA Version 2.0 implementations to
support older versions of the TOSCA specifications.

###### Examples:

A TOSCA file designed using the TOSCA Version 2.0 specification:

| tosca_definitions_version: tosca_2_0 |
|--------------------------------------|

##### <span class="comment-start" id="208" author="Chris Lauwers" date="2020-09-01T16:52:00Z">What happens if files imported by a “profile” file also defines a profile?</span>profile
<!----
{"id": "207", "author": "Chris Lauwers", "date": "2020-09-01T02:02:00Z", "comment": "Perhaps this should be its own section?", "target": "<span class=\"comment-start\" id=\"208\" author=\"Chris Lauwers\" date=\"2020-09-01T16:52:00Z\">What happens if files imported by a \u201cprofile\u201d file also defines a profile?</span>profile"}-->
</span>

The profile keyword is used to assign a profile name to the collection
of types defined in this TOSCA file. TOSCA implementations use profile
names to register known profiles into an internal repository. These
profiles can then be imported by other TOSCA files using the profile
keyword in their import statement.

###### Keyname

| profile |
|---------|

###### Grammar

| profile: \<string_value\> |
|---------------------------|

TOSCA does not place any restrictions on the value of the profile name
string. However, we encourage a Java-style reverse-domain notation with
version as a best-practice convention.

###### Examples

The following is an example of a TOSCA file that defines TOSCA Simple
Profile Version 2.0 types:

| profile: org.oasis-open.tosca.simple:2.0 |
|------------------------------------------|

The following defines a domain-specific profile for Kubernetes:

| profile: io.kubernetes:1.18 |
|-----------------------------|

##### metadata

This keyname is used to associate domain-specific metadata with the
Service Template. The metadata keyname allows a declaration of a map of
keynames with values that can use all types supported by the [YAML 1.2.2
recommended
schemas](https://yaml.org/spec/1.2.2/#chapter-10-recommended-schemas)
\[Yaml-1.2\]. Specifically, the following types can be used for metadata
values: map, seq, str, null, bool, int, float
<!----
{"id": "213", "author": "Chris Lauwers", "date": "2022-12-06T14:44:00Z", "comment": "Did we\ndecide to allow recursive metadata (i.e. maps of\nmaps?)", "target": "float"}-->
.

- 

###### Keyname

| metadata |
|----------|

###### Grammar

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>metadata:</p>
<p>&lt;map_of_yaml_values&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>metadata:</p>
<p>creation_date: 2015-04-14</p>
<p>date_updated: 2015-05-01</p>
<p>status: developmental</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### description

This optional keyname provides a means to include single or multiline
descriptions within a TOSCA template as a scalar string value.

###### Keyname

| description |
|-------------|

###### Grammar

| description: \<description\> |
|------------------------------|

###### Example

Single line example

| description: A simple example service template |
|------------------------------------------------|

Multi-line example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>description: "A multiline description</p>
<p>using a quoted string”</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### dsl_definitions

This optional keyname provides a section to define macros YAML-style
macros for use in the TOSCA file.

###### Keyname

| dsl_definitions |
|-----------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>dsl_definitions:</p>
<p>&lt;<a href="#TYPE_YAML_STRING">dsl_definition_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#TYPE_YAML_STRING">dsl_definition_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example
<!----
{"id": "236", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T11:18:00Z", "comment": "There should also be an example of how to use the macro once defined.", "target": "Example"}-->


<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>dsl_Example
<!----
{"id": "237\"\ndata-author=\"Chris Lauwers\" data-date=\"2022-12-06T14:48:00Z\">Show an\nexample of how these macros are used.</span>definitions<span\nclass=\"comment-end\" id=\"237\"></span>:</p>\n<p>ubuntu_image_props: &amp;ubuntu_image_props</p>\n<p>architecture: x86_64</p>\n<p>type: linux</p>\n<p>distribution: ubuntu</p>\n<p>os_version: 14.04</p>\n<p>redhat_image_props: &amp;redhat_image_props</p>\n<p>architecture: x86_64</p>\n<p>type: linux</p>\n<p>distribution: rhel</p>\n<p>os_version: 6.6</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### repositories\n\nThis optional keyname provides a section to define external repositories\nthat may contain artifacts or other TOSCA files that might be referenced\nor imported by this TOSCA file.\n\n###### Keyname\n\n| repositories |\n|--------------|\n\n###### Grammar \n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>repositories:</p>\n<p>&lt;<a href=\"#TYPE_YAML_STRING\">repository_definition_1</a>&gt;</p>\n<p>...</p>\n<p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">repository_definition_n</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### <span class=\"comment-start\" id=\"248", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T08:31:00Z", "comment": "This example is repeated in 4.2.3.2.3. It would be better to have an example which showed multiple repo definitions, probably using a mix of syntax the single line syntax.", "target": "Example"}-->


<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>repositories:</p>
<p>my_project_artifact_repo:</p>
<p>description: development repository for TAR archives and Bash
scripts</p>
<p>url: <a
href="http://mycompany.com/repository/myproject/">http://mycompany.com/repository/myproject/</a></p>
<p>external_repo: https://foo.bar</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### imports

This optional keyname provides a way to import a one or more TOSCA
profiles or other TOSCA files that contain reusable TOSCA type
definitions (e.g., Node Types, Relationship Types, Artifact Types,
etc.), function definitions, repository definitions, or other imports
defined by other authors. This mechanism provides an effective way for
companies and organizations to define domain-specific types and/or
describe their software applications for reuse in other TOSCA files.

###### Keyname

| imports |
|---------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>imports:</p>
<p>- &lt;<a
href="#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition">import_definition_1</a>&gt;</p>
<p>- ...</p>
<p>- &lt;<a
href="#it-would-be-good-to-allow-also-the-import-of-specific-types-via-their-fully-qualified-names-and-also-entire-namespaces-i.e.-types-from-entire-namespaces-from-athe-catalogue.-that-is-in-addition-to-importing-from-a-file-globally-well-known-local-catalog-fileimport-definition">import_definition_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># An example import of TOSCA files from a location relative to
the</p>
<p># file location of the TOSCA file declaring the import.</p>
<p>imports:</p>
<p>- relative_path/my_defns/my_typesdefs_1.yaml</p>
<p>- url: my_defns/my_typesdefs_n.yaml</p>
<p>repository: my_company_repo</p>
<p>namespace: mycompany</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### artifact_types

This optional keyname lists the Artifact Types that are defined by this
TOSCA file..

###### Keyname

| artifact_types |
|----------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>artifact_types:</p>
<p>&lt;<a href="#artifact-type">artifact_type_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#artifact-type">artifact type_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>artifact_types:</p>
<p>mycompany.artifacttypes.myFileType:</p>
<p>derived_from: tosca.artifacts.File</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### data_types

This optional keyname provides a section to define new data types in
TOSCA.

###### Keyname

| data_types |
|------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>data_types:</p>
<p>&lt;<a href="#data-type">tosca_datatype_def_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#data-type">tosca_datatype_def_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>data_types:</p>
<p># A complex datatype definition</p>
<p>simple_contactinfo_type:</p>
<p>properties:</p>
<p>name:</p>
<p>type: string</p>
<p>email:</p>
<p>type: string</p>
<p>phone:</p>
<p>type: string</p>
<p># datatype definition derived from an existing type</p>
<p>full_contact_info:</p>
<p>derived_from: simple_contact_info</p>
<p>properties:</p>
<p>street_address:</p>
<p>type: string</p>
<p>city:</p>
<p>type: string</p>
<p>state:</p>
<p>type: string</p>
<p>postalcode:</p>
<p>type: string</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### capability_types

This optional keyname lists the Capability Types that provide the
reusable type definitions that can be used to describe features of nodes
that can be used to fulfill requirements of other nodes.

###### Keyname

| capability_types |
|------------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>capability_types:</p>
<p>&lt;<a href="#capability-type">capability_type_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#capability-type">capability
type_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>capability_types:</p>
<p>mycompany.mytypes.myCustomEndpoint:</p>
<p>derived_from: tosca.capabilities.Endpoint</p>
<p>properties:</p>
<p># more details ...</p>
<p>mycompany.mytypes.myCustomFeature:</p>
<p>derived_from: tosca.capabilities.Feature</p>
<p>properties:</p>
<p># more details ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### interface_types

This optional keyname lists the Interface Types that provide the
reusable type definitions that can be used to describe operations
exposed by TOSCA relationships and nodes.

###### Keyname

| interface_types |
|-----------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>interface_types:</p>
<p>&lt;<a href="#interface-type">interface_type_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#interface-type">interface type_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>interface_types:</p>
<p>mycompany.interfaces.service.Signal:</p>
<p>operations:</p>
<p>signal_begin_receive:</p>
<p>description: Operation to signal start of some message
processing.</p>
<p>signal_end_receive:</p>
<p>description: Operation to signal end of some message
processed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### relationship_types

This optional keyname lists the Relationship Types that provide the
reusable type definitions that can be used to describe dependent
relationships between nodes.

###### Keyname

| relationship_types |
|--------------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>relationship_types:</p>
<p>&lt;<a
href="#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type">relationship_type_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a
href="#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type">relationship
type_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>relationship_types:</p>
<p>mycompany.mytypes.myCustomClientServerType:</p>
<p>derived_from: Example
<!----
{"id": "297\"\ndata-author=\"Jordan,PM,Paul,TNK6 R\"\ndata-date=\"2020-11-09T08:39:00Z\">This type is no longer defined so it\nshould not be used in an example</span>tosca.relationships.HostedOn<span\nclass=\"comment-end\" id=\"297\"></span></p>\n<p>properties:</p>\n<p># more details ...</p>\n<p>mycompany.mytypes.myCustomConnectionType:</p>\n<p>derived_from: tosca.relationships.ConnectsTo</p>\n<p>properties:</p>\n<p># more details ...</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### node_types\n\nThis optional keyname lists the Node Types that provide the reusable\ntype definitions for nodes in a service.\n\n###### Keyname\n\n| node_types |\n|------------|\n\n###### Grammar \n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_types:</p>\n<p>&lt;<a href=\"#node-type\">node_type_defn_1</a>&gt;</p>\n<p>...</p>\n<p>&lt;<a href=\"#node-type\">node_type_defn_n</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Example\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_types:</p>\n<p>my_webapp_node_type:</p>\n<p>derived_from: WebApplication</p>\n<p>properties:</p>\n<p>my_port:</p>\n<p>type: integer</p>\n<p>my_database_node_type:</p>\n<p>derived_from: Database</p>\n<p>capabilities:</p>\n<p>mytypes.myfeatures.transactSQL</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### group_types\n\nThis optional keyname lists the Group Types that are defined by this\nTOSCA file.\n\n###### Keyname\n\n| group_types |\n|-------------|\n\n###### Grammar \n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>group_types:</p>\n<p>&lt;<a href=\"#group-type\">group_type_defn_1</a>&gt;</p>\n<p>...</p>\n<p>&lt;<a href=\"#group-type\">group type_defn_n</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### <span class=\"comment-start\" id=\"316", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T08:48:00Z", "comment": "There should be a second group definition in the example or it is just a repeat of the group type def example", "target": "Example"}-->


<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>group_types:</p>
<p>mycompany.mytypes.myScalingGroup:</p>
<p>derived_from: tosca.groups.Root</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### policy_types

This optional keyname lists the Policy Types that are defined by this
TOSCA file.

###### Keyname

| policy_types |
|--------------|

###### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>policy_types:</p>
<p>&lt;<a href="#group-type">policy_type_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#group-type">policy type_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example
<!----
{"id": "327", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T08:48:00Z", "comment": "There should be a second policy definition in the example or it is just a repeat of the policy type definition example", "target": "Example"}-->


<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>policy_types:</p>
<p>mycompany.mytypes.myScalingPolicy:</p>
<p>derived_from: tosca.policies.Scaling</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Profiles

A profile is a named collection of TOSCA type definitions, artifacts,
and service templates that logically belong together. One can think of
TOSCA profiles as platform libraries exposed by the TOSCA orchestration
platform and made available to all services that use that platform.
Profiles in TOSCA are similar to libraries in traditional computer
programming languages.

Profiles contain a collection of pre-defined components that can be used
by service designers to compose complex service templates, Entities
defined in TOSCA profiles are used as follows:

- Types defined in a TOSCA profile provide reusable building blocks from
  which services can be composed.

- Artifacts and service templates defined in a TOSCA profile provide
  implementations for the TOSCA types defined in the profile. Whereas
  artifacts provide interface operation implementations for concrete
  nodes and relationships, service templates defined in TOSCA profiles
  are intended to implement abstract nodes through substitution mapping.

TOSCA implementations can organize supported profiles in a catalog to
allow other service templates to import those profiles by profile name.
This avoids the need for every service that use those profiles to
include the profile type definitions in their service definition
packages.

#### Examples

Version 1.x of the TOSCA specification included a collection of
normative type definitions for building cloud applications. This
collection of type definitions was defined as the **TOSCA Simple
Profile**. Implementations of TOSCA Version 1.x were expected to include
implementations for the types defined in the TOSCA Simple Profile, and
service templates defined using TOSCA Version 1.x implicitly imported
the corresponding TOSCA Simple Profile version.

Starting with TOSCA Version 2.0, the TOSCA Simple Profile type
definitions are no longer part of the TOSCA standard and support for the
TOSCA Simple Profile is no longer mandatory. Instead, the definition of
the TOSCA Simple Profile has been moved to an OASIS Open Github
repository with the goal of being maintained by the TOSCA community and
governed as an open-source project. In addition, TOSCA Version 2.0
removes the implicit import of the TOSCA Simple Profile. Service
templates that want to continue to use the TOSCA Simple Profile type
definitions must explicitly import that profile.

Eliminating mandatory support for the TOSCA Simple Profile makes it
easier for TOSCA to be used for additional application domains. For
example, the European Telecommunications Standards Institute (ETSI) has
introduced a TOSCA profile for **Network Functions Virtualization**
defines Virtualized Network Function Descriptors (VNFDs), Network
Service Descriptors (NSDs) and a Physical Network Function Descriptors
(PNFDs).

We should give a couple of additional examples.

#### Defining Profiles

A TOSCA file defines a TOSCA Profile if the profile keyword is used in
that service template. The value of the profile keyword defines the name
for the profile, which allows other service templates to import the
profile by name.

TOSCA does not impose naming conventions for profile names, but as a
best practice we recommend a domain-name-like structure as used for Java
package naming. For example, the following profile statement is used to
define TOSCA Simple Profile Version 2.0 types:

| profile: org.oasis-open.tosca.simple:2.0 |
|------------------------------------------|

TOSCA parsers MUST process profile definitions according to the
following rules:

- TOSCA files that define a profile (i.e., that contain a profile
  keyname) MUST NOT also define a service template.

- If the parser encounters the profile keyname in a TOSCA file, then the
  corresponding profile name will be applied to all types defined in
  that file as well as to types defined in any imported TOSCA files.

- If one of those imported files also defines the profile keyname—and
  that profile name is different from the name of the importing
  profile—then that profile name overrides the profile name value from
  that point in the import tree onward, recursively.

- TOSCA service templates defined in profiles MUST advertise
  substitution mapping to allow them to be used as implementations for
  abstract nodes defined using profile types.

#### Profile Versions

TOSCA Profiles are likely to evolve over time and profile designers will
release different versions of their profiles. For example, the TOSCA
Simple Profile has gone through minor revisions with each release of the
TOSCA Version 1 standard. It is expected that profile designers will use
a version qualifier to distinguish between different versions of their
profiles, and service template designers must use the proper string name
to make sure they import the desired versions of these profiles.

Do we impose a structure on profile names that distinguishes the version
qualifier from the base profile name? If so, is there a specific
separator character or string (in which case the use of the separator
must be escaped somehow (or disallowed) in profile names.

When multiple versions of the same profile exist, it is possibly that
service templates could mix and match different versions of a profile in
the same service definition. The following code snippets illustrate this
scenario:

Assume a profile designer creates version 1 of a base profile that
defines (among other things) a **Host** capability type and a
corresponding **HostedOn** relationship type as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>profile: org.base.v1</p>
<p>capability_types:</p>
<p>Host:</p>
<p>description: Hosting capability</p>
<p>relationship_types:</p>
<p>HostedOn:</p>
<p>valid_capability_types: [ Host ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Now let’s assume a different profile designer creates a
platform-specific profile that defines (among other things) a
**Platform** node type. The Platform node type defines a capability of
type **Host**. Since the **Host** capability is defined in the
**org.base.v1** profile, that profile must be imported as shown in the
snippet below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>profile: org.platform</p>
<p>imports:</p>
<p>- profile: org.base.v1</p>
<p>namespace: p1</p>
<p>node_types:</p>
<p>Platform:</p>
<p>capabilities:</p>
<p>host:</p>
<p>type: p1:Host</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

At some later point of time, the original profile designer updates the
**org.base** profile to Version 2. The updated version of this profile
just adds a **Credential** data type (in addition to defining the
**Host** capability type and the **HostedOn** relationship type), as
follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>profile: org.base.v2</p>
<p>capability_types:</p>
<p>Host:</p>
<p>description: Hosting capability</p>
<p>relationship_types:</p>
<p>HostedOn:</p>
<p>valid_capability_types: [ Host ]</p>
<p>data_types:</p>
<p>Credential:</p>
<p>properties:</p>
<p>key:</p>
<p>type: string</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Finally, let’s assume a service designer creates a template for a
service that is to be hosted on the platform defined in the
**org.platform** profile. The template introduces a **Service** node
type that has a requirement for the platform’s **Host** capability. It
also has a credential property of type **Credential** as defined in
**org.base.v2**:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>imports:</p>
<p>- profile: org.base.v2</p>
<p>namespace: p2</p>
<p>- profile: org.platform</p>
<p>namespace: pl</p>
<p>node_types:</p>
<p>Service:</p>
<p>properties:</p>
<p>credential:</p>
<p>type: p2:Credential</p>
<p>requirements:</p>
<p>- host:</p>
<p>capability: p2:Host</p>
<p>relationship: p2:HostedOn</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>service:</p>
<p>type: Service</p>
<p>properties:</p>
<p>credential:</p>
<p>key: password</p>
<p>requirements:</p>
<p>- host: platform</p>
<p>platform:</p>
<p>type: pl:Platform</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This service template is invalid, since the **platform** node template
does not define a capability of a type that is compatible with the
**valid_capability_types** specified by the **host** requirement in the
**service** node template. TOSCA grammar extensions are needed to
specify that the **Host** capability type defined in **org.base.v2** is
the same as the **Host** capability type defined in **org.base.v1**

The example in this section illustrates a general version compatibility
issue that exists when different versions of the same profile are used
in a TOSCA service.

A number of suggestions for these extensions are currently being
discussed. Grammar extensions will be included in this document one they
are agreed upon.

### Imports
<!----
{"id": "346", "author": "Chris Lauwers", "date": "2020-09-01T00:20:00Z", "comment": "I don\u2019t know what is meant by \u201creferences\u201d.", "target": "Imports"}-->
 and Namespaces

#### Import definition
<!----
{"id": "350", "author": "Calin Curescu", "date": "2019-01-30T15:54:00Z", "comment": "It would be good to allow also the import of specific types (via their fully qualified names) and also entire namespaces (i.e. types from entire namespaces) from a/the catalogue. That is, in addition to importing from a file: Globally well-known Local catalog File", "target": "Import definition"}-->


An import definition is used within a TOSCA file to locate and uniquely
name another TOSCA file or TOSCA profile that has type, repository, and
function 
<!----
{"id": "351", "author": "Chris Lauwers", "date": "2020-09-01T00:21:00Z", "comment": "I think it should be illegal to import a\nservice template that contains a topology\ntemplate.", "target": ""}-->
definitions to
be imported
<!----
{"id": "352", "author": "Matt Rutkowski", "date": "2016-09-06T09:49:00Z", "comment": "Nodejs has NPM that uses the following to\nimport new package modules:  \nA package is:  \na) a folder containing a program described by a\n[package.json](numbering.xml) file  \nb) a gzipped tarball containing (a)  \nc) a url that resolves to (b)  \nd) a \\<name\\>@\\<version\\> that is published on the registry (see\n[npm-registry](styles.xml)) with (c)  \ne) a \\<name\\>@\\<tag\\> (see [npm-dist-tag](settings.xml)) that points to\n(d)  \nf) a \\<name\\> that has a \"latest\" tag satisfying (e)  \ng) a \\<git remote url\\> that resolves to (a)  \nwe may want to adopt something similar if TOSCA references service\ntemplate (packages) from a\ncatalog)", "target": "imported"}-->

(included) into another TOSCA file.

##### Keynames

The following is the list of recognized keynames for a TOSCA import
definition:

| Keyname    | Mandatory   | Type                        | Description                                                                                                                                                             |
|------------|-------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| url        | conditional | [string](#TYPE_YAML_STRING) | The url that references a service template to be imported. An import statement must include either a url or a profile, but not both.                                    |
| profile    | conditional | string                      | The profile name that references a named type profile to be imported. An import statement must include either a url or a profile, but not both.                         |
| repository | conditional | [string](#TYPE_YAML_STRING) | The optional symbolic name of the repository definition where the imported file can be found as a string. The repository name can only be used when a url is specified. |
| namespace  | no          | [string](#TYPE_YAML_STRING) | The optional name of the namespace into which to import the type definitions from the imported template or profile.                                                     |

##### Grammar

Import definitions have one the following grammars:

###### Single-line grammar:

When using the single-line grammar, the url keyword is assumed:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>imports:</p>
<p>- &lt;URI_1&gt;</p>
<p>- &lt;URI_2&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Multi-line grammar

The following multi-line grammar can be used for importing TOSCA files:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CSAR 
<!----
{"id": "361\" data-author=\"Matt Rutkowski\"\ndata-date=\"2017-11-21T11:45:00Z\">Import means (import types into global\nnamespace and any sub-topologies are made available for\ncomposition.)</span>imports<span class=\"comment-end\"\nid=\"361\"></span>:</p>\n<p>- url: &lt;file_URI&gt;</p>\n<p>repository: &lt;repository_name&gt;</p>\n<p>namespace: &lt;namespace_name&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe following multi-line grammar can be used for importing TOSCA\nprofiles:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p><span class=\"comment-start\" id=\"362\" data-author=\"Matt Rutkowski\"\ndata-date=\"2017-11-21T11:45:00Z\">Import means (import types into global\nnamespace and any sub-topologies are made available for\ncomposition.)</span>imports<span class=\"comment-end\"\nid=\"362\"></span>:</p>\n<p>- profile: &lt;profile_name&gt;</p>\n<p>namespace: &lt;namespace_name&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- file_uri: contains the URL that references the service template file\n  to be imported as a [string](#TYPE_YAML_STRING).\n\n- repository_name: represents the optional symbolic name of the\n  repository definition where the imported file can be found as a\n  [string](#TYPE_YAML_STRING).\n\n- profile_name: the name of the well-known profile to be imported.\n\n- namespace_name: represents the optional name of the namespace into\n  which type definitions will be imported. The namespace name can be\n  used to form a namespace-qualified name that uniquely references type\n  definitions from the imported file or profile. If no namespace name is\n  specified, type definitions will be imported into the root namespace.\n\n##### Import processing rules \n\nTOSCA Orchestrators, Processors and tooling SHOULD handle import\nstatements as follows:\n\n###### Importing profiles\n\nIf the profile keyname is used in the import definition, then the TOSCA\norchestrator or processor SHOULD attempt to import the profile by name:\n\n- If \\<profile_name\\> represents the name of a profile that is known to\n  the TOSCA orchestrator or processor, then it SHOULD cause the Profile\n  Type definitions to be imported.\n\n- If \\<profile_name\\> is not known, the import SHOULD be considered a\n  failure.\n\n###### Importing service templates\n\nIf the url keyname is used, the TOSCA orchestrator or processor SHOULD\nattempt to import the file referenced by \\<file_URI\\> as follows:\n\n- If the \\<file_URI\\> includes a URL scheme (e.g. file: or https:)\n  then\\<file_URI\\> is considered to be a network accessible resource. If\n  the resource identified by \\<file_URL\\> represents a valid TOSCA file,\n  then it SHOULD cause the remote Service Template to be imported.\n\n<!-- -->\n\n- Note that if in addition to a URL with a URL scheme, the import\n  definition also specifies a \\<repository_name\\> (using the repository\n  key), then that import definition SHOULD be considered invalid.\n\n<!-- -->\n\n- If the \\<file_URI\\> does not include a URL scheme, it is a considered\n  a relative path URL. The TOSCA orchestrator or processor SHOULD handle\n  such a \\<file_URI\\> as follows:\n\n<!-- -->\n\n- If the import definition also specifies a \\<repository_name\\> (using\n  the repository keyname), then \\<file_URI\\> refers to the path name of\n  a file relative to the root of the named repository\n\n- If the import definition does not specify a \\<profile_name\\> then\n  \\<file_URI\\> refers to a TOSCA file located in the repository that\n  contains the Service Template file that includes the import\n  definition. If the importing service template is located in a\n  <span class=\"comment-start\" id=\"367", "author": "Matt Rutkowski", "date": "2017-12-05T11:33:00Z", "comment": "Claude: Could perhaps add hints to CSAR\n  file to indicate where STs can be imported from (based upon URI or\n  alias).", "target": "CSAR "}-->
file,
  then that CSAR file should be treated as the repository in which to
  locate the service template file that must be imported.

<!-- -->

- If \<file_URI\> starts with a leading slash (‘/’) then \<file_URI\>
  specifies a path name starting at the root of the repository.

- If \<file_URI\> does not start with a leading slash, then \<file_URI\>
  specifies a path that is relative to the importing document’s location
  within the repository. Double dot notation (‘../’) can be used to
  refer to parent directories in a file path name.

<!-- -->

- If \<file_URI\> does not reference a valid TOSCA file file, then the
  import SHOULD be considered a failure.

##### Examples

The first example shows how to use an import definition import a
well-known profile by name:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Importing a profile</p>
<p>imports:</p>
<p>- profile: org.oasis-open.tosca.simple:2.0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The next example shows an import definition used to import a
network-accessible resource using the https protocol:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Absolute URL with scheme</p>
<p>imports:</p>
<p>- url: https://myorg.org/tosca/types/mytypes.yaml</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following represents shows an import definition used to import a
service template in the same repository as the importing template. The
template to be imported is referenced using a path name that is relative
to the location of the importing template. This example shows the short
notation:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Short notation supported</p>
<p>imports:</p>
<p>- ../types/mytypes.yaml</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following shows the same example but using the long notation:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Long notation</p>
<p>imports:</p>
<p>- url: ../types/mytypes.yaml</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following example shows how to import service templates using
absolute path names (i.e. path names that start at the root of the
repository):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Root file</p>
<p>imports:</p>
<p>- url: /base.yaml</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

And finally, the following shows how to import templates from a
repository that is different than the repository that contains the
importing template:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># External repository</p>
<p>imports:</p>
<p>- url: types/mytypes.yaml</p>
<p>repository: my_repository</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Namespace
<!----
{"id": "373", "author": "Chris Lauwers", "date": "2020-09-01T00:19:00Z", "comment": "I recommend removing this entire section and rewriting any parts that are still relevant inside the \u201cimports\u201d section.", "target": "Namespace"}-->
s

When importing TOSCA files or TOSCA profiles, there exists a possibility
for name collision. For example, an imported file may define a node type
with the same name as a node type defined in the importing file.

For example, let say we have two TOSCA files, A and B, both of which
contain a Node Type definition for “MyNode”:

**TOSCA File B**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>description: TOSCA File B</p>
<p>node_types:</p>
<p>MyNode:</p>
<p>derived_from: SoftwareComponent</p>
<p>properties:</p>
<p># omitted here for brevity</p>
<p>capabilities:</p>
<p># omitted here for brevity</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**TOSCA File A**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca_definitions_version: tosca_2_0</p>
<p>description: TOSCA File A</p>
<p>imports:</p>
<p>- url: /templates/ServiceTemplateB.yaml</p>
<p>node_types:</p>
<p>MyNode:</p>
<p>derived_from: Root</p>
<p>properties:</p>
<p># omitted here for brevity</p>
<p>capabilities:</p>
<p># omitted here for brevity</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>my_node:</p>
<p>type: MyNode</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

As you can see, TOSCA file A imports TOSCA file B which results in
duplicate definitions of the MyNode node type. In this example, it is
not clear which type is intended to be used for the my_node node
template.

To address this issue, TOSCA uses the concept of namespaces:

- Each TOSCA file defines a root namespace for all type definitions
  defined in that template. Root namespaces are unnamed.

- When a TOSCA file imports other templates, it has two options:

<!-- -->

- It can import any type definitions from the imported templates into
  its root namespace

- Or it can import type definitions from the imported templates into a
  separate named namespace. This is done using the namespace keyname in
  the associated import statement. When using types imported into a
  named namespace, those type names must be qualified using the
  namespace name.

The following snippets update the previous example using namespaces to
disambiguate between the two MyNode type definitions. This first snippet
shows the scenario where the MyNode definition from TOSCA file B is
intended to be used:

tosca_definitions_version: tosca_2_0

description: TOSCA file A

imports:

\- url: /templates/ServiceTemplateB.yaml

namespace: templateB

node_types:

MyNode:

derived_from: Root

properties:

\# omitted here for brevity

capabilities:

\# omitted here for brevity

service_template:

node_templates:

my_node:

type: templateB:MyNode

The second snippet shows the scenario where the MyNode definition from
TOSCA file A is intended to be used:

tosca_definitions_version: tosca_2_0

description: TOSCA file A

imports:

\- url: /templates/ServiceTemplateB.yaml

namespace: templateB

node_types:

MyNode:

derived_from: Root

properties:

\# omitted here for brevity

capabilities:

\# omitted here for brevity

service_template:

node_templates:

my_node:

type: MyNode

In many scenarios, imported TOSCA files may in turn import their own
TOSCA files, and introduce their own namespaces to avoid name
collisions. In those scenarios, nested namespace names are used to
uniquely identify type definitions in the import tree.

The following example shows a mytypes.yaml TOSCA file that imports a
Kubernetes profile into the k8s namespace. It defines a SuperPod node
type that derives from the Pod node type defined in that Kubernetes
profile:

tosca_definitions_version: tosca_2_0

description: mytypes.yaml

imports:

\- profile: io.kubernetes:1.18

namespace: k8s

node_types:

MyNode: {}

SuperPod:

derived_from: k8s:Pod

The mytypes.yaml template is then imported into the main.yaml TOSCA
file, which defines both a node template of type SuperPod as well as a
node template of type Pod. Nested namespace names are used to identify
the Pod node type from the Kubernetes profile:

tosca_definitions_version: tosca_2_0

description: main.yaml

imports:

\- url: mytypes.yaml

namespace: my

service_template:

node_templates:

mynode:

type: my:MyType

pod:

type: my:k8s:Pod

##### Additional Requirements

Within each namespace, names must be unique. This means the following:

- Duplicate local names (i.e., within the same TOSCA file SHALL be
  considered an error. These include, but are not limited to duplicate
  names found for the following definitions:

<!-- -->

- Repositories (repositories)

- Data Types (data_types)

- Node Types (node_types)

- Relationship Types (relationship_types)

- Capability Types (capability_types)

- Artifact Types (artifact_types)

- Interface Types (interface_types)

<!-- -->

- Duplicate Template names within a Service Template SHALL be considered
  an error. These include, but are not limited to duplicate names found
  for the following template types:

<!-- -->

- Node Templates (node_templates)

- Relationship Templates (relationship_templates)

- Inputs (inputs)

- Outputs (outputs)

<!-- -->

- Duplicate names for the following keynames within Types or Templates
  SHALL be considered an error. These include, but are not limited to
  duplicate names found for the following keynames:

<!-- -->

- Properties (properties)

- Attributes (attributes)

- Artifacts (artifacts)

- R<span class="comment-start" id="376"
  author="Matt Rutkowski" date="2015-08-25T21:52:00Z">MUSTFIX: Verify
  duplicates are NOT allowed!!</span>equirements
  (requirements)
<!----
{"id": "375", "author": "Calin Curescu", "date": "2020-06-08T18:24:00Z", "comment": "But requirements assignments support\n  duplicates!", "target": "R<span class=\"comment-start\" id=\"376\"\n  author=\"Matt Rutkowski\" date=\"2015-08-25T21:52:00Z\">MUSTFIX: Verify\n  duplicates are NOT allowed!!</span>equirements\n  (requirements)"}-->


- Capabilities (capabilities)<span class="comment-end" id="376"></span>

- Interfaces (interfaces)

- Policies (policies)

- Groups (groups)

#### Repository definition

A repository definition defines an external repository which contains
deployment and implementation artifacts that are referenced within the
TOSCA file.

##### Keynames

The following is the list of recognized keynames for a TOSCA repository
definition:

| Keyname     | Mandatory | Type                        | Description                                                         |
|-------------|-----------|-----------------------------|---------------------------------------------------------------------|
| description | no        | [string](#TYPE_YAML_STRING) | The optional description for the repository.                        |
| url         | yes       | [string](#TYPE_YAML_STRING) | The mandatory URL or network address used to access the repository. |

##### Grammar

Repository definitions have one the following grammars:

###### Single-line grammar:

| \<[repository_name](#TYPE_YAML_STRING)\>: \<repository_address\> |
|------------------------------------------------------------------|

###### Multi-line grammar

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">repository_name</a>&gt;:</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">repository_description</a>&gt;</p>
<p>url: &lt;<a
href="#TYPE_YAML_STRING">repository_address</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- repository_name: represents the mandatory symbolic name of the
  repository as a [string](#TYPE_YAML_STRING).

- repository_description: contains an optional description of the
  repository.

- repository_address: represents the mandatory URL of the repository as
  a string.

##### Example

The following represents a repository definition:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>repositories:</p>
<p>my_code_repo:</p>
<p>description: My project’s code repository in GitHub</p>
<p>url: https://github.com/my-project/</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Additional information definitions

#### Description definition
<!----
{"id": "394", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T11:16:00Z", "comment": "Description is already described in 4.2.1.3.6", "target": "Description definition"}-->


This optional element provides a means include single or multiline
descriptions within a TOSCA template as a scalar string value.

##### Keyname

The following keyname is used to provide a description within the TOSCA
specification:

| description |
|-------------|

##### Grammar

Description definitions have the following grammar:

| description: \<[description_string](#TYPE_YAML_STRING)\> |
|----------------------------------------------------------|

##### Examples

Simple descriptions are treated as a single literal that includes the
entire contents of the line that immediately follows the description
key:

| description: This is an example of a single line description (no folding). |
|----------------------------------------------------------------------------|

The YAML “folded” style may also be used for multi-line descriptions
which “folds” line breaks as space characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>description: &gt;</p>
<p>This is an example of a multi-line description using YAML. It permits
for line</p>
<p>breaks for easier readability...</p>
<p>if needed. However, (multiple) line breaks are folded into a single
space</p>
<p>character when processed into a single string value.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes

- Use of “folded” style is discouraged for the YAML string type apart
  from when used with the description keyname.
  .
<!----
{"id": "403", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T11:13:00Z", "comment": "Can\u2019t I just use a double quoted string\n  for multi-line ?", "target": ""}-->


#### Metadata
<!----
{"id": "409", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T11:17:00Z", "comment": "Also covered by 4.2.1.3.2", "target": "Metadata"}-->


This optional element provides a means to include optional metadata as a
map of strings.

##### Keyname

The following keyname is used to provide metadata within the TOSCA
specification:

| metadata |
|----------|

##### Grammar

Metadata definitions have the following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>metadata:</p>
<p>DSL Definitions
<!----
{"id": "414\" data-author=\"Calin Curescu\"\ndata-date=\"2020-06-08T18:58:00Z\">Chris has a problem with the\nrestriction here, it should be able to combine more cases: map of map,\nor map of list, of string, etc.<br />\nTal want to think more if map of string or map of everything\u2026</span>map\nof &lt;<a href=\"#TYPE_YAML_STRING\">string</a>&gt;<span\nclass=\"comment-end\" id=\"414\"></span></p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### Examples\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>metadata:</p>\n<p>foo1: bar1</p>\n<p>foo2: bar2</p>\n<p>...</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### Notes\n\n- Data provided within metadata, wherever it appears, MAY be ignored by\n  TOSCA Orchestrators and SHOULD NOT affect runtime behavior.\n\n#### <span class=\"comment-start\" id=\"423", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-05T11:20:00Z", "comment": "Already in 4.2.1.3.7", "target": "DSL Definitions"}-->


TBD.

### Type definitions

TOSCA provides a type system to describe possible building blocks to
construct a service template (i.e. for the nodes, relationship, group
and policy templates, and the data, capabilities, interfaces, and
artifacts used in the node and relationship templates). TOSCA types are
reusable TOSCA entities and are defined in their specific sections in
the service template, see Section 4.2.1 Service Template definition.

Next, in Section 4.2.5.2 Common keynames in type definitions we present
the definitions of common keynames that are used by all TOSCA types.
Type-specific definitions for the different TOSCA type entities are
presented further in the document:

- Node Type in Section 4.3.1 Node Type.

- Relationship Type in Section 4.3.3 Relationship Type.

- Interface Type in Section 4.3.6.1 Interface Type.

- Capability Type in Section 4.3.5.1 Capability Type.

- Requirement Type in Section 4.3.5.4 Requirement Type.

- Data Type in Section 4.4.4 Data Type.

- Artifact Type in Section 4.3.7.1 Artifact Type.

- Group Type in Section 4.6.1 Group Type.

- Policy Type in Section 4.6.3 Policy Type.

#### General derivation and refinement rules

To simplify type creation and to promote type extensibility TOSCA allows
the definition of a new type (the derived type) based on another type
(the parent type). The derivation process can be applied recursively,
where a type may be derived from a long list of ancestor types (the
parent, the parent of the parent, etc).

Unless specifically stated in the derivation rules, when deriving new
types from parent types the keyname definitions are inherited from the
parent type. Moreover, the inherited definitions may be refined
according to the derivation rules of that particular type entity.

For definitions that are not inherited, a new definition **MUST** be
provided (if the keyname is mandatory) or **MAY** be provided (if the
keyname is not mandatory). If not provided, the keyname remains
undefined. For definitions that are inherited, a refinement of the
inherited definition is not mandatory even for mandatory keynames (since
it has been inherited). A definition refinement that is exactly the same
as the definition in the parent type does not change in any way the
inherited definition. While unnecessary, it is not wrong.

The following are some generic derivation rules used during type
derivation (the specific rules of each TOSCA type entity are presented
in their respective sections):

- If not refined, usually a keyname/entity definition, is inherited
  unchanged from the parent type, unless explicitly specified in the
  rules that it is “not inherited”.

- New entities (such as properties, attributes, capabilities,
  requirements, interfaces, operations, notification, parameters) may be
  added during derivation.

- Already defined entities that have a type may be
  redefined
  
<!----
{"id": "427", "author": "Mike Rehder", "date": "2020-12-14T14:25:00Z", "comment": "New term \u201credefined\u201d. The sentence is\n  confusing \u2013 what is it trying to say? Is it saying that you can change\n  the type of a derived_from type (how?)?", "target": "redefined\n  "}-->
to have a type derived from
  the original type.

- New validation clauses are added to already defined keynames/entities
  (i.e. the defined validation clauses do not replace the validation
  clause defined in the parent type but are added to it).

- Some definitions must be totally
  flexible
<!----
{"id": "428", "author": "Mike Rehder", "date": "2020-12-14T14:29:00Z", "comment": "Why \u201cshould\u201d? Isn\u2019t\n  this \u201care treated as a new declaration and\u201d?", "target": "must be totally\n  flexible"}-->
, so they will
  overwrite the definition in the parent type.

- Some definitions must 
<!----
{"id": "429", "author": "Mike Rehder", "date": "2020-12-14T14:28:00Z", "comment": "Why \u201cshould\u201d? Isn\u2019t\n  this \u201ccannot\u201d?", "target": "must "}-->
not be changed at all once defined (i.e. they
  represent some sort of “signature” fundamental to the type).

#### Common keynames in type definitions

The following keynames are used by all TOSCA type entities in the same
way. This section serves to define them at once.

##### Keynames

The following is the list of recognized keynames used by all TOSCA type
definitions:

| Keyname      | Mandatory | Type                                                                               | Description                                                        |
|--------------|-----------|------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| derived_from | no        | [string](#TYPE_YAML_STRING)                                                        | An optional parent type name from which this type derives.         |
| version      | no        | [version](#tosca-tal-suggests-removing-this.version)                               | An optional version for the type definition.                       |
| metadata     | no        | [map](\l) of [string](#TYPE_YAML_STRING)<span class="comment-end" id="435"></span> | Defines a section used to declare additional metadata information. |
| description  | no        | [string](#TYPE_YAML_STRING)                                                        | An optional description for the type.                              |

##### Grammar

The common keynames in type definitions have the following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;type_name&gt;:</p>
<p>derived_from: &lt;parent_type_name&gt;</p>
<p>version: &lt;<a
href="#tosca-tal-suggests-removing-this.version">version_number</a>&gt;</p>
<p>metadata:</p>
<p>&lt;<a
href="#also-covered-by-4.2.1.3.2metadata">metadata_map</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">type_description</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- parent_type_name: represents the optional parent type name.

- version_number: represents the optional TOSCA version number for the
  type.

- entity_description: represents the optional description string for the
  type.

- metadata_map: represents the optional metadata map of string.

##### Derivation rules

During type derivation the common keyname definitions use the following
rules:

- derived_from: obviously, the definition is not inherited from the
  parent type. If not defined, it remains undefined and this type does
  not derive from another type. If defined, then this type derives from
  another type, and all its keyname definitions must respect the
  derivation rules of the type entity.

- version: the definition is not inherited from the parent type. If
  undefined, it remains undefined.

- metadata: the definition is not inherited from the parent type. If
  undefined, it remains undefined.

- description: the definition is not inherited from the parent type. If
  undefined, it remains undefined.

### Service template definition

This section defines the service template of a TOSCA file. The main
ingredients of the service template are node templates representing
components of the application and relationship templates representing
links between the components. These elements are defined in the nested
node_templates section and the nested relationship_templates sections,
respectively. Furthermore, a service template allows for defining input
parameters, output parameters as well as grouping of node templates.

#### Keynames

The following is the list of recognized keynames for a TOSCA service
template:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The optional description for the service template.</td>
</tr>
<tr class="even">
<td>inputs</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#parameter-definition">parameter definitions</a></p></td>
<td>An optional map of input parameters (i.e., as parameter definitions)
for the service template.</td>
</tr>
<tr class="odd">
<td>node_templates</td>
<td>yes</td>
<td><p>map of</p>
<p><a href="#node-template">node templates</a></p></td>
<td>A mandatory map of node template definitions for the service
template.</td>
</tr>
<tr class="even">
<td>relationship_templates</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#relationship-template">relationship templates</a></p></td>
<td>An optional map of relationship templates for the service
template.</td>
</tr>
<tr class="odd">
<td>groups</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#group-definition">group definitions</a></p></td>
<td>An optional map of Group definitions whose members are node
templates defined within this same service template.</td>
</tr>
<tr class="even">
<td>policies</td>
<td>no</td>
<td><p>list of</p>
<p><a
href="#i-know-that-tmf-have-a-branch-of-their-information-model-to-describe-policy-but-that-it-is-not-used-much-and-that-mef-have-recently-been-more-active-in-specializing-policy-for-access-control-and-for-ip-forwarding-rules.-it-is-possible-that-tosca-could-draw-on-this-work-to-make-tosca-policy-framework-more-useful.policy-definition">policy
definitions</a></p></td>
<td>An optional list of Policy definitions for the service
template.</td>
</tr>
<tr class="odd">
<td>outputs</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#parameter-definition">parameter definitions</a></p></td>
<td>An optional map of output parameters (i.e., as parameter
definitions) for the service template.</td>
</tr>
<tr class="even">
<td>substitution_mappings</td>
<td>no</td>
<td>substitution_mapping</td>
<td><p>An optional declaration that exports the service template as an
implementation of a Node type.</p>
<p>This also includes the mappings between the external Node Types
capabilities and requirements to existing implementations of those
capabilities and requirements on Node templates declared within the
service template.</p></td>
</tr>
<tr class="odd">
<td>workflows</td>
<td>no</td>
<td>map of imperative workflow definitions</td>
<td>An optional map of imperative workflow definition for the service
template.</td>
</tr>
</tbody>
</table>

#### Grammar

The overall grammar of the service_template section is shown
below.Detailed grammar definitions are provided in subsequent
subsections.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>service_template:</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">template_description</a>&gt;</p>
<p>inputs: &lt;input_parameters&gt;</p>
<p>outputs: &lt;output_parameters&gt;</p>
<p>node_templates: &lt;node_templates&gt;</p>
<p>relationship_templates: &lt;relationship_templates&gt;</p>
<p>groups: &lt;group_definitions&gt;</p>
<p>policies:</p>
<p>- &lt;policy_definition_list&gt;</p>
<p>workflows: &lt;workflows&gt;</p>
<p># Optional declaration that exports the service template</p>
<p># as an implementation of a Node Type.</p>
<p>substitution_mappings:</p>
<p>&lt;substitution_mappings&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- template_description: represents the optional
  [description](#TYPE_YAML_STRING) string for service template.

- input_parameters: represents the optional map of input parameter
  definitions for the service template.

- output_parameters: represents the optional map of output parameter
  definitions for the service template.

- group_definitions: represents the optional map of [group
  definitions](#group-definition) whose members are node templates that
  also are defined within this service template.

- policy_definition_list: represents the optional list of sequenced
  policy definitions for the service template.

- workflows: represents the optional map of imperative workflow
  definitions for the service template.

- node_templates: represents the mandatory map of [node
  template](#node-template) definitions for the service template.

- relationship_templates: represents the optional map of [relationship
  templates](#relationship-template) for the service template.

- node_type_name: represents the optional name of a [Node
  Type](#node-type) that the service template implements as part of the
  substitution_mappings.

- map_of_capability_mappings_to_expose: represents the mappings that
  expose internal capabilities from node templates (within the service
  template) as capabilities of the Node Type definition that is declared
  as part of the substitution_mappings.

- map_of_requirement_mappings_to_expose: represents the mappings of link
  requirements of the Node Type definition that is declared as part of
  the substitution_mappings to internal requirements implementations
  within node templates (declared within the service template).

More detailed explanations for each of the service template grammar’s
keynames appears in the sections below.

##### inputs

The inputs section provides a means to define parameters using TOSCA
parameter definitions, their allowed values via validation clauses and
default values within a TOSCA template. Input parameters defined in the
inputs section of a service template can be mapped to properties of node
templates or relationship templates within the same service template and
can thus be used for parameterizing the instantiation of the service
template.

When deploying a service from the service template, values must be
provided for all mandatory input parameters that have no default value
defined. If no input is provided, then the default value is used.

###### Grammar

The grammar of the inputs section is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>inputs:</p>
<p>&lt;<a
href="#parameter-definition">parameter_definitions</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Examples

This section provides a set of examples for the single elements of a
service template.

Simple inputs example without any validation clauses:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>inputs:</p>
<p>fooName:</p>
<p>type: string</p>
<p>description: Simple string parameter without a validation clause.</p>
<p>default: bar</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example of inputs with a validation clause:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>inputs:</p>
<p>SiteName:</p>
<p>type: string</p>
<p>description: String parameter with validation clause.</p>
<p>default: My Site</p>
<p>validation: { $min_length: [ $value, 9 ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### node_templates

The node_templates section lists the Node Templates that describe the
(software) components that are used to compose cloud applications.

###### grammar

The grammar of the node_templates section is a follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>&lt;<a href="#node-template">node_template_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#node-template">node_template_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

Example of node_templates section:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>my_webapp_node_template:</p>
<p>type: WebApplication</p>
<p>my_database_node_template:</p>
<p>type: Database</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### relationship_templates

The relationship_templates section lists the Relationship Templates that
describe the relations between components that are used to compose cloud
applications.

Note that in TOSCA, the explicit definition of relationship templates as
it was required in TOSCA v1.0 is optional, since relationships between
nodes get implicitly defined by referencing other node templates in the
requirements sections of node templates.

###### Grammar

The grammar of the relationship_templates section is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>relationship_templates:</p>
<p>&lt;<a
href="#relationship-template">relationship_template_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a
href="#relationship-template">relationship_template_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

Example of relationship_templates section:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>relationship_templates:</p>
<p>my_connectsto_relationship:</p>
<p>type: tosca.relationships.ConnectsTo</p>
<p>interfaces:</p>
<p>Configure:</p>
<p>inputs:</p>
<p>speed: { $$get_attribute: [ SELF, SOURCE, connect_speed ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### outputs

The outputs section provides a means to define the output parameters
that are available from a TOSCA service template. It allows for exposing
attributes of node templates or relationship templates within the
containing service_template to users of a service.

###### Grammar

The grammar of the outputs section is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>outputs:</p>
<p>&lt;<a
href="#parameter-definition">parameter_definitions</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

Example of the outputs section:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>outputs:</p>
<p>server_address:</p>
<p>description: The first private IP address for the provisioned
server.</p>
<p>value: { $get_attribute: [ node5, networks, private, addresses, 0 ]
}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### groups

The groups section allows for grouping one or more node templates within
a TOSCA Service Template and for assigning special attributes like
policies to the group.

###### Grammar

The grammar of the groups section is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>groups:</p>
<p>&lt;<a href="#group-definition">group_defn_1</a>&gt;</p>
<p>...</p>
<p>&lt;<a href="#group-definition">group_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

The following example shows the definition of three Compute nodes in the
node_templates section of a service_template as well as the grouping of
two of the Compute nodes in a group server_group_1.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>server1:</p>
<p>type: tosca.nodes.Compute</p>
<p># more details ...</p>
<p>server2:</p>
<p>type: tosca.nodes.Compute</p>
<p># more details ...</p>
<p>server3:</p>
<p>type: tosca.nodes.Compute</p>
<p># more details ...</p>
<p>groups:</p>
<p># server2 and server3 are part of the same group</p>
<p>server_group_1:</p>
<p>type: tosca.groups.Root</p>
<p>members: [ server2, server3 ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### policies

The policies section allows for declaring policies that can be applied
to entities in the service template.

###### Grammar

The grammar of the policies section is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>policies:</p>
<p>- &lt;<a
href="#i-know-that-tmf-have-a-branch-of-their-information-model-to-describe-policy-but-that-it-is-not-used-much-and-that-mef-have-recently-been-more-active-in-specializing-policy-for-access-control-and-for-ip-forwarding-rules.-it-is-possible-that-tosca-could-draw-on-this-work-to-make-tosca-policy-framework-more-useful.policy-definition">policy_defn_1</a>&gt;</p>
<p>- ...</p>
<p>- &lt;<a
href="#i-know-that-tmf-have-a-branch-of-their-information-model-to-describe-policy-but-that-it-is-not-used-much-and-that-mef-have-recently-been-more-active-in-specializing-policy-for-access-control-and-for-ip-forwarding-rules.-it-is-possible-that-tosca-could-draw-on-this-work-to-make-tosca-policy-framework-more-useful.policy-definition">policy_defn_n</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Example

The following example shows the definition of a placement policy.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>policies:</p>
<p>- my_placement_policy:</p>
<p>type: mycompany.mytypes.policy.placement</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### substitution_mapping

###### requirement_mapping

The grammar of a requirement_mapping is as follows:

| \<requirement_name\>: \[ \<node_template_name\>, \<node_template_requirement_name\> \] |
|----------------------------------------------------------------------------------------|

The multi-line grammar is as follows :

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;requirement_name&gt;:</p>
<p>mapping: [ &lt;node_template_name&gt;,
&lt;node_template_capability_name&gt; ]</p>
<p>properties:</p>
<p>&lt;property_name&gt;: &lt;property_value&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- requirement_name: represents the name of the requirement as it appears
  in the Node Type definition for the Node Type (name) that is declared
  as the value for on the substitution_mappings’ “node_type” key.

- node_template_name: represents a valid name of a Node Template
  definition (within the same service_template declaration as the
  substitution_mapping is declared).

- node_template_requirement_name: represents a valid name of a
  requirement definition within the \<node_template_name\> declared in
  this mapping.

###### Example
<!----
{"id": "489", "author": "Calin Curescu", "date": "2020-06-17T18:23:00Z", "comment": "\\### need to revisit this. Example is wrong !!!", "target": "Example"}-->


The following example shows the definition of a placement policy.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>service_template:</p>
<p>inputs:</p>
<p>cpus:</p>
<p>type: integer</p>
<p>validation: { $less_than: [ $value, 2 ] } # OR use “defaults” key</p>
<p>substitution_mappings:</p>
<p>node_type: MyService</p>
<p>properties: # Do not care if running or matching (e.g., Compute
node)</p>
<p># get from outside? Get from contsraint?</p>
<p>num_cpus: cpus # Implied “PUSH”</p>
<p># get from some node in the topology…</p>
<p>num_cpus: [ &lt;node&gt;, &lt;cap&gt;, &lt;property&gt; ]</p>
<p># 1) Running</p>
<p>architecture:</p>
<p># a) Explicit</p>
<p>value: { $get_property: [some_service, architecture] }</p>
<p># b) implicit</p>
<p>value: [ some_service, &lt;req | cap name&gt;, &lt;property name&gt;
architecture ]</p>
<p>default: “amd”</p>
<p># c) INPUT mapping?</p>
<p>???</p>
<p># 2) Catalog (Matching)</p>
<p>architecture:</p>
<p>contraints: equals: “x86”</p>
<p>capabilities:</p>
<p>bar: [ some_service, bar ]</p>
<p>requirements:</p>
<p>foo: [ some_service, foo ]</p>
<p>node_templates:</p>
<p>some_service:</p>
<p>type: MyService</p>
<p>properties:</p>
<p>rate: 100</p>
<p>capabilities:</p>
<p>bar:</p>
<p>...</p>
<p>requirements:</p>
<p>- foo:</p>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Nodes and Relationships
-----------------------

### Node Type

A Node Type is a reusable entity that defines the type of one or more
Node Templates. As such, a Node Type defines the structure of observable
properties and attributes, the capabilities and requirements of the node
as well as its supported interfaces and the artifacts it uses.

#### Keynames

The Node Type is a TOSCA type entity and has the common keynames listed
in Section 4.2.5.2 Common keynames in type definitions. In addition, the
Node Type has the following recognized keynames:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>properties</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#_Schema_Definition">property definitions</a></p></td>
<td>An optional map of property definitions for the Node Type.</td>
</tr>
<tr class="even">
<td>attributes</td>
<td>no</td>
<td><p>map of</p>
<p><a
href="#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition">attribute
definitions</a></p></td>
<td>An optional map of attribute definitions for the Node Type.</td>
</tr>
<tr class="odd">
<td>capabilities</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#capability-definition">capability definitions</a></p></td>
<td>An optional map of capability definitions for the Node Type.</td>
</tr>
<tr class="even">
<td>requirements</td>
<td>no</td>
<td><p>list of</p>
<p><a href="#requirement-definition">requirement
definitions</a></p></td>
<td>An optional list of requirement definitions for the Node Type.</td>
</tr>
<tr class="odd">
<td>interfaces</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#interface-definition">interface definitions</a></p></td>
<td>An optional map of interface definitions supported by the Node
Type.</td>
</tr>
<tr class="even">
<td>artifacts</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#artifact-definition">artifact definitions</a></p></td>
<td>An optional map of artifact definitions for the Node Type.</td>
</tr>
</tbody>
</table>

#### Grammar 

Node Types have following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">node_type_name</a>&gt;:</p>
<p>derived_from: &lt;<a
href="#TYPE_YAML_STRING">parent_node_type_name</a>&gt;</p>
<p>version: &lt;<a
href="#tosca-tal-suggests-removing-this.version">version_number</a>&gt;</p>
<p>metadata:</p>
<p>&lt;<a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">node_type_description</a>&gt;</p>
<p>properties:</p>
<p>&lt;<a href="#_Schema_Definition">property_definitions</a>&gt;</p>
<p>attributes:</p>
<p>&lt;<a
href="#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition">attribute_definitions</a>&gt;</p>
<p>capabilities:</p>
<p>&lt;<a
href="#capability-definition">capability_definitions</a>&gt;</p>
<p>requirements:</p>
<p>- &lt;<a
href="#requirement-definition">requirement_definitions</a>&gt;</p>
<p>interfaces:</p>
<p>&lt;<a href="#interface-definition">interface_definitions</a>&gt;</p>
<p>artifacts:</p>
<p>&lt;<a
href="#artifact-definition">artifact_definitions</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- node_type_name: represents the mandatory symbolic name of the Node
  Type being declared.

- parent_node_type_name: represents the name (string) of the Node Type
  this Node Type definition derives from (i.e. its parent type).

- version_number: represents the optional TOSCA version number for the
  Node Type.

- node_type_description: represents the optional description string for
  the corresponding node_type_name.

- property_definitions: represents the optional map of property
  definitions for the Node Type.

- attribute_definitions: represents the optional map of attribute
  definitions for the Node Type.

- capability_definitions: represents the optional map of capability
  definitions for the Node Type.

- requirement_definitions: represents the optional list of requirement
  definitions for the Node Type.

- interface_definitions: represents the optional map of one or more
  interface definitions supported by the Node Type.

- artifact_definitions: represents the optional map of artifact
  definitions for the Node Type

#### Derivation rules

During Node Type derivation the keyname definitions follow these rules:

- properties: existing property definitions may be refined; new property
  definitions may be added.

- attributes: existing attribute definitions may be refined; new
  attribute definitions may be added.

- capabilities: existing capability definitions may be refined; new
  capability definitions may be added.

- requirements: existing requirement definitions may be refined; new
  requirement definitions may be added.

- interfaces: existing interface definitions may be refined; new
  interface definitions may be added.

- artifacts: existing artifact definitions (identified by their symbolic
  name) may be redefined; new artifact definitions may be added.

<!-- -->

- note that an artifact is created for a specific purpose and
  corresponds to a specific file (with e.g. a path name and checksum);
  if it cannot meet its purpose in a derived type then a new artifact
  should be defined and used.

- thus, if an artifact defined in a parent node type does not correspond
  anymore with the needs in the child node type, its definition may be
  completely redefined; thus, an existing artifact definition is not
  refined, but completely overwritten.

#### Additional Requirements

- Requirements are intentionally expressed as a list of TOSCA
  [Requirement definitions](#requirement-definition) which **SHOULD** be
  resolved (processed) in sequence by TOSCA Orchestrators.

#### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>my_company.my_types.my_app_node_type:</p>
<p>derived_from: tosca.nodes.SoftwareComponent</p>
<p>description: My company’s custom applicaton</p>
<p>properties:</p>
<p>my_app_password:</p>
<p>type: string</p>
<p>description: application password</p>
<p>validation:</p>
<p>$and:</p>
<p>- { $min_length: [ $value, 6 ] }</p>
<p>- { $max_length: [ $value, 10 ] }</p>
<p>attributes:</p>
<p>my_app_port:</p>
<p>type: integer</p>
<p>description: application port number</p>
<p>requirements:</p>
<p>- some_database:</p>
<p>capability: EndPoint.Database</p>
<p>node: Database</p>
<p>relationship: ConnectsTo</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Node Template

A Node Template specifies the occurrence of a manageable component as
part of an application’s topology model which is defined in a TOSCA
Service Template. A Node Template is an instance of a specified Node
Type and can provide customized properties, relationships, or interfaces
that complement and change the defaults provided by its Node Type.

#### Keynames

The following is the list of recognized keynames for a TOSCA Node
Template definition:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>type</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The mandatory name of the Node Type the Node Template is based
upon.</td>
</tr>
<tr class="even">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional description for the Node Template.</td>
</tr>
<tr class="odd">
<td>metadata</td>
<td>no</td>
<td><a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a></td>
<td>Defines a section used to declare additional metadata
information.</td>
</tr>
<tr class="even">
<td>directives</td>
<td>no</td>
<td>list of <a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional list of directive values to provide processing
instructions to orchestrators and tooling.</td>
</tr>
<tr class="odd">
<td>properties</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#property-assignment">property assignments</a></p></td>
<td>An optional map of property value assignments for the Node
Template.</td>
</tr>
<tr class="even">
<td>attributes</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#attribute-assignment">attribute assignments</a></p></td>
<td>An optional map of attribute value assignments for the Node
Template.</td>
</tr>
<tr class="odd">
<td>requirements</td>
<td>no</td>
<td><p>list of</p>
<p><a href="#requirement-assignment">requirement
assignments</a></p></td>
<td>An optional list of requirement assignments for the Node
Template.</td>
</tr>
<tr class="even">
<td>capabilities</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#capability-assignment">capability assignments</a></p></td>
<td>An optional map of capability assignments for the Node
Template.</td>
</tr>
<tr class="odd">
<td>interfaces</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#interface-assignment">interface assignments</a></p></td>
<td>An optional map of interface assignments for the Node Template.</td>
</tr>
<tr class="even">
<td>artifacts</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#artifact-definition">artifact definitions</a></p></td>
<td>An optional map of artifact definitions for the Node Template.</td>
</tr>
<tr class="odd">
<td>node_filter</td>
<td>no</td>
<td><a href="#node-filter-definition">node filter</a></td>
<td>The optional filter definition that TOSCA orchestrators will use to
select the correct target node.</td>
</tr>
<tr class="even">
<td>copy</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The optional (symbolic) name of another node template to copy into
(all keynames and values) and use as a basis for this node
template.</td>
</tr>
</tbody>
</table>

#### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">node_template_name</a>&gt;:</p>
<p>type: &lt;<a href="#TYPE_YAML_STRING">node_type_name</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">node_template_description</a>&gt;</p>
<p>directives: [&lt;<a href="#TYPE_YAML_STRING">directives</a>&gt;]</p>
<p>metadata:</p>
<p>&lt;<a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a>&gt;</p>
<p>properties:</p>
<p>&lt;<a href="#property-assignment">property_assignments</a>&gt;</p>
<p>attributes:</p>
<p>&lt;<a href="#attribute-assignment">attribute_assignments</a>&gt;</p>
<p>requirements:</p>
<p>- &lt;<a
href="#requirement-assignment">requirement_assignments</a>&gt;</p>
<p>capabilities:</p>
<p>&lt;<a
href="#capability-assignment">capability_assignments</a>&gt;</p>
<p>interfaces:</p>
<p>&lt;<a href="#interface-assignment">interface_assignments</a>&gt;</p>
<p>artifacts:</p>
<p>&lt;<a href="#artifact-definition">artifact_definitions</a>&gt;</p>
<p>node_filter:</p>
<p>&lt;<a
href="#node-filter-definition">node_filter_definition</a>&gt;</p>
<p>copy: &lt;<a
href="#TYPE_YAML_STRING">source_node_template_name</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- node_template_name: represents the mandatory symbolic name of the Node
  Template being declared.

- node_type_name: represents the name of the Node Type the Node Template
  is based upon.

- node_template_description: represents the optional description string
  for Node Template.

- directives: represents the optional list of processing instruction
  keywords (as strings) for use by tooling and orchestrators.

- property_assignments: represents the optional map of property
  assignments for the Node Template that provide values for properties
  defined in its declared Node Type.

- attribute_assignments: represents the optional map of attribute
  assignments for the Node Template that provide values for attributes
  defined in its declared Node Type.

- requirement_assignments: represents the optional list of requirement
  assignments for the Node Template for requirement definitions provided
  in its declared Node Type.

- capability_assignments: represents the optional map of capability
  assignments for the Node Template for capability definitions provided
  in its declared Node Type.

- interface_assignments: represents the optional map of interface
  assignments for the Node Template interface definitions provided in
  its declared Node Type.

- artifact_definitions: represents the optional map of artifact
  definitions for the Node Template that augment those provided by its
  declared Node Type.

- node_filter_definition: represents the optional node filter TOSCA
  orchestrators will use for selecting a matching node template.

- source_node_template_name: represents the optional (symbolic) name of
  another node template to copy into (all keynames and values) and use
  as a basis for this node template.

#### Additional requirements

- The source node template provided as a value on the copy keyname
  **MUST** **NOT** itself use the copy keyname (i.e., it must itself be
  a complete node template description and not copied from another node
  template).

#### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>mysql:</p>
<p>type: tosca.nodes.DBMS.MySQL</p>
<p>properties:</p>
<p>root_password: { $get_input: my_mysql_rootpw }</p>
<p>port: { $get_input: my_mysql_port }</p>
<p>requirements:</p>
<p>- host: db_server</p>
<p>interfaces:</p>
<p>Standard:</p>
<p>operations:</p>
<p>configure: scripts/my_own_configure.sh</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Relationship Type
<!----
{"id": "520", "author": "Michael Rehder", "date": "2020-12-15T13:33:00Z", "comment": "I still think this is simply a Requirement Type \u2013 I can\u2019t see why it isn\u2019t and what advantage there is in calling it something else.", "target": "Relationship Type"}-->


A Relationship Type is a reusable entity that defines the type of one or
more relationships between Node Types or Node Templates
<!----
{"id": "521", "author": "Michael Rehder", "date": "2020-12-15T12:12:00Z", "comment": "There is no\nrelationship type in a node template so why is this stated\nhere?", "target": "Node Templates"}-->
.

#### Keynames

The Relationship Type is a TOSCA type entity and has the common keynames
listed in Section 4.2.5.2 Common keynames in type definitions. In
addition, the Relationship Type has the following recognized keynames:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Definition/Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>properties</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#_Schema_Definition">property definitions</a></p></td>
<td>An optional map of property definitions for the Relationship
Type.</td>
</tr>
<tr class="even">
<td>attributes</td>
<td>no</td>
<td><p>map of</p>
<p><a
href="#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition">attribute
definitions</a></p></td>
<td>An optional map of attribute definitions for the Relationship
Type.</td>
</tr>
<tr class="odd">
<td>interfaces</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#interface-definition">interface definitions</a></p></td>
<td>An optional map of interface definitions supported by the
Relationship Type.</td>
</tr>
<tr class="even">
<td>valid_capability_types</td>
<td>no</td>
<td>list of <a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional list of one or more names of Capability Types that are
valid targets for this relationship. If undefined, all Capability Types
are valid.</td>
</tr>
<tr class="odd">
<td>valid_target_node_types</td>
<td>no</td>
<td>list of <a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional list of one or more names of Node Types that are valid
targets for this relationship. If undefined, all Node Types are valid
targets.</td>
</tr>
<tr class="even">
<td>valid_source_node_types</td>
<td>no</td>
<td>list of <a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional list of one or more names of Node Types that are valid
sources for this relationship. If undefined, all Node Types are valid
sources.</td>
</tr>
</tbody>
</table>

#### Grammar

Relationship Types have following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a
href="#TYPE_YAML_STRING">relationship_type_name</a>&gt;:</p>
<p>derived_from: &lt;<a
href="#TYPE_YAML_STRING">parent_relationship_type_name</a>&gt;</p>
<p>version: &lt;<a
href="#tosca-tal-suggests-removing-this.version">version_number</a>&gt;</p>
<p>metadata:</p>
<p>&lt;<a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">relationship_description</a>&gt;</p>
<p>properties:</p>
<p>&lt;<a href="#_Schema_Definition">property_definitions</a>&gt;</p>
<p>attributes:</p>
<p>&lt;<a
href="#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition">attribute_definitions</a>&gt;</p>
<p>interfaces:</p>
<p>&lt;<a href="#interface-definition">interface_definitions</a>&gt;</p>
<p>valid_capability_types: [ &lt;<a
href="#TYPE_YAML_STRING">capability_type_names</a>&gt; ]</p>
<p>valid_target_node_types: [ &lt;target_node_type_names&gt; ]</p>
<p>valid_source_node_types: [ &lt;source_node_type_names&gt; ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- relationship_type_name: represents the mandatory symbolic name of the
  Relationship Type being declared as a string.

- parent_relationship_type_name: represents the name (string) of the
  Relationship Type this Relationship Type definition derives from
  (i.e., its “parent” type).

- relationship_description: represents the optional description string
  for the corresponding relationship_type_name.

- version_number: represents the optional TOSCA version number for the
  Relationship Type.

- property_definitions: represents the optional map of property
  definitions for the Relationship Type.

- attribute_definitions: represents the optional map of attribute
  definitions for the Relationship Type.

- interface_definitions: represents the optional map of interface
  definitions supported by the Relationship Type.

- capability_type_names: represents the optional list of valid target
  Capability Types for the relationship; if undefined, the valid target
  types are not restricted at all (i.e., all Capability Types are
  valid).

- target_node_type_names: represents the optional list of valid target
  Node Types for the relationship; if undefined, the valid types are not
  restricted at all (i.e., all Node Types are valid).

- source_node_type_names: represents the optional list of valid source
  Node Types for the relationship; if undefined, the valid types are not
  restricted at all (i.e., all Node Types are valid).

#### Derivation rules

During Relationship Type derivation the keyname definitions follow these
rules:

- properties: existing property definitions may be refined; new property
  definitions may be added.

- attributes: existing attribute definitions may be refined; new
  attribute definitions may be added.

- interfaces: existing interface definitions may be refined; new
  interface definitions may be added.

- valid_capability_types: if valid_capability_types is defined in the
  parent type, each element in this list must either be in the parent
  type list or derived from an element in the parent type list; if
  valid_target_types is not defined in the parent type then no
  restrictions are applied.

- valid_target_node_types: same derivation rules as for
  valid_capability_types

- valid_source_node_types: same derivation rules as for
  valid_capability_types

#### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>mycompanytypes.myrelationships.AppDependency:</p>
<p>derived_from: tosca.relationships.DependsOn</p>
<p>valid_capability_types: [
mycompanytypes.mycapabilities.SomeAppCapability ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Relationship Template

A Relationship Template
specifies the occurrence of a manageable relationship between node
templates as part of an application’s topology model that is defined in
a TOSCA Service Template. A Relationship template is an instance of a
specified Relationship Type and can provide customized properties, or
operations that complement and change the defaults provided by its
Relationship Type and its implementations.
<!----
{"id": "532", "author": "Michael Rehder", "date": "2020-12-15T13:23:00Z", "comment": "My understanding is that this is an\nalternative to relations defined within node templates.  \nIt\u2019s not clear why this option would be chosen over the node-template\noption.  \nIf both relations in node-templates and Relationship Templates are used,\nhow are they combined together?  \nOr is this not recommended?  \nI can imagine that combination rules would be very difficult to define\nbut if it is possible, it must be defined", "target": "A Relationship Template\nspecifies the occurrence of a manageable relationship between node\ntemplates as part of an application\u2019s topology model that is defined in\na TOSCA Service Template. A Relationship template is an instance of a\nspecified Relationship Type and can provide customized properties, or\noperations that complement and change the defaults provided by its\nRelationship Type and its implementations."}-->


Relations between Node Templates can be defined either using
Relationship Templates or Requirements and Capability definitions within
Node Types. Use of Relationship Templates decouples relationship
definitions from Node Type definitions, allowing Node Type definitions
to be more “generic” for use in a wider set of service templates which
have varying relation definition requirements. The Relationship
Templates are local within a service template and so have a limited
scope. Requirements and Capabilities defined in Node Types have a wider
scope, exposed within any service template which contains a Node
Template of the Node Type.

Note that using the relationship templates is underspecified currently
and can be used only as a further template for relationships in
requirements definition. This topic needs further work.

#### Keynames

The following is the list of recognized keynames for a TOSCA
Relationship Template definition:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>type</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The mandatory name of the Relationship Type the Relationship
Template is based upon.</td>
</tr>
<tr class="even">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>An optional description for the Relationship Template.</td>
</tr>
<tr class="odd">
<td>valid_source_node_types: not applicable to the
  definitions in the parent node type but to the definitions in the
  capability type referred by the type keyname (see grammar above for
  the rules).
<!----
{"id": "535\" data-author=\"Calin Curescu\"\ndata-date=\"2022-04-18T17:14:00Z\">Add these to the relationship\ndefinition as part of the requirement definition</span>metadata</td>\n<td>no</td>\n<td><a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Defines a section used to declare additional metadata information.\n<span class=\"comment-end\" id=\"535\"></span></td>\n</tr>\n<tr class=\"even\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">property assignments</a></p></td>\n<td>An optional map of property assignments for the Relationship\nTemplate.</td>\n</tr>\n<tr class=\"odd\">\n<td>attributes</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#attribute-assignment\">attribute assignments</a></p></td>\n<td>An optional map of attribute assignments for the Relationship\nTemplate.</td>\n</tr>\n<tr class=\"even\">\n<td>interfaces</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#interface-assignment\">interface assignments</a></p></td>\n<td>An optional map of interface assignments for the relationship\ntemplate.</td>\n</tr>\n<tr class=\"odd\">\n<td>copy</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional (symbolic) name of another relationship template to\ncopy into (all keynames and values) and use as a basis for this\nrelationship template.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;relationship_template_name&gt;:</p>\n<p>type: &lt;<a\nhref=\"#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type\">relationship_type_name</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_type_description</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#property-assignment\">property_assignments</a>&gt;</p>\n<p>attributes:</p>\n<p>&lt;<a href=\"#attribute-assignment\">attribute_assignments</a>&gt;</p>\n<p>interfaces:</p>\n<p>&lt;<a href=\"#interface-assignment\">interface_assignments</a>&gt;</p>\n<p>copy:</p>\n<p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">source_relationship_template_name</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- relationship_template_name: represents the mandatory symbolic name of\n  the Relationship Template being declared.\n\n- relationship_type_name: represents the name of the Relationship Type\n  the Relationship Template is based upon.\n\n- relationship_template_description: represents the optional description\n  string for the Relationship Template.\n\n- property_assignments: represents the optional map of property\n  assignments for the Relationship Template that provide values for\n  properties defined in its declared Relationship Type.\n\n- attribute_assignments: represents the optional map of attribute\n  assignments for the Relationship Template that provide values for\n  attributes defined in its declared Relationship Type.\n\n- interface_assignments: represents the optional map of interface\n  assignments for the Relationship Template for interface definitions\n  provided by its declared Relationship Type.\n\n- source_relationship_template_name: represents the optional (symbolic)\n  name of another relationship template to copy into (all keynames and\n  values) and use as a basis for this relationship template.\n\n#### Additional requirements\n\n- The source relationship template provided as a value on the copy\n  keyname MUST NOT itself use the copy keyname (i.e., it must itself be\n  a complete relationship template description and not copied from\n  another relationship template).\n\n#### Example\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>relationship_templates:</p>\n<p>storage_attachment:</p>\n<p>type: AttachesTo</p>\n<p>properties:</p>\n<p>location: /my_mount_point</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Capabilities and Requirements\n\n#### Capability Type\n\nA Capability Type is a reusable entity that describes a kind of\ncapability that a Node Type can declare to expose. Requirements\n(implicit or explicit) that are declared as part of one node can be\nmatched to (i.e., fulfilled by) the Capabilities declared by another\nnode.\n\n##### Keynames\n\nThe Capability Type is a TOSCA type entity and has the common keynames\nlisted in Section 4.2.5.2 Common keynames in type definitions. In\naddition, the Capability Type has the following recognized keynames:\n\n<table>\n<colgroup>\n<col style=\"width: 22%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 52%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>properties</td>\n<td>no</td>\n<td>map of<br />\n<a href=\"#_Schema_Definition\">property definitions</a></td>\n<td>An optional map of property definitions for the Capability\nType.</td>\n</tr>\n<tr class=\"even\">\n<td>attributes</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute\ndefinitions</a></p></td>\n<td>An optional map of attribute definitions for the Capability\nType.</td>\n</tr>\n<tr class=\"odd\">\n<td>valid_source_node_types</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>An optional list of one or more valid names of Node Types that are\nsupported as valid sources of any relationship established to the\ndeclared Capability Type. If undefined, all Node Types are valid\nsources.</td>\n</tr>\n<tr class=\"even\">\n<td>valid_relationship_types</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>An optional list of one or more valid names of Relationship Types\nthat are supported as valid types of any relationship established to the\ndeclared Capability Type. If undefined, all Relationship Types are\nvalid.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nCapability Types have following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">capability_type_name</a>&gt;:</p>\n<p>derived_from: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parent_capability_type_name</a>&gt;</p>\n<p>version: &lt;<a\nhref=\"#tosca-tal-suggests-removing-this.version\">version_number</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_description</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#_Schema_Definition\">property_definitions</a>&gt;</p>\n<p>attributes:</p>\n<p>&lt;<a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute_definitions</a>&gt;</p>\n<p>valid_source_node_types: [ &lt;<a\nhref=\"#TYPE_YAML_STRING\">node_type_names</a>&gt; ]</p>\n<p>valid_relationship_types: [ &lt;relationship_type_names&gt;\n]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- capability_type_name: represents the mandatory name of the Capability\n  Type being declared as a string.\n\n- parent_capability_type_name: represents the name of the Capability\n  Type this Capability Type definition derives from (i.e., its \u201cparent\u201d\n  type).\n\n- version_number: represents the optional TOSCA version number for the\n  Capability Type.\n\n- capability_description: represents the optional description string for\n  the Capability Type.\n\n- property_definitions: represents the optional map of property\n  definitions for the Capability Type.\n\n- attribute_definitions: represents the optional map of attribute\n  definitions for the Capability Type.\n\n- node_type_names: represents the optional list of one or more names of\n  Node Types that the Capability Type supports as valid sources for a\n  successful relationship to be established to a capability of this\n  Capability Type; if undefined, the valid source types are not\n  restricted at all (i.e. all Node Types are valid).\n\n- relationship_type_names: represents the optional list of one or more\n  names of Relationship Types that the Capability Type supports as valid\n  types for a successful relationship to be established to a capability\n  of this Capability Type; if undefined, the valid types are not\n  restricted at all (i.e. all Relationship Types are valid).\n\n##### Derivation rules\n\nDuring Capability Type derivation the keyname definitions follow these\nrules:\n\n- properties: existing property definitions may be refined; new property\n  definitions may be added.\n\n- attributes: existing attribute definitions may be refined; new\n  attribute definitions may be added.\n\n- valid_source_node_types: if valid_source_types is defined in the\n  parent type, each element in this list must either be in the parent\n  type list or derived from an element in the parent type list; if\n  valid_source_types is not defined in the parent type then no\n  restrictions are applied.\n\n- valid_relationship_types: same derivations rules as for\n  valid_source_node_types.\n\n##### Example\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>mycompany.mytypes.myapplication.MyFeature:</p>\n<p>derived_from: tosca.capabilities.Root</p>\n<p>description: a custom feature of my company\u2019s application</p>\n<p>properties:</p>\n<p>my_feature_setting:</p>\n<p>type: string</p>\n<p>my_feature_value:</p>\n<p>type: integer</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n#### Capability definition\n\nA Capability definition defines a typed set of data that a node can\nexpose and is used to describe a relevant feature of the component\ndescribed by the node. A Capability is defined part of a Node Type\ndefinition and may be refined during Node Type derivation.\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA capability\ndefinition:\n\n<table style=\"width:100%;\">\n<colgroup>\n<col style=\"width: 27%\" />\n<col style=\"width: 15%\" />\n<col style=\"width: 14%\" />\n<col style=\"width: 42%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The mandatory name of the Capability Type this capability definition\nis based upon.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional description of the Capability definition.</td>\n</tr>\n<tr class=\"odd\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#_Schema_Definition\">property refinements</a></p></td>\n<td>An optional map of property refinements for the Capability\ndefinition. The referred properties must have been defined in the\nCapability Type definition referred by the type keyword. New properties\nmay not be added.</td>\n</tr>\n<tr class=\"even\">\n<td>attributes</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute\nrefinements</a></p></td>\n<td>An optional map of attribute refinements for the Capability\ndefinition. The referred attributes must have been defined in the\nCapability Type definition referred by the type keyword. New attributes\nmay not be added.</td>\n</tr>\n<tr class=\"odd\">\n<td>valid_source_node_types</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>An optional list of one or more valid names of Node Types that\nare supported as valid sources of any relationship established to the\ndeclared Capability Type. If undefined, all node types are valid\nsources.</p>\n<p>If valid_source_node_types is defined in the Capability Type, each\nelement in this list must either be or derived from an element in the\nlist defined in the type.</p></td>\n</tr>\n<tr class=\"even\">\n<td>valid_relationship_types</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>An optional list of one or more valid names of Relationship Types\nthat are supported as valid types of any relationship established to the\ndeclared Capability Type. If undefined, all Relationship Types are\nvalid.</p>\n<p>If valid_relationship_types is defined in the Capability Type, each\nelement in this list must either be or derived from an element in the\nlist defined in the type.</p></td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nCapability definitions have one of the following grammars:\n\n###### Short notation\n\nThe following single-line grammar may be used when only the capability\ntype needs to be declared, without further refinement of the definitions\nin the capability type:\n\n| \\<[capability_definition_name](#TYPE_YAML_STRING)\\>: \\<[capability_type](#capability-type)\\> |\n|----------------------------------------------------------------------------------------------|\n\n###### Extended notation\n\nThe following multi-line grammar may be used when additional information\non the capability definition is needed:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_definition_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">capability_type</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_description</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#_Schema_Definition\">property_refinements</a>&gt;</p>\n<p>attributes:</p>\n<p>&lt;<a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute_refinements</a>&gt;</p>\n<p>valid_source_node_types: [ &lt;node_type_names&gt; ]</p>\n<p>valid_relationship_types: [ &lt;relationship_type_names&gt;\n]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- capability_definition_name**:** represents the symbolic name of the\n  capability as a string.\n\n- capability_type: represents the mandatory name of a capability type\n  the capability definition is based upon.\n\n- capability_description: represents the optional description of the\n  capability definition.\n\n- property_refinements: represents the optional map of property\n  definitions refinements for properties already defined in the\n  capability type; new properties may not be added.\n\n- attribute_refinements: represents the optional map of attribute\n  definitions refinements for attributes already defined in the\n  capability type; new attributes may not be added.\n\n- node_type_names: represents the optional list of one or more names of\n  node types that the capability definition supports as valid sources\n  for a successful relationship to be established to said capability\n\n- if valid_source_node_types is defined in the capability type, each\n  > element in this list MUST either be in that list or derived from an\n  > element in that list; if valid_source_types is not defined in the\n  > capability type then no restrictions are applied.\n\n- relationship_type_names: represents the optional list of one or more\n  names of relationship types that the capability definition supports as\n  valid type for a successful relationship to be established to said\n  capability\n\n- if valid_relationship_types is defined in the capability type, each\n  > element in this list MUST either be in that list or derived from an\n  > element in that list; if valid_source_types is not defined in the\n  > capability type then no restrictions are applied.\n\n##### Refinement rules\n\nA capability definition within a node type uses the following definition\nrefinement rules when the containing node type is derived:\n\n- type: must be derived from (or the same as) the type in the capability\n  definition in the parent node type definition.\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the capability definition in the parent node type\n  definition.\n\n- properties: not applicable to the definitions in the parent node type\n  but to the definitions in the capability type referred by the type\n  keyname (see grammar above for the rules).\n\n- attributes: not applicable to the definitions in the parent node type\n  but to the definitions in the capability type referred by the type\n  keyname (see grammar above for the rules).\n\n- <span class=\"comment-start\" id=\"567", "author": "Michael Rehder", "date": "2020-12-15T11:17:00Z", "comment": "What are the refinement rules for this? Is\n  it a logical AND of the node types or an intersection set or a\n  replacement?", "target": "valid_source_node_types: not applicable to the\n  definitions in the parent node type but to the definitions in the\n  capability type referred by the type keyname (see grammar above for\n  the rules)."}-->


- valid_relationship_types: not applicable to the definitions in the
  parent node type but to the definitions in the capability type
  referred by the type keyname (see grammar above for the rules).

##### Examples

The following examples show capability definitions in both simple and
full forms:

###### Simple notation example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Simple notation, no properties need to be refined</p>
<p>some_capability: mytypes.mycapabilities.MyCapabilityTypeName</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Full notation example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Full notation, refining properties</p>
<p>some_capability:</p>
<p>type: mytypes.mycapabilities.MyCapabilityTypeName</p>
<p>properties:</p>
<p>limit:</p>
<p>default: 100</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Additional requirements

- Capability symbolic names SHALL be unique; it is an error if a
  capability name is found to occur more than once.

##### Note

- The occurrences keyname is deprecated in TOSCA 2.0. By default, the
  number of “occurrences” is UNBOUNDED, i.e. any number of relationships
  can be created with a certain capability as a target. To constrain the
  creation of a relationship to a target capability, the new
  “allocation” keyname is used within a requirement assignment.

#### Capability assignment

A capability assignment allows node template authors to assign values to
properties and attributes for a capability definition that is part of
the node templates’ respective type definition, and also to set the
capability occurrences.

##### Keynames

The following is the list of recognized keynames for a TOSCA capability
assignment:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 42%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>properties</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#property-assignment">property assignments</a></p></td>
<td colspan="2">An optional map of property assignments for the
Capability definition.</td>
</tr>
<tr class="even">
<td>attributes</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#attribute-assignment">attribute assignments</a></p></td>
<td colspan="2">An optional map of attribute assignments for the
Capability definition.</td>
</tr>
<tr class="odd">
<td>directives</td>
<td><p>no</p>
<p>default: [internal, external]</p></td>
<td><p>list of string</p>
<p>valid string values:</p>
<p>“internal”,</p>
<p>“external”</p></td>
<td>Describes if the fulfillment of this capability assignment should
use relationships with source nodes created within this template
(“internal”) or should use source nodes created outside this template as
available to the TOSCA environment ("external”) or if it should use a
combination of the above. If so, the order of the strings in the list
defines which scope should be attempted first. If no scope is defined,
the default value is [internal, external]. If no directives are defined,
the default value is left to the particular implementation.</td>
<td></td>
</tr>
</tbody>
</table>

##### Grammar

Capability assignments have one of the following grammars:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a
href="#TYPE_YAML_STRING">capability_definition_name</a>&gt;:</p>
<p>properties:</p>
<p>&lt;<a href="#property-assignment">property_assignments</a>&gt;</p>
<p>attributes:</p>
<p>&lt;<a href="#attribute-assignment">attribute_assignments</a>&gt;</p>
<p>directives: &lt;directives_list&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammars, the pseudo values that appear in angle brackets
have the following meaning:

- capability_definition_name: represents the symbolic name of the
  capability as a string.

- property_assignments: represents the optional map of property
  assignments that provide values for properties defined in the
  Capability definition.

- attribute_assignments: represents the optional map of attribute
  assignments that provide values for attributes defined in the
  Capability definition.

- directives_list: represents the optional list of strings that defines
  directives for this capability:

- valid values for the strings:

- “internal” – relationships to this capability can be created from
  > source nodes created within this template.

- “external” – relationships to this capability can be created from
  > source nodes created outside this template as available to the TOSCA
  > environment.

- the order of the strings in the list defines which scope should be
  > attempted first when fulfilling the assignment.

- If no directives are defined, the default value is left to the
  > particular implementation.

##### Example

The following example shows a capability assignment:

###### Notation example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>some_node_template:</p>
<p>capabilities:</p>
<p>some_capability:</p>
<p>properties:</p>
<p>limit: 100</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Note

- The occurrences keyname is deprecated in TOSCA 2.0. By default, the
  number of “occurrences” is UNBOUNDED, i.e. any number of relationships
  can be created with a certain capability as a target. To constrain the
  creation of a relationship to a target capability, the new
  “allocation” keyname is used within a requirement assignment.

#### Requirement
<!----
{"id": "591", "author": "Chris Lauwers", "date": "2022-06-22T20:47:00Z", "comment": "It seems to me that the only reason this section is here is to point out a difference with the XML spec. I recommend removing it.", "target": "Requirement"}-->
 Type 

Requirement types are not defined in TOSCA. TOSCA seeks to simplify the
modeling by not declaring specific Requirement Types with nodes
declaring their features sets using TOSCA Capability Types. So, it
suffices that capabilities are advertised a-priory by Capability Types,
while requirement definitions can be directly created during Node Type
design.

#### Requirement definition

The Requirement definition describes a requirement (dependency) of a
TOSCA node which needs to be fulfilled by a matching Capability
definition declared by another TOSCA node. A Requirement is defined as
part of a Node Type definition and may be refined during Node Type
derivation.

##### Keynames

The following is the list of recognized keynames for a TOSCA requirement
definition:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 12%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The optional description of the Requirement definition.</td>
</tr>
<tr class="even">
<td>As opposed to an operation
definition, a notification definition does not include an inputs keyname
since notifications are not invoked from the
orchestrator.
<!----
{"id": "597\" data-author=\"Calin Curescu\"\ndata-date=\"2020-06-17T18:53:00Z\">Chris is suggesting the possibility to\nrequire several capabilities from one requirement! Need to discuss how\nthat could be solved.</span>capability<span class=\"comment-end\"\nid=\"597\"></span></td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The mandatory keyname used to provide either the:</p>\n<ul>\n<li><p>symbolic name of a <strong>Capability definition</strong> within\na <em>target</em> Node Type that can fulfill the requirement.</p></li>\n<li><p>name of a <strong>Capability Type</strong> that the TOSCA\norchestrator will use to select a type-compatible <em>target</em> node\nto fulfill the requirement at runtime.</p></li>\n</ul></td>\n</tr>\n<tr class=\"odd\">\n<td>node</td>\n<td>conditional</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The optional keyname used to provide the name of a valid <a\nhref=\"#node-type\">Node Type</a> that contains the capability definition\nthat can be used to fulfill the requirement.</p>\n<p>If a symbolic name of a <strong>Capability definition</strong> has\nbeen used for the capability keyname, then the node keyname is\nmandatory.</p></td>\n</tr>\n<tr class=\"even\">\n<td><span class=\"comment-start\" id=\"598\" data-author=\"Calin Curescu\"\ndata-date=\"2020-04-18T23:42:00Z\">!!! I think we need to make the\nrelationship mandatory, otherwise we cannot decouple the Simple\nProfile.<br />\nFor backward compatibility, we can state that for TOSCA &lt; v2.0 if a\nrelationship is not defined then the orchestrator can always fall back\nto tosca.relationships.Root.</span>relationship<span class=\"comment-end\"\nid=\"598\"></span></td>\n<td>conditional</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The optional keyname used to provide the name of a valid <a\nhref=\"#i-still-think-this-is-simply-a-requirement-type-i-cant-see-why-it-isnt-and-what-advantage-there-is-in-calling-it-something-else.relationship-type\">Relationship\nType</a> to construct a relationship when fulfilling the\nrequirement.</p>\n<p>The relationship definition is mandatory either in the requirement\ndefinition of in the requirement assignment.</p></td>\n</tr>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"599\" data-author=\"Calin Curescu\"\ndata-date=\"2022-02-22T16:12:00Z\">Node_filter is not in TOSCA 1.3 so we\nneed to check again.</span>node_filter<span class=\"comment-end\"\nid=\"599\"></span></td>\n<td>no</td>\n<td><a href=\"#node-filter-definition\">node filter</a></td>\n<td>The optional filter definition that TOSCA orchestrators will use to\nselect a type-compatible <em>target</em> node that can fulfill the\nassociated abstract requirement at runtime.</td>\n</tr>\n<tr class=\"even\">\n<td>count_range</td>\n<td>no</td>\n<td><a href=\"#TYPE_TOSCA_RANGE\">range</a> of <a\nhref=\"#TYPE_YAML_INTEGER\">integer</a></td>\n<td><p>The optional minimum required and maximum allowed number of\nrelationships created by the requirement. If this key is not specified,\nthe implied default of [0, UNBOUNDED] will be used.</p>\n<p>Note: the keyword UNBOUNDED is also supported to represent any\npositive integer.</p></td>\n</tr>\n</tbody>\n</table>\n\n###### Additional keynames for multi-line relationship grammar\n\nThe Requirement definition contains the Relationship Type information\nneeded by TOSCA Orchestrators to construct relationships to other TOSCA\nnodes with matching capabilities; however, it is sometimes recognized\nthat additional parameters may need to be passed to the relationship\n(perhaps for configuration). In these cases, additional grammar is\nprovided so that the requirement definition may declare interface\nrefinements (e.g. changing the implementation definition or declaring\nadditional parameter definitions to be used as inputs/outputs).\n\n| Keyname    | Mandatory | Type                                                  | Description                                                                                                                  |\n|------------|-----------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|\n| type       | yes       | [string](#TYPE_YAML_STRING)                           | The optional keyname used to provide the name of the Relationship Type as part of the relationship keyname definition.       |\n| interfaces | no        | map of [interface refinements](#interface-definition) | The optional keyname used to reference declared interface definitions on the corresponding Relationship Type for refinement. |\n\n##### Grammar\n\nRequirement definitions have one of the following grammars:\n\n###### Simple grammar (Capability Type only)\n\n| \\<[requirement_definition_name](#TYPE_YAML_STRING)\\>: \\<[capability_type_name](#TYPE_YAML_STRING)\\> |\n|-----------------------------------------------------------------------------------------------------|\n\n###### Extended grammar (with Node and Relationship Types)\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">requirement_definition_name</a>&gt;:</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">requirement_description</a>&gt;</p>\n<p>capability: &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_symbolic_name</a>&gt; | &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_type_name</a>&gt;</p>\n<p>node: &lt;<a href=\"#TYPE_YAML_STRING\">node_type_name</a>&gt;</p>\n<p>relationship: &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_type_name</a>&gt;</p>\n<p>node_filter: &lt;<a\nhref=\"#node-filter-definition\">node_filter_definition</a>&gt;</p>\n<p>count_range: [ &lt;min_count&gt;, &lt;max_count&gt; ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Extended grammar for declaring Parameter Definitions on the relationship\u2019s Interfaces\n\nThe following additional multi-line grammar is provided for the\nrelationship keyname in order to declare new parameter definitions for\ninputs/outputs of known Interface definitions of the declared\nRelationship Type.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">requirement_definition_name</a>&gt;:</p>\n<p># Other keynames omitted for brevity</p>\n<p>relationship:</p>\n<p>type: &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_type_name</a>&gt;</p>\n<p>interfaces: &lt;<a\nhref=\"#interface-definition\">interface_refinements</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- requirement_definition_name: represents the mandatory symbolic name of\n  the requirement definition as a string.\n\n- requirement_description: represents the optional description of the\n  requirement definition.\n\n- capability_symbolic_name: represents the mandatory symbolic name of\n  the Capability definition within the target Node Type.\n\n- capability_type_name: represents the mandatory name of a Capability\n  Type that can be used to fulfill the requirement.\n\n- node_type_name: represents the name of a Node Type that contains\n  either the Capability Type or the Capability definition the\n  requirement can be fulfilled by; the node_type_name is mandatory if\n  the capability_symbolic_name was used, and is optional if the\n  capability_type_name was used.\n\n- relationship_type_name: represents the optional name of a Relationship\n  Type to be used to construct a relationship between this requirement\n  definition (i.e. in the source node) to a matching capability\n  definition (in a target node).\n\n- node_filter_definition: represents the optional node filter TOSCA\n  orchestrators will use to fulfill the requirement when selecting a\n  target node, or to verify that the specified node template fulfills\n  the requirement (if a node template was specified during requirement\n  assignment).\n\n- min_count, max_count: represents the optional range between a minimum\n  required and maximum allowed count of the requirement\n\n- this range constrains how many relationships from this requirement\n  > towards target capabilities (in target nodes) are created, and that\n  > number MUST be within the range specified here.\n\n- by default (i.e. if count_range\u00a0is undefined here), a requirement\n  > shall form exactly one relationship ( \\[1, 1\\] i.e. allowed at least\n  > one, and at most one).\n\n- interface_refinements: represents refinements for one or more already\n  declared interface definitions in the Relationship Type (as declared\n  on the type keyname)\n\n- allowing for the declaration of new parameter definitions for these\n  > interfaces or for specific operation or notification definitions of\n  > these interfaces or for the change of the description or\n  > implementation definitions.\n\n##### Refinement rules\n\nA requirement definition within a node type uses the following\ndefinition refinement rules when the containing node type is derived:\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the requirement definition in the parent node type\n  definition.\n\n- capability: the type of the capability must be derived from (or the\n  same as) the capability type in the requirement definition in the\n  parent node type definition.\n\n- if the capability was specified using the symbolic name of a\n  > capability definition in the target node type, then the capability\n  > keyname definition MUST remain unchanged in any subsequent\n  > refinements or during assignment.\n\n- node: must be derived from (or the same as) the node type in the\n  requirement definition in the parent node type definition; if node is\n  not defined in the parent type then no restrictions are applied;\n\n- the node type specified by the node keyname must also contain a\n  > capability definition that fulfills the requirement set via the\n  > capability keyname above.\n\n- relationship: must be derived from (or the same as) the relationship\n  type in the requirement definition in the parent node type definition;\n  if relationship is not defined in the parent type then no restrictions\n  are applied.\n\n- node_filter: a new definition is unrestricted and will be considered\n  in addition (i.e. logical and) to the node_filter definition in the\n  parent node type definition; further refinements may add further node\n  filters.\n\n- count_range: the new range MUST be within the range defined in the\n  requirement definition in the parent node type definition.\n\n##### Additional requirements\n\n- Requirement symbolic names SHALL be unique; it is an error if a\n  requirement name is found to occur more than once.\n\n- If the count_range keyname is not present, then a default declaration\n  as follows will be assumed:\n\n  count_range: \\[0, UNBOUNDED\\]\n\n##### Notes\n\n- The requirement symbolic name is used for identification of the\n  requirement definition only and not relied upon for establishing any\n  relationships in the topology.\n\n##### Requirement definition is a tuple with a filter \n\nA requirement definition allows type designers to govern which types are\nallowed (valid) for fulfillment using three levels of specificity with\nonly the Capability definition or Capability Type being mandatory.\n\n5.  Node Type (mandatory/optional)\n\n6.  Relationship Type (optional)\n\n7.  Capability definition or Capability Type (mandatory)\n\nThe first level allows selection, as shown in both the simple or complex\ngrammar, simply providing the node\u2019s type using the node keyname. The\nsecond level allows specification of the relationship type to use when\nconnecting the requirement to the capability using the relationship\nkeyname. Finally, the specific Capability definition or Capability Type\non the target node is provided using the capability keyname. Note that\nif a Capability definition is used, the Node Type definition is\nmandatory (as it refers to a Capability definition in that Node Type).\n\nIn addition to the node, relationship and capability types, a filter,\nwith the keyname node_filter, may be provided to constrain the allowed\nset of potential target nodes based upon their properties and their\ncapabilities\u2019 properties. This allows TOSCA orchestrators to help find\nthe \u201cbest fit\u201d when selecting among multiple potential target nodes for\nthe expressed requirements. Also, if a Node Template was specified\nduring requirement assignment it allows TOSCA orchestrators to verify\nthat the specified node template fulfills the requirement.\n\n#### Requirement assignment\n\nA Requirement assignment allows Node Template authors to provide\nassignments for the corresponding Requirement definition (i.e. having\nthe same symbolic name) in the Node Type definition.\n\nA Requirement assignment provides either names of Node Templates or\nselection criteria for TOSCA orchestrators to find matching TOSCA nodes\nthat are used to fulfill the requirement\u2019s declared Capability Type\nand/or Node Type. A Requirement assignment also provides either names of\nRelationship Templates (to use) or the name of Relationship Types (to\ncreate relationships) for relating the source node (containing the\nRequirement) to the target node (containing the Capability).\n\nNote that several Requirement assignments in the Node Template\ndefinition can have the same symbolic name, each referring to different\ncounts of the Requirement definition. To how many counts a particular\nassignment allows is set via the count_range keyname. Nevertheless, the\nsum of the count values for all of the Requirement assignments with the\nsame symbolic name MUST be within the range of count_range specified by\nthe corresponding Requirement definition.\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA requirement\nassignment:\n\n<table>\n<colgroup>\n<col style=\"width: 13%\" />\n<col style=\"width: 13%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 61%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>capability</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The optional keyname used to provide either the:</p>\n<ul>\n<li><p>symbolic name of a <strong>Capability definition</strong> within\na <em>target</em> node that can fulfill the requirement.</p></li>\n<li><p>name of a <strong>Capability Type</strong> that the TOSCA\norchestrator will use to select a type-compatible <em>target</em> node\nto fulfill the requirement at runtime.</p></li>\n</ul></td>\n</tr>\n<tr class=\"even\">\n<td>node</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The optional keyname used to identify the target node of a\nrelationship; specifically, it is used to provide either the:</p>\n<ul>\n<li><p>name of a <strong>Node Template</strong> that can fulfill the\n<em>target</em> node requirement.</p></li>\n<li><p>name of a <strong>Node Type</strong> that the TOSCA orchestrator\nwill use to select a type-compatible <em>target</em> node to fulfill the\nrequirement at runtime.</p></li>\n</ul></td>\n</tr>\n<tr class=\"odd\">\n<td>relationship</td>\n<td>conditional</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p><span class=\"comment-start\" id=\"622\" data-author=\"Michael Rehder\"\ndata-date=\"2020-12-15T13:05:00Z\">What about the type, properties,\ninterfaces keynames below?</span>The conditional keyname used to provide\neither the:</p>\n<ul>\n<li><p><span class=\"comment-start\" id=\"623\" data-author=\"Calin Curescu\"\ndata-date=\"2022-04-18T17:21:00Z\">To take out</span>name of a\n<strong>Relationship Template</strong> to use to relate <em>this</em>\nnode to the <em>target</em> node when fulfilling the requirement.<span\nclass=\"comment-end\" id=\"623\"></span></p></li>\n<li><p>name of a <strong>Relationship Type</strong> that the TOSCA\norchestrator will use to create a relationship to relate <em>this</em>\nnode to the <em>target</em> node when fulfilling the requirement.<span\nclass=\"comment-end\" id=\"622\"></span></p></li>\n<li><p>Details of a <strong>Relationship Type</strong> and its property\nand interface assignments that the TOSCA orchestrator will use to create\na relationship to relate <em>this</em> node to the <em>target</em> node\nwhen fulfilling the requirement.</p></li>\n</ul>\n<p>The relationship definition is mandatory either in the requirement\ndefinition of in the requirement assignment.</p></td>\n</tr>\n<tr class=\"even\">\n<td>allocation</td>\n<td>no</td>\n<td>allocation block</td>\n<td><p>The optional keyname that allows the inclusion of an allocation\nblock. The allocation block contains a map of property assignments that\nsemantically represent \u201callocations\u201d from the property with the same\nname in the target capability.</p>\n<ul>\n<li><p>The allocation acts as a \u201ccapacity filter\u201d for the target\ncapability in the target node. When the requirement is resolved, a\ncapability in a node is a valid target for the requirement relationship\nif for each property of the target capability, the sum of all existing\nallocations plus the current allocation is less_or_equal to the property\nvalue.</p></li>\n</ul></td>\n</tr>\n<tr class=\"odd\">\n<td>node_filter</td>\n<td>no</td>\n<td><a href=\"#node-filter-definition\">node filter</a></td>\n<td>The optional filter definition that TOSCA orchestrators will use to\nselect a type-compatible <em>target</em> node that can fulfill the\nrequirement at runtime.</td>\n</tr>\n<tr class=\"even\">\n<td>count</td>\n<td>no</td>\n<td>non-negative <a href=\"#TYPE_YAML_INTEGER\">integer</a></td>\n<td><p>An optional keyname that sets the cardinality of the requirement\nassignment, that is how many relationships to be established from this\nrequirement assignment specification.</p>\n<p>If not defined, the assumed count for an assignment is 1.</p>\n<p>Note that there can be multiple requirement assignments for a\nrequirement with a specific symbolic name.</p>\n<ul>\n<li><p>The sum of all count values of assignments for a requirement with\na specific symbolic name must be within the count_range defined in the\nrequirement definition.</p></li>\n<li><p>Moreover, the sum of all count values of non-optional assignments\nfor a requirement with a specific symbolic name must also be within the\ncount_range defined in the requirement definition.</p></li>\n</ul></td>\n</tr>\n<tr class=\"odd\">\n<td>directives</td>\n<td>no</td>\n<td><p>list of string</p>\n<p>valid string values:</p>\n<p>\u201cinternal\u201d,</p>\n<p>\u201cexternal\u201d</p></td>\n<td>Describes if the fulfillment of this requirement assignment should\nuse relationships with target nodes created within this template\n(\u201cinternal\u201d) or should use target nodes created outside this template as\navailable to the TOSCA environment (\"external\u201d) or if it should use a\ncombination of the above. If so, the order of the strings in the list\ndefines which directive should be attempted first. If no directives are\ndefined, the default value is left to the particular\nimplementation.</td>\n</tr>\n<tr class=\"even\">\n<td>optional</td>\n<td><p>no</p>\n<p>default:</p>\n<p>false</p></td>\n<td>boolean</td>\n<td><p>Describes if the fulfillment of this requirement assignment is\noptional (true) or not (false).</p>\n<p>If not specified, the requirement assignment must be fulfilled, i.e.\nthe default value is false.</p>\n<p>Note also, that non-optional requirements have precedence, thus\nduring a service deployment, the optional requirements for all nodes\nshould be resolved only after the non-optional requirements for all\nnodes have been resolved.</p></td>\n</tr>\n</tbody>\n</table>\n\nThe following is the list of recognized keynames for a TOSCA requirement\nassignment\u2019s relationship keyname which is used when property\nassignments or interface assignments (for e.g. changing the\nimplementation keyname or declare additional parameter definitions to be\nused as inputs/outputs) need to be provided:\n\n<table>\n<colgroup>\n<col style=\"width: 13%\" />\n<col style=\"width: 13%\" />\n<col style=\"width: 10%\" />\n<col style=\"width: 62%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional keyname used to provide the name of the Relationship\nType for the Requirement assignment\u2019s relationship.</td>\n</tr>\n<tr class=\"even\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">property assignments</a></p></td>\n<td>An optional keyname providing property assignments for the\nrelationship.</td>\n</tr>\n<tr class=\"odd\">\n<td>interfaces</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#interface-assignment\">interface assignments</a></p></td>\n<td>The optional keyname providing Interface assignments for the\ncorresponding Interface definitions in the Relationship Type.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nRequirement assignments have one of the following grammars:\n\n###### Short notation:\n\nThe following single-line grammar may be used if only a concrete Node\nTemplate for the target node needs to be declared in the requirement:\n\n| \\<[requirement_name](#TYPE_YAML_STRING)\\>: \\<[node_template_name](#TYPE_YAML_STRING)\\> |\n|----------------------------------------------------------------------------------------|\n\n###### Extended notation:\n\nThe following grammar should be used if the requirement assignment needs\nto provide more information than just the Node Template name:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">requirement_name</a>&gt;:</p>\n<p>capability: &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_symbolic_name</a>&gt; | &lt;<a\nhref=\"#TYPE_YAML_STRING\">capability_type_name</a>&gt;</p>\n<p>node: &lt;<a href=\"#TYPE_YAML_STRING\">node_template_name</a>&gt; |\n&lt;<a href=\"#TYPE_YAML_STRING\">node_type_name</a>&gt;</p>\n<p>relationship: &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_template_name</a>&gt; | &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_type_name</a>&gt;</p>\n<p>node_filter: &lt;<a\nhref=\"#node-filter-definition\">node_filter_definition</a>&gt;</p>\n<p>count: &lt;<a href=\"#TYPE_YAML_INTEGER\">count</a>_value&gt;</p>\n<p>directives: &lt;directives_list&gt;</p>\n<p>optional: &lt;is_optional&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Extended grammar with Property Assignments and Interface Assignments for the relationship\n\nThe following additional multi-line grammar is provided for the\nrelationship keyname in order to provide new Property assignments and\nInterface assignments for the created relationship of the declared\nRelationship.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">requirement_name</a>&gt;:</p>\n<p># Other keynames omitted for brevity</p>\n<p>relationship:</p>\n<p>type: &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_template_name</a>&gt; | &lt;<a\nhref=\"#TYPE_YAML_STRING\">relationship_type_name</a>&gt;</p>\n<p>properties: &lt;<a\nhref=\"#property-assignment\">property_assignments</a>&gt;</p>\n<p>interfaces: &lt;<a\nhref=\"#interface-assignment\">interface_assignments</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Extended grammar with capacity allocation \n\nThe following additional multi-line grammar is provided for capacity\nallocation in the target capability. The property assignments under the\nallocation keyname represent \u201callocations\u201d from the property with the\nsame name in the target capability.\n\n- The sum of all the allocations for all requirements assignments for a\n  property in a target capability cannot exceed the value of that\n  property.\n\n- This means that during the deployment time of a certain service\n  template \u2013 as a certain requirement assignment is resolved \u2013 a\n  capability in a node is a valid target if\n\n- for each property of the target capability\n\n- the sum of all existing allocations plus the current allocation is\n  less_or_equal to the property value\n\n- Of course, allocations can be defined only for integer, float, or\n  scalar property types.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;requirement_name&gt;:</p>\n<p># Other keynames omitted for brevity</p>\n<p>allocation:</p>\n<p>properties: &lt;<a\nhref=\"#property-assignment\">allocation_property_assignments</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- requirement_name: represents the symbolic name of a requirement\n  assignment as a string.\n\n- capability_symbolic_name: represents the optional name of the\n  Capability definition within the target Node Type or Node Template;\n\n- if the capability in the Requirement definition was specified using\n  > the symbolic name of a capability definition in a target node type,\n  > then the capability keyname definition\n\n- <span class=\"comment-start\" id=\"633", "author": "Michael Rehder\"\n  > date=\"2020-12-15T13:10:00Z\">This is within an assignment so why\n  > would there be anything subsequent?</span>MUST remain unchanged in\n  > any subsequent refinements or during\n  > assignment.<span class=\"comment-end\" id=\"633\"></span>\n\n- if the capability in the Requirement definition was specified using\n  > the name of a Capability Type, then the Capability definition\n  > referred here by the capability_symbolic_name must be of a type that\n  > is the same as or derived from the said Capability Type in the\n  > Requirement definition.\n\n- capability_type_name: represents the optional name of a Capability\n  Type definition within the target Node Type or Node Template this\n  requirement needs to form a relationship with;\n\n- may not be used if the capability in the Requirement definition was\n  > specified using the symbolic name of a capability definition in a\n  > target node type.\n\n- otherwise the capability_type_name must be of a type that is the same\n  > as or derived from the type defined by the capability keyname in the\n  > Requirement definition.\n\n- node_template_name: represents the optional name of a Node Template\n  that contains the capability this requirement will be fulfilled by;\n\n- in addition, the Node Type of the Node Template must be of a type that\n  > is the same as or derived from the type defined by the node keyname\n  > (if the node keyname is defined) in the Requirement definition,\n\n- in addition, the Node Template must fulfill the node filter\n  > requirements of the node_filter (if a node_filter is defined) in the\n  > Requirement definition.\n\n- node_type_name: represents the optional name of a Node Type that\n  contains the capability this Requirement will be fulfilled by;\n\n- in addition, the node_type_name must be of a type that is the same as\n  > or derived from the type defined by the node keyname (if the node\n  > keyname is defined) in the Requirement definition.\n\n- relationship_template_name: represents the optional name of a\n  Relationship Template to be used when relating the Requirement to the\n  Capability in the target node.\n\n- in addition, the Relationship Type of the Relationship Template must\n  > be of a type that is the same as or derived from the type defined by\n  > the relationship keyname (if the relationship keyname is defined) in\n  > the Requirement definition.\n\n- relationship_type_name: represents the optional name of a Relationship\n  Type that is compatible with the Capability Type in the target node;\n  the TOSCA orchestrator will create a relationship of the Relationship\n  Type when relating the Requirement to the Capability in the target\n  node.\n\n- in addition, the relationship_type_name must be of a type that is the\n  > same as or derived from the type defined by the relationship keyname\n  > (if the relationship keyname is defined) in the Requirement\n  > definition.\n\n- property_assignments: within the relationship declaration, it\n  represents the optional map of property assignments for the declared\n  relationship.\n\n- interface_assignments: represents the optional map of interface\n  assignments for the declared relationship used to provide parameter\n  assignments on inputs and outputs of interfaces, operations and\n  notifications or changing the implementation definition.\n\n- allocation_property_assignments: within the allocation declaration, it\n  represents the optional map of property assignments that semantically\n  represent \u201callocations\u201d from the property with the same name in the\n  target capability. Syntactically their form is the same as for a\n  normal property assignments.\n\n- The allocation acts as a \u201ccapacity filter\u201d for the target capability\n  > in the target node. When the requirement is resolved, a capability\n  > in a node is a valid target for the requirement relationship if for\n  > each property of the target capability, the sum of all existing\n  > allocations plus the current allocation is less_or_equal to the\n  > property value.\n\n- Intuitively, the sum of \u201callocations\u201d from all the incoming\n  > relationships for a certain capability property cannot exceed the\n  > value of the property.\n\n- If the \u201callocation\u201d refers (via its name) to a property that does not\n  > exist in a capability, then that capability cannot be a valid\n  > target.\n\n- Of course, allocations can be defined only for integer, float, or\n  > scalar property types.\n\n- node_filter_definition: represents the optional node filter TOSCA\n  orchestrators will use to fulfill the requirement for selecting a\n  target node; if a node template was specified during requirement\n  assignment, the TOSCA orchestrator verifies that the specified node\n  template fulfills the node filter.\n\n- this node_filter does not replace the node_filter definition in the\n  > Requirement definition, it is applied in addition to that.\n\n- count_value: represents the optional cardinality of this requirement\n  assignment, that is how many relationships are to be established from\n  this requirement assignment specification.\n\n- If count is not defined, the assumed count_value for an assignment is\n  > 1.\n\n- Note that there can be multiple requirement assignments for a\n  > requirement with a specific symbolic name.\n\n- The sum of all count values of assignments for a requirement with a\n  > specific symbolic name must be within the count_range defined in the\n  > requirement definition.\n\n- Moreover, the sum of all count values of non-optional assignments for\n  > a requirement with a specific symbolic name must also be within the\n  > count_range defined in the requirement definition.\n\n- directives: represents the optional list of strings that defines\n  directives for this requirement assignment:\n\n- valid values for the strings:\n\n- \u201cinternal\u201d \u2013 relationship created by this requirement assignment use\n  > target nodes created within this template.\n\n- \u201cexternal\u201d \u2013 relationship created by this requirement assignment use\n  > target nodes created outside this template as available to the TOSCA\n  > environment.\n\n- the order of the strings in the list defines which directive should be\n  > attempted first when fulfilling the assignment.\n\n- If no directives are defined, the default value is left to the\n  > particular implementation.\n\n- is_optional: represents the optional boolean value specifying if this\n  requirement assignment is optional or not.\n\n- If is_optional is false, the assignment MUST be fulfilled.\n\n- If is_optional is true, the assignment SHOULD be fulfilled, but if not\n  > possible the service deployment is still considered valid.\n\n- The default value for is_optional is false.\n\n##### Notes\n\n- If no explicit requirement assignment for a requirement with symbolic\n  name is defined, a default requirement assignment with keynames:\n  capability, node, relationship, node_filter having the same values as\n  in the requirement definition in the corresponding node type is\n  assumed.\n\n- Additionally, the count_value is assumed to be equal to the min_count\n  > value of the requirement definition in the corresponding node type.\n\n- For all explicit requirement assignments with the same symbolic name:\n\n- the sum of the count_value must be within the count_range specified in\n  > the corresponding requirement definition.\n\n- the sum of the count_value for all non-optional requirements\n  > assignments must be within the count_range specified in the\n  > corresponding requirement definition.\n\n- Non-optional requirements have precedence, thus during a service\n  deployment, the optional requirements for all nodes should be resolved\n  only after the non-optional requirements for all nodes have been\n  resolved.\n\n##### Examples\n\nExamples of uses for the extended requirement assignment grammar\ninclude:\n\n- The need to allow runtime selection of the target node a Node Type\n  rather than a Node Template. This may include use of the node_filter\n  keyname to provide node and capability filtering information to find\n  the \u201cbest match\u201d of a node at runtime.\n\n- The need to further specify the Relationship Template or Relationship\n  Type to use when relating the source node\u2019s requirement to the target\n  node\u2019s capability.\n\n- The need to further specify the capability (symbolic) name or\n  Capability Type in the target node to form a relationship between.\n\n- The need to specify the number of counts the requirement assigns (when\n  greater than 1).\n\n###### Example 1 \u2013 Hosting requirement on a Node Type\n\nA web application node template named \u2018my_application_node_template\u2019 of\ntype WebApplication declares a requirement named \u2018host\u2019 that needs to be\nfulfilled by any node that derives from the node type WebServer.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p># Example of a requirement fulfilled by a specific web server\nnode template</p>\n<p>node_templates:</p>\n<p>my_application_node_template:</p>\n<p>type: tosca.nodes.WebApplication</p>\n<p>...</p>\n<p>requirements:</p>\n<p>- host:</p>\n<p>node: tosca.nodes.WebServer</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn this case, the node template\u2019s type is WebApplication which already\ndeclares the Relationship Type HostedOn to use to relate to the target\nnode and the Capability Type of Container to be the specific target of\nthe requirement in the target node.\n\n###### Example 2 - Requirement with Node Template and a custom Relationship Type\n\nThis example is similar to the previous example; however, the\nrequirement named \u2018database\u2019 describes a requirement for a connection to\na database endpoint (Endpoint.Database) Capability Type in a node\ntemplate (my_database). However, the connection requires a custom\nRelationship Type (my.types.CustomDbConnection\u2019) declared on the keyname\n\u2018relationship\u2019.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p># Example of a (database) requirement that is fulfilled by a node\ntemplate named</p>\n<p># \u201cmy_database\u201d, but also requires a custom database connection\nrelationship</p>\n<p>my_application_node_template:</p>\n<p>requirements:</p>\n<p>- database:</p>\n<p>node: my_database</p>\n<p>capability: Endpoint.Database</p>\n<p>relationship: my.types.CustomDbConnection</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Example 3 - Requirement for a Compute node with additional selection criteria (filter) \n\nThis example shows how to extend an abstract \u2018host\u2019 requirement for a\nCompute node with a filter definition that further constrains TOSCA\norchestrators to include additional properties and capabilities on the\ntarget node when fulfilling the requirement.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_templates:</p>\n<p>mysql:</p>\n<p>type: tosca.nodes.DBMS.MySQL</p>\n<p>properties:</p>\n<p># omitted here for brevity</p>\n<p>requirements:</p>\n<p>- host:</p>\n<p>node: tosca.nodes.Compute</p>\n<p>node_filter:</p>\n<p>capabilities:</p>\n<p>- host:</p>\n<p>properties:</p>\n<p>- num_cpus: { in_range: [ 1, 4 ] }</p>\n<p>- mem_size: { greater_or_equal: 512 MB }</p>\n<p>- os:</p>\n<p>properties:</p>\n<p>- architecture: { equal: x86_64 }</p>\n<p>- type: { equal: linux }</p>\n<p>- distribution: { equal: ubuntu }</p>\n<p>- mytypes.capabilities.compute.encryption:</p>\n<p>properties:</p>\n<p>- algorithm: { equal: aes }</p>\n<p>- keylength: { valid_values: [ 128, 256 ] }</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Example 4 - Requirement assignment for definition with count_range: \\[2,2\\]\n\nThis example shows how the assignments can look if the Requirement\ndefinition has the count_range different from the default \\[1,1\\]. In\nthis case the redundant_database requirement has count_range: \\[2,2\\].\nThe Requirement definition is not presented here for brevity. In the\nRequirement assignment we use the short notation. Note that the count\nkeyname for each assignment is not declared (i.e. the default value of 1\nis used) and that the sum of the count values of both assignments is 2\nwhich is in the range of \\[2,2\\] as specified in the Requirement\ndefinition.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p># Example of a (redundant_database) requirement that is fulfilled\nby</p>\n<p># two node templates named \u201cdatabase1\u201d and \u201cdatabase1</p>\n<p>my_critical_application_node_template:</p>\n<p>requirements:</p>\n<p>- redundant_database: database1</p>\n<p>- redundant_database: database2</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Example 5 - Requirement assignment for definition with capacity allocation\n\nThis example shows how the assignment can look if the requirement is\nassuming a \u201ccapacity allocation\u201d on the properties of the target\ncapability (in this case a capability of type\n\u201ctosca.capabilities.Compute\u201d). When this requirement is resolved, a node\nis a valid target and a relationship is created only if both the\ncapacity allocations for num_cpu and mem_size are fulfilled, that is the\nsum of the capacity allocations from all established relationships +\ncurrent allocation is less or equal to the value of each respective\nproperty in the target capability.\n\nSo assuming that num_cpu property in the target capability of a\ncandidate node has value 4 and the sum of capacity allocations of the\nother resolved requirements to that capability for num_cpu is 1 then\nthen there is enough \u201cremaining capacity\u201d (4 \u2013 1 = 3) to fulfill the\ncurrent allocation (2), and a relationship to that node is established.\nAnother node with num_cpu with value 2 could not be a valid target since\n1 (existing) + 2 (current) = 3, and that is larger than the property\nvalue which is 2. Of course, similar calculations must be done for the\nmem_size allocation.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p># Example of a (redundant_database) requirement that is fulfilled\nby</p>\n<p># two node templates named \u201cdatabase1\u201d and \u201cdatabase1</p>\n<p>my_critical_application_node_template:</p>\n<p>requirements:</p>\n<p>- host:</p>\n<p>node: tosca.nodes.Compute</p>\n<p>allocation:</p>\n<p>properties:</p>\n<p>num_cpu: 2</p>\n<p>mem_size: 128 MB</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n#### Node Filter definition\n\n##### Grammar\n\nNode filters are defines using condition clauses as shown in the\nfollowing grammar:\n\n| node_filter: \\<condition_clause\\> |\n|-----------------------------------|\n\nIn the above grammar, the condition_clause represents a Boolean\nexpression that will be used to select (filter) TOSCA nodes that are\nvalid candidates for fulfilling the requirement that defines the node\nfilter. TOSCA orchestrators use node filters are follows:\n\n- Orchestrators select an initial set of target node candidates based on\n  the target capability type and/or the target node type specified in\n  the requirement definition.\n\n- A node in this initial set is a valid target node candidate if\u2014when\n  that node is used as the target node for the requirement\u2014the node\n  filter condition clause evaluates to True.\n\n- Note that the context within which the node filter must be evaluated\n  is the relationship that is established to the target node as a result\n  of fulfilling the requirement. Specifically, this means that the SELF\n  keyword in any TOSCA Path expressions refer to that relationship.\n\n##### Example\n\nThe following example is a filter that will be used to select a Compute\nnode based upon the values of its defined capabilities. Specifically,\nthis filter will select Compute nodes that support a specific range of\nCPUs (i.e., num_cpus value between 1 and 4) and memory size (i.e.,\nmem_size of 2 or greater) from its declared \u201chost\u201d capability.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>my_node_template:</p>\n<p># other details omitted for brevity</p>\n<p>requirements:</p>\n<p>- host:</p>\n<p>node_filter:</p>\n<p>$and:</p>\n<p>- $in_range:</p>\n<p>- $get_property: [ SELF, CAPABILITY, num_cpus ]</p>\n<p>- [ 1, 4 ]</p>\n<p>- $greater_or_equal:</p>\n<p>- $get_property: [ SELF, CAPABILITY, mem_size ]</p>\n<p>- 512 MB</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Interfaces\n\n#### Interface Type\n\nAn Interface Type is a reusable entity that describes a set of\noperations that can be used to interact with or to manage a node or\nrelationship in a TOSCA topology.\n\n##### Keynames\n\nThe Interface Type is a TOSCA type entity and has the common keynames\nlisted in Section 4.2.5.2 Common keynames in type definitions. In\naddition, the Interface Type has the following recognized keynames:\n\n| Keyname       | Mandatory | Type                                                        | Description                                                                                             |\n|---------------|-----------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|\n| inputs        | no        | map of [parameter definitions](#parameter-definition)       | The optional map of input parameter definitions available to all operations defined for this interface. |\n| operations    | no        | map of [operation definitions](#operation-definition)       | The optional map of operations defined for this interface.                                              |\n| notifications | no        | map of [notification definitions](#notification-definition) | The optional map of notifications defined for this interface.                                           |\n\n##### Grammar\n\nInterface Types have following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">interface_type_name</a>&gt;:</p>\n<p>derived_from: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parent_interface_type_name</a>&gt;</p>\n<p>version: &lt;<a\nhref=\"#tosca-tal-suggests-removing-this.version\">version_number</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">interface_description</a>&gt;</p>\n<p>inputs:</p>\n<p>&lt;<a href=\"#parameter-definition\">parameter_definitions</a>&gt;</p>\n<p><span class=\"comment-start\" id=\"661\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-06-29T18:10:00Z\">Double-check all the examples to make\nsure \u2018operations\u2019 keyword is used everywhere</span>operations<span\nclass=\"comment-end\" id=\"661\"></span>:</p>\n<p>&lt;<a href=\"#operation-definition\">operation_definitions</a>&gt;</p>\n<p>notifications:</p>\n<p>&lt;<a href=\"#notification-definition\">Notification\ndefinition</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- interface_type_name: represents the mandatory name of the interface as\n  a string.\n\n- parent_interface_type_name: represents the name of the Interface Type\n  this Interface Type definition derives from (i.e. its \u201cparent\u201d type).\n\n- version_number: represents the optional TOSCA version number for the\n  Interface Type.\n\n- interface_description: represents the optional description for the\n  Interface Type.\n\n- parameter_definitions: represents the optional map of parameter\n  definitions which the TOSCA orchestrator will make available (i.e., or\n  pass) to all implementation artifacts for operations declared on the\n  interface during their execution.\n\n- operation_definitions: represents the optional map of one or more\n  operation definitions.\n\n- notification_definitions: represents the optional map of one or more\n  notification definitions.\n\n##### Derivation rules\n\nDuring Interface Type derivation the keyname definitions follow these\nrules:\n\n- inputs: existing parameter definitions may be refined; new parameter\n  definitions may be added.\n\n- operations: existing operation definitions may be refined; new\n  operation definitions may be added.\n\n- notifications: existing notification definitions may be refined; new\n  notification definitions may be added.\n\n##### Example\n\nThe following example shows a custom interface used to define multiple\nconfigure operations.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>mycompany.mytypes.myinterfaces.MyConfigure:</p>\n<p>derived_from: tosca.interfaces.relationship.Root</p>\n<p>description: My custom configure Interface Type</p>\n<p>inputs:</p>\n<p>mode:</p>\n<p>type: string</p>\n<p>operations:</p>\n<p>pre_configure_service:</p>\n<p>description: pre-configure operation for my service</p>\n<p>post_configure_service:</p>\n<p>description: post-configure operation for my service</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### Additional Requirements\n\n- Interface Types **MUST NOT** include any implementations for defined\n  operations or notifications; that is, the implementation keyname is\n  invalid in this context.\n\n#### Interface definition\n\nAn Interface definition defines an interface (containing operations and\nnotifications definitions) that can be associated with (i.e. defined\nwithin) a Node or Relationship Type definition (including Interface\ndefinitions in Requirements definitions). An Interface definition may be\nrefined in subsequent Node or Relationship Type derivations.\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA interface\ndefinition:\n\n<table>\n<colgroup>\n<col style=\"width: 12%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 15%\" />\n<col style=\"width: 59%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>yes</td>\n<td>string</td>\n<td>The mandatory name of the Interface Type this interface definition\nis based upon.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional description for this interface definition.</td>\n</tr>\n<tr class=\"odd\">\n<td>inputs</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#parameter-definition\">parameter definitions and\nrefinements</a></p></td>\n<td>The optional map of input parameter refinements and new input\nparameter definitions available to all operations defined for this\ninterface (the input parameters to be refined have been defined in the\nInterface Type definition).</td>\n</tr>\n<tr class=\"even\">\n<td>operations</td>\n<td>no</td>\n<td>map of <a href=\"#operation-definition\">operation\nrefinements</a></td>\n<td>The optional map of operations refinements for this interface. The\nreferred operations must have been defined in the Interface Type\ndefinition.</td>\n</tr>\n<tr class=\"odd\">\n<td>notifications</td>\n<td>no</td>\n<td>map of <a href=\"#notification-definition\">notification</a>\nrefinements</td>\n<td>The optional map of notifications refinements for this interface.\nThe referred operations must have been defined in the Interface Type\ndefinition.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nInterface definitions in Node or Relationship Type definitions have the\nfollowing grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">interface_definition_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">interface_type_name</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">interface_description</a>&gt;</p>\n<p>inputs:</p>\n<p>&lt;<a\nhref=\"#parameter-definition\">parameter_definitions_and_refinements</a>&gt;</p>\n<p>operations:</p>\n<p>&lt;<a href=\"#operation-definition\">operation_refinements</a>&gt;</p>\n<p>notifications:</p>\n<p>&lt;<a href=\"#notification-definition\">notification\ndefinition</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- interface_definition_name: represents the mandatory symbolic name of\n  the interface as a string.\n\n- interface_type_name: represents the mandatory name of the Interface\n  Type for the interface definition.\n\n- interface_description: represents the optional description string for\n  the interface.\n\n- parameter_definitions_and_refinements: represents the optional map of\n  input parameters which the TOSCA orchestrator will make available\n  (i.e. pass) to all defined operations. This means these parameters and\n  their values will be accessible to the implementation artifacts (e.g.,\n  scripts) associated to each operation during their execution\n\n- the map represents a mix of parameter refinements (for parameters\n  > already defined in the Interface Type) and new parameter\n  > definitions.\n\n- with the new parameter definitions, we can flexibly add new parameters\n  > when changing the implementation of operations and notifications\n  > during refinements or assignments.\n\n- operation_refinements: represents the optional map of operation\n  definition refinements for this interface; the referred operations\n  must have been previously defined in the Interface Type.\n\n- notification_refinements: represents the optional map of notification\n  definition refinements for this interface; the referred notifications\n  must have been previously defined in the Interface Type.\n\n##### Refinement rules\n\nAn interface definition within a node or relationship type (including\ninterface definitions in requirements definitions) uses the following\ndefinition refinement rules when the containing entity type is derived:\n\n- type: must be derived from (or the same as) the type in the interface\n  definition in the parent entity type definition.\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the interface definition in the parent entity type\n  definition.\n\n- inputs: not applicable to the definitions in the parent entity type\n  but to the definitions in the interface type referred by the type\n  keyname (see grammar above for the rules).\n\n- operations: not applicable to the definitions in the parent entity\n  type but to the definitions in the interface type referred by the type\n  keyname (see grammar above for the rules).\n\n- notifications: not applicable to the definitions in the parent entity\n  type but to the definitions in the interface type referred by the type\n  keyname (see grammar above for the rules).\n\n#### Interface assignment\n\nAn Interface assignment is used to specify assignments for the inputs,\noperations and notifications defined in the Interface. Interface\nassignments may be used within a Node or Relationship Template\ndefinition (including when Interface assignments are referenced as part\nof a Requirement assignment in a Node Template).\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA interface\ndefinition:\n\n| Keyname       | Mandatory | Type                                                              | Description                                                                                                                                                                          |\n|---------------|-----------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| inputs        | no        | map of [parameter value assignments](#parameter-value-assignment) | The optional map of input parameter assignments. Template authors MAY provide parameter assignments for interface inputs that are not defined in their corresponding Interface Type. |\n| operations    | no        | map of [operation assignme](#operation-definition)nts             | The optional map of operations assignments specified for this interface.                                                                                                             |\n| notifications | no        | map of [notification assignments](#notification-definition)       | The optional map of notifications assignments specified for this interface.                                                                                                          |\n\n##### Grammar\n\nInterface assignments have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a\nhref=\"#TYPE_YAML_STRING\">interface_definition_name</a>&gt;:</p>\n<p>inputs:</p>\n<p>&lt;<a\nhref=\"#parameter-value-assignment\">parameter_value_assignments</a>&gt;</p>\n<p>operations:</p>\n<p>&lt;<a href=\"#operation-definition\">operation_assignments</a>&gt;</p>\n<p>notifications:</p>\n<p>&lt;<a\nhref=\"#notification-definition\">notification_assignments</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- interface_definition_name: represents the mandatory symbolic name of\n  the interface as a string.\n\n- parameter_value_assignments: represents the optional map of parameter\n  value assignments for passing input parameter values to all interface\n  operations\n\n- template authors MAY provide new parameter assignments for interface\n  > inputs that are not defined in the Interface definition.\n\n- operation_assignments: represents the optional map of operation\n  assignments for operations defined in the Interface definition.\n\n- notification_assignments: represents the optional map of notification\n  assignments for notifications defined in the Interface definition.\n\n#### Operation definition\n\nAn operation definition defines a function or procedure to which an\noperation implementation can be bound.\n\nA new operation definition may be declared only inside interface type\ndefinitions (this is the only place where new operations can be\ndefined). In interface type, node type, or relationship type definitions\n(including operation definitions as part of a requirement definition) we\nmay further refine operations already defined in an interface type.\n\nAn operation definition or refinement inside an interface type\ndefinition may not contain an operation implementation definition and it\nmay not contain an attribute mapping as part of its output definition\n(as both these keynames are node/relationship specific).\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA operation\ndefinition (including definition refinement)\n\n<table>\n<colgroup>\n<col style=\"width: 24%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 15%\" />\n<col style=\"width: 48%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\"><span>string</span></a></td>\n<td>The optional description string for the associated operation.</td>\n</tr>\n<tr class=\"even\">\n<td>implementation</td>\n<td>no</td>\n<td><a\nhref=\"#operation-and-notification-implementation-definition\">operation\nimplementation definition</a></td>\n<td>The optional definition of the operation implementation. May not be\nused in an interface type definition (i.e. where an operation is\ninitially defined), but only during refinements.</td>\n</tr>\n<tr class=\"odd\">\n<td>inputs</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#parameter-definition\">parameter definitions</a></p></td>\n<td>The optional map of parameter definitions for operation input\nvalues.</td>\n</tr>\n<tr class=\"even\">\n<td>outputs</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#parameter-definition\">parameter definitions</a></p></td>\n<td><p>The optional map of parameter definitions for operation output\nvalues.</p>\n<p>Only as part of node and relationship type definitions, the output\ndefinitions may include mappings onto attributes of the node or\nrelationship type that contains the definition.</p></td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nOperation definitions have the following grammar:\n\n###### Short notation\n\nThe following single-line grammar may be used when the operation\u2019s\nimplementation definition is the only keyname that is needed, and when\nthe operation implementation definition itself can be specified using a\nsingle line grammar:\n\n| \\<[operation_name](#TYPE_YAML_STRING)\\>: \\<[operation_implementation_definition](# BKM_Implementation_Oper_Notif_Def)\\> |\n|-------------------------------------------------------------------------------------------------------------------------|\n\n###### Extended notation \n\nThe following multi-line grammar may be used when additional information\nabout the operation is needed:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">operation_name</a>&gt;:</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">operation_description</a>&gt;</p>\n<p>implementation: &lt;<a\nhref=\"#operation-and-notification-implementation-definition\">operation_implementation_definition</a>&gt;</p>\n<p>inputs:</p>\n<p>&lt;<a href=\"#parameter-definition\">parameter_definitions</a>&gt;</p>\n<p>outputs:</p>\n<p>&lt;<a\nhref=\"#parameter-definition\">parameter_definitions</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- operation_name: represents the mandatory symbolic name of the\n  operation as a string.\n\n- operation_description: represents the optional description string for\n  the operation.\n\n- operation_implementation_definition: represents the optional\n  specification of the operation\u2019s implementation).\n\n- parameter_definitions: represents the optional map of parameter\n  definitions which the TOSCA orchestrator will make available as inputs\n  to or receive as outputs from the corresponding implementation\n  artifact during its execution.\n\n##### Refinement rules\n\nAn operation definition within an interface, node, or relationship type\n(including interface definitions in requirements definitions) uses the\nfollowing refinement rules when the containing entity type is derived:\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the operation definition in the parent entity type\n  definition.\n\n- implementation: a new definition is unrestricted and will overwrite\n  the one inherited from the operation definition in the parent entity\n  type definition.\n\n- inputs: parameter definitions inherited from the parent entity type\n  may be refined; new parameter definitions may be added.\n\n- outputs: parameter definitions inherited from the parent entity type\n  may be refined; new parameter definitions may be added.\n\n##### Additional requirements\n\n- The definition of implementation is not allowed in interface type\n  definitions (as a node or node type context is missing at that point).\n  Thus, it can be part only of an operation refinement and not of the\n  original operation definition.\n\n- The default refinement behavior for implementations SHALL be\n  overwrite. That is, implementation definitions in a derived type\n  overwrite any defined in its parent type.\n\n- Defining a fixed value for an input parameter (as part of its\n  definition) may only use a parameter_value_expression that is\n  meaningful in the scope of the context. For example, within the\n  context of an Interface Type definition functions such as get_propery\n  or get_attribute cannot be used. Within the context of Node or\n  Relationship Type definitions, these functions may only reference\n  properties and attributes accessible starting from SELF (i.e.\n  accessing a node by symbolic name is not meaningful).\n\n- Defining attribute mapping as part of the output parameter definition\n  is not allowed in interface type definitions (i.e. as part of\n  operation definitions). It is allowed only in node and relationship\n  type definitions (as part of operation refinements) and has to be\n  meaningful in the scope of the context (e.g. SELF).\n\n- Implementation artifact file names (e.g., script filenames) may\n  include file directory path names that are relative to the TOSCA file\n  file itself when packaged within a TOSCA Cloud Service Archive (CSAR)\n  file.\n\n##### Examples\n\n###### Single-line example\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>interfaces:</p>\n<p>Standard:</p>\n<p>start: scripts/start_server.sh</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Multi-line example with shorthand implementation definitions\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>interfaces:</p>\n<p>Configure:</p>\n<p>pre_configure_source:</p>\n<p>implementation:</p>\n<p>primary: scripts/pre_configure_source.sh</p>\n<p>dependencies:</p>\n<p>- scripts/setup.sh</p>\n<p>- binaries/library.rpm</p>\n<p>- scripts/register.py</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Multi-line example with extended implementation definitions\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>interfaces:</p>\n<p>Configure:</p>\n<p>pre_configure_source:</p>\n<p>implementation:</p>\n<p>primary:</p>\n<p>file: scripts/pre_configure_source.sh</p>\n<p>type: tosca.artifacts.Implementation.Bash</p>\n<p>repository: my_service_catalog</p>\n<p>dependencies:</p>\n<p>- file\u00a0: scripts/setup.sh</p>\n<p>type\u00a0: tosca.artifacts.Implementation.Bash</p>\n<p>repository\u00a0: my_service_catalog</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n#### Operation assignment\n\nAn operation assignment may be used to assign values for input\nparameters, specify attribute mappings for output parameters, and\ndefine/redefine the implementation definition of an already defined\noperation in the interface definition. An operation assignment may be\nused inside interface assignments inside node template or relationship\ntemplate definitions (this includes when operation assignments are part\nof a requirement assignment in a node template).\n\nAn operation assignment may add or change the implementation and\ndescription definition of the operation. Assigning a value to an input\nparameter that had a fixed value specified during operation definition\nor refinement is not allowed. Providing an attribute mapping for an\noutput parameter that was mapped during an operation refinement is also\nnot allowed.\n\nNote also that in the operation assignment we can use inputs and outputs\nthat have not been previously defined in the operation definition. This\nis equivalent to an ad-hoc definition of a parameter, where the type is\ninferred from the assigned value (for input parameters) or from the\nattribute to map to (for output parameters).\n\n##### Keynames\n\nThe following is the list of recognized keynames for an operation\nassignment:\n\n<table>\n<colgroup>\n<col style=\"width: 21%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 19%\" />\n<col style=\"width: 46%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>implementation</td>\n<td>no</td>\n<td><a\nhref=\"#operation-and-notification-implementation-definition\">operation\nimplementation definition</a></td>\n<td>The optional definition of the operation implementation. Overrides\nimplementation provided at operation definition.</td>\n</tr>\n<tr class=\"even\">\n<td>inputs</td>\n<td>no</td>\n<td>map of <a href=\"#parameter-value-assignment\">parameter value\nassignments</a></td>\n<td>The optional map of parameter value assignments for assigning values\nto operation inputs.</td>\n</tr>\n<tr class=\"odd\">\n<td>outputs</td>\n<td>no</td>\n<td><p>map of <a href=\"\\l\">parameter</a></p>\n<p><a href=\"\\l\">mapping assignments</a></p></td>\n<td>The optional map of parameter mapping assignments that specify how\noperation outputs are mapped onto attributes of the node or relationship\nthat contains the operation definition.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nOperation assignments have the following grammar:\n\n###### Short notation\n\nThe following single-line grammar may be used when the operation\u2019s\nimplementation definition is the only keyname that is needed, and when\nthe operation implementation definition itself can be specified using a\nsingle line grammar:\n\n| \\<[operation_name](#TYPE_YAML_STRING)\\>: \\<[operation_implementation_definition](#operation-and-notification-implementation-definition)\\> |\n|-------------------------------------------------------------------------------------------------------------------------------------------|\n\n###### Extended notation\n\nThe following multi-line grammar may be used in Node or Relationship\nTemplate definitions when additional information about the operation is\nneeded:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">operation_name</a>&gt;:</p>\n<p>implementation: &lt;<a\nhref=\"#operation-and-notification-implementation-definition\">operation_implementation_definition</a>&gt;</p>\n<p>inputs:</p>\n<p>&lt;<a\nhref=\"#parameter-value-assignment\">parameter_value_assignments</a>&gt;</p>\n<p>outputs:</p>\n<p>&lt;<a\nhref=\"#parameter-mapping-assignment\">parameter_mapping_assignments</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- operation_name: represents the mandatory symbolic name of the\n  operation as a [string](#TYPE_YAML_STRING).\n\n- operation_implementation_definition: represents the optional\n  specification of the operation\u2019s implementation\n\n- the implementation declared here overrides the implementation provided\n  > at operation definition.\n\n- parameter_value_assignments: represents the optional map of parameter\n  value assignments for passing input parameter values to operations.\n\n- assignments for operation inputs that are not defined in the operation\n  > definition may be provided\n\n- parameter_mapping_assignments: represents the optional map of\n  parameter mapping assignments that consists of named output values\n  returned by operation implementations (i.e. artifacts) and associated\n  attributes into which this output value must be stored\n\n- assignments for operation outputs that are not defined in the\n  > operation definition may be provided.\n\n##### Additional requirements\n\n- The behavior for implementation of operations SHALL be override. That\n  is, implementation definitions assigned in an operation assignment\n  override any defined in the operation definition.\n\n- Template authors MAY provide parameter assignments for operation\n  inputs that are not defined in the operation definition.\n\n- Template authors MAY provide attribute mappings for operation outputs\n  that are not defined in the operation definition.\n\n- Implementation artifact file names (e.g., script filenames) may\n  include file directory path names that are relative to the TOSCA file\n  file itself when packaged within a TOSCA Cloud Service Archive (CSAR)\n  file.\n\n##### Examples\n\nTBD\n\n#### Notification definition\n\nA notification definition defines an asynchronous notification or\nincoming message that can be associated with an interface. The\nnotification is a way for an external event to be transmitted to the\nTOSCA orchestrator. Values can be sent with a notification as\nnotification outputs and we can map them to node/relationship attributes\nsimilarly to the way operation outputs are mapped to attributes. The\nartifact that the orchestrator is registering with in order to receive\nthe notification is specified using the implementation keyname in a\nsimilar way to operations. <span class=\"comment-start\" id=\"723\"\nauthor=\"Chris Lauwers [2]", "date": "2019-09-05T21:51:00Z", "comment": "I think\nnotifications DO need inputs (in order to provide information about the\nexternal system they\u2019re monitoring)", "target": "As opposed to an operation\ndefinition, a notification definition does not include an inputs keyname\nsince notifications are not invoked from the\norchestrator."}-->


When the notification is received an event is generated within the
orchestrator that can be associated to triggers in policies to call
other internal operations and workflows. The notification name (using
the \<interface_name\>.\<notification_name\> notation) itself identifies
the event type that is generated and can be textually used when defining
the associated triggers.

A notification definition may be used only inside interface type
definitions (this is the only place where new notifications can be
defined). Inside interface type, node type, or relationship type
definitions (including notifications definitions as part of a
requirement definition) we may further refine a notification already
defined in the interface type.

A notification definition or refinement inside an interface type
definition may not contain a notification implementation definition and
it may not contain an attribute mapping as part of its output definition
(as both these keynames are node/relationship specific).

##### Keynames

The following is the list of recognized keynames for a TOSCA
notification definition:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING"><span>string</span></a></td>
<td>The optional description string for the associated
notification.</td>
</tr>
<tr class="even">
<td>implementation</td>
<td>no</td>
<td><a
href="#operation-and-notification-implementation-definition">notification
implementation definition</a></td>
<td>The optional definition of the notification implementation.</td>
</tr>
<tr class="odd">
<td>outputs</td>
<td>no</td>
<td>map of parameter definitions</td>
<td><p>The optional map of parameter definitions that specify
notification output values.</p>
<p>Only as part of node and relationship type definitions, the output
definitions may include their mappings onto attributes of the node type
or relationship type that contains the definition.</p></td>
</tr>
</tbody>
</table>

##### Grammar

Notification definitions have the following grammar:

###### Short notation

The following single-line grammar may be used when the notification’s
implementation definition is the only keyname that is needed and when
the notification implementation definition itself can be specified using
a single line grammar:

| \<[notification_name](#TYPE_YAML_STRING)\>: \<[notification_implementation_definition](#operation-and-notification-implementation-definition)\> |
|-------------------------------------------------------------------------------------------------------------------------------------------------|

###### Extended notation 

The following multi-line grammar may be used when additional information
about the notification is needed:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;notification_name&gt;:</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">notification_description</a>&gt;</p>
<p>implementation: &lt;<a
href="#operation-and-notification-implementation-definition">notification_implementation_definition</a>&gt;</p>
<p>outputs:</p>
<p>&lt;<a
href="#parameter-definition">parameter_definitions</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- notification_name: represents the mandatory symbolic name of the
  notification as a string.

- notification_description: represents the optional description string
  for the notification.

- notification_implementation_definition: represents the optional
  specification of the notification implementation (i.e. the external
  artifact that may send notifications)

- parameter_definitions: represents the optional map of parameter
  definitions for parameters that the orchestrator will receive as
  outputs from the corresponding implementation artifact during its
  execution.

##### Refinement rules

A notification definition within an interface, node, or relationship
type (including interface definitions in requirements definitions) uses
the following refinement rules when the containing entity type is
derived:

- description: a new definition is unrestricted and will overwrite the
  one inherited from the notification definition in the parent entity
  type definition.

- implementation: a new definition is unrestricted and will overwrite
  the one inherited from the notification definition in the parent
  entity type definition.

- outputs: parameter definitions inherited from the parent entity type
  may be refined; new parameter definitions may be added.

##### Additional requirements

- The definition of implementation is not allowed in interface type
  definitions (as a node or node type context is missing at that point).
  Thus, it can be part only of a notification refinement and not of the
  original notification definition.

- The default sub-classing (i.e. refinement) behavior for
  implementations of notifications SHALL be overwrite. That is,
  implementation artifacts definitions in a derived type overwrite any
  defined in its parent type.

- Defining attribute mapping as part of the output parameter definition
  is not allowed in interface type definitions (i.e. as part of
  operation definitions). It is allowed only in node and relationship
  type definitions (as part of operation refinements).

- Defining a mapping in an output parameter definition may use an
  attribute target that is meaningful in the scope of the context.
  Within the context of Node or Relationship Type definitions these
  functions may only reference attributes starting from the same node
  (i.e. SELF).

- Implementation artifact file names (e.g., script filenames) may
  include file directory path names that are relative to the TOSCA file
  file itself when packaged within a TOSCA Cloud Service Archive (CSAR)
  file.

##### Examples

TBD

#### Notification assignment

A notification assignment may be used to specify attribute mappings for
output parameters and to define/redefine the implementation definition
and description definition of an already defined notification in the
interface definition. A notification assignment may be used inside
interface assignments inside node or relationship template definitions
(this includes when notification assignments are part of a requirement
assignment in a node template).

Providing an attribute mapping for an output parameter that was mapped
during a previous refinement is not allowed. Note also that in the
notification assignment we can use outputs that have not been previously
defined in the operation definition. This is equivalent to an ad-hoc
definition of an output parameter, where the type is inferred from the
attribute to map to.

##### Keynames

The following is the list of recognized keynames for a TOSCA
notification assignment:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>implementation</td>
<td>no</td>
<td><a
href="#operation-and-notification-implementation-definition">notification
implementation definition</a></td>
<td>The optional definition of the notification implementation.
Overrides implementation provided at notification definition.</td>
</tr>
<tr class="even">
<td>outputs</td>
<td>no</td>
<td><p>map of <a href="\l">parameter</a></p>
<p><a href="\l">mapping assignments</a></p></td>
<td>The optional map of parameter mapping assignments that specify how
notification outputs values are mapped onto attributes of the node or
relationship type that contains the notification definition.</td>
</tr>
</tbody>
</table>

##### Grammar

Notification assignments have the following grammar:

###### Short notation

The following single-line grammar may be used when the notification’s
implementation definition is the only keyname that is needed, and when
the notification implementation definition itself can be specified using
a single line grammar:

| \<[notification_name](#TYPE_YAML_STRING)\>: \<[notification_implementation_definition](#operation-and-notification-implementation-definition)\> |
|-------------------------------------------------------------------------------------------------------------------------------------------------|

###### Extended notation

The following multi-line grammar may be used in Node or Relationship
Template definitions when additional information about the notification
is needed:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">notification_name</a>&gt;:</p>
<p>implementation: &lt;<a
href="#operation-and-notification-implementation-definition">notification_implementation_definition</a>&gt;</p>
<p>outputs:</p>
<p>&lt;<a
href="#parameter-mapping-assignment">parameter_mapping_assignments</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- notification_name: represents the mandatory symbolic name of the
  notification as a string.

- notification_implementation_definition: represents the optional
  specification of the notification implementation (i.e. the external
  artifact that is may send notifications)

- the implementation declared here overrides the implementation provided
  > at notification definition.

- parameter_mapping_assignments: represents the optional map of
  parameter_mapping_assignments that consists of named output values
  returned by operation implementations (i.e. artifacts) and associated
  attributes into which this output value must be stored

- assignments for notification outputs that are not defined in the
  > operation definition may be provided.

##### Additional requirements

- The behavior for implementation of notifications SHALL be override.
  That is, implementation definitions assigned in a notification
  assignment override any defined in the notification definition.

- Template authors MAY provide attribute mappings for notification
  outputs that are not defined in the corresponding notification
  definition.

- Implementation artifact file names (e.g., script filenames) may
  include file directory path names that are relative to the TOSCA file
  file itself when packaged within a TOSCA Cloud Service Archive (CSAR)
  file.

##### Examples

TBD

#### Operation and notification implementation definition

An operation implementation definition specifies one or more artifacts
(e.g. scripts) to be used as the implementation for an operation in an
interface.

A notification implementation definition specifies one or more artifacts
to be used by the orchestrator to subscribe and receive a particular
notification (i.e. the artifact implements the notification).

The operation implementation definition and the notification
implementation definition share the same keynames and grammar, with the
exception of the timeout keyname that has no meaning in the context of a
notification implementation definition and should not be used in such.

##### Keynames

The following is the list of recognized keynames for an operation
implementation definition or a notification implementation definition:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>primary</td>
<td>no</td>
<td><a href="#artifact-definition">artifact definition</a></td>
<td>The optional implementation artifact (i.e., the primary script file
within a TOSCA CSAR file).</td>
</tr>
<tr class="even">
<td>dependencies</td>
<td>no</td>
<td><p>list of</p>
<p><a href="#artifact-definition">artifact definition</a></p></td>
<td><p>The optional list of one or more dependent or secondary
implementation artifacts which are referenced by the primary
implementation artifact (e.g., a library the script installs or a</p>
<p>secondary script).</p></td>
</tr>
<tr class="odd">
<td>1
<!----
{"id": "757\" data-author=\"Calin Curescu\"\ndata-date=\"2020-06-02T16:46:00Z\">Let\u2019s ask Thinh if there is any valid\nreason to keep the timeout as a \u201cexecution directive\u201d for the\norchestrator. The people present in WG meeting on 2020-06-02 did not\nthink that.</span>timeout</td>\n<td>no</td>\n<td>integer</td>\n<td>Timeout value in seconds. Has no meaning and should not be used\nwithin a notification implementation definition.<span\nclass=\"comment-end\" id=\"757\"></span></td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nOperation implementation definitions and notification implementation\ndefinitions have the following grammar:\n\n###### Short notation for use with single artifact\n\nThe following single-line grammar may be used when only a primary\nimplementation artifact name is needed:\n\n| [implementation](#TYPE_YAML_STRING): \\<[primary_artifact_name](#TYPE_YAML_STRING)\\> |\n|-------------------------------------------------------------------------------------|\n\nThis notation can be used when the primary artifact name uniquely\nidentifies the artifact, either because it refers to an artifact\nspecified in the artifacts section of a type or template, or because it\nrepresents the name of a script in the CSAR file that contains the\ndefinition.\n\n###### Short notation for use with multiple artifacts\n\nThe following multi-line short-hand grammar may be used when multiple\nartifacts are needed, but each of the artifacts can be uniquely\nidentified by name as before:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>implementation:</p>\n<p>primary: &lt;<a\nhref=\"#TYPE_YAML_STRING\">primary_artifact_name</a>&gt;</p>\n<p>dependencies:</p>\n<p>- &lt;<a\nhref=\"#TYPE_YAML_STRING\">list_of_dependent_artifact_names</a>&gt;</p>\n<p>timeout: 60</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Extended notation for use with single artifact\n\nThe following multi-line grammar may be used in Node or Relationship\nType or Template definitions when only a single artifact is used but\nadditional information about the primary artifact is needed (e.g. to\nspecify the repository from which to obtain the artifact, or to specify\nthe artifact type when it cannot be derived from the artifact file\nextension):\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>implementation:</p>\n<p>primary:</p>\n<p>&lt;<a\nhref=\"#artifact-definition\">primary_artifact_definition</a>&gt;</p>\n<p>timeout: 100</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n###### Extended notation for use with multiple artifacts\n\nThe following multi-line grammar may be used in Node or Relationship\nType or Template definitions when there are multiple artifacts that may\nbe needed for the operation to be implemented and additional information\nabout each of the artifacts is required:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>implementation:</p>\n<p>primary:</p>\n<p>&lt;<a\nhref=\"#artifact-definition\">primary_artifact_definition</a>&gt;</p>\n<p>dependencies:</p>\n<p>- &lt;<a href=\"#artifact-definition\">list_of_dependent_artifact\ndefinitions</a>&gt;</p>\n<p>timeout: 120</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- primary_artifact_name: represents the optional name\n  ([string](#TYPE_YAML_STRING)) of an implementation artifact definition\n  (defined elsewhere), or the direct name of an implementation\n  artifact\u2019s relative filename (e.g., a service template-relative,\n  path-inclusive filename or absolute file location using a URL).\n\n- primary_artifact_definition: represents a full inline definition of an\n  implementation artifact.\n\n- list_of_dependent_artifact_names: represents the optional ordered list\n  of one or more dependent or secondary implementation artifact names\n  (as strings) which are referenced by the primary implementation\n  artifact. TOSCA orchestrators will copy these files to the same\n  location as the primary artifact on the target node so as to make them\n  accessible to the primary implementation artifact when it is executed.\n\n- list_of_dependent_artifact_definitions: represents the ordered list of\n  one or more inline definitions of dependent or secondary\n  implementation artifacts. TOSCA orchestrators will copy these\n  artifacts to the same location as the primary artifact on the target\n  node so as to make them accessible to the primary implementation\n  artifact when it is executed.\n\n### Artifacts\n\n#### Artifact Type\n\nAn Artifact Type is a reusable entity that defines the type of one or\nmore files that are used to define implementation or deployment\nartifacts that are referenced by nodes or relationships.\n\n##### Keynames\n\nThe Artifact Type is a TOSCA type entity and has the common keynames\nlisted in Section 4.2.5.2 Common keynames in type definitions. In\naddition, the Artifact Type has the following recognized keynames:\n\n<table>\n<colgroup>\n<col style=\"width: 19%\" />\n<col style=\"width: 24%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 43%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"775\" data-author=\"Calin Curescu\"\ndata-date=\"2020-05-04T15:06:00Z\">Tal proposes to make it a list of\nstring to cover several mime-types, but maybe this is not needed since\nit can be freely changed in the derived types and a certain specific\nfile cannot have two mime-types at the same time,\nno?</span>mime_type<span class=\"comment-end\" id=\"775\"></span></td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional mime type property for the Artifact Type.</td>\n</tr>\n<tr class=\"even\">\n<td>file_ext</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional file extension property for the Artifact Type.</td>\n</tr>\n<tr class=\"odd\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#_Schema_Definition\">property definitions</a></p></td>\n<td>An optional map of property definitions for the Artifact Type.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nArtifact Types have following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">artifact_type_name</a>&gt;:</p>\n<p>derived_from: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parent_artifact_type_name</a>&gt;</p>\n<p>version: &lt;<a\nhref=\"#tosca-tal-suggests-removing-this.version\">version_number</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">artifact_description</a>&gt;</p>\n<p>mime_type: &lt;<a\nhref=\"#TYPE_YAML_STRING\">mime_type_string</a>&gt;</p>\n<p>file_ext: [ &lt;<a href=\"#TYPE_YAML_STRING\">file_extensions</a>&gt;\n]</p>\n<p>properties:</p>\n<p>&lt;<a\nhref=\"#_Schema_Definition\">property_definitions</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- artifact_type_name: represents the name of the Artifact Type being\n  declared as a string.\n\n- parent_artifact_type_name: represents the name of the Artifact Type\n  this Artifact Type definition derives from (i.e., its \u201cparent\u201d type).\n\n- version_number: represents the optional TOSCA version number for the\n  Artifact Type.\n\n- artifact_description: represents the optional description string for\n  the Artifact Type.\n\n- mime_type_string: represents the optional Multipurpose Internet Mail\n  Extensions (MIME) standard string value that describes the file\n  contents for this type of Artifact Type as a string.\n\n- file_extensions: represents the optional list of one or more\n  recognized file extensions for this type of artifact type as strings.\n\n- property_definitions: represents the optional map of property\n  definitions for the artifact type.\n\n##### Derivation rules\n\nDuring Artifact Type derivation the keyname definitions follow these\nrules:\n\n- mime_type: a new definition is unrestricted and will overwrite the one\n  inherited from the parent type.\n\n- file_ext: a new definition is unrestricted and will overwrite the one\n  inherited from the parent type.\n\n- properties: existing property definitions may be refined; new property\n  definitions may be added.\n\n##### Examples\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>my_artifact_type:</p>\n<p>description: Java Archive artifact type</p>\n<p>derived_from: tosca.artifact.Root</p>\n<p>mime_type: application/java-archive</p>\n<p>file_ext: [ jar ]</p>\n<p>properties:</p>\n<p>id:</p>\n<p>description: Identifier of the jar</p>\n<p>type: string</p>\n<p>required: true</p>\n<p>creator:</p>\n<p>description: Vendor of the java implementation on which the jar is\nbased</p>\n<p>type: string</p>\n<p>required: false</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n##### Additional Requirements\n\n- The \u2018mime_type\u2019 keyname is meant to have values that are Apache mime\n  types such as those defined here:\n  <http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types>\n\n##### Notes\n\nInformation about artifacts can be broadly classified in two categories\nthat serve different purposes:\n\n- Selection of artifact processor. This category includes informational\n  elements such as artifact version, checksum, checksum algorithm etc.\n  and s used by TOSCA Orchestrator to select the correct artifact\n  processor for the artifact. These informational elements are captured\n  in TOSCA as keywords for the artifact.\n\n- Properties processed by artifact processor. Some properties are not\n  processed by the Orchestrator but passed on to the artifact processor\n  to assist with proper processing of the artifact. These informational\n  elements are described through artifact properties.\n\n#### Artifact definition\n\nAn artifact definition defines a named, typed file that can be\nassociated with Node Type or Node Template and used by orchestration\nengine to facilitate deployment and implementation of interface\noperations.\n\n##### Keynames\n\nThe following is the list of recognized keynames for a TOSCA artifact\ndefinition when using the extended notation:\n\n<table>\n<colgroup>\n<col style=\"width: 18%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 56%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The mandatory artifact type for the artifact definition.</td>\n</tr>\n<tr class=\"even\">\n<td>file</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The mandatory URI string (relative or absolute) which can be used to\nlocate the artifact\u2019s file.</td>\n</tr>\n<tr class=\"odd\">\n<td>repository</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional name of the repository definition which contains the\nlocation of the external repository that contains the artifact. The\nartifact is expected to be referenceable by its file URI within the\nrepository.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional description for the artifact definition.</td>\n</tr>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"791\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-06-29T18:45:00Z\">Remove and suggest that property should\nbe used instead?</span>deploy_path</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The file path the associated file will be deployed on within the\ntarget node\u2019s container. <span class=\"comment-end\" id=\"791\"></span></td>\n</tr>\n<tr class=\"even\">\n<td>artifact_version</td>\n<td>no</td>\n<td>string</td>\n<td>The version of this artifact. One use of this artifact_version is to\ndeclare the particular version of this artifact type, in addition to its\nmime_type (that is declared in the artifact type definition). Together\nwith the mime_type it may be used to select a particular artifact\nprocessor for this artifact. For example, a python interpreter that can\ninterpret python version 2.7.0.</td>\n</tr>\n<tr class=\"odd\">\n<td>checksum</td>\n<td>no</td>\n<td>string</td>\n<td>The checksum used to validate the integrity of the artifact.</td>\n</tr>\n<tr class=\"even\">\n<td>checksum_algorithm</td>\n<td>no</td>\n<td>string</td>\n<td>Algorithm used to calculate the artifact checksum (e.g. MD5, SHA\n<mark>[Ref]).</mark> Shall be specified if checksum is specified for an\nartifact.</td>\n</tr>\n<tr class=\"odd\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">property</a></p>\n<p>assignments</p></td>\n<td>The optional map of property assignments associated with the\nartifact.</td>\n</tr>\n</tbody>\n</table>\n\n##### Grammar\n\nArtifact definitions have one of the following grammars:\n\n###### Short notation\n\nThe following single-line grammar may be used when the artifact\u2019s type\nand mime type can be inferred from the file URI:\n\n| \\<[artifact_name](#TYPE_YAML_STRING)\\>: \\<[artifact_file_URI](#TYPE_YAML_STRING)\\> |\n|------------------------------------------------------------------------------------|\n\n###### Extended notation:\n\nThe following multi-line grammar may be used when the artifact\u2019s\ndefinition\u2019s type and mime type need to be explicitly declared:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">artifact_name</a>&gt;:</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">artifact_description</a>&gt;</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">artifact_type_name</a>&gt;</p>\n<p>file: &lt;<a href=\"#TYPE_YAML_STRING\">artifact_file_URI</a>&gt;</p>\n<p>repository: &lt;<a\nhref=\"#TYPE_YAML_STRING\">artifact_repository_name</a>&gt;</p>\n<p>deploy_path: &lt;<a\nhref=\"#TYPE_YAML_STRING\">file_deployment_path</a>&gt;</p>\n<p>version: &lt;artifact _version&gt;</p>\n<p>checksum: &lt;artifact_checksum&gt;</p>\n<p>checksum_algorithm: &lt;artifact_checksum_algorithm&gt;</p>\n<p>properties: &lt;property assignments&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammars, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- artifact_name: represents the mandatory symbolic name of the artifact\n  as a string.\n\n- artifact_description: represents the optional description for the\n  artifact.\n\n- artifact_type_name: represents the mandatory artifact type the\n  artifact definition is based upon.\n\n- artifact_file_URI: represents the mandatory URI string (relative or\n  absolute) which can be used to locate the artifact\u2019s file.\n\n- artifact_repository_name: represents the optional name of the\n  repository definition to use to retrieve the associated artifact\n  (file) from.\n\n- file_deployement_path: represents the optional path the\n  artifact_file_URI will be copied into within the target node\u2019s\n  container.\n\n- artifact_version: represents the version of artifact\n\n- artifact_checksum: represents the checksum of the Artifact\n\n- artifact_checksum_algorithm:represents the algorithm for verifying the\n  checksum. Shall be specified if checksum is specified\n\n- properties: represents an optional map of property assignments\n  associated with the artifact\n\n##### Refinement rules\n\nArtifact definitions represent specific external entities. If a certain\nartifact definition cannot be reused as is, then it may be completely\nredefined.\n\n- If an artifact is redefined, the symbolic name from the definition in\n  the parent node type is reused, but no keyname definitions are\n  inherited from the definition in the parent node type, and the new\n  definition completely overwrites the definition in the parent.\n\n- If the artifact is not redefined the complete definition is inherited\n  from the parent node type.\n\n##### Examples\n\nThe following represents an artifact definition:\n\n| my_file_artifact: ../my_apps_files/operation_artifact.txt |\n|-----------------------------------------------------------|\n\nThe following example represents an artifact definition with property\nassignments:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>artifacts:</p>\n<p>sw_image:</p>\n<p>description: Image for virtual machine</p>\n<p>type: tosca.artifacts.Deployment.Image.VM</p>\n<p>file: <a\nhref=\"http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2\">http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2</a></p>\n<p>checksum: ba411cafee2f0f702572369da0b765e2</p>\n<p>version: 3.2</p>\n<p>checksum_algorithm: MD5</p>\n<p>properties:</p>\n<p>name: vSRX</p>\n<p>container_format: BARE</p>\n<p>disk_format: QCOW2</p>\n<p>min_disk: 1 GB</p>\n<p>size: 649 MB</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nProperties, Attributes, and Parameters\n--------------------------------------\n\nThis section presents handling data in TOSCA via properties, attributes,\nand parameters.\n\nThe type of the values they contain can be divided into built-in\nprimitive types, special types that are extensions of the primitive\ntypes, and collection types, as well as user-defined refinements of\nthese and complex data types that can themselves be defined in TOSCA\nprofiles and the TOSCA file.\n\nValues can also be evaluated from expressions based on TOSCA functions.\n\\[See XXX\\]\n\nThe following table summarizes the built-in types. All of these type\nnames are reserved and cannot be used for custom data types. Note,\nhowever, that it is possible to derive a custom data type from a\nprimitive type in order to add validation clauses.\n\nPrimitive Types: (section 4.4.<span class=\"comment-start\" id=\"803", "author": "Chris Lauwers", "date": "2020-08-04T16:23:00Z", "comment": "Include cross\nreferences", "target": "1"}-->
)

- string

- integer

- float

- boolean

- bytes

- nil

Special Types: (section 4.4.2)

- range

- timestamp

- scalar-unit.size

- scalar-unit.time

- scalar-unit.frequency

- scalar-unit.bitrate

Collection Types: (section 4.4.3)

- list

- map

Notes that were originally in the metadata section:

Important notes:

YAML map keys can be any value, not just strings. TOSCA metadata grammar
allows that full YAML expressiveness and does not add additional
restrictions beyond requiring correct YAM syntax.

YAML does not specify the bit width of integers and floats but suggests
that 32 bits should be acceptable.

Users should be careful about the difference between parsing floats and
integers. If they explicitly want a float, they should add ".0".

Users should be careful with version strings being parsed as floats.
E.g., "3.2" is a float but "3.2.1" is a string,

### Primitive Types

The TOSCA primitive types have been specified to allow for the broadest
possible support for implementations.

Guiding principles:

1.  Because TOSCA files are written in YAML they must support all the
    literal primitives in YAML. However, it is important to also allow
    for consistency of representation of external data, e.g. service
    template inputs and outputs, property and attribute values stored in
    a database, etc.

<!-- -->

8.  Adherence to 64-bit precision to ensure portability of numeric data.

9.  TOSCA parsers *shall not* automatically convert between primitive
    types. Thus, care should be taken to use the correct YAML notation
    for that type. Details will be provided below.

#### string

An array of Unicode runes. (For storing an arbitrary array of bytes see
the “bytes” type, below.)

Because we adhere to 64-bit precision, the minimum length of strings is
0 and the maximum length of strings is 4,294,967,295.

TOSCA *does not* specify a character encoding. For example, a string
could be encoded as UTF-8 or UTF-16. The exact encoding used depends on
the implementation.

Be aware that YAML parsers will attempt to parse unquoted character
sequences as other types (booleans, integers, floats, etc.) *before*
falling back to the !!string type. For example, the unquoted sequence
“0.1” would be interpreted as a YAML !!float. Likewise, the unquoted
sequence “nan” would become the !!float value of not-a-number. However,
in TOSCA a string value *must* be specified in YAML as a !!string.

A TOSCA parser *shall not* attempt to convert other primitive types to
strings if a string type is required. This requirement is necessary for
ensuring portability, because there is no single, standard
representation for the other types, e.g. scientific notations for
decimals, the words “true” vs. “True” for booleans, etc. In YAML users
should thus add quotation marks around literal strings that YAML would
otherwise interpret as other types.

This following example would be invalid if there were no quotation marks
around “0.1”:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Node:</p>
<p>properties:</p>
<p>name:</p>
<p>type: string</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>node:</p>
<p>type: Node</p>
<p>properties:</p>
<p>name: "0.1"</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes
<!----
{"id": "807", "author": "Chris Lauwers", "date": "2020-08-18T23:01:00Z", "comment": "(From Tal): Do we want the comparison constraints to work for strings? E.g. should \"greater_than\" do a sorting-based comparison? I'll just point that it is non-trivial to sort Unicode strings. The most common way is to use the Unicode Collation Algorithm, which involves a database of information. There is a reference implementation in [ICU](webSettings.xml). Good and proper Unicode libraries will support it (e.g. [here is Go's](footnotes.xml)), but I do imagine it may be a burden for some implementations. I suggest we discuss this in the ad hoc and consider the pros and cons.", "target": "Notes"}-->
:

1.  There are various ways to specify literal !!string data in YAML for
    handling indentation, newlines, as well as convenient support for
    line folding for multiline strings. All may be used in TOSCA. A
    TOSCA parser shall not modify the YAML string in any way, e.g. no
    trimming of whitespace or newlines. [\[YAML 1.2 chapter
    6\]](https://yaml.org/spec/1.2/spec.html#Basic)

<!-- -->

10. The TOSCA functions “concat”, “join”, “token”, “length”,
    “min_length”, “max_length”, and “pattern” are all Unicode-aware.
    Specifically, the length of a string is a count of its runes, not
    the length of the byte array, which may differ according to the
    encoding. \[See XXX\]

11. The TOSCA functions that check for equality, “equal” and
    “valid_values”, should work regardless of the Unicode encoding. For
    example, comparing two strings that are “!”, one of which is in
    UTF-8 and is encoded as “0x21”, the other which is in UTF-16 and is
    encoded as “0x0021”, would result in equality.  For simplicity,
    implementations may standardize on a single encoding, e.g., UTF-8,
    and convert all other encodings to it. \[See XXX\]

12. Relatedly, although in YAML 1.2 a !!string is already defined as a
    Unicode sequence [\[YAML 1.2 section
    10.1.1.3\]](https://yaml.org/spec/1.2/spec.html#id2802842), this
    sequence can be variously encoded according to the character set and
    encoding of the YAML stream [\[YAML 1.2 chapter
    5\]](https://yaml.org/spec/1.2/spec.html#Characters). The
    consequence is that a TOSCA string specified in literal YAML may
    inherit the encoding of the YAML document. Again, implementations
    may prefer to convert all strings to a single encoding.

13. TOSCA strings *cannot* be the null value but *can* be empty strings
    (a string with length zero). \[See “nil”, below\]

14. YAML is a streaming format, but TOSCA strings are explicitly *not*
    streams and thus do have a size limit. Thus, TOSCA implementations
    should check against the size limit.

\[Tal’s comment: for functions we should specify their exact behavior
for various primitive types. Some won’t work on all types, e.g. “length”
should not work on integers.\]

#### integer

A 64-bit signed integer.

For simplicity, TOSCA does not have integers of other bit widths, nor
does it have an unsigned integer type. However, it is possible to
enforce most of these variations using data type validation clauses
\[see XXX\].

For example, this would be a custom data type for unsigned 16-bit
integers:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>data_types:</p>
<p>UInt16:</p>
<p>derived_from: integer</p>
<p>validation: { $in_range: [ $value, [ 0, 0xFFFF ] ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes

YAML allows for the standard decimal notation as well as hexadecimal and
octal notations \[[YAML 1.2 example
2.19](https://yaml.org/spec/1.2/spec.html#id2761509)\]. In the above
example we indeed used the hexadecimal notation.

1.  The JSON schema for YAML 1.2 [\[YAML 1.2 chapter
    10.2\]](https://yaml.org/spec/1.2/spec.html#id2803231) allows for
    compatibility with JSON, such that YAML would be a superset of JSON.
    However, note that the JSON format does not distinguish between
    integers and floats, and thus many JSON implementations use floats
    instead of integers.

<!-- -->

15. TOSCA does not specify the endianness of integers and indeed makes
    no requirements for data representation.

#### float

A 64-bit (double-precision) floating-point number \[IEEE 754\],
including the standard values for negative infinity, positive infinity,
and not-a-number.

Be aware that YAML parsers will parse numbers with a decimal point as
!!float even if they *could* be represented as !!int, and likewise
numbers without a decimal point would *always* be parsed as !!int.

A TOSCA parser *shall not* attempt to convert a YAML !!int to a float.
This requirement is necessary for avoiding rounding errors and ensuring
portability. Users should thus add a “.0” suffix to literal integers
that must be floats. Note that this even includes zero, i.e. users must
specify “0” for a zero integer and “0.0” for a zero float.

This following example would be invalid if there were no “.0” suffix
added to “10”:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Node:</p>
<p>properties:</p>
<p>velocity:</p>
<p>type: float</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>node:</p>
<p>type: Node</p>
<p>properties:</p>
<p>velocity: 10.0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes

1.  In addition to decimal, YAML also allows for specifying floats using
    scientific notation as well as special unquoted words for negative
    infinity, positive infinity, and not-a-number [\[YAML 1.2 example
    2.20\]](https://yaml.org/spec/1.2/spec.html#id2761530).

<!-- -->

16. TOSCA does not specify how to convert to other precisions nor to
    other formats, e.g. Bfloat16 and TensorFloat-32.

17. TOSCA does not specify the endianness of floats and indeed makes no
    requirements for data representation.

#### boolean

A single bit.

Note that in YAML literal booleans can be *only* either the unquoted
all-lowercase words “true” or “false”.

A TOSCA parser *shall not* attempt to convert these values, nor
variations such as “yes” or “True”, as quoted strings to booleans, nor
shall it attempt to convert integer values (such as 1 and 0) to
booleans. This requirement is necessary for ensuring portability as well
as clarity.

#### bytes

An array of arbitrary bytes. Because we adhere to 64-bit precision, the
minimum length of bytes is 0 and the maximum length of bytes is
4,294,967,295.

To specify literal bytes in YAML you *must* use a Base64-encoded
!!string \[RFC 2045 section 6.8\]. There exist many free tools to help
you convert arbitrary data to Base64.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Node:</p>
<p>properties:</p>
<p>preamble:</p>
<p>type: bytes</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>node:</p>
<p>type: Node</p>
<p>properties:</p>
<p>preamble: "\</p>
<p>R0lGODlhDAAMAIQAAP//9/X17unp5WZmZgAAAOfn515eXvPz7Y6OjuDg4J+fn5\</p>
<p>OTk6enp56enmlpaWNjY6Ojo4SEhP/++f/++f/++f/++f/++f/++f/++f/++f/+\</p>
<p>+f/++f/++f/++f/++f/++SH+Dk1hZGUgd2l0aCBHSU1QACwAAAAADAAMAAAFLC\</p>
<p>AgjoEwnuNAFOhpEMTRiggcz4BNJHrv/zCFcLiwMWYNG84BwwEeECcgggoBADs="</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes

1.  There is no standard way to represent literal bytes in YAML 1.2.
    Though some YAML implementations may support the [!!binary type
    working draft](https://yaml.org/type/binary.html), to ensure
    portability TOSCA implementations *shall not* accept this YAML type.

<!-- -->

18. The TOSCA functions “length”, “min_length”, and “max_length” work
    differently for the bytes type vs. the string type. For the latter
    the length is the count of Unicode runes, not the count of bytes.

19. TOSCA bytes values *cannot* be the null value but *can* be empty
    arrays (a bytes value with length zero). \[See “nil”, below\]

#### nil

The nil type always has the same singleton value. No other type can have
this value.

This value is provided literally in YAML via the unquoted all-lowercase
word “null”.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Node:</p>
<p>properties:</p>
<p>nothing:</p>
<p>type: nil</p>
<p>required: true</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>node:</p>
<p>type: Node</p>
<p>properties:</p>
<p>nothing: null</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Note that a nil-typed value is *distinct* from an unassigned value. For
consistency TOSCA *requires* you to assign nil values even though their
value is obvious. Thus, the above example would be invalid if we did not
specify the null value for the property at the node template.

Following is a valid example of *not* assigning a value:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Node:</p>
<p>properties:</p>
<p>nothing:</p>
<p>type: nil</p>
<p>required: false</p>
<p>service_template:</p>
<p>node_templates:</p>
<p>node:</p>
<p>type: Node</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Special
<!----
{"id": "817", "author": "Chris Lauwers", "date": "2020-08-04T16:22:00Z", "comment": "Need to add timestamp type", "target": "Special"}-->
 Types

#### TOSCA version
<!----
{"id": "821", "author": "Chris Lauwers", "date": "2020-08-18T23:03:00Z", "comment": "Tal suggests removing this.", "target": "version"}-->


A TOSCA version string.

TOSCA supports the concept of “reuse” of type definitions, as well as
template definitions which could be versioned and change over time. It
is important to provide a reliable, normative means to represent a
version string which enables the comparison and management of types and
templates over time.

##### Grammar

TOSCA version strings have the following grammar:

| \<major_version\>.\<minor_version\>\[.\<fix_version\>\[.\<qualifier\>\[-\<build_version\] \] \] |
|-------------------------------------------------------------------------------------------------|

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- major_version: is a mandatory integer value greater than or equal to 0
  (zero)

- minor_version: is a mandatory integer value greater than or equal to 0
  (zero).

- fix_version: is an optional integer value greater than or equal to 0
  (zero).

- qualifier: is an optional string that indicates a named, pre-release
  version of the associated code that has been derived from the version
  of the code identified by the combination major_version, minor_version
  and fix_version numbers.

- build_version: is an optional integer value greater than or equal to 0
  (zero) that can be used to further qualify different build versions of
  the code that has the same qualifer_string.

##### Version Comparison

- When specifying a version string that contains just a major and a
  minor version number, the version string must be enclosed in quotes to
  prevent the YAML parser from treating the version as a floating point
  value.

- When comparing TOSCA versions, all component versions (i.e., *major*,
  *minor* and *fix*) are compared in sequence from left to right.

- TOSCA versions that include the optional qualifier are considered
  older than those without a qualifier.

- TOSCA versions with the same major, minor, and fix versions and have
  the same qualifier string, but with different build versions can be
  compared based upon the build version.

- Qualifier strings are considered domain-specific. Therefore, this
  specification makes no recommendation on how to compare TOSCA versions
  with the same major, minor and fix versions, but with different
  qualifiers strings and simply considers them different branches
  derived from the same code.

##### Examples

Examples of valid TOSCA version strings:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># basic version strings</p>
<p>‘6.1’</p>
<p>2.0.1</p>
<p># version string with optional qualifier</p>
<p>3.1.0.beta</p>
<p># version string with optional qualifier and build version</p>
<p>1.0.0.alpha-10</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Notes

- \[[Maven-Version](#CIT_MAVEN_VERSION)\] The TOSCA version type is
  compatible with the Apache Maven versioning policy.

##### Additional Requirements

- A version value of zero (i.e., ‘0.0’, or ‘0.0.0’) SHALL indicate there
  no version provided.

- A version value of zero used with any qualifiers SHALL NOT be valid.

#### TOSCA timestamp type

A local instant in time containing two elements: the local notation plus
the time zone offset.

TOSCA timestamps are represented as strings following \[[RFC
3339](https://tools.ietf.org/html/rfc3339)\], which in turn uses a
simplified profile of \[[ISO
8601](https://www.iso.org/iso-8601-date-and-time-format.html)\]. TOSCA
adds an exception to RFC 3339: though RFC 3339 supports timestamps with
[unknown local
offsets](https://tools.ietf.org/html/rfc3339#section-4.3), represented
as the "-0" timezone, TOSCA *does not* support this feature and will
treat the unknown time zone as UTC. There are two reasons for this
exception: the first is that many systems do not support this
distinction and TOSCA aims for interoperability, and the second is that
timestamps with unknown time zones cannot be converted to UTC, making it
impossible to apply comparison functions. If this feature is required,
it can be supported via a custom data type (see XXX).

##### Notes

- It is strongly recommended that all literal YAML timestamps be
  enclosed in quotation marks to ensure that they are parsed as strings.
  Otherwise, some YAML parsers might interpret them as the YAML
  !!timestamp type, which is rejected by TOSCA (see below).

- The TOSCA functions "equal", "greater_than", "greater_or_equal",
  "less_than", and "less_or_equal" all use the *universal* instant, i.e.
  as the local instant is converted to UTC by applying the timezone
  offset.

- Some YAML implementations may support the [!!timestamp type working
  draft](https://yaml.org/type/timestamp.html), but to ensure
  portability TOSCA implementations *shall not* accept this YAML type.
  Also note that the YAML !!timestamp supports a relaxed notation with
  whitespace, which *does not* conform to RFC 3339.

- RFC 3339 is based on the Gregorian calendar, including leap years and
  leap seconds, and is thus explicitly culturally biased. It cannot be
  used for non-Gregorian locales. Other calendar representations can be
  supported via custom data types (see XXX).

- Time zone information is expressed and stored numerically as an offset
  from UTC, thus daylight savings and other local changes are not
  included.

- TOSCA does not specify a canonical representation for timestamps. The
  only requirement is that representations adhere to RFC 3339.

#### TOSCA scalar-unit type

The scalar-unit type can be used to define scalar values along with a
unit from the list of recognized units provided below.

##### Grammar

TOSCA scalar-unit typed values have the following grammar:

| \<scalar\> \<unit\> |
|---------------------|

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- scalar: is a mandatory scalar value.

- unit: is a mandatory unit value. The unit value MUST be
  type-compatible with the scalar.

##### Additional requirements

- **<u>Whitespace</u>**: any number of spaces (including zero or none)
  SHALL be allowed between the scalar value and the unit value.

- It SHALL be considered an error if either the scalar or unit portion
  is missing on a property or attribute declaration derived from any
  scalar-unit type.

- When performing validation clause evaluation on values of the
  scalar-unit type, both the scalar value portion and unit value portion
  **SHALL** be compared together (i.e., both are treated as a single
  value). For example, if we have a property called storage_size (which
  is of type scalar-unit) a valid range constraint would appear as
  follows:

<!-- -->

- storage_size: in_range \[ 4 GB, 20 GB \]

where storage_size’s range will be evaluated using both the numeric and
unit values (combined together), in this case ‘4 GB’ and ’20 GB’.

##### Concrete Types

The scalar-unit type grammar is abstract and has four recognized
concrete types in TOSCA:

- **scalar-unit.size** – used to define properties that have scalar
  values measured in size units.

- **scalar-unit.time** – used to define properties that have scalar
  values measured in size units.

- **scalar-unit.frequency** – used to define properties that have scalar
  values measured in units per second.

- **scalar**-**unit.bitrate** – used to define properties that have
  scalar values measured in bits or bytes per second

These types and their allowed unit values are defined below.

##### scalar-unit.size
<!----
{"id": "839", "author": "Chris Lauwers", "date": "2020-07-27T18:39:00Z", "comment": "What don\u2019t we allow multiples of bits", "target": "size"}-->


###### Recognized Units

| Unit | Usage | Description                    |
|------|-------|--------------------------------|
| B    | size  | byte                           |
| kB   | size  | kilobyte (1000 bytes)          |
| KiB  | size  | kibibytes (1024 bytes)         |
| MB   | size  | megabyte (1000000 bytes)       |
| MiB  | size  | mebibyte (1048576 bytes)       |
| GB   | size  | gigabyte (1000000000 bytes)    |
| GiB  | size  | gibibytes (1073741824 bytes)   |
| TB   | size  | terabyte (1000000000000 bytes) |
| TiB  | size  | tebibyte (1099511627776 bytes) |

###### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Storage size in Gigabytes</p>
<p>properties:</p>
<p>storage_size: 10 GB</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Notes

- The unit values recognized by TOSCA for size-type units are based upon
  a subset of those defined by GNU at
  <http://www.gnu.org/software/parted/manual/html_node/unit.html>, which
  is a non-normative reference to this specification.

- TOSCA treats these unit values as case-insensitive (e.g., a value of
  ‘kB’, ‘KB’ or ‘kb’ is equivalent), but it is considered best practice
  to use the case of these units as prescribed by
  GNU
<!----
{"id": "843", "author": "Chris Lauwers", "date": "2020-07-20T18:40:00Z", "comment": "Bitrate units are case sensitive. We\n  should make this consistent.", "target": "GNU"}-->
.

- Some cloud providers may not support byte-level granularity for
  storage size allocations. In those cases, these values could be
  treated as desired sizes and actual allocations will be based upon
  individual provider capabilities.

##### scalar-unit.time

###### Recognized Units

| Unit | Usage | Description  |
|------|-------|--------------|
| d    | time  | days         |
| h    | time  | hours        |
| m    | time  | minutes      |
| s    | time  | seconds      |
| ms   | time  | milliseconds |
| us   | time  | microseconds |
| ns   | time  | nanoseconds  |

###### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Response time in milliseconds</p>
<p>properties:</p>
<p>respone_time: 10 ms</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Notes

- The unit values recognized by TOSCA for time-type units are based upon
  a subset of those defined by International System of Units whose
  recognized abbreviations are defined within the following reference:

<!-- -->

- <http://www.ewh.ieee.org/soc/ias/pub-dept/abbreviation.pdf>

- This document is a non-normative reference to this specification and
  intended for publications or grammars enabled for Latin characters
  which are not accessible in typical programming languages

##### scalar-unit.frequency

###### Recognized Units

| Unit | Usage     | Description                                                                       |
|------|-----------|-----------------------------------------------------------------------------------|
| Hz   | frequency | Hertz, or Hz. equals one cycle per second.                                        |
| kHz  | frequency | Kilohertz, or kHz, equals to 1,000 Hertz                                          |
| MHz  | frequency | Megahertz, or MHz, equals to 1,000,000 Hertz or 1,000 kHz                         |
| GHz  | frequency | Gigahertz, or GHz, equals to 1,000,000,000 Hertz, or 1,000,000 kHz, or 1,000 MHz. |

###### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Processor raw clock rate</p>
<p>properties:</p>
<p>clock_rate: 2.4 GHz</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Notes

- The value for Hertz (Hz) is the International Standard Unit (ISU) as
  described by the Bureau International des Poids et Mesures (BIPM) in
  the “*SI Brochure: The International System of Units (SI) \[8th
  edition, 2006; updated in 2014\]*”,
  <http://www.bipm.org/en/publications/si-brochure/>

##### scalar-unit.bitrate

###### Recognized Units

| Unit  | Usage   | Description                              |
|-------|---------|------------------------------------------|
| bps   | bitrate | bit per second                           |
| Kbps  | bitrate | kilobit (1000 bits) per second           |
| Kibps | bitrate | kibibits (1024 bits) per second          |
| Mbps  | bitrate | megabit (1000000 bits) per second        |
| Mibps | bitrate | mebibit (1048576 bits) per second        |
| Gbps  | bitrate | gigabit (1000000000 bits) per second     |
| Gibps | bitrate | gibibits (1073741824 bits) per second    |
| Tbps  | bitrate | terabit (1000000000000 bits) per second  |
| Tibps | bitrate | tebibits (1099511627776 bits) per second |

###### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># Somewhere in a node template definition</p>
<p>requirements:</p>
<p>- link:</p>
<p>node_filter:</p>
<p>capabilities:</p>
<p>- myLinkable</p>
<p>properties:</p>
<p>bitrate:</p>
<p>- greater_or_equal: 10 Kbps # 10 * 1000 bits per second at
least</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Collection Types

#### TOSCA list type

The list type allows for specifying multiple values for a
a parameter of
property
<!----
{"id": "859", "author": "Mike Rehder", "date": "2020-12-14T14:56:00Z", "comment": "What is a \u201cparameter of property\u201d?  \nShould just say \u201cfor a property\u201d.", "target": "a parameter of\nproperty"}-->
. For example, if an
application allows for being configured to listen on multiple ports, a
list of ports could be configured using the list data type.

Note that entries in a list must be of the same type. The type (for
simple entries) or schema (for complex entries) is defined by the
mandatory entry_schema attribute of the respective [property
definition](#_Schema_Definition), [attribute
definitions](#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition),
or input or output [parameter definitions](#parameter-definition).
Schema definitions can be arbitrarily complex (they may themselves
define a list).

##### Grammar

TOSCA lists are essentially normal YAML lists with the following
grammars:

######  Square bracket notation

| \[ \<list_entry_1\>, \<list_entry_2\>, ... \] |
|-----------------------------------------------|

###### Bulleted list notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>- &lt;list_entry_1&gt;</p>
<p>- ...</p>
<p>- &lt;list_entry_n&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammars, the pseudo values that appear in angle brackets
have the following meaning:

- \<list_entry\_\*\>: represents one entry of the list.

##### Declaration Examples

###### List declaration using a simple type

The following example shows a list declaration with an entry schema
based upon a simple integer type (which has an additional validation
clause):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;some_entity&gt;:</p>
<p>...</p>
<p>properties:</p>
<p>listen_ports:</p>
<p>type: <a href="#tosca-list-type">list</a></p>
<p>entry_schema:</p>
<p>description: listen port entry (simple integer type)</p>
<p>type: <a href="#TYPE_YAML_INTEGER">integer</a></p>
<p>validation: { $max_length: [ $value, 128 ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### List declaration using a complex type

The following example shows a list declaration with an entry schema
based upon a complex type:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;some_entity&gt;:</p>
<p>...</p>
<p>properties:</p>
<p>products:</p>
<p>type: <a href="#tosca-list-type">list</a></p>
<p>entry_schema:</p>
<p>description: Product information entry (complex type) defined
elsewhere</p>
<p>type: ProductInfo</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Definition Examples

These examples show two notation options for defining lists:

- A single-line option which is useful for only short lists with simple
  entries.

- A multi-line option where each list entry is on a separate line; this
  option is typically useful or more readable if there is a large number
  of entries, or if the entries are complex.

###### Square bracket notation

| listen_ports: \[ 80, 8080 \] |
|------------------------------|

###### Bulleted list notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>listen_ports:</p>
<p>- 80</p>
<p>- 8080</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### TOSCA map type

The map type allows for specifying multiple values for a parameter of
property as a map. In contrast to the list type, where each entry can
only be addressed by its index in the list, entries in a map are named
elements that can be addressed by their keys.

Note that entries in a map for one property or parameter must be of the
same type. The type (for simple entries) or schema (for complex entries)
is defined by the entry_schema attribute of the respective [property
definition](#_Schema_Definition), [attribute
definition](#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition),
or input or output [parameter definition](#parameter-definition). In
addition, the keys that identify entries in a map must be of the same
type as well. The type of these keys is defined by the key_schema
attribute of the respective property_definition, attribute_definition,
or input or output parameter_definition. If the key_schema is not
specified, keys are assumed to be of type string.

##### Grammar

TOSCA maps are normal YAML dictionaries with following grammar:

###### Single-line grammar

| { \<entry_key_1\>: \<entry_value_1\>, ..., \<entry_key_n\>: \<entry_value_n\> } |
|---------------------------------------------------------------------------------|

###### Multi-line grammar

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;entry_key_1&gt;: &lt;entry_value_1&gt;</p>
<p>...</p>
<p>&lt;entry_key_n&gt;: &lt;entry_value_n&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammars, the pseudo values that appear in angle brackets
have the following meaning:

- entry_key\_\*: is the mandatory key for an entry in the map

- entry_value\_\*: is the value of the respective entry in the map

##### Declaration Examples

###### Map declaration using a simple type

The following example shows a map with an entry schema definition based
upon an existing string type (which has an additional validation
clause):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;some_entity&gt;:</p>
<p>...</p>
<p>properties:</p>
<p>emails:</p>
<p>type: <a href="#tosca-map-type">map</a></p>
<p>entry_schema:</p>
<p>description: basic email address</p>
<p>type: <a href="#TYPE_YAML_STRING">string</a></p>
<p>validation: { $max_length: [ $value, 128 ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Map declaration using a complex type

The following example shows a map with an entry schema definition for
contact information:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;some_entity&gt;:</p>
<p>...</p>
<p>properties:</p>
<p>contacts:</p>
<p>type: <a href="#tosca-map-type">map</a></p>
<p>entry_schema:</p>
<p>description: simple contact information</p>
<p>type: ContactInfo</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Definition Examples

These examples show two notation options for defining maps:

- A single-line option which is useful for only short maps with simple
  entries.

- A multi-line option where each map entry is on a separate line; this
  option is typically useful or more readable if there is a large number
  of entries, or if the entries are complex.

###### Single-line notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># notation option for shorter maps</p>
<p>user_name_to_id_map: { user1: 1001, user2: 1002 }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

###### Multi-line notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># notation for longer maps</p>
<p>user_name_to_id_map:</p>
<p>user1: 1001</p>
<p>user2: 1002</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Data Type

A Data Type definition defines the schema for new datatypes in TOSCA.

#### Keynames

The Data Type is a TOSCA type entity and has the common keynames listed
in Section 4.2.5.2 Common keynames in type definitions. In addition, the
Data Type has the following recognized keynames:

| Keyname      | Mandatory                     | Type                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| validation   | no                            | [validation clause](#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition) | The optional validation clause that must evaluate to True for values of this Data Type
<!----
{"id": "904", "author": "Chris Lauwers", "date": "2021-01-26T03:12:00Z", "comment": "Edit suggested by Mike Rehder: Not valid for a type derived from a complex type (parent has property definitions) or a type with property, key_schema or entry_schema definitions.", "target": "Type"}-->
 to be valid. |
| properties   | no                            | map of [property definitions](#_Schema_Definition)                                                                                                                                                                       | The optional map property definitions that comprise the schema for a complex Data Type in TOSCA
<!----
{"id": "905", "author": "Chris Lauwers", "date": "2021-01-26T03:13:00Z", "comment": "Edit suggested by Mike Rehder: Not valid for a type derived from a simple type (parent has no property definitions) or a type with constraint definitions.", "target": "TOSCA"}-->
.                            |
| key_schema   | conditional (default: string) | [schema definition](#schema-definition)                                                                                                                                                                                  | For data types that derive from the TOSCA map data type, the optional schema definition for the keys used to identify entries in properties of this data type. If not specified, the key_schema defaults to string. For data types that do not derive from the TOSCA map data type, the key_schema is not allowed.                                                                                                             |
| entry_schema | conditional                   | [schema definition](#schema-definition)                                                                                                                                                                                  | For data types that derive from the TOSCA map or list data types, the mandatory schema definition for the entries in properties of this data type. For data types that do not derive from the TOSCA list or map data type, the entry_schema is not allowed.                                                                                                                                                                    |

#### Grammar

Data Types have the following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">data_type_name</a>&gt;:</p>
<p>derived_from: &lt;<a
href="#TYPE_YAML_STRING">existing_type_name</a>&gt;</p>
<p>version: &lt;<a
href="#tosca-tal-suggests-removing-this.version">version_number</a>&gt;</p>
<p>metadata:</p>
<p>&lt;<a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">datatype_description</a>&gt;</p>
<p>validation: &lt;<a
href="#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition">validation_clause</a>&gt;</p>
<p>properties:</p>
<p>&lt;<a href="#_Schema_Definition">property_definitions</a>&gt;</p>
<p>key_schema: &lt;key_schema_definition&gt;</p>
<p>entry_schema: &lt;entry_schema_definition&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- data_type_name: represents the mandatory symbolic name of the data
  type as a string.

- version_number: represents the optional TOSCA version number for the
  data type.

- datatype_description: represents the optional description for the data
  type.

- existing_type_name: represents the optional name of a valid TOSCA
  primitive type or data type this new data type derives from.

- validation_clause: represents the optional validation clause that must
  evaluate to True for values of this data type to be valid.

- property_definitions: represents the optional map of one or more
  property definitions that provide the schema for the data type

<!-- -->

- property_definitions may not be added to data types derived_from TOSCA
  primitive types.

<!-- -->

- key_schema_definition: if the data type derives from the TOSCA map
  type (i.e existing_type_name is a map or derives from a map), it
  represents the optional schema definition for the keys used to
  identify entry properties of this type.

- entry_schema_definition: if the data type derives from the TOSCA map
  or list types (i.e. existing_type name is a map or list or derives
  from a map or list), it represents the mandatory schema definition for
  the entries in properties of this type.

#### Derivation rules

During Data Type derivation the keyname definitions follow these rules:

- validation: a new validation clause may be defined; this validation
  clause does not replace the validation clause defined in the parent
  type but is considered in addition to it.

- properties: existing property definitions may be refined; new property
  definitions may be added.

- key_schema: the key_schema definition may be refined according to
  schema refinement rules.

- entry_schema: the entry_schema definition may be refined according to
  schema refinement rules.

#### Additional Requirements

- A valid datatype
  definition **MUST** have either a valid derived_from declaration or at
  least one valid property definition.
<!----
{"id": "910", "author": "Mike Rehder", "date": "2020-12-14T15:10:00Z", "comment": "This implies that type is optional.\n  However it is listed as required \u2013 which is it?", "target": "A valid datatype\n  definition **MUST** have either a valid derived_from declaration or at\n  least one valid property definition."}-->


- Any validation clauses **SHALL** be type-compatible with the type
  declared by the derived_from keyname.

- If a properties keyname is provided, it **SHALL** contain one or more
  valid property definitions.

- Property definitions may not be added to data types derived from TOSCA
  primitive types.

#### Examples

The following example represents a Data Type definition based upon an
existing string type:

##### Defining a complex datatype

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># define a new complex datatype</p>
<p>mytypes.phonenumber:</p>
<p>description: my phone number datatype</p>
<p>properties:</p>
<p>countrycode:</p>
<p>type: integer</p>
<p>areacode:</p>
<p>type: integer</p>
<p>number:</p>
<p>type: integer</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Defining a datatype derived from an existing datatype

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># define a new datatype that derives from existing type and
extends it</p>
<p>mytypes.phonenumber.extended:</p>
<p>derived_from: mytypes.phonenumber</p>
<p>description: custom phone number type that extends the basic
phonenumber type</p>
<p>properties:</p>
<p>phone_description:</p>
<p>type: string</p>
<p>validation: { $max_length: [ $value, 128 ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Schema definition

All entries in a map or list for one property or
parameter must be of the same type. Similarly, all keys for map entries
for one property or parameter must be of the same type as well.

<!----
{"id": "920", "author": "Mike Rehder", "date": "2020-12-14T15:12:00Z", "comment": "Repeats from the map and list primitive\nsection.", "target": "All entries in a map or list for one property or\nparameter must be of the same type. Similarly, all keys for map entries\nfor one property or parameter must be of the same type as well.\n"}-->
A TOSCA schema definition
specifies the type (for simple entries) or schema (for complex entries)
for keys and entries in TOSCA set types such as the TOSCA list or map.

If the schema definition specifies a map key, the type of the key schema
must be derived originally from the string type (which basically ensures
that the schema type is a string with additional validation clauses). As
there is little need for complex keys this caters to more
straight-forward and clear specifications. If the key schema is not
defined it is assumed to be string by default.

Schema definitions appear in data type definitions when derived_from a
map or list type or in parameter, property, or attribute definitions of
a map or list type.

#### Keynames

The following is the list of recognized keynames for a TOSCA schema
definition:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>type</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td><p>The mandatory data type for the key or entry.</p>
<p>If this schema definition is for a map key, then the referred type
must be derived originally from string.</p></td>
</tr>
<tr class="even">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING"><span>string</span></a></td>
<td>The optional description for the schema.</td>
</tr>
<tr class="odd">
<td>validation</td>
<td>no</td>
<td><a
href="#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition">validation
clauses</a>\</td>
<td>The optional validation clause that must evaluate to True for the
description: a new
  definition is unrestricted and will overwrite the one inherited from
  the schema definition in the parent entity type
  definition.
<!----
{"id": "923\" data-author=\"Chris Lauwers\"\ndata-date=\"2021-01-26T03:17:00Z\">Edit suggested by Mike Rehder: The\noptional list of constraint clauses for the map or list as a whole (not\nto its key or entry schema).</span>property<span class=\"comment-end\"\nid=\"923\"></span>.</td>\n</tr>\n<tr class=\"even\">\n<td>key_schema</td>\n<td>no (default: string)</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>When the schema itself is of type map, the optional schema\ndefinition that is used to specify the type of the keys of that map\u2019s\nentries (if key_schema is not defined it is assumed to be \u201cstring\u201d by\ndefault). For other schema types, the key_schema must not be\ndefined.</td>\n</tr>\n<tr class=\"odd\">\n<td>entry_schema</td>\n<td>conditional</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>When the schema itself is of type map or list, the schema definition\nis mandatory and is used to specify the type of the entries in that map\nor list. For other schema types, the entry_schema must not be\ndefined.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\n##### Short notation\n\nThe following single-line grammar may be used when only the schema type\nneeds to be declared:\n\n| \\<schema_definition\\>: \\<schema_type\\> |\n|----------------------------------------|\n\n##### Extended Notation\n\nThe following multi-line grammar may be used when additional information\non the schema definition is needed:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">schema_definition</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">schema_type</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">schema_description</a>&gt;</p>\n<p>validation: &lt;<a\nhref=\"#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition\">schema_validation_clause</a>&gt;</p>\n<p>key_schema: &lt;<a\nhref=\"#schema-definition\">key_schema_definition</a>&gt;</p>\n<p>entry_schema: &lt;<a\nhref=\"#schema-definition\">entry_schema_definition</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- schema_type: represents the mandatory type name for entries of the\n  specified schema\n\n<!-- -->\n\n- if this schema definition is for a map key, then the schema_type must\n  be derived originally from string.\n\n<!-- -->\n\n- schema_description: represents the optional description of the schema\n  definition\n\n- schema_validation_clause: represents the optional validation clause\n  for entries of the specified schema.\n\n- key_schema_definition: if the schema_type is map, it represents the\n  optional schema definition for the keys of that map\u2019s entries.\n\n- entry_schema_definition: if the schema_type is map or list, it\n  represents the mandatory schema definition for the entries in that map\n  or list.\n\n#### Refinement rules\n\nA schema definition uses the following definition refinement rules when\nthe containing entity type is derived:\n\n- type: must be derived from (or the same as) the type in the schema\n  definition in the parent entity type definition.\n\n- <span class=\"comment-start\" id=\"929", "author": "Mike Rehder", "date": "2020-12-14T14:39:00Z", "comment": "Description is not inherited for derived\n  type \u2013 why is it inherited for schema?", "target": "description: a new\n  definition is unrestricted and will overwrite the one inherited from\n  the schema definition in the parent entity type\n  definition."}-->


- validation: a new definition is unrestricted; this validation clause
  does not replace the validation clause defined in the schema
  definition in the parent entity type but is considered in addition to
  it.

- key_schema: may be refined (recursively) according to schema
  refinement rules.

- entry_schema: may be refined (recursively) according
  to schema refinement rules.
<!----
{"id": "930", "author": "Mike Rehder", "date": "2020-12-14T14:45:00Z", "comment": "What if the derived_from type is a list\n  with a complex data type entry_schema? What are the rules about\n  refinement/augmentation of that complex\n  definition?", "target": "entry_schema: may be refined (recursively) according\n  to schema refinement rules."}-->


### Validation clause definition
<!----
{"id": "939", "author": "Mike Rehder", "date": "2020-12-14T14:40:00Z", "comment": "This should have its own refinement rule section to explain how conflicts are resolved, if at all. For example, if there is \u201crange 0..10\u201d and \u201cgreated_than 15\u201d what happens?", "target": "Validation clause definition"}-->


A validation clause that must evaluate to True if the value for the
entity it references is considered valid.

#### Grammar

Validation clauses have the following grammar:

| validation: \< validation_clause\> |
|------------------------------------|

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- validation_clause: represents a Boolean expression that must evaluate
  to True in order for values to be valid. Any Boolean expression can be
  used with any function with any degree of nesting.

#### The \$value Function

The Boolean expression used as a validation clause must have a mechanism
for referencing the value to which the expression applies. A
special-purpose function is introduced for this purpose. This function
is named **\$value** and refers to the value used for the data type or
the parameter definition that contains the validation clause.

#### Examples

The following shows an example of validation clauses used in data type
definitions:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>data_types:</p>
<p># Full function syntax for the $value function</p>
<p>Count1:</p>
<p>derived_from: integer</p>
<p>validation: { $greater_or_equal: [ { $value: [] }, 0 ] }</p>
<p># Simple function syntax for the $value function</p>
<p>Count2:</p>
<p>derived_from: integer</p>
<p>validation: { $greater_or_equal: [ $value, 0 ] }</p>
<p># Full function syntax with arguments</p>
<p>FrequencyRange:</p>
<p>properties:</p>
<p>low:</p>
<p>type: scalar-unit.frequency</p>
<p>high:</p>
<p>type: scalar-unit.frequency</p>
<p>validation:</p>
<p>$greater_or_equal: [ { $value: [ high ] }, { $value: [ low ] }
]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Schema_Definition" class="anchor"></span>The following shows
an example of validation clauses used in property definitions:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_types:</p>
<p>Scalable:</p>
<p>properties:</p>
<p>minimum_instances:</p>
<p>type: integer</p>
<p>validation: { $greater_or_equal: [ $value, 0 ] } # positive
integer</p>
<p>maximum_instances:</p>
<p>type: integer</p>
<p>validation:</p>
<p>$greater_or_equal:</p>
<p>- $value</p>
<p>- $get_property: [ SELF, minimum_instances ]</p>
<p>default_instances:</p>
<p>type: integer</p>
<p>validation:</p>
<p>$and:</p>
<p>- $greater_or_equal:</p>
<p>- $value</p>
<p>- $get_property: [ SELF, minimum_instances ]</p>
<p>- $less_or_equal:</p>
<p>- $value</p>
<p>- $get_property: [ SELF, maximum_instances ]</p>
<p>required: false</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Property definition

A property definition defines a named, typed value and related data that
can be associated with an entity defined in this specification (e.g.,
Node Types, Relationship Types, Capability Types, etc.). Properties are
used by template authors to provide input values to TOSCA entities which
indicate their “desired state” when they are instantiated. The value of
a property can be retrieved using the get_property function within TOSCA
Service Templates.

#### Attribute and Property reflection 

The actual state of the entity, at any point in its lifecycle once
instantiated, is reflected by an attribute. TOSCA orchestrators
automatically create an attribute for every declared property (with the
same symbolic name) to allow introspection of both the desired state
(property) and actual state (attribute). If an attribute is reflected
from a property, its initial value is the value of the reflected
property.

#### Keynames

The following is the list of recognized keynames for a TOSCA property
definition:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>type</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The mandatory data type for the property.</td>
</tr>
<tr class="even">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING"><span>string</span></a></td>
<td>The optional description for the property.</td>
</tr>
<tr class="odd">
<td>required</td>
<td>No (default: true)</td>
<td><a href="#TYPE_YAML_BOOLEAN">boolean</a></td>
<td>An optional key that declares a property as required (true) or not
(false). Defaults to true.</td>
</tr>
<tr class="even">
<td>default</td>
<td>no</td>
<td>&lt;must match property type&gt;</td>
<td><p>An optional key that may provide a value to be used as a default
if not provided by another means.</p>
<p>The default keyname SHALL NOT be defined when property is not
required (i.e. the value of the required keyname is false).</p></td>
</tr>
<tr class="odd">
<td>value</td>
<td>no</td>
<td>&lt;see below&gt;</td>
<td>An optional key that may provide a fixed value to be used. A
property that has a fixed value provided (as part of a definition or
refinement) cannot be subject to a further refinement or assignment.
That is, a fixed value cannot be changed.</td>
</tr>
<tr class="even">
<td>status</td>
<td>No (default: supported)</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The optional status of the property relative to the specification or
implementation. See table below for valid values. Defaults to
supported.</td>
</tr>
<tr class="odd">
<td>validation</td>
<td>no</td>
<td><a
href="#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition">validation
clause</a></td>
<td>The optional validation clause for the Status values
<!----
{"id": "955\" data-author=\"Chris Lauwers\"\ndata-date=\"2021-01-26T03:20:00Z\">Edit suggested by Mike Rehder:\nApplicable to simple type property definitions (not derived from a type\nwith propertys).</span>property<span class=\"comment-end\"\nid=\"955\"></span>.</td>\n</tr>\n<tr class=\"even\">\n<td>key_schema</td>\n<td>conditional (default: string)</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>The schema definition for the keys used to identify entries in\nproperties of type TOSCA map (or types that derive from map). If not\nspecified, the key_schema defaults to string. For properties of type\nother than map, the key_schema is not allowed.</td>\n</tr>\n<tr class=\"odd\">\n<td>entry_schema</td>\n<td>conditional</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>The schema definition for the entries in properties of TOSCA\ncollection types such as list, map, or types that derive from list or\nmap) If the property type is a collection type, the entry schema is\nmandatory. For other types, the entry_schema is not allowed.</td>\n</tr>\n<tr class=\"even\">\n<td>external-schema</td>\n<td>no</td>\n<td>string</td>\n<td><p>The optional key that contains a schema definition that TOSCA\nOrchestrators MAY use for validation when the \u201ctype\u201d key\u2019s value\nindicates an External schema (e.g., \u201cjson\u201d).</p>\n<p>See section \u201cExternal schema\u201d below for further explanation and <span\nclass=\"comment-start\" id=\"956\" data-author=\"Chris Lauwers\"\ndata-date=\"2021-01-26T03:21:00Z\">Edit suggested by Mike Rehder:\nApplicable to simple type property definitions (not derived from a type\nwith propertys).</span>usage<span class=\"comment-end\"\nid=\"956\"></span>.</p></td>\n</tr>\n<tr class=\"odd\">\n<td>metadata</td>\n<td>no</td>\n<td><a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Defines a section used to declare additional metadata\ninformation.</td>\n</tr>\n</tbody>\n</table>\n\n#### <span class=\"comment-start\" id=\"960", "author": "Calin Curescu", "date": "2020-06-09T16:28:00Z", "comment": "!!! %%% Move this in the metadata, in a \u201crecommended metadata\u201d section (for profile writing).", "target": "Status values"}-->


The following property status values are supported:

| Value            | Description                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------|
| **supported**    | Indicates the property is supported. This is the **default** value for all property definitions. |
| **unsupported**  | Indicates the property is not supported.                                                         |
| **experimental** | Indicates the property is experimental and has no official standing.                             |
| **deprecated**   | Indicates the property has been deprecated by a new specification version.                       |

#### Grammar

Property definitions have the following grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">property_name</a>&gt;:</p>
<p>type: &lt;<a href="#TYPE_YAML_STRING">property_type</a>&gt;</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">property_description</a>&gt;</p>
<p>required: &lt;<a
href="#TYPE_YAML_BOOLEAN">property_required</a>&gt;</p>
<p>default: &lt;default_value&gt;</p>
<p>value: &lt;property_value&gt; | { &lt;property_value_expression&gt;
}</p>
<p>status: &lt;<a
href="#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values">status_value</a>&gt;</p>
<p>validation: &lt;<a
href="#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition">validation_clause</a>&gt;</p>
<p>key_schema: &lt;<a
href="#schema-definition">key_schema_definition</a>&gt;</p>
<p>entry_schema: &lt;<a
href="#schema-definition">entry_schema_definition</a>&gt;</p>
<p>metadata:</p>
<p>&lt;<a
href="#also-covered-by-4.2.1.3.2metadata">metadata_map</a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following single-line grammar is supported when only a fixed value
or fixed value expression needs to be provided to a property:

| \<[property_name](#TYPE_YAML_STRING)\>: \<property_value\> \| { \<property_value_expression\> } |
|-------------------------------------------------------------------------------------------------|

This single-line grammar is equivalent to the following:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">property_name</a>&gt;:</p>
<p>value: &lt;property_value&gt; | { &lt;property_value_expression&gt;
}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Note that the short form can be used only during a refinement (i.e. the
property has been previously defined).

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- property_name: represents the mandatory symbolic name of the property
  as a string.

- property_description: represents the optional description of the
  property.

- property_type: represents the mandatory data type of the property.

- property_required: represents an optional boolean value (true or
  false) indicating whether or not the property is required. If this
  keyname is not present on a property definition, then the property
  SHALL be considered required (i.e., true) by default.

- default_value: contains a type-compatible value that is used as a
  default value if a value is not provided by another means (via the
  fixed_value definition or via property assignment);

<!-- -->

- the default_value shall not be defined for properties that are not
  required (i.e. property_required is “false”) as they will stay
  undefined.

<!-- -->

- \<property_value\> \| { \<property_value_expression\> }: contains a
  type-compatible value or value expression that may be defined during
  property definition or refinement to set and fix the value definition
  of the property

<!-- -->

- note that a value definition cannot be changed; once defined, the
  property cannot be further refined or assigned. Thus, value
  definitions should be avoided in data_type definitions.

<!-- -->

- status_value: a string that contains a keyword that indicates the
  status of the property relative to the specification or
  implementation.

- validation_clause: represents the optional Boolean expression that
  must evaluate to true for a value of this property to be valid.

- key_schema_definition: if the property_type is map, represents the
  optional schema definition for the keys used to identify entries in
  that map.

- entry_schema_definition: if the property_type is map or list,
  represents the mandatory schema definition for the entries in that map
  or list.

- metadata_map: represents the optional map of string.

#### Refinement rules

A property definition within data, capability, node, relationship,
group, policy, and artifact types (including capability definitions in
node types) matching the name of a property in the derived entity type
uses the following refinement rules to combine the two property
definitions together:

- type: must be derived from (or the same as) the type in the property
  definition in the parent entity type definition.

- description: a new definition is unrestricted
  and will overwrite the one inherited from the property definition in
  the parent entity type definition.
<!----
{"id": "966", "author": "Mike Rehder", "date": "2020-12-14T14:49:00Z", "comment": "Section 4.2.5.2.3 says that description\n  isn\u2019t inherited", "target": "description: a new definition is unrestricted\n  and will overwrite the one inherited from the property definition in\n  the parent entity type definition."}-->


- required: if defined to “false” in the property definition parent
  entity type it may be redefined to “true”; note that if undefined it
  is automatically considered as being defined to “true”.

- default: a new definition is unrestricted and will overwrite the one
  inherited from the property definition in the parent entity type
  definition (note that the definition of a default value is only
  allowed if the required keyname is (re)defined as “true”).

- value: if undefined in the property definition in the parent entity
  type, it may be defined to any type-compatible value; once defined,
  the property cannot be further refined or assigned.

- status: a new definition is unrestricted and will overwrite
  the one inherited from the property definition in the parent entity
  type definition.
<!----
{"id": "967", "author": "Mike Rehder", "date": "2020-12-14T14:50:00Z", "comment": "I don\u2019t see how this is feasible. If\n  deprecated in the parent, how can a child make it active?  \n  I don\u2019t think this should be allowed to be refined at\n  all.", "target": "status: a new definition is unrestricted and will overwrite\n  the one inherited from the property definition in the parent entity\n  type definition."}-->


- validation: a new definition is unrestricted; this validation clause
  does not replace the validation clause defined in the property
  definition in the parent entity type but is considered in addition to
  it.

- key_schema: if defined in the property definition in the parent entity
  type it may be refined according to schema refinement rules.

- entry_schema: if defined in the property definition in the parent
  entity type it may be refined according to schema refinement rules.

- metadata: a new definition is unrestricted and will overwrite the one
  inherited from the property definition in the parent entity type
  definition.

#### Additional Requirements

- Implementations of TOSCA **SHALL** automatically reflect (i.e., make
  available) any property defined on an entity as an attribute of the
  entity with the same name as the property.

- A property **SHALL** be considered <u>required by default</u> (i.e.,
  as if the required keyname on the definition is set to true) unless
  the definition’s required keyname is explicitly set to false.

- The value provided on a property definition’s default keyname SHALL be
  type compatible with the type declared on the definition’s type
  keyname.

- If a key_schema or entry_schema keyname is provided, its value
  (string) MUST represent a valid schema definition that matches the
  property type (i.e. the property type as defined by the type keyword
  must be the same as or derived originally from map (for key_schema) or
  map or list (for entry_schema).

- TOSCA Orchestrators MAY choose to validate the value of the ‘schema’
  keyname in accordance with the corresponding schema specification for
  any recognized external types.

#### Examples

The following represents an example of a property definition with a
validation clause:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>num_cpus:</p>
<p>type: integer</p>
<p>description: Number of CPUs requested for a software node
instance.</p>
<p>default: 1</p>
<p>required: true</p>
<p>validation; { $valid_values: [ $value, [ 1, 2, 4, 8 ] ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following shows an example of a property refinement. Consider the
definition of an Endpoint capability type:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca.capabilities.Endpoint:</p>
<p>derived_from: tosca.capabilities.Root</p>
<p>properties:</p>
<p>protocol:</p>
<p>type: string</p>
<p>required: true</p>
<p>default: tcp</p>
<p>port:</p>
<p>type: PortDef</p>
<p>required: false</p>
<p>secure:</p>
<p>type: boolean</p>
<p>required: false</p>
<p>default: false</p>
<p># Other property definitions omitted for brevity</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The Endpoint.Admin capability type refines the secure property of the
Endpoint capability type from which it derives by forcing its value to
always be true:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>tosca.capabilities.Endpoint.Admin:</p>
<p>derived_from: tosca.capabilities.Endpoint</p>
<p># Change Endpoint secure indicator to true from its default of
false</p>
<p>properties:</p>
<p>secure: true</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Property assignment

This section defines the grammar for assigning values to properties
within TOSCA templates.

#### Keynames

The TOSCA property assignment has no keynames.

#### Grammar

Property assignments have the following grammar:

##### Short notation:

The following single-line grammar may be used when a simple value
assignment is needed:

| \<property_name\>: \<property_value\> \| { \<property_value_expression\> } |
|----------------------------------------------------------------------------|

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- property_name: represents the name of a property that will be used to
  select a property definition with the same name within on a TOSCA
  entity (e.g., Node Template, Relationship Template, etc.) which is
  declared in its declared type (e.g., a Node Type, Node Template,
  Capability Type, etc.).

- property_value, property_value_expression: represent the
  type-compatible value to assign to the property. Property values may
  be provided as the result of the evaluation of
  an expression or a
  function
<!----
{"id": "983", "author": "Chris Lauwers", "date": "2022-11-21T11:36:00Z", "comment": "What is the difference between an\n  expression and a function", "target": "an expression or a\n  function"}-->
.

#### Additional Requirements

- Properties that have a (fixed) value defined during their definition
  or during a subsequent refinement may not be assigned (as their value
  is already set).

- If a required property has no value defined or assigned, its default
  value is assigned

- A non-required property that is not assigned it stays undefined, thus
  the default keyname is irrelevant for a non-required property.

### Attribute definition
<!----
{"id": "990", "author": "Calin Curescu", "date": "2020-05-07T23:14:00Z", "comment": "%%% !!! To implement this, throughout the specification. Default can have also value_expression! I think we might need also an attribute \u201cvalue_expresssion\u201d keyname that allows to define an attribute as a function of a different attribute (of the same entity), that we can define when creating node/relationship types, even before template design time.", "target": "Attribute definition"}-->


An attribute definition defines a named, typed value that can be
associated with an entity defined in this specification (e.g., a Node,
Relationship or Capability Type). Specifically, it is used to expose the
“actual state” of some property of a TOSCA entity after it has been
deployed and instantiated (as set by the TOSCA orchestrator). Attribute
values can be retrieved via the get_attribute function from the instance
model and used as values to other entities within TOSCA Service
Templates
<!----
{"id": "991", "author": "Chris Lauwers", "date": "2022-11-21T11:36:00Z", "comment": "Can also be set using operation\noutputs", "target": "Templates"}-->
.

#### Attribute and Property reflection 

The actual state of the entity, at any point in its lifecycle once
instantiated, is reflected by an attribute. TOSCA orchestrators
automatically create an attribute for every declared property (with the
same symbolic name) to allow introspection of both the desired state
(property) and actual state (attribute). If an attribute is reflected
from a property, its initial value is the value of the reflected
property.

#### Keynames

The following is the list of recognized keynames for a TOSCA attribute
definition:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>It is also possible that a node
template assigns a value to an attribute that has an operation output
mapped to it (including a value that is the result of calling an
intrinsic function). 
<!----
{"id": "996\" data-author=\"Mike Rehder\"\ndata-date=\"2020-12-14T15:23:00Z\">Similar comments as for property\ndefinition</span>Description<span class=\"comment-end\"\nid=\"996\"></span></th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The mandatory data type for the attribute.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\"><span>string</span></a></td>\n<td>The optional description for the attribute.</td>\n</tr>\n<tr class=\"odd\">\n<td>default</td>\n<td>no</td>\n<td>&lt;any&gt;</td>\n<td><p>An optional key that may provide a value to be used as a default\nif not provided by another means.</p>\n<p>This value SHALL be type compatible with the type declared by the\nattribute definition\u2019s type keyname.</p></td>\n</tr>\n<tr class=\"even\">\n<td>status</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional status of the attribute relative to the specification\nor implementation. See supported <a\nhref=\"#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values\">status\nvalues</a> . Defaults to supported.</td>\n</tr>\n<tr class=\"odd\">\n<td>validation</td>\n<td>no</td>\n<td><a\nhref=\"#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition\">validation\nclause</a></td>\n<td>The optional validation clause for the attribute.</td>\n</tr>\n<tr class=\"even\">\n<td>key_schema</td>\n<td>conditional (default: string)</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>The schema definition for the keys used to identify entries in\nattributes of type TOSCA map (or types that derive from map). If not\nspecified, the key_schema defaults to string. For attributes of type\nother than map, the key_schema is not allowed.</td>\n</tr>\n<tr class=\"odd\">\n<td>entry_schema</td>\n<td>conditional</td>\n<td><a href=\"#schema-definition\">schema definition</a></td>\n<td>The schema definition for the entries in attributes of TOSCA\ncollection types such as list, map, or types that derive from list or\nmap) If the attribute type is a collection type, the entry schema is\nmandatory. For other types, the entry_schema is not allowed.</td>\n</tr>\n<tr class=\"even\">\n<td>metadata</td>\n<td>no</td>\n<td><a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Defines a section used to declare additional metadata\ninformation.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nAttribute definitions have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>attributes:</p>\n<p>&lt;<a href=\"#TYPE_YAML_STRING\">attribute_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">attribute_type</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">attribute_description</a>&gt;</p>\n<p>default: &lt;default_value&gt;</p>\n<p>status: &lt;<a\nhref=\"#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values\">status_value</a>&gt;</p>\n<p>validation: &lt;<a\nhref=\"#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition\">attribute_validation_clause</a>&gt;</p>\n<p>key_schema: &lt;<a\nhref=\"#schema-definition\">key_schema_definition</a>&gt;</p>\n<p>entry_schema: &lt;<a\nhref=\"#schema-definition\">entry_schema_definition</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a\nhref=\"#also-covered-by-4.2.1.3.2metadata\">metadata_map</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- attribute_name: represents the mandatory symbolic name of the\n  attribute as a string.\n\n- attribute_type: represents the mandatory data type of the attribute.\n\n- attribute_description: represents the optional description of the\n  attribute.\n\n- default_value: contains a type-compatible value that may be used as a\n  default if not provided by another means.\n\n- status_value: contains a value indicating the attribute\u2019s status\n  relative to the specification version (e.g., supported, deprecated,\n  etc.); supported status values for this keyname are defined in the\n  property definition section.\n\n- attribute_validation_clause: represents the optional [validation\n  clause](#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition)\n  that must evaluate to True for values for the defined attribute to be\n  valid.\n\n- key_schema_definition: if the attribute_type is map, represents the\n  optional schema definition for the keys used to identify entries in\n  that map.\n\n- entry_schema_definition: if the attribute_type is map or list,\n  represents the mandatory schema definition for the entries in that map\n  or list.\n\n- metadata_map: represents the optional map of string.\n\n#### Refinement rules\n\nAn attribute definition within data, capability, node, relationship, and\ngroup types (including capability definitions in node types) uses the\nfollowing refinement rules when the containing entity type is derived:\n\n- type: must be derived from (or the same as) the type in the attribute\n  definition in the parent entity type definition.\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the attribute definition in the parent entity type\n  definition.\n\n- default: a new definition is unrestricted and will overwrite the one\n  inherited from the attribute definition in the parent entity type\n  definition.\n\n- status: a new definition is unrestricted and will overwrite the one\n  inherited from the attribute definition in the parent entity type\n  definition.\n\n- validation: a new definition is unrestricted; this validation clause\n  does not replace the validation clause defined in the attribute\n  definition in the parent entity type but is considered in addition to\n  it.\n\n- key_schema: if defined in the attribute definition in the parent\n  entity type it may be refined according to schema refinement rules.\n\n- entry_schema: if defined in the attribute definition in the parent\n  entity type it may be refined according to schema refinement rules.\n\n- metadata: a new definition is unrestricted and will overwrite the one\n  inherited from the attribute definition in the parent entity type\n  definition\n\n#### Additional Requirements\n\n- In addition to any explicitly defined attributes on a TOSCA entity\n  (e.g., Node Type, Relationship Type, etc.), implementations of TOSCA\n  **MUST** automatically reflect (i.e., make available) any property\n  defined on an entity as an attribute of the entity with the same name\n  as the property.\n\n- Values for the default keyname **MUST** be derived or calculated from\n  other attribute or operation output values (that reflect the actual\n  state of the instance of the corresponding resource) and not\n  hard-coded or derived from a property settings or inputs (i.e.,\n  desired state).\n\n#### Notes\n\n- Attribute definitions are very similar to [Property\n  definitions](#_Schema_Definition); however, properties of entities\n  reflect an input that carries the template author\u2019s requested or\n  desired value (i.e., desired state) which the orchestrator (attempts\n  to) use when instantiating the entity whereas attributes reflect the\n  actual value (i.e., actual state) that provides the actual\n  instantiated value.\n\n<!-- -->\n\n- For example, a property can be used to request the IP address of a\n  node using a property (setting); however, the actual IP address after\n  the node is instantiated may by different and made available by an\n  attribute.\n\n#### Example\n\nThe following represents a mandatory attribute definition:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>actual_cpus:</p>\n<p>type: integer</p>\n<p>description: Actual number of CPUs allocated to the node\ninstance.</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Attribute assignment\n\nThis section defines the grammar for assigning values to attributes\nwithin TOSCA templates.\n\n#### Keynames\n\nThe TOSCA attribute assignment has no keynames.\n\n#### Grammar\n\nAttribute assignments have the following grammar:\n\n##### Short notation:\n\nThe following single-line grammar may be used when a simple value\nassignment is needed:\n\n| \\<attribute_name\\>: \\<attribute_value\\> \\| { \\<attribute_value_expression\\> } |\n|-------------------------------------------------------------------------------|\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- attribute_name: represents the name of an attribute that will be used\n  to select an attribute definition with the same name within on a TOSCA\n  entity (e.g., Node Template, Relationship Template, etc.) which is\n  declared (or reflected from a Property definition) in its declared\n  type (e.g., a Node Type, Node Template, Capability Type, etc.).\n\n- attribute_value, attribute_value_expresssion: represent the\n  type-compatible value to assign to the attribute. Attribute values may\n  be provided as the result from the evaluation of an expression or a\n  function.\n\n#### Additional requirements\n\n- Attributes that are the target of a parameter mapping assignment\n  cannot also be assigned a value using an attribute assignment.\n\n### Parameter definition\n\nA parameter definition defines a named, typed value and related data and\nmay be used to exchange values between the TOSCA orchestrator and the\nexternal world. Such values may be\n\n- inputs and outputs of interface operations and notifications\n\n- inputs and outputs of workflows\n\n- inputs and outputs of service templates\n\nFrom the perspective of the TOSCA orchestrator such parameters are\neither \u201cincoming\u201d (i.e. transferring a value from the external world to\nthe orchestrator) or \u201coutgoing\u201d (transferring a value from the\norchestrator to the external world). Thus:\n\n- outgoing parameters are:\n\n<!-- -->\n\n- template outputs\n\n- internal workflow outputs\n\n- external workflow inputs\n\n- operation inputs\n\n<!-- -->\n\n- incoming parameters are:\n\n<!-- -->\n\n- template inputs\n\n- internal workflow inputs\n\n- external workflow outputs\n\n- operation outputs\n\n- notification outputs\n\nAn \u201coutgoing\u201d parameter definition is essentially the same as a TOSCA\nproperty definition, however it may optionally inherit the data type of\nthe value assigned to it rather than have an explicit data type defined.\n\nAn \u201cincoming\u201d parameter definition may define an attribute mapping of\nthe parameter value to an attribute of a node. Optionally, it may\ninherit the data type of the attribute it is mapped to, rather than have\nan explicit data type defined for it.\n\n#### Keynames\n\nThe TOSCA parameter definition has all the keynames of a TOSCA property\ndefinition with the following additional or changed keynames:\n\n<table>\n<colgroup>\n<col style=\"width: 14%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 10%\" />\n<col style=\"width: 61%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The data type of the parameter.</p>\n<p><strong>Note</strong>: This keyname is mandatory for a TOSCA Property\ndefinition but is not mandatory for a TOSCA Parameter\ndefinition.</p></td>\n</tr>\n<tr class=\"even\">\n<td>value</td>\n<td>no</td>\n<td>&lt;any&gt;</td>\n<td>The type-compatible value to assign to the parameter. Parameter\nvalues may be provided as the result from the evaluation of an\nexpression or a function. May only be defined for outgoing parameters.\nMutually exclusive with the \u201cmapping\u201d keyname.</td>\n</tr>\n<tr class=\"odd\">\n<td>mapping</td>\n<td>no</td>\n<td><a href=\"#attribute-selection-format\">attribute selection\nformat</a></td>\n<td>A mapping that specifies the node or relationship attribute into\nwhich the returned output value must be stored. May only be defined for\nincoming parameters. Mutually exclusive with the \u201cvalue\u201d keyname.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nParameter definitions have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">parameter_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">parameter_type</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parameter_description</a>&gt;</p>\n<p>value: &lt;parameter_value&gt; | { &lt;parameter_value_expression&gt;\n}</p>\n<p>required: &lt;<a\nhref=\"#TYPE_YAML_BOOLEAN\">parameter_required</a>&gt;</p>\n<p>default: &lt;parameter_default_value&gt;</p>\n<p>status: &lt;<a\nhref=\"#move-this-in-the-metadata-in-a-recommended-metadata-section-for-profile-writing.status-values\">status_value</a>&gt;</p>\n<p>validation: &lt;<a\nhref=\"#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition\">parameter_validation_clause</a>&gt;</p>\n<p>key_schema: &lt;key_schema_definition&gt;</p>\n<p>entry_schema: &lt;entry_schema_definition&gt;</p>\n<p>mapping: &lt;<a\nhref=\"#attribute-selection-format\">attribute_selection_form</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe following single-line grammar is supported when only a fixed value\nneeds to be provided provided to an outgoing parameter:\n\n| \\<[parameter_name](#TYPE_YAML_STRING)\\>: \\<parameter_value\\> \\| { \\<parameter_value_expression\\> } |\n|----------------------------------------------------------------------------------------------------|\n\nThis single-line grammar is equivalent to the following:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">parameter_name</a>&gt;:</p>\n<p>value: &lt;parameter_value&gt; | { &lt;parameter_value_expression&gt;\n}</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe following single-line grammar is supported when only a parameter to\nattribute mapping needs to be provided to an incoming parameter:\n\n| \\<[parameter_name](#TYPE_YAML_STRING)\\>: \\<[attribute_selection_form](#attribute-selection-format)\\> |\n|------------------------------------------------------------------------------------------------------|\n\nThis single-line grammar is equivalent to the following:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">parameter_name</a>&gt;:</p>\n<p>mapping: &lt;<a\nhref=\"#attribute-selection-format\">attribute_selection_form</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nNote that the context of the parameter definition unambiguously\ndetermines if the parameter is an incoming or an outgoing parameter.\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- parameter_name: represents the mandatory symbolic name of the\n  parameter as a [string](#TYPE_YAML_STRING).\n\n- parameter_description: represents the optional\n  [description](#TYPE_YAML_STRING) of the parameter.\n\n- parameter_type: represents the optional data type of the parameter.\n  Note, this keyname is mandatory for a TOSCA Property definition, but\n  is not for a TOSCA Parameter definition.\n\n- parameter_value, parameter_value_expresssion: represent the\n  type-compatible value to assign to the parameter. Parameter values may\n  be provided as the result from the evaluation of an expression or a\n  function.\n\n<!-- -->\n\n- once the value keyname is defined, the parameter cannot be further\n  refined or assigned.\n\n- the value keyname is relevant only for \u201coutgoing\u201d parameter\n  definitions and SHOULD NOT be defined in \u201cincoming\u201d parameter\n  definitions.\n\n<!-- -->\n\n- parameter_required: represents an optional\n  [boolean](#TYPE_YAML_BOOLEAN) value (true or false) indicating whether\n  or not the parameter is required. If this keyname is not present on a\n  parameter definition, then the parameter SHALL be considered required\n  (i.e., true) by default.\n\n- default_value: contains a type-compatible value that may be used as a\n  default if not provided by other means.\n\n<!-- -->\n\n- the default keyname SHALL NOT be defined for parameters that are not\n  required (i.e. parameter_required is \u201cfalse\u201d) as they will stay\n  undefined.\n\n<!-- -->\n\n- status_value: a [string](#TYPE_YAML_STRING) that contains a keyword\n  that indicates the status of the parameter relative to the\n  specification or implementation.\n\n- parameter_validation_clause: represents the optional [validation\n  clause](#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition)\n  on the parameter definition.\n\n- key_schema_definition: if the parameter_type is map, represents the\n  optional schema definition for the keys used to identify entries in\n  that map. Note that if the key_schema is not defined, the key_schema\n  defaults to string.\n\n- entry_schema_definition: if the parameter_type is map or list,\n  represents the mandatory schema definition for the entries in that map\n  or list.\n\n- attribute_selection_form: a list that corresponds to a valid\n  attribute_selection_format; the parameter is mapped onto an attribute\n  of the containing entity\n\n<!-- -->\n\n- the mapping keyname is relevant only for \u201cincoming\u201d parameter\n  definitions and SHOULD NOT be defined in \u201coutgoing\u201d parameter\n  definitions.\n\n#### Refinement rules\n\nA parameter definition within interface types, interface definitions in\nnode and relationship types, uses the following refinement rules when\nthe containing entity type is derived:\n\n- type: must be derived from (or the same as) the type in the parameter\n  definition in the parent entity type definition.\n\n- description: a new definition is unrestricted and will overwrite the\n  one inherited from the parameter definition in the parent entity type\n  definition.\n\n- required: if defined to \u201cfalse\u201d in the parameter definition parent\n  entity type it may be redefined to \u201ctrue\u201d; note that if undefined it\n  is automatically considered as being defined to \u201ctrue\u201d.\n\n- default: a new definition is unrestricted and will overwrite the one\n  inherited from the parameter definition in the parent entity type\n  definition (note that the definition of a default value is only\n  allowed if the required keyname is (re)defined as \u201ctrue\u201d).\n\n- value: if undefined in the parameter definition in the parent entity\n  type, it may be defined to any type-compatible value; once defined,\n  the parameter cannot be further refined or assigned\n\n<!-- -->\n\n- the value keyname should be defined only for \u201coutgoing\u201d parameters.\n\n<!-- -->\n\n- mapping: if undefined in the parameter definition in the parent entity\n  type, it may be defined to any type-compatible attribute mapping; once\n  defined, the parameter cannot be further refined or mapped\n\n<!-- -->\n\n- the mapping keyname should be defined only for \u201cincoming\u201d parameters.\n\n<!-- -->\n\n- status: a new definition is unrestricted and will overwrite the one\n  inherited from the parameter definition in the parent entity type\n  definition.\n\n- validation: a new definition is unrestricted; this validation clause\n  does not replace the validation clause defined in the parameter\n  definition in the parent entity type but is considered in addition to\n  it.\n\n- key_schema: if defined in the parameter definition in the parent\n  entity type it may be refined according to schema refinement rules.\n\n- entry_schema: if defined in the parameter definition in the parent\n  entity type it may be refined according to schema refinement rules.\n\n- metadata: a new definition is unrestricted and will overwrite the one\n  inherited from the parameter definition in the parent entity type\n  definition.\n\n#### Additional requirements\n\n- A parameter **SHALL** be considered <u>required by default</u> (i.e.,\n  as if the required keyname on the definition is set to true) unless\n  the definition\u2019s required keyname is explicitly set to false.\n\n- The value provided on a parameter definition\u2019s default keyname\n  **SHALL** be type compatible with the type declared on the\n  definition\u2019s type keyname.\n\n#### Example\n\nThe following represents an example of an input parameter definition\nwith a validation clause:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>inputs:</p>\n<p>cpus:</p>\n<p>type: integer</p>\n<p>description: Number of CPUs for the server.</p>\n<p>validation: { $valid_values: [ $value, [ 1, 2, 4, 8 ] ] }</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe following represents an example of an (untyped) output parameter\ndefinition:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p><span class=\"comment-start\" id=\"1033\"\ndata-author=\"Jacques Durand\" data-date=\"2015-08-25T21:52:00Z\">In v1.0,\noutput parameters are associated with Plans or operations. The semantics\nof having \u201coutputs\u201d defined here in at the top of a topology, should be\nclarified: are we saying that these outputs are automatically settled\nafter some initial deployment/provisioning of a new instance? Who is\nsupposed to use these \u201coutputs\u201d? Can a single node define its own\noutputs, available as soon as this node is deployed? Could these outputs\nchange e.g. after some reconfiguration of the instance?</span><span\nclass=\"comment-start\" id=\"1034\" data-author=\"Thomas Spatzier\"\ndata-date=\"2016-01-13T09:39:00Z\">Compared to v1.0 those outputs kind of\ncorrespond to the Properties in the BoundaryDefinitiions of a\nServiceTemplate.<br />\nIt represents data that you want to expose to the user of the template\nto avoid him having to scan the internals of the template in order to\nget information important to him (like a web URL).<br />\nThis features becomes important also for nested templates (I am working\non it).<br />\nSingle nodes cannot expose outputs. It is a decision of the template\nauthor which ones shall be exposed outside of the template.<br />\nAnd yes, the values could change, since they are linked to node\nproperties.</span>outputs<span class=\"comment-end\" id=\"1033\"><span\nclass=\"comment-end\" id=\"1034\"></span></span>:</p>\n<p>server_ip:</p>\n<p>description: The private IP address of the provisioned server.</p>\n<p>value: { $get_attribute: [ my_server, private_<span\nclass=\"comment-start\" id=\"1035\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-07-27T18:57:00Z\">Needs to be discussed in the context of\nsubstitution mapping</span>address<span class=\"comment-end\"\nid=\"1035\"></span> ] }</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Parameter value assignment\n\nThis section defines the grammar for assigning values to \u201coutgoing\u201d\nparameters in TOSCA templates.\n\n#### Keynames\n\nThe TOSCA parameter value assignment has no keynames.\n\n#### Grammar\n\nParameter value assignments have the following grammar:\n\n| \\<parameter_name\\>: \\<parameter_value\\> \\| { \\<parameter_value_expression\\> } |\n|-------------------------------------------------------------------------------|\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- parameter_name: represents the symbolic name of the parameter to\n  assign; note that in some cases, even parameters that do not have a\n  corresponding definition in the entity type of the entity containing\n  them may be assigned (see e.g. inputs and outputs in interfaces).\n\n- parameter_value, parameter_value_expression: represent the\n  type-compatible value to assign to the parameter. Parameter values may\n  be provided as the result from the evaluation of an expression or a\n  function.\n\n#### Additional requirements\n\n- Parameters that have a (fixed) value defined during their definition\n  or during a subsequent refinement may not be assigned (as their value\n  is already set).\n\n- If a required parameter has no value defined or assigned, its default\n  value is assigned.\n\n- A non-required parameter that has no value assigned it stays\n  undefined, thus the default keyname is irrelevant for a non-required\n  parameter.\n\n### Parameter mapping assignment\n\nA parameter to attribute mapping defines an \u201cincoming\u201d parameter value\n(e.g. an output value that is expected to be returned by an operation\nimplementation) and a mapping that specifies the node or relationship\nattribute into which the returned \u201cincoming\u201d parameter value must be\nstored.\n\n#### Keynames\n\nThe TOSCA parameter mapping assignment has no keynames.\n\n#### Grammar\n\nParameter mapping assignments have the following grammar:\n\n| \\<parameter_name\\>: \\<attribute_selection_format\\> |\n|----------------------------------------------------|\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- parameter_name: represents the symbolic name of the parameter to\n  assign; note that in some cases, even parameters that do not have a\n  corresponding definition in the entity type of the entity containing\n  them may be assigned (see e.g. inputs and outputs in interfaces).\n\n- attribute_selection_format: represents a format that is used to select\n  an attribute or a nested attribute on which to map the parameter value\n  of the incoming parameter referred by parameter_name.\n\n#### Attribute selection format\n\nThe attribute_selection_format is a list of the following format:\n\n| \\[\\<tosca_traversal_path\\>, \\<attribute_name\\>, \\<nested_attribute_name_or_index_1\\>, ..., \\<nested_attribute_name_or_index_n\\> \\] |\n|------------------------------------------------------------------------------------------------------------------------------------|\n\nThe various entities in this grammar are defined as follows:\n\n<table>\n<colgroup>\n<col style=\"width: 30%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 56%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Parameter</th>\n<th>Mandatory</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>&lt;tosca_traversal_path&gt;</td>\n<td>yes</td>\n<td><p>Using the &lt;tosca_traversal_path&gt; we can traverse the\nrepresentation graph to reach the attribute we need to store the output\nvalue into. The specification of the &lt;tosca_traversal_path&gt; is\nexplicated in section 6.1.2 get_property.</p>\n<p>Note that while the &lt;tosca_traversal_path&gt; is very powerful,\nits usage should normally be restricted to reach attributes in the local\nnode ore relationship (i.e. SELF) or in a local capability\ndefinition.</p></td>\n</tr>\n<tr class=\"even\">\n<td>&lt;attribute_name&gt;</td>\n<td>yes</td>\n<td>The name of the attribute into which the output value must be\nstored.</td>\n</tr>\n<tr class=\"odd\">\n<td>&lt;nested_attribute_name_or_index_or_key_*&gt;</td>\n<td>no</td>\n<td><p>Some TOSCA attributes are complex (i.e., composed as nested\nstructures). These parameters are used to dereference into the names of\nthese nested structures when needed.</p>\n<p>Some attributes represent list or map types. In these cases, an index\nor key may be provided to reference a specific entry in the list or map\n(identified by the previous parameter).</p></td>\n</tr>\n</tbody>\n</table>\n\nNote that it is possible for multiple operations to define outputs that\nmap onto the same attribute value. For example, a *create* operation\ncould include an output value that sets an attribute to an initial\nvalue, and the subsequence *configure* operation could then update that\nsame attribute to a new value.\n\n<span class=\"comment-start\" id=\"1050", "author": "Calin Curescu", "date": "2020-04-22T12:28:00Z", "comment": "!!! I would prefer this to be avoided, since\nit creates confusion, it\u2019s better to use the default value of a\nparameter definition for that.  \n%%% This is not allowed !!!", "target": "It is also possible that a node\ntemplate assigns a value to an attribute that has an operation output\nmapped to it (including a value that is the result of calling an\nintrinsic function). "}-->
Orchestrators could use the assigned value for the
attribute as its initial value. After the operation runs that maps an
output value onto that attribute, the orchestrator must then use the
updated value, and the value specified in the node template will no
longer be used.

#### Additional requirements

- Parameters that have a mapping defined during their definition or
  during a subsequent refinement may not be assigned (as their mapping
  is already set).

### Function syntax

TOSCA supports the use of functions for providing dynamic service data
values at runtime. The syntax of

a function has two representations:

- Any function can be represented by a YAML map with a single key, where
  the key is a string starting with a \$ (dollar sign) character and
  where the remainder of the string represents the function name. If
  present, the value in the key-value pair represents the function
  arguments.

- A function without arguments can alternatively be represented by a
  YAML string value, where the string starts with a \$ (dollar sign)
  character and where the remainder of the string represents the
  function name. This representation cannot be used in map keys.

- Function names may not contain the \$ character as it will conflict
  with the escape mechanisms described below.

Therefore, any string starting with a \$ (dollar sign) character will be
interpreted as a function call. To allow for strings starting with \$
character to be specified, the \$ character at the start of the string
needs to be escaped by using \$\$ (two dollar signs) characters instead.
For example:

- \$\$name will represent the literal string \$name

- \$\$\$item will represent the literal string \$\$item, as only the
  first \$ character is escaped.

As we could have function calls that return values to be used as keys in
a map, hypothetically it is possible that we use the same function call
as a YAML key more than once. Because YAML does not allow for duplicate
map keys, in such cases we must allow for key variation. This is
achieved by adding suffixes after the function name starting with a
second \$ character. For example, the following is a valid map where the
function “keygen” is called three times and the returned values are used
as keys in the hint map:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>hint:</p>
<p>{ $keygen: [ UUID ] }: 34</p>
<p>{ $keygen$1: [ UUID ] }: 56</p>
<p>{ $keygen$2: [ UUID ] }: 78</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

TOSCA functions may be used wherever a value is expected, such as:

- a value for a TOSCA keyname

- a value for a parameter or property or attribute, including a value
  within a complex datatype

- a value for the arguments of another function

- other places such as in validation clauses, conditions, etc.

TOSCA parsers are expected to evaluate function values at runtime based
on the provided function arguments.

The following snippet shows an example of a node template that uses a
function to retrieve a security context at runtime:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>context: { $get_security_context: { env: staging, role: admin }
}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Nested functions are supported, that is, functions can be used in the
arguments of another function. The result of the internal function will
be passed as an argument to the outer function:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>nested: {$outer_func: [{$inner_func: [iarg1, iarg2]},
oarg2]}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To allow for strings that are not function names to start with \$, the
dollar sign can be escaped by using \$\$ (two consecutive dollar
characters). The following snippet shows escaped strings in a map that
do not represent function calls:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>prop1:</p>
<p>$$myid1: myval1</p>
<p>myid2: $$myval2</p>
<p>$$myid3: $$myval3</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The arguments to the functions can be arbitrary TOSCA data, although
TOSCA defines a number of built-in functions that define
function-specific syntax for providing arguments. In addition, service
designers can optionally define custom function signatures definitions
for function arguments and function return values as specified in
section 5.4.15.

#### Parsing rule

When parsing TOSCA files, TOSCA parsers MUST identify functions wherever
values are specified using the following algorithm:

- Does the YAML string start with \$?

  - If yes, is the second character \$?

    - If yes, discard the first \$ and stop here (escape).

    - If no, is this a key in a YAML map?

      - If yes, is this the only key in a YAML map?

        - If yes, this is a function call.

        - If no, emit a parsing syntax error ("malformed function").

      - If no, this is a function call without arguments.

### Function definitions

TOSCA includes grammar for defining function signatures and associated
implementation artifacts in TOSCA profiles or in TOSCA service
templates. This allows for validation of function return values and
function arguments at design time, and the possibility to provide
function implementation artifacts within CSARs. Note that the use of
custom function definitions is entirely optional, service designers can
use custom functions without defining associated function signatures and
instead rely on support for those functions directly in the TOSCA
orchestrator that will be used to process the TOSCA files. Of course,
TOSCA processors may support custom functions that are not user-defined.

#### Keynames

The following is the list of recognized keynames for TOSCA function
definition:

| Keyname     | Mandatory | Type                                             | Description                              |
|-------------|-----------|--------------------------------------------------|------------------------------------------|
| signatures  | yes       | map of signature definitions                     | The map of signature definitions.        |
| description | no        | [[string](#TYPE_YAML_STRING)](#TYPE_YAML_STRING) | The description of the function.         |
| metadata    | no        | [map](#tosca-map-type) of metadata               | Defines additional metadata information. |

The following is the list of recognized keynames for TOSCA function
signature definition:

| Keyname            | Mandatory           | Type                       | Description                                                                                                                                                                                                                                                |
|--------------------|---------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arguments          | no                  | list of schema definitions | All defined arguments must be used in the function invocation (and in the order defined here). If no arguments are defined, the signature either accepts no argumats or any arguments of any form (depending on if the variadic keyname is false or true). |
| optional_arguments | no                  | list of schema definitions | Optional arguments may be used in the function invocation after the regular arguments. Still the order defined here must be respected.                                                                                                                     |
| variadic           | no (default: false) | boolean                    | Specifies if the last defined argument (or optional_argument if defined) may be repeated any number of times in the function invocation                                                                                                                    |
| result             | no                  | schema definition          | Defines the type of the function result. If no result keyname is defined, then the function may return any result                                                                                                                                          |
| implementation     | no                  | implementation definition  | Defines the implementation (e.g., artifact) for the function. The same definition as for operation/notification implementation is used.                                                                                                                    |

#### Grammar

Function signatures can be defined in TOSCA profiles or TOSCA service
templates using a YAML map under the functions keyname as follows. Note
that this grammar allows the definition of functions that have arguments
expressed within a YAML seq, however intrinsic functions may accept
other argument definition syntaxes.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>&lt;function_def&gt;</p>
<p>&lt;function_def&gt;</p>
<p>...</p>
<p>&lt;function_def&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Each \<function_def\> defines the name of a function with an associated
list of signature definitions as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;function_name&gt;:</p>
<p>signatures:</p>
<p>- &lt;signature_def&gt;</p>
<p>- &lt;signature_def&gt;</p>
<p>- &lt;signature_def&gt;</p>
<p>...</p>
<p>- &lt;signature_def&gt;</p>
<p>description: &lt;string&gt;</p>
<p>metadata: &lt;map_of_metadata&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Only the signatures keyname is mandatory and must provide at least one
signature
definition
<!----
{"id": "1055", "author": "Calin Curescu", "date": "2022-09-20T16:21:00Z", "comment": "Put an example of an empty signature that\nmeans the function takes no parameters and my return any result. Put\nalso of this example with variadic: true.", "target": "signature\ndefinition"}-->
. Note that the
signatures are tested in the order of their definition. The first
matching implementation is used.

Each \<signature_def\> is a map of following keywords definitions:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>arguments:</p>
<p>- &lt;schema_def&gt;</p>
<p>- &lt;schema_def&gt;</p>
<p>...</p>
<p>- &lt;schema_def&gt;</p>
<p>optional_arguments:</p>
<p>- &lt;schema_def&gt;</p>
<p>- &lt;schema_def&gt;</p>
<p>...</p>
<p>- &lt;schema_def&gt;</p>
<p>variadic: &lt;boolean&gt;</p>
<p>result: &lt;schema_def&gt;</p>
<p>implementation: &lt;implementation_def&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

None of the keynames in the signature definition are mandatory.

The keynames have the following meaning:

- The arguments keyname defines the type and the position of the
  function arguments. All defined arguments must be used in the function
  invocation (and in the order defined here).

  - The full flexibility of the schema definition for types can be used.

- The optional_arguments keyname defines the type and the position of
  the function arguments. Optional arguments may be used in the function
  invocation after the regular arguments. Still the order defined here
  must be respected (that is, if m out of n of the optional arguments
  are used, they will correspond to the first m \<schema_def\>).

  - The full flexibility of the schema definition for types can be used.

- The result keyname defines the type of the function result.

  - Again, the full flexibility of the schema definition for types can
    be used.

  - If no result keyname is defined, then the function may return any
    result.

- The variadic keyname defines if the last defined argument may be
  repeated any number of times in the function invocation.

  - If variadic is true, the last defined argument may be repeated any
    number of times in the function invocation (on the last positions).

    - If optional_arguments is defined, then the last defined argument
      is the last defined optional_argument. Note that in this case we
      have a 0+ usage of the last argument.

    - If optional_arguments is not defined, then the last defined
      argument is the last defined regular argument. Note that in this
      case we have a 1+ usage of the last argument.

  - If variadic is false, the last argument definition has no special
    semantics.

  - If the arguments list is empty or not defined:

    - If variadic is false, the function is not accepting any arguments.

    - If variadic is true, the function is considered to accept any
      numbers of arguments of any type or form.

  - Default value of variadic is false.

- The implementation keyname defines the implementation (e.g., artifact)
  for the function.

  - The same definition as for operation/notification implementation is
    used.

  - If no implementation is specified, then it's assumed that the TOSCA
    processor is preconfigured to handle the function call.

  - Note that several signatures of a function (or even of several
    functions) may refer to the same implementation in the
    implementation definition.

The functions section can be defined both outside and/or inside a
service_template section:

- Function definitions outside a service_template can be within a
  profile TOSCA file or imported TOSCA file

  - Namespacing works as for types. Overlapping definitions under the
    same \<function_name\> are not allowed.

  - Note that in that case the \$ (dollar sign) character will be put in
    front of the namespace name. For example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>rnd_nr: { $namespace1:random_generator: [ seed ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Function definitions inside a service_template that are having the
  same \<function_name\> are considered a refinement of the homonymous
  definition outside the service_template, see refinement rules below.

- For example, this would allow for two separated design moments in
  function design:

  - At profile design time (outside the service_template), when e.g. the
    arguments and the result is defined and thus the function can be
    correctly used in the node type definitions.

  - At service template design time (inside the service_template), when
    function implementation references within a current CSAR can be
    decided, and thus the implementation or the description may be added
    or changed.

  - Note also that we could have the whole definition in the service
    template or outside the service template, in the latter case
    defining a global implementation.

#### Refinement rules

Function definitions inside a service_template that are having the same
\<function_name\> are considered a refinement of the homonymous
definition outside the service_template.

- signatures: as a general function refinement rule, for an already
  defined signature only the implementation may be changed.

  - New function signatures may be added to the signatures list, but
    only after the refinements of the existing signatures.

  - If an existing signature is not refined, an empty element must be
    used at the relevant location in the list.

- description: a new definition is unrestricted and will overwrite the
  one inherited from the function definition outside the
  service_template.

- metadata: a new definition is unrestricted and will overwrite the one
  inherited from the function definition outside the service_template.

#### Examples

##### Square root function with several signatures

The following example shows the definition of a square root function:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  sqrt:</p>
<p>signatures:</p>
<p>    - arguments:</p>
<p>       - type: integer</p>
<p>validation: { $greater_or_equal: [ $value, 0 ] }</p>
<p>       result:</p>
<p>         type: float</p>
<p>      implementation: scripts/sqrt.py</p>
<p>    - arguments:</p>
<p>      - type: float</p>
<p>validation: { $greater_or_equal: [ $value, 0.0 ] }</p>
<p>      result:</p>
<p>        type: float</p>
<p>      implementation: scripts/sqrt.py</p>
<p>description: &gt;</p>
<p>This is a square root function that defines two signatures:</p>
<p>the argument is either integer or float and the function</p>
<p>returns the suare root as a float.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The next sqrt is similar to above, but uses a simplified type notation
(in this short form no validation clause can be expressed):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  sqrt:</p>
<p>signatures:</p>
<p>      - arguments: [ integer ]</p>
<p>        result: float</p>
<p>        implementation: scripts/sqrt.py</p>
<p>      - arguments: [ float ]</p>
<p>        result: float</p>
<p>        implementation: scripts/sqrt.py</p>
<p>description: &gt;</p>
<p>This is a square root function that defines two signatures:</p>
<p>the argument is either integer or float and the function</p>
<p>returns the suare root as a float.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Function with list of arguments

The following example shows a function that takes a list of arguments
with different types:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  my_func_with_different_argument_types:</p>
<p>signatures:</p>
<p>    - arguments:</p>
<p>- type: MyType1</p>
<p>description: "this is the first argument ..."</p>
<p>- type: string</p>
<p>description: "this is the second argument ..."</p>
<p>- type: string</p>
<p>description: "this is the third argument ..."</p>
<p>- type: MyType2</p>
<p>description: "this is the argument that can be repeated ..."</p>
<p>      variadic: true</p>
<p>      result:</p>
<p>type: MyTypeRez</p>
<p>      implementation: scripts/my.py</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Same as the above, but in compact notation:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  my_func_with_different_argument_types:</p>
<p>signatures:</p>
<p>    - arguments: [MyType1, string, string, MyType2]</p>
<p>      variadic: true</p>
<p>      result: MyTypeRez</p>
<p>      implementation: scripts/my.py</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Function with no arguments

The arguments list can be empty or completely missing. In such a case,
when using the function the arguments will be an empty list:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  get_random_nr:</p>
<p>signatures:</p>
<p>      - result: float</p>
<p>        implementation: scripts/myrnd.py</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Function with polymorphic arguments/result inside of lists

Function signatures with different types within the arguments and result
lists:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>  union:</p>
<p>signatures:</p>
<p>     - arguments:</p>
<p>        - type: list</p>
<p>          entry_schema: integer</p>
<p>   variadic: true</p>
<p>        result:</p>
<p>          type: list</p>
<p>          entry_schema: integer</p>
<p>        implementation: scripts/libpi.py</p>
<p>      - arguments:</p>
<p>        - type: list</p>
<p>          entry_schema: float</p>
<p>   variadic: true</p>
<p>        result:</p>
<p>          type: list</p>
<p>          entry_schema: float</p>
<p>        implementation: scripts/libpi.py</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### Defining a list in a map argument

The following shows the use of a argument that is a map of lists of
MyType:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>functions:</p>
<p>complex_arg_function:</p>
<p>signatures:</p>
<p>- arguments:</p>
<p>- type: map</p>
<p>key_schema: string</p>
<p>entry_schema:</p>
<p>type: list</p>
<p>entry_schema: MyType</p>
<p>      result: string</p>
<p>      implementation: scripts/complex.py</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##### User-defined function usage

The following shows more examples of function usage. Note that in the
usage of the polymorphic union function, the TOSCA parser knows to
identify the right signature via the types of the function arguments.
Also note the usage of a user-defined function with no parameters; an
empty list is used for the arguments.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>properties:</p>
<p>integer_union: {$union: [[1, 7], [3, 4, 9], [15, 16]]}</p>
<p>float_union: {$union: [[3.5, 8.8], [1.3]]}</p>
<p>rnd: {$get_random_nr: []}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Substitution
------------

### Substitution mapping

A substitution mapping allows a given service template to be used as an
implementation of abstract node templates of a specific node type. This
allows the consumption of complex systems using a simplified vision.

#### Keynames

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>node_type</td>
<td>yes</td>
<td>string</td>
<td>The mandatory name of the Node Type the service template is
providing an implementation for.</td>
</tr>
<tr class="even">
<td>substitution_filter</td>
<td>no</td>
<td><a href="#node-filter-definition">node filter</a></td>
<td>The optional filter that further constrains the abstract node
templates for which this service template can provide an
implementation.</td>
</tr>
<tr class="odd">
<td>properties</td>
<td>no</td>
<td>map of property mappings</td>
<td>The optional map of properties mapping allowing to map properties of
the node_type to inputs of the service template.</td>
</tr>
<tr class="even">
<td>attributes</td>
<td>no</td>
<td>map of attribute mappings</td>
<td>Keynames
<!----
{"id": "1061\" data-author=\"Michael Rehder\"\ndata-date=\"2020-12-15T16:45:00Z\">If these are optional, what happens if\nthey are not defined?<br />\nIs there an assumption of name match across the node type and topology\ntemplate inputs?<br />\nThis needs to be described.</span>The optional map of attribute mappings\nallowing to map outputs from the service template to attributes of the\nnode_type.<span class=\"comment-end\" id=\"1061\"></span></td>\n</tr>\n<tr class=\"odd\">\n<td>capabilities</td>\n<td>no</td>\n<td>map of capability mappings</td>\n<td>The optional map of capabilities mapping.</td>\n</tr>\n<tr class=\"even\">\n<td>requirements</td>\n<td>no</td>\n<td>map of requirement mappings</td>\n<td>The optional map of requirements mapping.</td>\n</tr>\n<tr class=\"odd\">\n<td>interfaces</td>\n<td>no</td>\n<td>map of interfaces mappings</td>\n<td>The optional map of interface mapping allows to map an interface and\noperations of the node type to implementations that could be either\nworkflows or node template interfaces/operations.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nThe grammar of the substitution_mapping section is as follows:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_type: &lt;<a\nhref=\"#TYPE_YAML_STRING\">node_type_name</a>&gt;</p>\n<p>substitution_filter\u00a0: &lt;node_filter&gt;</p>\n<p>properties:</p>\n<p>&lt;property_mappings&gt;</p>\n<p>capabilities:</p>\n<p>&lt;capability_mappings&gt;</p>\n<p>requirements:</p>\n<p>&lt;requirement_mappings&gt;</p>\n<p>attributes:</p>\n<p>&lt;attribute_mappings&gt;</p>\n<p>interfaces:</p>\n<p>&lt;interface_mappings&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- node_type_name: represents the mandatory Node Type name that the\n  Service Template is offering an implementation for.\n\n- node_filter: represents the optional node filter that reduces the set\n  of abstract node templates for which this service template is an\n  implementation by only substituting for those node templates whose\n  properties and capabilities satisfy the condition expression specified\n  in the node filter.\n\n- **properties**: represents the \\<optional\\> map of properties\n  mappings.\n\n- **capability_mappings**: represents the \\<optional\\> map of capability\n  mappings.\n\n- **requirement_mappings**: represents the \\<optional\\> map of\n  requirement mappings.\n\n- **attributes**: represents the \\<optional\\> map of attributes\n  mappings.\n\n- **interfaces:** represents the \\<optional\\> map of interfaces\n  mappings.\n\n#### Examples\n\n#### Additional requirements\n\n- The substitution mapping MUST provide mapping for every property,\n  capability and requirement defined in the specified \\<node_type\\>\n\n#### Notes\n\n- The node_type specified in the substitution mapping SHOULD be abstract\n  (does not provide implementation for normative operations).\n\n### Property mapping\n\nA property mapping allows to map the property of a substituted node type\nto an input of the service template.\n\n#### Keynames\n\nThe following is the list of recognized keynames for a TOSCA property\nmapping:\n\n| Keyname | Mandatory | Type                               | Description                                                                                                                                   |\n|---------|-----------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|\n| mapping | no        | list of strings                    | An array with 1 string element that references an input of the service.                                                                       |\n| value   | no        | matching the type of this property | This **deprecated** keyname allows to explicitly assigne a value to this property. This field is mutually exclusive with the mapping keyname. |\n\n#### Grammar\n\nThe single-line grammar of a property_mapping is as follows:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;property_name&gt;: <span class=\"comment-start\" id=\"1076\"\ndata-author=\"Luc Boutier\" data-date=\"2017-06-13T14:05:00Z\">Do we want to\nallow such definition for non-list properties ?<br />\nSuch notation will be prohibited for list properties values to avoid\ncollision with the single line grammar of a node property\nmapping.</span>&lt;property_value&gt;<span class=\"comment-end\"\nid=\"1076\"></span> # This use is deprecated</p>\n<p>&lt;property_name&gt;: [ &lt;input_name&gt; ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe multi-line grammar is as follows\u00a0:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;property_name&gt;:</p>\n<p>mapping: [ &lt; input_name &gt; ]</p>\n<p>&lt;property_name&gt;:</p>\n<p>value: &lt;property_value&gt; # This use is deprecated</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n#### Notes\n\n- Single line grammar for a property value assignment is not allowed for\n  properties of type in order to avoid collision with the mapping single\n  line grammar.\n\n- The property_value mapping grammar has been deprecated. The original\n  intent of the *property-to-constant-value* mapping was not to provide\n  a *mapping*, but rather to present a *matching* mechanism to drive\n  selection of the appropriate substituting template when more than one\n  template was available as a substitution for the abstract node. In\n  that case, a service template was only a valid candidate for\n  substitution if the property value in the abstract node template\n  matched the constant value specified in the property_value mapping for\n  that property. With the introduction of substitution filter syntax to\n  drive matching, there is no longer a need for the\n  property-to-constant-value mapping functionality.\n\n- The previous version of the specification allowed direct mappings from\n  properties of the abstract node template to properties of node\n  templates in the substituting service template. Support for these\n  mappings has been deprecated since they would have resulted in\n  unpredictable behavior, for the following reason. If the substituting\n  template is a valid TOSCA template, then all the (required) properties\n  of all its node templates must have valid property assignments already\n  defined. If the substitution mappings of the substituting template\n  include direct property-to-property mappings, the the substituting\n  template ends up with two conflicting property assignments: one\n  defined in the substituting template itself, and one defined by the\n  substitution mappings. These conflicting assignments lead to\n  unpredictable behavior.\n\n#### Additional constraints\n\n- When Input mapping it may be referenced by multiple nodes in the\n  topologies with resulting attributes values that may differ later on\n  in the various nodes. In any situation, the attribute reflecting the\n  property of the substituted type will remain a constant value set to\n  the one of the input at deployment time.\n\n### Attribute mapping\n\nAn attribute mapping allows to map the attribute of a substituted node\ntype an output of the service template.\n\n#### Keynames\n\nThe following is the list of recognized keynames for a TOSCA attribute\nmapping:\n\n| Keyname | Mandatory | Type            | Description                                                              |\n|---------|-----------|-----------------|--------------------------------------------------------------------------|\n| mapping | no        | list of strings | An array with 1 string element that references an output of the service. |\n\n#### Grammar\n\nThe single-line grammar of an attribute_mapping is as follows:\n\n| \\<attribute_name\\>: \\[ \\<output_name\\> \\] |\n|-------------------------------------------|\n\n### Capability mapping\n\nA capability mapping allows to map the capability of one of the nodes of\nthe service template to the capability of the node type the service\ntemplate offers an implementation for.\n\n#### <span class=\"comment-start\" id=\"1091", "author": "Calin Curescu [2]", "date": "2018-08-23T07:37:00Z", "comment": "Here at the end we should add also the occurences keyname that should allow assignement as for properties and attributes (see capability assignment changes to be made)", "target": "Keynames"}-->


The following is the list of recognized keynames for a TOSCA capability
mapping:

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>mapping</td>
<td>no</td>
<td>list of strings (with 2 members)</td>
<td>A list of strings with 2 members, the first one being the name of a
node template, the second the name of a capability of the specified node
template.</td>
</tr>
<tr class="even">
<td>properties</td>
<td>no</td>
<td>Keynames
<!----
{"id": "1092\" data-author=\"Luc Boutier\"\ndata-date=\"2017-06-13T14:31:00Z\">Do we want to allow the usage of\nproperty mapping ?<br />\nTo map properties of various nodes, capabilities from within the\ntemplate to create the capability ?</span>map of property\nassignment<span class=\"comment-end\" id=\"1092\"></span>s</td>\n<td><span class=\"comment-start\" id=\"1093\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-08-03T18:25:00Z\">This needs to be cleaned up since it is\nwrong. This is an oversight left over from 1.3</span>This field is\nmutually exclusive<span class=\"comment-end\" id=\"1093\"></span> with the\nmapping keyname and allows to provide a capability <span\nclass=\"comment-start\" id=\"1094\" data-author=\"Chris Lauwers\"\ndata-date=\"2020-08-03T18:20:00Z\">What is the direction of the property\nmapping? Value of abstract node is propagated to substituting template,\nor the other way around?</span>assignment<span class=\"comment-end\"\nid=\"1094\"></span> for the <span class=\"comment-start\" id=\"1095\"\ndata-author=\"Chris Lauwers\" data-date=\"2020-08-03T18:22:00Z\">Should we\nsupport mapping of properties of capabilities to inputs of the\nsubstituting template?</span>template<span class=\"comment-end\"\nid=\"1095\"></span> and specify it\u2019s related properties.</td>\n</tr>\n<tr class=\"odd\">\n<td>attributes</td>\n<td>no</td>\n<td>map of attributes assignments</td>\n<td>This field is mutually exclusive with the mapping keyname and allows\nto provide a capability assignment for the template and specify it\u2019s\nrelated attributes.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nThe single-line grammar of a capability_mapping is as follows:\n\n| \\<capability_name\\>: \\[ \\<node_template_name\\>, \\<node_template_capability_name\\> \\] |\n|--------------------------------------------------------------------------------------|\n\nThe multi-line grammar is as follows\u00a0:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;capability_name&gt;:</p>\n<p>mapping: [ &lt;node_template_name&gt;,\n&lt;node_template_capability_name&gt; ]</p>\n<p>properties:</p>\n<p>&lt;property_name&gt;: &lt;property_value&gt;</p>\n<p>attributes:</p>\n<p>&lt;attribute_name&gt;: &lt;attribute_value&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- capability_name: represents the name of the capability as it appears\n  in the Node Type definition for the Node Type (name) that is declared\n  as the value for on the substitution_mappings\u2019 \u201cnode_type\u201d key.\n\n- node_template_name: represents a valid name of a Node Template\n  definition (within the same service_template declaration as the\n  substitution_mapping is declared).\n\n- node_template_capability_name: represents a valid name of a\n  [capability definition](#capability-definition) within the\n  \\<node_template_name\\> declared in this mapping.\n\n- property_name: represents the name of a property of the capability.\n\n- property_value: represents the value to assign to a property of the\n  capability.\n\n- attribute_name: represents the name a an attribute of the capability.\n\n- attribute_value: represents the value to assign to an attribute of the\n  capability.\n\n### Requirement mapping\n\nA requirement mapping allows to map the requirement of one of the nodes\nof the service template to the requirement of the node type the service\ntemplate offers an implementation for.\n\n#### <span class=\"comment-start\" id=\"1102", "author": "Calin Curescu [2]", "date": "2018-08-23T07:47:00Z", "comment": "The properties and attributes are totally wrong here as a requirement does not have them. One should not be able to assign a requirement without having a real dependency to match. The last two rows should be deleted!", "target": "Keynames"}-->


The following is the list of recognized keynames for a TOSCA requirement
mapping:

| Keyname    | Mandatory | Type                          | Description                                                                                                                                                                                                                                                                                                            |
|------------|-----------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mapping    | no        | list of strings (2 members)   | A list of strings with 2 elements, the first one being the name of a node template, the second the name of a requirement of the specified node template.                                                                                                                                                               |
| properties | no        | List of property assignment   | This field is mutually
<!----
{"id": "1103", "author": "Chris Lauwers", "date": "2020-08-03T18:36:00Z", "comment": "These need to be removed.", "target": "mutually"}-->
 exclusive with the mapping keyname and allow to provide a requirement for the template and specify it’s related properties. |
| attributes | no        | List of attributes assignment | This field is mutually exclusive with the mapping keyname and allow to provide a requirement for the template and specify it’s related attributes.                                                                                                                                                                     |

#### Grammar

The single-line grammar of a requirement_mapping is as follows:

| \<requirement_name\>: \[ \<node_template_name\>, \<node_template_requirement_name\> \] |
|----------------------------------------------------------------------------------------|

The multi-line grammar is as follows :

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;requirement_name&gt;:</p>
<p>mapping: [ &lt;node_template_name&gt;,
&lt;node_template_requirement_name&gt; ]</p>
<p>properties:</p>
<p>&lt;property_name&gt;: &lt;property_value&gt;</p>
<p>attributes:</p>
<p>&lt;attribute_name&gt;: &lt;attribute_value&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- requirement_name: represents the name of the requirement as it appears
  in the Node Type definition for the Node Type (name) that is declared
  as the value for on the substitution_mappings’ “node_type” key.

- node_template_name: represents a valid name of a Node Template
  definition (within the same service_template declaration as the
  substitution_mapping is declared).

- node_template_requirement_name: represents a valid name of a
  requirement definition within the \<node_template_name\> declared in
  this mapping.

- property_name: represents the name of a property of the requirement.

- property_value: represents the value to assign to a property of the
  requirement.

- attribute_name: represents the name of an attribute of the
  requirement.

- attribute_value: represents the value to assign to an attribute of the
  requirement.

### Interface mapping

An interface mapping allows to map a workflow of the service template to
an operation of the node type the service template offers an
implementation for.

#### Grammar
<!----
{"id": "1110", "author": "Calin Curescu [2]", "date": "2018-08-23T08:33:00Z", "comment": "This could change if we introduce the operations keyname in the interface definitions", "target": "Grammar"}-->


The grammar of an interface_mapping is as follows
<!----
{"id": "1111", "author": "Chris Lauwers", "date": "2020-08-03T18:40:00Z", "comment": "What about\nnotification mappings?", "target": "follows"}-->
:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;interface_Policies
<!----
{"id": "1112\"\ndata-author=\"Chris Lauwers\" data-date=\"2020-08-03T18:41:00Z\">Do we need\nto add support for mapping operation name to an operation on a node in\nthe substituting template?</span>name<span class=\"comment-end\"\nid=\"1112\"></span>&gt;:</p>\n<p>&lt;operation_name&gt;: &lt;workflow_name&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- **interface_name:** represents the name of the interface as it appears\n  in the Node Type definition for the Node Type (name) that is declared\n  as the value for on the substitution_mappings\u2019 \u201cnode_type\u201d key. Or the\n  name of a new management interface to add to the generated type.\n\n- **operation_name:** represents the name of the operation as it appears\n  in the interface type definition.\n\n- **workflow_name:** represents the name of a workflow of the template\n  to map to the specified operation.\n\n#### Notes\n\n- Declarative workflow generation will be applied by the TOSCA\n  orchestrator after the service template have been substituted. Unless\n  one of the normative operations of the standard interface is mapped\n  through an interface mapping. In that case the declarative workflow\n  generation will consider the substitution node as any other node\n  calling the create, configure and start mapped workflows as if they\n  where single operations.\n\n- Operation implementation being TOSCA workflows the TOSCA orchestrator\n  replace the usual operation_call activity by an inline activity using\n  the specified workflow.\n\nGroups and <span class=\"comment-start\" id=\"1117", "author": "Chris Lauwers", "date": "2021-01-17T02:44:00Z", "comment": "Language suggested by Paul Jordan: In TOSCA Policy is used to affect or govern an application or service\u2019s topology at some stage of its lifecycle, but is not explicitly part of the topology itself. The policy scope can be limited to a collection of Nodes or Node Types by using Groups and Group Types.", "target": "Policies"}-->

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Group Type

A Group Type defines logical grouping types for nodes, typically for
different management purposes. Conceptually, group definitions allow the
creation of logical
“membership” relationships 
<!----
{"id": "1121", "author": "Chris Lauwers", "date": "2020-08-03T18:44:00Z", "comment": "Edit to remove the implication that these\nare similar to \u201cTOSCA relationships\u201d", "target": "creation of logical\n\u201cmembership\u201d relationships "}-->
to
nodes in a service template that are not a part of the application’s
explicit requirement dependencies in the service template (i.e. those
required to actually get the application deployed and running). Instead,
such logical membership allows for the introduction of things such as
group management and uniform application of policies (i.e. requirements
that are also not bound to the application itself) to the group’s
members
<!----
{"id": "1122", "author": "Chris Lauwers", "date": "2021-01-17T02:47:00Z", "comment": "Alternative language suggested by PJ: A\nGroup Type defines logical grouping types for nodes for purposes of\nuniform application of policies to collections of nodes. Conceptually,\ngroup definitions allow the creation of logical \u201cmembership\u201d\nrelationships to nodes in a service template that are not a part of the\napplication\u2019s explicit requirement dependencies in the topology template\n(i.e. those required to actually get the application deployed and\nrunning). Instead, such logical membership allows for the introduction\nof things such as group management and uniform application of policies\n(i.e. requirements that are also not bound to the application itself) to\nthe group\u2019s members.", "target": "members"}-->
. .
<!----
{"id": "1123", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T08:56:00Z", "comment": "I don\u2019t think\nthe text definitions of group and group type are sufficiently different.\nSo I\u2019ve added some suggested new text but will leave it to the editors\nto consider how much of the existing text can be\nremoved.", "target": ""}-->


#### Keynames

The Group Type is a TOSCA type entity and has the common keynames listed
in Section 4.2.5.2 Common keynames in type definitions. In addition, the
Group Type has the following recognized keynames:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 20%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Policy definition
<!----
{"id": "1126\" data-author=\"Matt Rutkowski\"\ndata-date=\"2018-02-20T12:36:00Z\">TBD, MUSTFIX<br />\nv1.3 \u2013 We clearly need artifact defns. On yGroup defn. Do we need to add\nto Group Type (allowed) Artifact Types?<br />\nThis impacts how we allow adding Artifact defintions to Node Types\ntoday\u2026 we should not have allowed artifact defns. On Types (only Types\non Types, Defns. On Defns. Within a topology template).<br />\nChris L. has some v1.3 goals that may address these\nissues.</span>Keyname<span class=\"comment-end\" id=\"1126\"></span></th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#_Schema_Definition\">property definitions</a></p></td>\n<td>An optional map of property definitions for the Group Type.</td>\n</tr>\n<tr class=\"even\">\n<td><span class=\"comment-start\" id=\"1127\"\ndata-author=\"Chris Lauwers [2]\" data-date=\"2019-02-12T11:05:00Z\">What is\nthe use case for having properties and attributes in\ngroups?</span>attributes<span class=\"comment-end\" id=\"1127\"></span></td>\n<td>no</td>\n<td><p>map of</p>\n<p><a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute\ndefinitions</a></p></td>\n<td>An optional map of attribute definitions for the Group Type.</td>\n</tr>\n<tr class=\"odd\">\n<td>members</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>An optional list of one or more names of Node Types that are valid\n(allowed) as members of the Group Type.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nGroup Types have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">group_type_name</a>&gt;:</p>\n<p>derived_from: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parent_group_type_name</a>&gt;</p>\n<p>version: &lt;<a\nhref=\"#tosca-tal-suggests-removing-this.version\">version_number</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">group_description</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#_Schema_Definition\">property_definitions</a>&gt;</p>\n<p>attributes:</p>\n<p>&lt;<a\nhref=\"#to-implement-this-throughout-the-specification.-default-can-have-also-value_expression-i-think-we-might-need-also-an-attribute-value_expresssion-keyname-that-allows-to-define-an-attribute-as-a-function-of-a-different-attribute-of-the-same-entity-that-we-can-define-when-creating-noderelationship-types-even-before-template-design-time.attribute-definition\">attribute_definitions</a>&gt;</p>\n<p>members: [ &lt;list_of_valid_member_types&gt; ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- group_type_name: represents the mandatory symbolic name of the Group\n  Type being declared as a string.\n\n- parent_group_type_name: represents the name (string) of the Group Type\n  this Group Type definition derives from (i.e. its \u201cparent\u201d type).\n\n- version_number: represents the optional TOSCA version number for the\n  Group Type.\n\n- group_description: represents the optional description string for the\n  corresponding group_type_name.\n\n- attribute_definitions: represents the optional map of attribute\n  definitions for the Group Type.\n\n- property_definitions: represents the optional map of property\n  definitions for the Group Type.\n\n- list_of_valid_member_types: represents the optional list of TOSCA Node\n  Types that are valid member types for being added to (i.e. members of)\n  the Group Type; if the members keyname is not defined then there are\n  no restrictions to the member types;\n\n<!-- -->\n\n- note that the members of a group ultimately resolve to nodes, the\n  types here just restrict which nodes can be defined as members in a\n  group definition.\n\n- A node type is matched if it is the specified type or is derived from\n  the node type\n\n#### Derivation rules\n\nDuring Group Type derivation the keyname definitions follow these rules:\n\n- properties: existing property definitions may be refined; new property\n  definitions may be added.\n\n- attributes: existing attribute definitions may be refined; new\n  attribute definitions may be added.\n\n- members: if the members keyname is defined in the parent type, each\n  element in this list must either be in the parent type list or derived\n  from an element in the parent type list; if the members keyname is not\n  defined in the parent type then no restrictions are applied to the\n  definition.\n\n#### Example\n\nThe following represents a Group Type definition:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>group_types:</p>\n<p>mycompany.mytypes.groups.placement:</p>\n<p>description: My company\u2019s group type for placing nodes of type\nCompute</p>\n<p>members: [ tosca.nodes.Compute ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Group definition\n\nCollections of Nodes may be defined using a Group. A group definition\ndefines a logical grouping of node templates, typically for management\npurposes, but is separate from the application\u2019s service template.\n\n#### Keynames\n\nThe following is the list of recognized keynames for a TOSCA group\ndefinition:\n\n<table>\n<colgroup>\n<col style=\"width: 15%\" />\n<col style=\"width: 14%\" />\n<col style=\"width: 20%\" />\n<col style=\"width: 49%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>type</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The mandatory name of the group type the group definition is based\nupon.</td>\n</tr>\n<tr class=\"even\">\n<td>description</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\"><span>string</span></a></td>\n<td>The optional description for the group definition.</td>\n</tr>\n<tr class=\"odd\">\n<td>metadata</td>\n<td>no</td>\n<td><a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a></td>\n<td>Defines a section used to declare additional metadata\ninformation.</td>\n</tr>\n<tr class=\"even\">\n<td>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">property assignments</a></p></td>\n<td><span class=\"comment-start\" id=\"1139\" data-author=\"Michael Rehder\"\ndata-date=\"2020-12-15T16:26:00Z\">Shouldn\u2019t there be a mention of what\ncould be the source of the assignment?<br />\nThere is no \u201cinput\u201d section like in a Topology Template so what can be\nthe source definitions?</span>An optional map of property value\nassignments for the group definition.<span class=\"comment-end\"\nid=\"1139\"></span></td>\n</tr>\n<tr class=\"odd\">\n<td>attributes</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">attribute assignments</a></p></td>\n<td>An optional map of attribute value assignments for the group\ndefinition.</td>\n</tr>\n<tr class=\"even\">\n<td>members</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional list of one or more node template names that are\nmembers of this group definition.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nGroup definitions have one the following grammars:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">group_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">group_type_name</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">group_description</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#property-assignment\">property_assignments</a>&gt;</p>\n<p>attributes:</p>\n<p>&lt;<a href=\"#attribute-assignment\">attribute_assignments</a>&gt;</p>\n<p>members: [ &lt;list_of_node_templates&gt; ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- group_name: represents the mandatory symbolic name of the group as a\n  string.\n\n- group_type_name: represents the name of the Group Type the definition\n  is based upon.\n\n- group_description: contains an optional description of the group.\n\n- property_assignments: represents the optional map of property\n  assignments for the group definition that provide values for\n  properties defined in its declared Group Type.\n\n- attribute_assigments: represents the optional map of attribute\n  assignments for the group definition that provide values for\n  attributes defined in its declared Group Type.\n\n- list_of_node_templates: contains the mandatory list of one or more\n  node template names or group symbolic names (within the same service\n  template) that are members of this logical group\n\n<!-- -->\n\n- if the members keyname was defined (by specifying a\n  list_of_valid_member_types) in the group type of this group then the\n  nodes listed here must be compatible (i.e. be of that type or of type\n  that is derived from) with the node types in the\n  list_of_valid_member_types\n\n#### Example\n\nThe following represents a group definition:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>groups:</p>\n<p>my_app_placement_group:</p>\n<p>type: tosca.groups.Root</p>\n<p>description: My application\u2019s logical component grouping for\nplacement</p>\n<p>members: [ my_web_server, my_sql_database ]</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### Policy Type\n\nA Policy Type defines a type of a policy that affects or governs an\napplication or service\u2019s topology at some stage of its lifecycle but is\nnot explicitly part of the topology itself (i.e., it does not prevent\nthe application or service from being deployed or run if it did not\nexist).\n\n#### Keynames\n\nThe Policy Type is a TOSCA type entity and has the common keynames\nlisted in Section 4.2.5.2 Common keynames in type definitions. In\naddition, the Policy Type has the following recognized keynames:\n\n<table>\n<colgroup>\n<col style=\"width: 15%\" />\n<col style=\"width: 13%\" />\n<col style=\"width: 16%\" />\n<col style=\"width: 55%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"1149\" data-author=\"Chris Lauwers\"\ndata-date=\"2022-10-03T19:54:00Z\">How/where can these properties be used?\nThey cannot be referenced using $get_property\nfunctions.</span>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#_Schema_Definition\">property definitions</a></p></td>\n<td>An optional map of property definitions for the Policy Type.<span\nclass=\"comment-end\" id=\"1149\"></span></td>\n</tr>\n<tr class=\"even\">\n<td><span class=\"comment-start\" id=\"1150\" data-author=\"Matt Rutkowski\"\ndata-date=\"2016-01-27T10:41:00Z\"><strong>MUSTFIX, TODO</strong>:\ntosca-parser throws an expecction if this is empty / zero-length. Should\nwe allow an empty list here?</span><span class=\"comment-start\" id=\"1151\"\ndata-author=\"Chris Lauwers\" data-date=\"2022-10-03T19:53:00Z\">The\ndescription says that \"a policy affects or governs an application or\nservice's topology\". What do \"targets\" mean in this context? Isn't the\nentire service topology the target?</span>targets<span\nclass=\"comment-end\" id=\"1150\"></span></td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>An optional list of valid <span class=\"comment-start\" id=\"1152\"\ndata-author=\"Matt Rutkowski\"\ndata-date=\"2016-01-27T10:46:00Z\"><strong>MUSTFIX</strong>,\n<strong>TODO</strong>: tosca-parser assumes the list is either group\ntypes &lt;or&gt; node types, but not both (mixed). Is this a correct\ninterpretation?</span>Node Types or Group Types <span\nclass=\"comment-end\" id=\"1152\"></span>the Policy Type can be applied\nto.<span class=\"comment-end\" id=\"1151\"></span></td>\n</tr>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"1153\" data-author=\"Chris Lauwers\"\ndata-date=\"2022-10-03T19:55:00Z\">Triggers require a service topology as\ncontext. It does not make any sense to define triggers in a Policy Type\noutside of a service template.</span>triggers</td>\n<td>no</td>\n<td>map of <a href=\"#trigger-definition\">trigger definitions</a></td>\n<td>An optional map of policy triggers for the Policy Type.<span\nclass=\"comment-end\" id=\"1153\"></span></td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nPolicy Types have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">policy_type_name</a>&gt;:</p>\n<p>derived_from: &lt;<a\nhref=\"#TYPE_YAML_STRING\">parent_policy_type_name</a>&gt;</p>\n<p>version: &lt;<a\nhref=\"#tosca-tal-suggests-removing-this.version\">version_number</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">policy_description</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#_Schema_Definition\">property_definitions</a>&gt;</p>\n<p>targets: [ &lt;list_of_valid_target_types&gt; ]</p>\n<p>triggers:</p>\n<p>&lt;<a\nhref=\"#trigger-definition\">trigger_definitions</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- policy_type_name: represents the mandatory symbolic name of the Policy\n  Type being declared as a string.\n\n- parent_policy_type_name: represents the name (string) of the Policy\n  Type this Policy Type definition derives from (i.e., its \u201cparent\u201d\n  type).\n\n- version_number: represents the optional TOSCA version number for the\n  Policy Type.\n\n- policy_description: represents the optional description string for the\n  corresponding policy_type_name.\n\n- property_definitions: represents the optional map of property\n  definitions for the Policy Type.\n\n- list_of_valid_target_types: represents the optional list of TOSCA\n  types (i.e. Group or Node Types) that are valid targets for this\n  Policy Type; if the targets keyname is not defined then there are no\n  restrictions to the targets\u2019 types.\n\n- trigger_definitions: represents the optional map of trigger\n  definitions for the policy.\n\n#### Derivation rules\n\nDuring Policy Type derivation the keyname definitions follow these\nrules:\n\n- properties: existing property definitions may be refined; new property\n  definitions may be added.\n\n- targets: if the targets keyname is defined in the parent type, each\n  element in this list must either be in the parent type list or derived\n  from an element in the parent type list; if the targets keyname is not\n  defined in the parent type then no restrictions are applied to this\n  definition.\n\n- triggers: existing trigger definitions may not be changed; new trigger\n  definitions may be added.\n\n#### Example\n\nThe following represents a Policy Type definition:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>policy_types:</p>\n<p>mycompany.mytypes.policies.placement.Container.Linux:</p>\n<p>description: My company\u2019s placement policy for linux</p>\n<p>derived_from: tosca.policies.Root</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### <span class=\"comment-start\" id=\"1164", "author": "Jordan,PM,Paul,TNK6 R", "date": "2020-11-09T09:55:00Z", "comment": "I know that TMF have a branch of their information model to describe policy but that it is not used much and that MEF have recently been more active in specializing policy for access control and for IP forwarding rules. It is possible that TOSCA could draw on this work to make TOSCA policy framework more useful.", "target": "Policy definition"}-->


A policy definition defines a policy that can be associated with a TOSCA
service or top-level entity definition (e.g., group definition, node
template, etc.).

#### Keynames

The following is the list of recognized keynames for a TOSCA policy
definition
<!----
{"id": "1167", "author": "Chris Lauwers", "date": "2022-10-03T19:59:00Z", "comment": "Policies apply to entire service templates,\nnot to individual node templates. What was the intended use of targets\nin policy definitions?", "target": "definition"}-->
:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 20%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>type</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The mandatory name of the policy type the policy definition is based
upon.</td>
</tr>
<tr class="even">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING"><span>string</span></a></td>
<td>The optional description for the policy definition.</td>
</tr>
<tr class="odd">
<td>metadata</td>
<td>no</td>
<td><a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a></td>
<td>Defines a section used to declare additional metadata
information.</td>
</tr>
<tr class="even">
<td>epresents the optional list of names of node
  templates or groups that the policy is to applied
  to.
<!----
{"id": "1168\" data-author=\"Chris Lauwers\"\ndata-date=\"2022-10-03T20:00:00Z\">How/where can these properties be\nused?</span>properties</td>\n<td>no</td>\n<td><p>map of</p>\n<p><a href=\"#property-assignment\">property assignments</a></p></td>\n<td>An optional map of property value assignments for the policy\ndefinition.<span class=\"comment-end\" id=\"1168\"></span></td>\n</tr>\n<tr class=\"odd\">\n<td>targets</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>An optional list of valid Node Templates or Groups the Policy can be\napplied to.</td>\n</tr>\n<tr class=\"even\">\n<td><span class=\"comment-start\" id=\"1169\" data-author=\"Calin Curescu\"\ndata-date=\"2020-05-06T10:51:00Z\">!!! What is the meaning of these\ntriggers here w.r.t. the triggers defined in the policy type?<br />\nI assume we should allow the definition of new triggers, that are used\nin addition to the triggers defined in the policy type.<br />\nIn interface we did not allow to add new operations or\nnotifications</span>triggers</td>\n<td>no</td>\n<td>map of <a href=\"#trigger-definition\">trigger definitions</a></td>\n<td>An optional map of trigger definitions to invoke when the policy is\napplied by an orchestrator against the associated TOSCA entity. These\ntriggers apply in addition to the triggers defined in the policy\ntype.<span class=\"comment-end\" id=\"1169\"></span></td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nPolicy definitions have one the following grammars:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;<a href=\"#TYPE_YAML_STRING\">policy_name</a>&gt;:</p>\n<p>type: &lt;<a href=\"#TYPE_YAML_STRING\">policy_type_name</a>&gt;</p>\n<p>description: &lt;<a\nhref=\"#TYPE_YAML_STRING\">policy_description</a>&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>properties:</p>\n<p>&lt;<a href=\"#property-assignment\">property_assignments</a>&gt;</p>\n<p>targets: [&lt;list_of_policy_targets&gt;]</p>\n<p>triggers:</p>\n<p>&lt;trigger_definitions&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- policy_name: represents the mandatory symbolic name of the policy as a\n  [string](#TYPE_YAML_STRING).\n\n- policy_type_name: represents the name of the policy the definition is\n  based upon.\n\n- policy_description: contains an optional description of the policy.\n\n- property_assignments: represents the optional map of [property\n  assignments](#property-assignment) for the policy definition that\n  provide values for properties defined in its declared Policy Type.\n\n- list_of_policy_targets: r<span class=\"comment-start\" id=\"1172", "author": "Luc Boutier [2]", "date": "2016-05-03T06:45:00Z", "comment": "Do we have prose\n  to say that node template names and group names are unique all\n  together ?", "target": "epresents the optional list of names of node\n  templates or groups that the policy is to applied\n  to."}-->


<!-- -->

- if the targets keyname was defined (by specifying a
  list_of_valid_target_types) in the policy type of this policy then the
  targets listed here must be compatible (i.e. be of that type or of
  type that is derived from) with the types (of nodes or groups) in the
  list_of_valid_target_types.

<!-- -->

- trigger_definitions: represents the optional map
  of [trigger definitions](#trigger-definition) for the policy; these
  triggers apply in addition to the triggers defined in the policy
  type.
<!----
{"id": "1173", "author": "Calin Curescu", "date": "2020-05-06T10:56:00Z", "comment": "!!! What is the meaning of these triggers\n  here w.r.t. the triggers defined in the policy type?  \n  I assume we should allow the definition of new triggers, that are used\n  in addition to the triggers defined in the policy type.  \n  But, in interface we did not allow to add new operations or\n  notifications.", "target": "trigger_definitions: represents the optional map\n  of [trigger definitions](#trigger-definition) for the policy; these\n  triggers apply in addition to the triggers defined in the policy\n  type."}-->


#### Example

The following represents a policy definition:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>policies:</p>
<p>- my_compute_placement_policy:</p>
<p>type: tosca.policies.placement</p>
<p>description: Apply my placement policy to my application’s
servers</p>
<p>targets: [ my_server_1, my_server_2 ]</p>
<p># remainder of policy definition left off for brevity</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Trigger definition

A trigger definition defines the event, condition and action that is
used to “trigger” a policy with which it is associated.

#### Keynames
<!----
{"id": "1181", "author": "Matt Rutkowski", "date": "2017-09-26T11:38:00Z", "comment": "RECALL; Policy type defn were to be consumed by a \u201cPolicy Engine\u201d that would create events on a known event monitoring service. We need to create diagram and explain the event-condition-action flow of policy (defn.)", "target": "Keynames"}-->


The following is the list of recognized keynames for a TOSCA trigger
definition:

| Keyname     | Mandatory | Type                                                 | Description                                                                                                                                                                                                                                                                                                      |
|-------------|-----------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description | no        | [[string](#TYPE_YAML_STRING)](#TYPE_YAML_STRING)     | The optional description string for the trigger.                                                                                                                                                                                                                                                                 |
| event       | yes       | [string](#TYPE_YAML_STRING)                          | The mandatory name
<!----
{"id": "1182", "author": "Chris Lauwers", "date": "2022-10-03T20:01:00Z", "comment": "We need to clarify the context in which event names can be interpreted. Are they globally scoped?", "target": "name"}-->
 of the event that activates the trigger’s action. |
| condition   | no        | [condition clause](#BKM_Condition_Clause_Def)        | The optional condition that must evaluate to true in order for the trigger’s action to be performed. Note: this is optional since sometimes the event occurrence itself is enough to trigger the action.                                                                                                         |
| action      | yes       | list of [activity definition](#activity-definitions) | The list of sequential activities to be performed when the event is triggered, and the condition is met (i.e., evaluates to true).                                                                                                                                                                               |

#### 
<!----
{"id": "1185", "author": "Calin Curescu", "date": "2020-05-06T11:29:00Z", "comment": "This does not make any sense. Needs to be deleted.", "target": ""}-->
Grammar

Trigger definitions have the following grammars:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;<a href="#TYPE_YAML_STRING">trigger_name</a>&gt;:</p>
<p>description: &lt;<a
href="#TYPE_YAML_STRING">trigger_description</a>&gt;</p>
<p>
<!----
{"id": "1186\" data-author=\"Matt Rutkowski\"\ndata-date=\"2016-01-13T11:20:00Z\">TBD: Add \u201csimple\u201d grammar which accepts\na single line \u201ctype\u201d only and no other child properties.</span>event:\n<span class=\"comment-end\" id=\"1186\"></span>&lt;event_name&gt;</p>\n<p><span class=\"comment-start\" id=\"1187\" data-author=\"Matt Rutkowski\"\ndata-date=\"2016-01-13T11:53:00Z\">TBD: Again, a simple grammar and\nextended/full grammar is needed for the condition.</span>condition<span\nclass=\"comment-end\" id=\"1187\"></span>: &lt;<a\nhref=\"#BKM_Condition_Clause_Def\">condition_clause</a>&gt;</p>\n<p>action:</p>\n<p>- &lt;<a\nhref=\"#activity-definitions\">list_of_activity_definition</a>&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n<span class=\"comment-start\" id=\"1188", "author": "Calin Curescu", "date": "2020-05-06T11:30:00Z", "comment": "!!! This corresponds to the additional\nkeynames and makes no sense. Needs to be\nremoved.", "target": ""}-->
In the above
grammar, the pseudo values that appear in angle brackets have the
following meaning:

- trigger_name: represents the mandatory symbolic name of the trigger as
  a [string](#TYPE_YAML_STRING).

- trigger_description: represents the optional
  [description](#TYPE_YAML_STRING) string for the corresponding
  trigger_name.

- event_name: represents the mandatory name of an event associated with
  an interface notification on the identified resource (node). .

- condition_clause: an optional Boolean expression that can be evaluated
  within the context of the service with which the policy is associated
  and that must evaluate to true in order for the trigger’s action to be
  performed. Note that the arguments to the condition clause function
  can in turn be other TOSCA functions. If no condition clause is
  specified, the trigger event will always result in the trigger’s
  action being taken.

- list_of_activity_definition: represents the list of activities that
  are performed in response to the event if the (optional) condition is
  met.

### Activity definitions

An activity defines an operation to be performed in a TOSCA workflow
step or in an action body of a policy trigger. Activity definitions can
be of the following types:

- Delegate workflow activity definition:

<!-- -->

- Defines the name of the delegate workflow and optional input
  assignments. This activity requires the target to be provided by the
  orchestrator (no-op node or relationship).

<!-- -->

- Set state activity definition:

<!-- -->

- Sets the state of a node.

<!-- -->

- Call operation activity definition:

<!-- -->

- Calls an operation defined on a TOSCA interface of a node,
  relationship or group. The operation name uses the
  \<interface_name\>.\<operation_name\> notation. Optionally,
  assignments for the operation inputs can also be provided. If
  provided, they will override for this operation call the operation
  inputs assignment in the node template.

<!-- -->

- Inline workflow activity definition:

<!-- -->

- Inlines another workflow defined in the service (allowing
  reusability). The definition includes the name of a workflow to be
  inlined and optional workflow input assignments.

#### Delegate workflow activity definition

##### Keynames

The following is a list of recognized keynames for a delegate activity
definition.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Keyname</strong></th>
<th><strong>Mandatory</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>delegate</td>
<td>yes</td>
<td><p>string or empty</p>
<p>(see grammar below)</p></td>
<td><p>Defines the name of the delegate workflow and optional input
assignments.</p>
<p>This activity requires the target to be provided by the orchestrator
(no-op node or relationship).</p></td>
</tr>
<tr class="even">
<td>workflow</td>
<td>no</td>
<td>string</td>
<td>The name of the delegate workflow. Mandatory in the extended
notation.</td>
</tr>
<tr class="odd">
<td>inputs</td>
<td>no</td>
<td>map of <a href="#parameter-definition">parameter
assignments</a></td>
<td>The optional map of input parameter assignments for the delegate
workflow.</td>
</tr>
</tbody>
</table>

##### Grammar

A delegate activity definition has the following grammar. The short
notation can be used if no input assignments are provided.

#####  Short notation

| \- delegate: \<[delegate_workflow_name](#TYPE_YAML_STRING)\> |
|--------------------------------------------------------------|

#####  Extended notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>- delegate:</p>
<p>workflow: &lt;<a
href="#TYPE_YAML_STRING"><u>delegate_workflow_name</u></a>&gt;</p>
<p>inputs:</p>
<p>&lt;<a
href="#parameter-value-assignment"><u>parameter_assignments</u></a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- **delegate_workflow_name**: represents the name of the workflow of the
  node provided by the TOSCA orchestrator.

- **parameter_assignments**: represents the optional map of parameter
  assignments for passing parameters as inputs to this workflow
  delegation.

#### Set state activity definition

Sets the state of the target node.

##### Keynames

The following is a list of recognized keynames for a set state activity
definition.

| **Keyname** | **Mandatory** | **Type**      | **Description**          |
|-------------|---------------|---------------|--------------------------|
| set_state   | yes           | <u>string</u> | Value of the node state. |

##### Grammar

A set state activity definition has the following grammar.

| \- set_state: \<new_node_state\> |
|----------------------------------|

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- new_node_state: represents the state that will be affected to the node
  once the activity is performed.

#### Call operation activity definition

This activity is used to call an operation on the target node. Operation
input assignments can be optionally provided.

##### Keynames

The following is a list of recognized keynames for a call operation
activity definition.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Keyname</strong></th>
<th><strong>Mandatory</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>call_operation</td>
<td>yes</td>
<td><p>string or empty</p>
<p>(see grammar below)</p></td>
<td><p>Defines the opration call. The operation name uses the
&lt;interface_name&gt;.&lt;operation_name&gt; notation.</p>
<p>Optionally, assignments for the operation inputs can also be
provided. If provided, they will override for this operation call the
operation inputs assignment in the node template.</p></td>
</tr>
<tr class="even">
<td>operation</td>
<td>no</td>
<td>string</td>
<td><p>The name of the operation to call, using the
&lt;interface_name&gt;.&lt;operation_name&gt; notation.</p>
<p>Mandatory in the extended notation.</p></td>
</tr>
<tr class="odd">
<td>inputs</td>
<td>no</td>
<td>map of <a href="#parameter-definition">parameter
assignments</a></td>
<td>The optional map of input parameter assignments for the called
operation. Any provided input assignments will override the operation
input assignment in the target node template for this operation
call.</td>
</tr>
</tbody>
</table>

##### Grammar

A call operation activity definition has the following grammar. The
short notation can be used if no input assignments are provided.

#####  Short notation

| \- call_operation: \<operation_name\> |
|---------------------------------------|

#####  Extended notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>- call_operation:</p>
<p>operation: &lt;<a
href="#TYPE_YAML_STRING"><u>operation_name</u></a>&gt;</p>
<p>inputs:</p>
<p>&lt;<a
href="#parameter-value-assignment"><u>parameter_assignments</u></a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- operation_name: represents the name of the operation that will be
  called during the workflow execution. The notation used is
  \<interface_sub_name\>.\<operation_sub_name\>, where
  interface_sub_name is the interface name and the operation_sub_name is
  the name of the operation within this interface.

- **parameter_assignments**: represents the optional map of parameter
  assignments for passing parameters as inputs to this workflow
  delegation.

#### Inline workflow activity definition

This activity is used to inline a workflow in the activities sequence.
The definition includes the name of the inlined workflow and optional
input assignments.

##### Keynames

The following is a list of recognized keynames for an inline workflow
activity definition.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Keyname</strong></th>
<th><strong>Mandatory</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inline</td>
<td>yes</td>
<td><p>string or empty</p>
<p>(see grammar below)</p></td>
<td>The definition includes the name of a workflow to be inlined and
optional workflow input assignments.</td>
</tr>
<tr class="even">
<td>workflow</td>
<td>no</td>
<td><u>string</u></td>
<td>The name of the inlined workflow. Mandatory in the extended
notation.</td>
</tr>
<tr class="odd">
<td>inputs</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#parameter-definition">parameter assignments</a></p></td>
<td>The optional map of input parameter assignments for the inlined
workflow.</td>
</tr>
</tbody>
</table>

##### Grammar

An inline workflow activity definition has the following grammar. The
short notation can be used if no input assignments are provided.

#####  Short notation

| \- inline: \<inlined_workflow_name\> |
|--------------------------------------|

#####  Extended notation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>- inline:</p>
<p>workflow: &lt;<a
href="#TYPE_YAML_STRING"><u>inlined_workflow_name</u></a>&gt;</p>
<p>inputs:</p>
<p>&lt;<a
href="#parameter-value-assignment"><u>parameter_assignments</u></a>&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the above grammar, the pseudo values that appear in angle brackets
have the following meaning:

- inlined_workflow_name: represents the name of the workflow to inline.

- **parameter_assignments**: represents the optional map of parameter
  assignments for passing parameters as inputs to this workflow
  delegation.

#### Example

The following represents a list of activity definitions (using the short
notation):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>- delegate: deploy</p>
<p>- set_state: started</p>
<p>- call_operation: tosca.interfaces.node.lifecycle.Standard.start</p>
<p>- inline: my_workflow</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Workflows
---------

### Imperative Workflow definition

A workflow definition defines an imperative workflow that is associated
with a TOSCA service. A workflow definition can either include the steps
that make up the workflow, or it can refer to an artifact that expresses
the workflow using an external workflow language.

#### Keynames

The following is the list of recognized keynames for a TOSCA workflow
definition:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyname</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>description</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING"><span>string</span></a></td>
<td>The optional description for the workflow definition.</td>
</tr>
<tr class="even">
<td>metadata</td>
<td>no</td>
<td><a href="#tosca-map-type">map</a> of <a
href="#TYPE_YAML_STRING">string</a></td>
<td>Defines a section used to declare additional metadata
information.</td>
</tr>
<tr class="odd">
<td>inputs</td>
<td>no</td>
<td><p>map of</p>
<p><a href="#parameter-definition">parameter definitions</a></p></td>
<td>The optional map of input parameter definitions.</td>
</tr>
<tr class="even">
<td>precondition</td>
<td>no</td>
<td>condition clause</td>
<td>Condition clause that must evaluate to true before the workflow can
be processed.</td>
</tr>
<tr class="odd">
<td>steps</td>
<td>no</td>
<td>map of <a href="#workflow-step-definition">step definitions</a></td>
<td>An optional map of valid imperative workflow step definitions.</td>
</tr>
<tr class="even">
<td>implementation</td>
<td>no</td>
<td><a
href="#operation-and-notification-implementation-definition">operation
implementation definition</a></td>
<td>The optional definition of an external workflow definition. This
keyname is mutually exclusive with the <strong>steps</strong> keyname
above.</td>
</tr>
<tr class="odd">
<td>unctions
<!----
{"id": "1246\" data-author=\"Calin Curescu\"\ndata-date=\"2019-01-30T17:51:00Z\">I think we should leave the declaration\nof output values to v1.4. As last discussed it was not clear to what\nthey should be mapped.<br />\nAlso, if this is an externally invoked workflow, then should we allow\nfor the case that the outputs are only only returned\nexternally?</span>outputs</td>\n<td>no</td>\n<td><p>map of</p>\n<p>attribute mappings</p></td>\n<td>The optional map of attribute mappings that specify workflow output\nvalues and their mappings onto attributes of a node or relationship\ndefined in the <span class=\"comment-end\" id=\"1246\"></span>service.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nImperative workflow definitions have the following grammar:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>&lt;workflow_name&gt;:</p>\n<p>description: &lt;workflow_description&gt;</p>\n<p>metadata:</p>\n<p>&lt;<a href=\"#tosca-map-type\">map</a> of <a\nhref=\"#TYPE_YAML_STRING\">string</a>&gt;</p>\n<p>inputs:</p>\n<p>&lt;<a href=\"#parameter-definition\">parameter_definitions</a>&gt;</p>\n<p>precondition:</p>\n<p>&lt;condition_clause&gt;</p>\n<p>steps:</p>\n<p>&lt;<a href=\"#workflow-step-definition\">workflow_steps</a>&gt;</p>\n<p>implementation:</p>\n<p>&lt;<a\nhref=\"#artifact-definition\">operation_implementation_definitions</a>&gt;</p>\n<p>outputs:</p>\n<p>&lt;attribute_mappings&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- workflow_name:\n\n- workflow_description:\n\n- parameter_definitions:\n\n- condition_clause:\n\n- workflow_steps:\n\n- operation_implementation_definition: represents a full inline\n  definition of an implementation artifact\n\nattribute_mappings: represents the optional map of attribute_mappings\nthat consists of named output values returned by operation\nimplementations (i.e. artifacts) and associated mappings that specify\nthe attribute into which this output value must be stored.\n\n### Workflow precondition definition\n\nA workflow precondition defines a condition clause that checks if a\nworkflow can be processed or not based on the state of the instances of\na TOSCA service deployment. If the condition is not met, the workflow\nwill not be triggered.\n\n#### Examples\n\n\\<\\<TO BE PROVIDED\\>\\>\n\n### Workflow step definition\n\nA workflow step allows to define one or multiple sequenced activities in\na workflow and how they are connected to other steps in the workflow.\nThey are the building blocks of a declarative workflow.\n\n#### Keynames\n\nThe following is the list of recognized keynames for a TOSCA workflow\nstep definition:\n\n<table>\n<colgroup>\n<col style=\"width: 20%\" />\n<col style=\"width: 12%\" />\n<col style=\"width: 13%\" />\n<col style=\"width: 53%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>Keyname</th>\n<th>Mandatory</th>\n<th>Type</th>\n<th>Description</th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"odd\">\n<td>target</td>\n<td>yes</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The target of the step (this can be a node template name, a group\nname)</td>\n</tr>\n<tr class=\"even\">\n<td>target_relationship</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional name of a requirement of the target in case the step\nrefers to a relationship rather than a node or group. Note that this is\napplicable only if the target is a node.</td>\n</tr>\n<tr class=\"odd\">\n<td><span class=\"comment-start\" id=\"1260\" data-author=\"Chris Lauwers\"\ndata-date=\"2022-10-03T20:27:00Z\">We should remove this keyname. It has\nbeen removed in operation implementation definitions as well, since\npresumable the \"operation host\" is always the orchestrator\nhost.</span>operation_host<span class=\"comment-end\"\nid=\"1260\"></span></td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>The node on which operations should be executed (for TOSCA\ncall_operation activities).</p>\n<p>This element is mandatory only for relationships and groups\ntarget.</p>\n<p>If target is a relationship then operation_host is mandatory and\nvalid_values are SOURCE or TARGET \u2013 referring to the relationship source\nor target node.</p>\n<p>If target is a group then operation_host is optional.</p>\n<p>If not specified the operation will be triggered on every node of the\ngroup.</p>\n<p>If specified the valid_value is a node_type or the name of a node\ntemplate.<span class=\"comment-start\" id=\"1261\"\ndata-author=\"Luc Boutier [2]\"\ndata-date=\"2016-05-03T12:06:00Z\">Alternative would be to add this\ninformation on the interface for a relationship or group.</span><span\nclass=\"comment-end\" id=\"1261\"></span></p></td>\n</tr>\n<tr class=\"even\">\n<td><span class=\"comment-start\" id=\"1262\" data-author=\"Chris Lauwers\"\ndata-date=\"2022-10-03T20:28:00Z\">What is the expected behavior if the\nfilter evaluates to False?</span><span class=\"comment-start\" id=\"1263\"\ndata-author=\"Chris Lauwers\" data-date=\"2022-10-03T20:27:00Z\">Should this\nbe replaced with condition clauses as well?</span>filter</td>\n<td>no</td>\n<td>list of <a\nhref=\"#this-should-have-its-own-refinement-rule-section-to-explain-how-conflicts-are-resolved-if-at-all.-for-example-if-there-is-range-0..10-and-greated_than-15-what-happensvalidation-clause-definition\">validation\nclauses</a></td>\n<td>Filter is a list of validation clauses that allows to provide a\nfiltering logic.<span class=\"comment-end\" id=\"1262\"><span\nclass=\"comment-end\" id=\"1263\"></span></span></td>\n</tr>\n<tr class=\"odd\">\n<td>activities</td>\n<td>yes</td>\n<td>list of <a href=\"#activity-definitions\">activity definition</a></td>\n<td>The list of sequential activities to be performed in this step.</td>\n</tr>\n<tr class=\"even\">\n<td>on_success</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional list of step names to be performed after this one has\nbeen completed with success (all activities has been correctly\nprocessed).</td>\n</tr>\n<tr class=\"odd\">\n<td>on_failure</td>\n<td>no</td>\n<td>list of <a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td>The optional list of step names to be called after this one in case\none of the step activity failed.</td>\n</tr>\n</tbody>\n</table>\n\n#### Grammar\n\nWorkflow step definitions have the following grammars:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>steps:</p>\n<p>&lt;<a href=\"#TYPE_YAML_STRING\">step_name</a>&gt;</p>\n<p>target: &lt;<a href=\"#TYPE_YAML_STRING\">target_name</a>&gt;</p>\n<p>target_relationship: &lt;target_requirement_name&gt;</p>\n<p>operation_host: &lt;operation_host_name&gt;</p>\n<p>filter:</p>\n<p>- &lt;<a\nhref=\"#BKM_Condition_Clause_Def\">list_of_condition_clause_definition</a>&gt;</p>\n<p>activities:</p>\n<p>- &lt;<a\nhref=\"#activity-definitions\">list_of_activity_definition</a>&gt;</p>\n<p>on_success:</p>\n<p>- &lt;target_step_name&gt;</p>\n<p>on_failure:</p>\n<p>- &lt;target_step_name&gt;</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn the above grammar, the pseudo values that appear in angle brackets\nhave the following meaning:\n\n- target_name: represents the name of a node template or group in the\n  service.\n\n- target_requirement_name: represents the name of a requirement of the\n  node template (in case target_name refers to a node template.\n\n- **operation_host:** the node on which the operation should be executed\n\n- **list_of_condition_clause_definition:** represents a list of\n  condition clause definition.\n\n- **list_of_activity_definition**: represents a list of activity\n  definition\n\n- **target_step_name**: represents the name of another step of the\n  workflow.\n\nTOSCA built-in f<span class=\"comment-start\" id=\"1315", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-214](endnotes.xml) \u2013 New functions: get_node_instance( node_template_name, node_filter) \u00a0\u00a0\u00a0\u00a0\u00a0returns ( node_instance_id \\| failure ) invoke_node_operations( node_instance_id, operation_name, operation_input_parms) \u00a0\u00a0\u00a0\u00a0returns ( operation_outputs \\| failure ) create_node_instance( node_template_name, input_parameters ) \u00a0\u00a0\u00a0\u00a0returns ( node_instance_id \\| failure ) delete_node_instance( node_instance_id) \u00a0\u00a0\u00a0\u00a0returns result (success \\| failure ) set_instance_properties( node_instance_id, property_name, ..., property_name_x, property_value ) \u00a0\u00a0\u00a0\u00a0returns ( success \\| failure )", "target": "unctions"}-->

===========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Representation graph query functions
<!----
{"id": "1316", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-146](media/image1.png): WD02: Need to include grammar and examples for each function.", "target": "Representation graph query functions"}-->

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### get_input 

The get_input function is used to retrieve the values of parameters
declared within the inputs section of a TOSCA Service Template.

#### Grammar 

| \$get_input: \<input_parameter_name\> |
|---------------------------------------|

or

| \$get_input: \[ \<input_parameter_name\>, \<nested_input_parameter_name_or_index_1\>, ..., \<nested_input_parameter_name_or_index_n\> \] |
|------------------------------------------------------------------------------------------------------------------------------------------|

Note that the first signature does not conform to the custom function
definition, but it does not have to as it is a TOSCA built-in function.

#### Arguments

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;input_parameter_name&gt;</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The name of the parameter as defined in the inputs section of the
service template.</td>
</tr>
<tr class="even">
<td>&lt;nested_input_parameter_name_or_index_*&gt;</td>
<td>no</td>
<td><a href="#TYPE_YAML_STRING">string</a>| <a
href="#TYPE_YAML_INTEGER">integer</a></td>
<td><p>Some TOSCA input parameters are complex (i.e., composed as nested
structures). These parameters are used to dereference into the names of
these nested structures when needed.</p>
<p>Some parameters represent list types. In these cases, an index may be
provided to reference a specific entry in the list (as identified by the
previous parameter) to return.</p></td>
</tr>
</tbody>
</table>

#### Examples

The following snippet shows an example of the simple get_input grammar:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>inputs:</p>
<p>cpus:</p>
<p>type: integer</p>
<p>node_templates:</p>
<p>my_server:</p>
<p>type: Note that the get_property function may only
retrieve the static values of parameter or property definitions of a
TOSCA application as defined in the TOSCA Service Template.

<!----
{"id": "1317\"\ndata-author=\"Jordan,PM,Paul,TNK6 R\" data-date=\"2020-11-09T12:09:00Z\">No\nlonger defined so may be confusing to include in an\nexample</span>tosca.nodes.Compute<span class=\"comment-end\"\nid=\"1317\"></span></p>\n<p>capabilities:</p>\n<p>host:</p>\n<p>properties:</p>\n<p>num_cpus: { $get_input: cpus }</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThe following template shows an example of the nested get_input grammar.\nThe template expects two input values, each of which has a complex data\ntype. The get_input function is used to retrieve individual fields from\nthe complex input data.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>data_types:</p>\n<p>NetworkInfo:</p>\n<p>derived_from: <span class=\"comment-start\" id=\"1318\"\ndata-author=\"Jordan,PM,Paul,TNK6 R\" data-date=\"2020-11-09T12:09:00Z\">No\nlonger defined so may be confusing to include in an\nexample</span>tosca.Data.Root<span class=\"comment-end\"\nid=\"1318\"></span></p>\n<p>properties:</p>\n<p>name:</p>\n<p>type: string</p>\n<p>gateway:</p>\n<p>type: string</p>\n<p>RouterInfo:</p>\n<p>derived_from: tosca.Data.Root</p>\n<p>properties:</p>\n<p>ip:</p>\n<p>type: string</p>\n<p>external:</p>\n<p>type: string</p>\n<p>service_template:</p>\n<p>inputs:</p>\n<p>management_network:</p>\n<p>type: NetworkInfo</p>\n<p>router:</p>\n<p>type: RouterInfo</p>\n<p>node_templates:</p>\n<p>Bono_Main:</p>\n<p>type: vRouter.Cisco</p>\n<p>directives: [ substitutable ]</p>\n<p>properties:</p>\n<p>mgmt_net_name: { $get_input: [management_network, name]}</p>\n<p>mgmt_cp_v4_fixed_ip: { $get_input: [router, ip]}</p>\n<p>mgmt_cp_gateway_ip: { $get_input: [management_network, gateway]}</p>\n<p>mgmt_cp_external_ip: { $get_input: [router, external]}</p>\n<p>requirements:</p>\n<p>- lan_port:</p>\n<p>node: host_with_net</p>\n<p>capability: virtualBind</p>\n<p>- mgmt_net: mgmt_net</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### get_property\n\nThe get_property function is used to retrieve property values of\nmodelable entities in the representation graph.\n<span class=\"comment-start\" id=\"1320", "author": "Calin Curescu", "date": "2022-05-16T17:16:00Z", "comment": "This is wrong, the representation graph is\nstill traversed !!!", "target": "Note that the get_property function may only\nretrieve the static values of parameter or property definitions of a\nTOSCA application as defined in the TOSCA Service Template.\n"}-->
The get_attribute function
should be used to retrieve values for attribute definitions (or property
definitions reflected as attribute definitions) from the representation
graph of the TOSCA application (as realized by the TOSCA orchestrator).

#### Grammar 
<!----
{"id": "1321", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-169](comments.xml): is this always a separate service template? Can have local refs? TODO: See what remains of this JIRA issue that is not addressed by this new method.", "target": "Grammar "}-->


| \$get_property: \[ \<tosca_traversal_path\>, \<property_name\>, \<nested_property_name_or_index_1\>, ..., \<nested_property_name_or_index_n\> \] |
|--------------------------------------------------------------------------------------------------------------------------------------------------|

#### Arguments

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt; tosca_traversal_path &gt;</td>
<td>yes</td>
<td>Using the &lt;tosca_traversal_path&gt; we can traverse the
representation graph to extract information from a certain node or
relationship. We start from a specific node or relationship identified
by its symbolic name (or by the SELF keyword representing the node or
relationship containing the definition) and then we may further traverse
the relationships and nodes of the representation graph (using a
variable number of steps) until reaching the desired node or
relationship. In the following subsection the specification of the
&lt;tosca_traversal_path&gt; is explicated.</td>
</tr>
<tr class="even">
<td>&lt;property_name&gt;</td>
<td>yes</td>
<td>The name of the property definition the function will return the
value from.</td>
</tr>
<tr class="odd">
<td>&lt;nested_property_name_or_index_*&gt;</td>
<td>no</td>
<td><p>Some TOSCA properties are complex (i.e., composed as nested
structures). These parameters are used to dereference into the names of
these nested structures when needed.</p>
<p>Some properties represent list types. In these cases, an index may be
provided to reference a specific entry in the list (as identified by the
previous parameter) to return.</p></td>
</tr>
</tbody>
</table>

##### The simplified TOSCA_PATH definition in BNF format

*\<tosca_traversal_path\> ::= \<initial_context\>, \<node_context\> \|*

> *\<initial_context\>, \<rel_context\>*

*\<initial_context\> ::= \<node_symbolic_name\> \|*

*\<relationship_symbolic_name\>* \|

*SELF*

*\<rel_context\> ::= SOURCE, \<node_context\> \| *

*TARGET, \<node_context\> \| *

*CAPABILITY \|*

*\<empty\>*

*\<node_context\> ::= RELATIONSHIP, \<requirement_name\>,
\<idx_of_out_rel_in_req\>, \<rel_context\> \|*

*CAPABILITY, \<capability_name\>, RELATIONSHIP, \<idx_of_incoming_rel\>,
\<rel_context\> \|*

*CAPABILITY, \<capability_name\> \|*

*\<empty\>*

*\<idx_of_out_rel_in_req\> ::= \<integer_index\> \| *

*ALL \| *

*\<empty\>*

*\< idx_of_incoming_rel \> ::= \<integer_index\> \| *

*ALL \| *

*\<empty\>*

The initial context (if we refer to a node or relationship) determines
if the next context is a relationship context or a node context. Then,
each *\<node_context\>* can further resolve to a *\<rel_context\>* and
vice versa, thus building additional traversal steps. In the end we
reach either a node context, a relationship context, or a capability
context as presented above.

A *\<rel_context\>* can

- further lead to the source node of the current relationship

- further lead to the target node of the current relationship

- end within the target capability of the current relationship

- end within the current relationship via the \<empty\> resolution

A *\<node_context\>* can

- further lead to the relationship with index \<idx_of_out_rel_in_req\>
  defined by requirement with symbolic name \<requirement_name\> of the
  current node

- further lead to the relationship with index \<idx_of_incoming_rel\>
  that has as target the capability with symbolic name
  \<capability_name\> of the current node

- end within the capability with symbolic name \<capability_name\> in
  the current node

- end within the current node via the \<empty\> resolution

Note that both the indexes can either be a non-negative integer, the
keyword ALL, or missing. If it is a non-negative integer, 0 represents
the first index and so on incrementally. If the index is missing, the
semantic meaning is that the first index (index with value 0) is used.
If it is the keyword ALL, then we return the result for all possible
indices (further resolved separately) as a list. If the there are
multiple ALL keywords in the definition, then all the results shall be
merged into a single list.

#### Note

We further list the changes from the get_property and get_attribute
expression from v1.3 to v2.0:

- Added multi-step traversal of the representation graph

- Added the backward traversal from capabilities to incoming
  relationships

- Added the target capability of a relationship as a possible traversal

- Added the specification of indexes and allowing traversal of
  multi-count requirements

- Changed the following syntax to work better in multi-step traversal:

<!-- -->

- The initial SOURCE, … becomes SELF, SOURCE, …

- The initial TARGET, … becomes SELF, TARGET, …

#### Examples
<!----
{"id": "1322", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "WD03: TODO: Need examples for returning simple types and complex/nested structures (e.g., Maps of Maps)", "target": "Examples"}-->


The following example shows how to use the get_property function with an
actual Node Template name:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>mysql_database:</p>
<p>type: tosca.nodes.Database</p>
<p>properties:</p>
<p>name: sql_database1</p>
<p>wordpress:</p>
<p>type: tosca.nodes.WebApplication.WordPress</p>
<p>...</p>
<p>interfaces:</p>
<p>Standard:</p>
<p>configure:</p>
<p>inputs:</p>
<p>wp_db_name: { $get_property: [ mysql_database, name ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following example shows how to use the get_property function
traversing from the relationship to its target node:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>relationship_templates:</p>
<p>my_connection:</p>
<p>type: ConnectsTo</p>
<p>interfaces:</p>
<p>Configure:</p>
<p>inputs:</p>
<p>targets_value: { $get_property: [ SELF, TARGET, value ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following example shows how to use the get_property function using
the SELF keyword, and traversing from a wordpress node (via the first
relationship of the database_endpoint requirement to the target
capability in the target node) and accessing the port property of that
capability:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>node_templates:</p>
<p>mysql_database:</p>
<p>type: tosca.nodes.Database</p>
<p>...</p>
<p>capabilities:</p>
<p>database_endpoint:</p>
<p>properties:</p>
<p>port: 3306</p>
<p>wordpress:</p>
<p>type: tosca.nodes.WebApplication.WordPress</p>
<p>requirements:</p>
<p>...</p>
<p>- database_endpoint: mysql_database</p>
<p>interfaces:</p>
<p>Standard:</p>
<p>create: wordpress_install.sh</p>
<p>configure:</p>
<p>implementation: wordpress_configure.sh</p>
<p>inputs:</p>
<p>...</p>
<p>wp_db_port:</p>
<p>$get_property:</p>
<p>- SELF</p>
<p>- RELATIONSHIP</p>
<p>- TODO: An example of second
index (i.e. 1) and index ALL !!\!
<!----
{"id": "1323\"\ndata-author=\"Chris Lauwers [3]\" data-date=\"2015-08-25T21:52:00Z\">In this\nexample, get_property refers to the database_endpoint requirement on the\nwordpress node template, which is satisfied by the mysql_database node\ntemplate. mysql_database is of type tosca.nodes.Database, and does not\nhave a port property. The database_endpoint capability in\ntosca.nodes.Database has a port, however. How do we know we\u2019re referring\nto the capability in mysql_database, and not to the mysql_database node\ntemplate?</span><span class=\"comment-start\" id=\"1324\"\ndata-author=\"Calin Curescu\" data-date=\"2022-05-24T19:06:00Z\">Solved with\nthe new syntax.</span>database_endpoint<span class=\"comment-end\"\nid=\"1323\"><span class=\"comment-end\" id=\"1324\"></span></span></p>\n<p>- 0</p>\n<p>- CAPABILITY</p>\n<p>- port</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nNOTE that in the above example the index 0 is used but can also be\nomitted with the same semantic meaning.\n\nThe following example shows how to use the get_property function to\ntraverse over two requirement relationships, from the wordpress node to\nits database node and further to its DBMS host to get its\nadmin_credential property:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_templates:</p>\n<p>mysql_database:</p>\n<p>type: tosca.nodes.Database</p>\n<p>...</p>\n<p>capabilities:</p>\n<p>database_endpoint:</p>\n<p>properties:</p>\n<p>port: 3306</p>\n<p>wordpress:</p>\n<p>type: tosca.nodes.WebApplication.WordPress</p>\n<p>requirements:</p>\n<p>...</p>\n<p>- database_endpoint: mysql_database</p>\n<p>interfaces:</p>\n<p>Standard:</p>\n<p>create: wordpress_install.sh</p>\n<p>configure:</p>\n<p>implementation: wordpress_configure.sh</p>\n<p>inputs:</p>\n<p>...</p>\n<p>host_dbms_admin_credential:</p>\n<p>$get_property:</p>\n<p>- SELF</p>\n<p>- RELATIONSHIP</p>\n<p>- database_endpoint</p>\n<p>- TARGET</p>\n<p>- RELATIONSHIP</p>\n<p>- host</p>\n<p>- TARGET</p>\n<p>- admin_credential</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n<span class=\"comment-start\" id=\"1325", "author": "Calin Curescu", "date": "2023-01-04T16:11:00Z", "comment": "TODO more examples: TODO: An example of\nsecond index (i.e. 1) and index ALL !!!", "target": "TODO: An example of second\nindex (i.e. 1) and index ALL !!\\!"}-->


### get_attribute

The **get_attribute** function is used within a representation graph to
obtain attribute values from nodes and relationships that have been
created from an application model described in a service template. The
nodes or relationships can be referenced by their name as assigned in
the service template or relative to the context where they are being
invoked.

#### Grammar 
<!----
{"id": "1326", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-169](commentsExtended.xml): is this always a separate service template? Can have local refs? TODO: See what remains of this JIRA issue that is not addressed by this new method.", "target": "Grammar "}-->


| \$get_attribute: \[\<tosca_traversal_path\>, \<attribute_name\>, \<nested_attribute_name_or_index_1\>, ..., \<nested_attribute_name_or_index_n\> \] |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|

#### Arguments

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;tosca_traversal_path&gt;</td>
<td>yes</td>
<td>Using the &lt;tosca_traversal_path&gt; we can traverse the
representation graph to extract information from a certain node or
relationship. We start from a specific node or relationship identified
by its symbolic name (or by the SELF keyword representing the node or
relationship containing the definition) and then we may further traverse
the relationships and nodes of the representation graph (using a
variable number of steps) until reaching the desired node or
relationship. The specification of the &lt;tosca_traversal_path&gt; is
explicated in the get_property section.</td>
</tr>
<tr class="even">
<td>&lt;attribute_name&gt;</td>
<td>yes</td>
<td>The name of the attribute definition the function will return the
value from.</td>
</tr>
<tr class="odd">
<td>&lt;nested_attribute_name_or_index_*&gt;</td>
<td>no</td>
<td><p>Some TOSCA attributes are complex (i.e., composed as nested
structures). These parameters are used to dereference into the names of
these nested structures when needed.</p>
<p>Some attributes represent list types. In these cases, an index may be
provided to reference a specific entry in the list (as identified by the
previous parameter) to return.</p></td>
</tr>
</tbody>
</table>

#### Examples:

The attribute
functions are used in the same way as the equivalent Property functions
described above. Please see their examples and replace “get_property”
with “get_attribute” function name.
<!----
{"id": "1327", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "Is this always true?", "target": "The attribute\nfunctions are used in the same way as the equivalent Property functions\ndescribed above. Please see their examples and replace \u201cget_property\u201d\nwith \u201cget_attribute\u201d function name."}-->


### get_artifact

The get_artifact function is used to retrieve artifact location between
modelable entities defined in the same service template.

#### Grammar 

| \$get_artifact: \[ \<modelable_entity_name\>, \<artifact_name\>, \<location\>, \<remove\> \] |
|----------------------------------------------------------------------------------------------|

#### Arguments

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;modelable entity name&gt; | SELF | SOURCE | TARGET | HOST</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The mandatory name of a modelable entity (e.g., Node Template or
Relationship Template name) as declared in the service template that
contains the property definition the function will return the value
from. See section B.1 for valid keywords.</td>
</tr>
<tr class="even">
<td>&lt;artifact_name&gt;</td>
<td>yes</td>
<td><a href="#TYPE_YAML_STRING">string</a></td>
<td>The name of the artifact definition the function will return the
value from.</td>
</tr>
<tr class="odd">
<td>value
<!----
{"id": "1328\"\ndata-author=\"Chris Lauwers [3]\" data-date=\"2015-08-25T21:52:00Z\">These\nvalues are very confusing. When we specify \u201cLOCAL_FILE\u201d, don\u2019t we really\nmean \u201cUNSPECIFIED\u201d, which means we should leave it up to the\norchestrator to decide? Also, what is the expected behavior when the\nartifact definition includes a \u201cdeploy_path\u201d that is different from the\n\u201clocation\u201d specified here?</span>&lt;location&gt; | LOCAL_FILE<span\nclass=\"comment-end\" id=\"1328\"></span></td>\n<td><span class=\"comment-start\" id=\"1329\"\ndata-author=\"Chris Lauwers [3]\" data-date=\"2015-08-25T21:52:00Z\">Either\nthis value must be required or we must specify what the default is.\nAlternatively, we should specify the behavior when this value isn\u2019t\nset.</span>no<span class=\"comment-end\" id=\"1329\"></span></td>\n<td><a href=\"#TYPE_YAML_STRING\">string</a></td>\n<td><p>Location value must be either a valid path e.g.\n\u2018/etc/var/my_file\u2019 or \u2018LOCAL_FILE\u2019.</p>\n<p>If the value is LOCAL_FILE the orchestrator is responsible for\nproviding a path as the result of the get_artifact call where the\nartifact file can be accessed. The orchestrator will also remove the\nartifact from this location at the end of the operation.</p>\n<p>If the location is a path specified by the user the orchestrator is\nresponsible to copy the artifact to the specified location. The\norchestrator will return the path as the value of the get_artifact\nfunction and leave the file here after the execution of the\noperation.</p></td>\n</tr>\n<tr class=\"even\">\n<td>remove</td>\n<td>no</td>\n<td><a href=\"#TYPE_YAML_BOOLEAN\">boolean</a></td>\n<td><p>Boolean flag to override the orchestrator default behavior so it\nwill remove or not the artifact at the end of the operation\nexecution.</p>\n<p>If not specified the removal will depends of the location e.g.\nremoves it in case of \u2018LOCAL_FILE\u2019 and keeps it in case of a path.</p>\n<p>If true the artifact will be removed by the orchestrator at the end\nof the operation execution, if false it will not be removed.</p></td>\n</tr>\n</tbody>\n</table>\n\n#### Examples\n\nThe following example uses a snippet of a WordPress\n\\[[WordPress](#CIT_WORDPRESS)\\] web application to show how to use the\nget_artifact function with an actual Node Template name:\n\n##### Example: Retrieving artifact without specified location\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_templates:</p>\n<p>wordpress:</p>\n<p>type: tosca.nodes.WebApplication.WordPress</p>\n<p>...</p>\n<p>interfaces:</p>\n<p>Standard:</p>\n<p>configure:</p>\n<p>create:</p>\n<p>implementation: wordpress_install.sh</p>\n<p>inputs</p>\n<p>wp_zip: { $get_artifact: [ SELF, zip ] }</p>\n<p>artifacts:</p>\n<p>zip: /data/wordpress.zip</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn such implementation the TOSCA orchestrator may provide the\nwordpress.zip archive as\n\n- a local URL (example:\n  [file://home/user/wordpress.zip](file:///\\\\home\\user\\wordpress.zip))\n  or\n\n- a remote one (example: <http://cloudrepo:80/files/wordpress.zip>)\n  where some orchestrator may indeed provide some global artifact\n  repository management features.\n\n##### Example: Retrieving artifact as a local path\n\nThe following example explains how to force the orchestrator to copy the\nfile locally before calling the operation\u2019s implementation script:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_templates:</p>\n<p>wordpress:</p>\n<p>type: tosca.nodes.WebApplication.WordPress</p>\n<p>...</p>\n<p>interfaces:</p>\n<p>Standard:</p>\n<p>configure:</p>\n<p>create:</p>\n<p>implementation: wordpress_install.sh</p>\n<p>inputs</p>\n<p>wp_zip: { $get_artifact: [ SELF, zip, LOCAL_FILE] }</p>\n<p>artifacts:</p>\n<p>zip: /data/wordpress.zip</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn such implementation the TOSCA orchestrator must provide the\nwordpress.zip archive as a local path (example:\n[/tmp/wordpress.zip](file:///\\\\home\\user\\wordpress.zip)) and **will\nremove it** after the operation is completed.\n\n##### Example: Retrieving artifact in a specified location\n\nThe following example explains how to force the orchestrator to copy the\nfile locally to a specific location before calling the operation\u2019s\nimplementation script:\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>node_templates:</p>\n<p>wordpress:</p>\n<p>type: tosca.nodes.WebApplication.WordPress</p>\n<p>...</p>\n<p>interfaces:</p>\n<p>Standard:</p>\n<p>configure:</p>\n<p>create:</p>\n<p>implementation: wordpress_install.sh</p>\n<p>inputs</p>\n<p><span class=\"comment-start\" id=\"1330\" data-author=\"Matt Rutkowski\"\ndata-date=\"2015-08-25T21:52:00Z\">TBD: Would this not simpky be the path\nand not include the filename?</span>wp_zip: { $get_artifact: [ SELF,\nzip, C:/wpdata/wp.zip ] }<span class=\"comment-end\" id=\"1330\"></span></p>\n<p>artifacts:</p>\n<p>zip: /data/wordpress.zip</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nIn such implementation the TOSCA orchestrator must provide the\nwordpress.zip archive as a local path (example: C:/wpdata/wp.zip ) and\n**will let it** after the operation is completed.\n\n### <span class=\"comment-start\" id=\"1331", "author": "Calin Curescu", "date": "2023-01-04T16:12:00Z", "comment": "Section missing\u2026", "target": "value"}-->


This function is used as an argument inside validation functions. It
returns the value of the property, attribute, or parameter for which the
validation clause is defined.

#### Grammar 

| \$value: \[\<nested_value_name_or_index\>, ... \] |
|---------------------------------------------------|

#### Arguments

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;nested_value_name_or_index&gt;</td>
<td>no</td>
<td><p>Some TOSCA data are complex (i.e., composed as nested
structures). These parameters are used to dereference into the names of
these nested structures when needed.</p>
<p>Some data represent lists. In these cases, an index may be provided
to reference a specific entry in the list (as identified by the previous
parameter) to return.</p></td>
</tr>
</tbody>
</table>

Boolean Functions
<!----
{"id": "1332", "author": "Calin Curescu", "date": "2022-12-06T16:00:00Z", "comment": "I would not call them condition functions since they can appear also outside conditions.", "target": " Functions"}-->

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TOSCA includes a number of functions that return Boolean values. These
functions are used in validation expressions and in condition clauses in
workflow definitions and policy definitions. They are also used as node
filters in requirement definitions and requirement templates and as
substitution filters in substitution mappings.

### Boolean Logic Functions

#### and

The \$and function takes two or more Boolean arguments. It evaluates to
true if all its arguments evaluate to true. It evaluates to false in all
other cases.

##### Grammar 

| \$and: \[ \<boolean_arg1\>, \<boolean_arg2\>, ... \<boolean_argn\>\] |
|----------------------------------------------------------------------|

#####  Note

Note that the evaluation of the arguments in the \$and function may stop
as soon as a false argument is encountered, and the function may return
immediately without evaluating the rest of the arguments.

#### or

The \$or function takes two or more Boolean arguments. It evaluates to
false if all of its arguments evaluate to false. It evaluates to true in
all other cases.

##### Grammar 

| \$or: \[ \<boolean_arg1\>, \<boolean_arg2\>, ... \<boolean_argn\>\] |
|---------------------------------------------------------------------|

##### Note

Note that the evaluation of the arguments in the \$or function may stop
as soon as a true argument is encountered, and the function may return
immediately without evaluating the rest of the arguments.

#### not

The \$not function takes one Boolean argument. It evaluates to true if
its argument evaluates to false and evaluates to false if its argument
evaluates to true.

##### Grammar 

| \$not: \[ \<boolean_arg\> \] |
|------------------------------|

#### xor

The \$xor function takes two Boolean arguments. It evaluates to false if
both arguments either evaluate to true or both arguments evaluate to
false, and evaluates to true otherwise.

##### Grammar 

| \$xor: \[ \<boolean_arg1\>, \<boolean_arg2\> \] |
|-------------------------------------------------|

### Comparison Functions

The following is the list of recognized comparison functions.

- Note that some implementations may fail the evaluation if the
  arguments are not of the same type.

- Also note that Unicode string comparisons are implementation specific.

- TODO explanation on how versions are
  compared!!\!
<!----
{"id": "1333", "author": "Calin Curescu", "date": "2023-01-04T16:19:00Z", "comment": "TODO explanation on how versions are\n  compared!!!", "target": "TODO explanation on how versions are\n  compared!!\\!"}-->


#### equal

The function takes two arguments of any type. It evaluates to true if
the arguments are equal (that is in both type and value) and evaluates
to false otherwise.

##### Grammar 

| \$equal: \[ \<any_type_arg1\>, \<any_type_arg2\> \] |
|-----------------------------------------------------|

#### greater_than

The function takes two arguments of integer, float, string, timestamp,
version, any scalar type, or their derivations. It evaluates to true if
both arguments are of the same type, and if the first argument is
greater than the second argument and evaluates to false otherwise.

##### Grammar 

| \$greater_than: \[ \<comparable_type_arg1\>, \<comparable_type_arg2\> \] |
|--------------------------------------------------------------------------|

#### greater_or_equal

The function takes two arguments of integer, float, string, timestamp,
version, any scalar type, or their derivations. It evaluates to true if
both arguments are of the same type, and if the first argument is
greater than or equal to the second argument and evaluates to false
otherwise.

##### Grammar 

| \$greater_or_equal: \[ \<comparable_type_arg1\>, \<comparable_type_arg2\> \] |
|------------------------------------------------------------------------------|

#### less_than

The function takes two arguments of integer, float, string, timestamp,
version, any scalar type, or their derivations. It evaluates to true if
both arguments are of the same type, and if the first argument is less
than the second argument and evaluates to false otherwise.

##### Grammar 

| \$less_than: \[ \<comparable_type_arg1\>, \<comparable_type_arg2\> \] |
|-----------------------------------------------------------------------|

#### less_or_equal

The function takes two arguments of integer, float, string, timestamp,
version, any scalar type, or their derivations. It evaluates to true if
both arguments are of the same type, and if the first argument is less
than or equal to the second argument and evaluates to false otherwise.

##### Grammar 

| \$less_or_equal: \[ \<comparable_type_arg1\>, \<comparable_type_arg2\> \] |
|---------------------------------------------------------------------------|

#### valid_values

The function takes two arguments. The first argument is of any type and
the second argument is a list with any number of values of any type. It
evaluates to true if the first argument is equal to a value in the
second argument list and false otherwise.

!!! This function is equivalent to the has_entry function (with reversed
arguments). A good candidate to remove!

#####  Grammar 

| \$valid_values: \[ \<any_type_arg1\>, \<any_type_list_arg2\> \] |
|-----------------------------------------------------------------|

#### matches

The function takes two arguments. The first argument is a general
string, and the second argument is a string that encodes a regular
expression pattern. It evaluates to true if the first argument matches
the regular expression pattern represented by the second argument and
false otherwise.

#####  Grammar 

| \$matches: \[ \<string_type_arg1\>, \<regex_pattern_arg2\> \] |
|---------------------------------------------------------------|

#####  Note

Future drafts of this specification will detail the use of regular
expressions and reference an appropriate standardized grammar.

Note also that if ones means that the whole string is to be matched, the
regular expression must start with a caret ^ and end with a \$.

!!! Check for new lines and maybe add a third argument – e.g. as in
<https://www.pcre.org/> !!!

### Boolean list, map and string functions

#### has_suffix

The function takes two arguments. Both arguments are either of type
string or list. It evaluates to true if the second argument is a suffix
of the first argument. For lists this means that the values of the
second list are the last values of the first list in the same order.

#####  Grammar 

| \$has_suffix: \[ \<string_or_list_type_arg1\>, \<string_or_list_type_arg2\> \] |
|--------------------------------------------------------------------------------|

#### has_prefix

The function takes two arguments. Both arguments are either of type
string or list. It evaluates to true if the second argument is a prefix
of the first argument. For lists this means that the values of the
second list are the first values of the first list in the same order.

#####  Grammar 

| \$has_prefix: \[ \<string_or_list_type_arg1\>, \<string_or_list_type_arg2\> \] |
|--------------------------------------------------------------------------------|

#### contains

The function takes two arguments. Both arguments are either of type
string or list. It evaluates to true if the second argument is contained
in the first argument. For strings that means that the second argument
is a substring of the first argument. For lists this means that the
values of the second list are contained in the first list in an
uninterrupted sequence and in the same order.

#####  Grammar 

| \$contains: \[ \<string_or_list_type_arg1\>, \<string_or_list_type_arg2\> \] |
|------------------------------------------------------------------------------|

#### has_entry

The function takes two arguments. The first argument is a list or a map.
The second argument is of the type matching the entry_schema of the
first argument. It evaluates to true if the second argument is an entry
in the first argument. For lists this means that the second argument is
a value in the first argument list. For maps this means that the second
argument is a value in any of the key-value pairs in the first argument
map.

#####  Grammar 

| \$has_entry: \[ \<list_or_map_type_arg1\>, \<any_type_arg2\> \] |
|-----------------------------------------------------------------|

#### has_key

The function takes two arguments. The first argument is a map. The
second argument is of the type matching the key_schema of the first
argument. It evaluates to true if the second argument is a key in any of
the key-value pairs in the first argument map.

#####  Grammar 

| \$has_key: \[ \<map_type_arg1\>, \<any_type_arg2\> \] |
|-------------------------------------------------------|

#### has_all_entries

The function takes two arguments. The first argument is a list or a map.
The second argument is a list with the entry_schema matching the
entry_schema of the first argument. It evaluates to true if for all
entries in the second argument there is an equal value entry in the
first argument.

#####  Grammar 

| \$has_all_entries: \[ \<list_or_map_type_arg1\>, \<list_type_arg2\> \] |
|------------------------------------------------------------------------|

#### has_all_keys

The function takes two arguments. The first argument is a map. The
second argument is a list with the entry_schema matching the key_schema
of the first argument. It evaluates to true if for all entries in the
second argument there is an equal value key in the first argument.

#####  Grammar 

| \$has_all_keys: \[ \<map_type_arg1\>, \<list_type_arg2\> \] |
|-------------------------------------------------------------|

#### has_any_entry

The function takes two arguments. The first argument is a list or a map.
The second argument is a list with the entry_schema matching the
entry_schema of the first argument. It evaluates to true if there is an
entry in the second argument that is equal to an entry in the first
argument.

#####  Grammar 

| \$has_any_entry: \[ \<list_or_map_type_arg1\>, \<list_type_arg2\> \] |
|----------------------------------------------------------------------|

#### has_any_key

The function takes two arguments. The first argument is a map. The
second argument is a list with the entry_schema matching the key_schema
of the first argument. It evaluates to true if there is an entry in the
second argument which is equal to a key in the first argument.

#####  Grammar 

| \$has_any_key: \[ \<map_type_arg1\>, \<list_type_arg2\> \] |
|------------------------------------------------------------|

String, list, and map functions
<!----
{"id": "1334", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-212](commentsIds.xml) \u2013 Concat intrinsic function", "target": ""}-->
<span class="comment-start" id="1335" author="Chris Lauwers" date="2022-10-10T20:39:00Z">We should rename this section to String Manipulation Functions</span><span class="comment-end" id="1335"></span>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### length

The function takes an argument of type string, list, or map. It returns
the number of nicode characters in the string, or the numbers of values
in the list, or the number of key-values pairs in the map.

####  Grammar 

| \$length: \[ \<string_list_or_map_type_arg\> \] |
|-------------------------------------------------|

### concat

The concat function takes one or more arguments of either the type
string or the type list with the same type of their entry_schema. In the
case of strings, it returns a string which is the concatenation of the
argument strings. In the case of lists, it returns a list that contains
all the entries of all the argument lists. Order is preserved both for
strings and lists. This function does not recurse into the entries of
the lists.

#### Grammar 

| \$concat: \[\<string_or_list_type_arg1\>, … \] |
|------------------------------------------------|

#### Examples

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>outputs:</p>
<p>description: Concatenate the URL for a server from other template
values</p>
<p>server_url:</p>
<p>value: { $concat: [ 'http://',</p>
<p>$get_attribute: [ server, public_address ],</p>
<p>':',</p>
<p>$get_attribute: [ server, port ] ] }</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### join

The join function takes either one or two arguments where the first one
is of type list of strings and the second (optional) argument is of type
string. It returns a string that is the joining of the entries in the
first argument while adding an optional delimiter between the strings.

!!! Make an
example for concat and join where the differences are
clear!!\!
<!----
{"id": "1336", "author": "Calin Curescu", "date": "2023-01-17T17:54:00Z", "comment": "Make a better example.", "target": "!!! Make an\nexample for concat and join where the differences are\nclear!!\\!"}-->


#### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$join: [&lt;list_of_strings&gt; ]</p>
<p>$join: [&lt;list of strings&gt;, &lt;delimiter&gt; ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Arguments

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Mandatory</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;list of strings&gt;</td>
<td>yes</td>
<td><p>
<!----
{"id": "1337\"\ndata-author=\"Matt Rutkowski\" data-date=\"2017-04-18T12:03:00Z\">MUSTFIX:\nInclusive of values in YAML that can be treated as string such as int,\netc.<br />\nMUSTFIX: Optional delimter like an underscore \u2018_\u2019</span>list of</p>\n<p><a href=\"#TYPE_YAML_STRING\">string</a> or</p>\n<p><a href=\"#TYPE_YAML_STRING\">string</a> value expressions<span\nclass=\"comment-end\" id=\"1337\"></span></p></td>\n<td>A list of one or more strings (or expressions that result in a list\nof string values) which can be joined together into a single\nstring.</td>\n</tr>\n<tr class=\"even\">\n<td>&lt;delimiter&gt;</td>\n<td>no</td>\n<td>string</td>\n<td>An optional delimiter used to join the string in the provided\nlist.</td>\n</tr>\n</tbody>\n</table>\n\n#### Examples\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>outputs:</p>\n<p>example1:</p>\n<p># Result: prefix_1111_suffix</p>\n<p>value: { $join: [ [\"prefix\", 1111, \"suffix\" ], \"_\" ] }</p>\n<p>example2:</p>\n<p># Result: 9.12.1.10,9.12.1.20</p>\n<p>value: { $join: [ { $get_input: my_IPs }, \u201c,\u201d ] }</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\n### token\n\nThe token function is used within a TOSCA service template on a string\nto parse out (tokenize) substrings separated by one or more token\ncharacters within a larger string.\n\n#### Grammar \n\n| \\$token: \\[ \\<string_with_tokens\\>, \\<string_of_token_chars\\>, \\<substring_index\\> \\] |\n|---------------------------------------------------------------------------------------|\n\n#### Arguments\n\n| Argument              | Mandatory | Type                          | Description                                                                                                                                                           |\n|-----------------------|-----------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| string_with_tokens    | yes       | [string](#TYPE_YAML_STRING)   | The composite string that contains one or more substrings separated by token characters.                                                                              |\n| string_of_token_chars | yes       | [string](#TYPE_YAML_STRING)   | The string that contains one or more token characters that separate substrings within the composite string.                                                           |\n| substring_index       | yes       | [integer](#TYPE_YAML_INTEGER) | The integer indicates the index of the substring to return from the composite string. Note that the first substring is denoted by using the \u20180\u2019 (zero) integer value. |\n\n#### Examples\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>outputs:</p>\n<p>webserver_port:</p>\n<p>description: the port provided at the end of my server\u2019s endpoint\u2019s\nIP address</p>\n<p>value: { <span class=\"comment-start\" id=\"1338\"\ndata-author=\"Matt Rutkowski\" data-date=\"2015-08-25T21:52:00Z\">TBD:\ndocument behavior when token not found in string or index represents a\ntoken that does not exist (e.g., input string does not contain that many\ntokens, array index out of bounds).</span>token<span class=\"comment-end\"\nid=\"1338\"></span>: [ $get_attribute: [ my_server, data_endpoint,\nip_address ],</p>\n<p>\u2018:\u2019,</p>\n<p><span class=\"comment-start\" id=\"1339\" data-author=\"Matt Rutkowski\"\ndata-date=\"2015-08-25T21:52:00Z\">Alternatives:<br />\ntokenize to a list (array)<br />\n</span>1 ] }<span class=\"comment-end\" id=\"1339\"></span></p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nSet functions<span class=\"comment-start\" id=\"1340", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-212](commentsExtensible.xml) \u2013 Concat intrinsic function", "target": ""}-->
<span class="comment-start" id="1341" author="Chris Lauwers" date="2022-10-10T20:39:00Z">We should rename this section to String Manipulation Functions</span><span class="comment-end" id="1341"></span>
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!!!Note: We should discuss order!!!!

### union

The function takes one or more list arguments, all having the entry
schema of the same type. The result is a list that contains all
non-duplicate entries from all the argument lists. By non-duplicate is
meant that no two entries in the result list are equal.

#### Grammar 

| \$union: \[ \<list_arg1\>, … \] |
|---------------------------------|


<!----
{"id": "1342", "author": "Chris Lauwers", "date": "2022-10-10T20:39:00Z", "comment": "We should rename this section to String\nManipulation Functions", "target": ""}-->


#### Note 

The union applied to only one list will return a result where all the
duplicate entries of the argument list are eliminated. Note also that
the order of the elements in the result list is not specified.

### intersection

The function takes one or more list arguments, all having the entry
schema of the same type. The result is a list that contains all entries
that can be found in each of the argument lists.

#### Grammar 

| \$intersection: \[ \<list_arg1\>, … \] |
|----------------------------------------|

#### Note 

The intersection applied to only one list will return a result where all
the duplicate entries of the argument list are eliminated. Note also
that the order of the elements in the result list is not specified.

Arithmetic functions
<!----
{"id": "1343", "author": "Matt Rutkowski", "date": "2015-08-25T21:52:00Z", "comment": "[TOSCA-212](https://www.oasis-open.org/committees/tosca/) \u2013 Concat intrinsic function", "target": ""}-->

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### sum

The function takes one or more arguments of either integer, float, or
scalar type. The result is of the same type as the arguments and its
value is the arithmetic sum of the arguments’ values.

#### Grammar 

| \$sum: \[ \<int_float_or_scalar_type_arg1\>, \< int_float_or_scalar_type_arg2\>, … \] |
|---------------------------------------------------------------------------------------|

### difference

The function takes two arguments of either integer, float, or scalar
type. The result is of the same type as the arguments and its value is
the arithmetic subtraction of the second argument value from the first
argument value.

#### Grammar 

| \$difference: \[ \<int_float_scalar_type_arg1\>, \< int_float_scalar_type_arg2\> \] |
|-------------------------------------------------------------------------------------|

### product

The function takes either:

- Two arguments where the first argument is of a scalar type and the
  second argument is of an integer or float type. The result is of the
  same type as the first argument and its value is the arithmetic
  product of the first argument value and the second argument value.

- Any number of arguments of type integer or float. If all inputs are of
  type integer, then the result is of type integer, otherwise it is of
  type float. The result value is the arithmetic product of all the
  arguments values.

#### Grammar 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$product: [ &lt;scalar_type_arg1&gt;, &lt;
int_or_float_type_arg2&gt; ]</p>
<p>$product: [ &lt;int_or_float_type_arg1&gt;, &lt;
int_or_float_type_arg2&gt;, … ]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### quotient

The function takes two arguments where the first argument is of an
integer, float, or scalar type and the second argument is of an integer
or float type. The result is of

- A scalar type if the first argument is a scalar, and its value is the
  arithmetic division of the first argument value by the second argument
  value. If necessary, the result might be truncated, as decided by the
  implementation.

- A float if the first argument is an integer or a float. Note that to
  transform the float to an integer a round or ceil or floor function
  must be used.

#### Grammar 

| \$quotient: \[ \<int_float_or_scalar_type_arg1\>, \< int_or_float_type_arg2\> \] |
|----------------------------------------------------------------------------------|

### remainder

The function takes two arguments where the first argument is of an
integer, or scalar type and the second argument is of an integer. The
result is of the same type as the first argument and its value is the
remainder of the division to the second argument.

#### Grammar 

| \$remainder: \[ \<int_or_scalar_type_arg1\>, \< int_type_arg2\> \] |
|--------------------------------------------------------------------|

### round

The function takes a float argument. The result is an integer with the
closest value to the float argument. Equal value distance is rounded
down (e.g. 3.5 is rounded down to 3, while 3.53 is rounded up to 4).

#### Grammar 

| \$round: \[ \<float_type_arg\> \] |
|-----------------------------------|

### floor

The function takes a float argument. The result is an integer with the
closest value that is less or equal to the value of the float argument.

#### Grammar 

| \$floor: \[ \<float_type_arg\> \] |
|-----------------------------------|

### ceil

The function takes a float argument. The result is an integer with the
closest value that is greater or equal to the value of the float
argument.

#### Grammar 

| \$ceil: \[ \<float_type_arg\> \] |
|----------------------------------|

TOSCA Cloud Service Archive (CSAR) format
=========================================

This section defines the metadata of a cloud service archive as well as
its overall structure. Except for the examples, this section is
**normative.**

Overall Structure of a CSAR
---------------------------

A CSAR is a
zip file 
<!----
{"id": "1367", "author": "Calin Curescu", "date": "2020-06-09T17:00:00Z", "comment": "Thinh would like to have this resolved\nbefore publishing TOSCA v2.0. What is zip? We need to give a clearer\ndefinition of the zip format. What version. Thinh will get back with a\nmore specific definition.  \nTal: look at java **jar specification**? It is zip...", "target": "A CSAR is a\nzip file "}-->
where TOSCA
definitions along with all accompanying artifacts (e.g. scripts,
binaries, configuration files) can be packaged together. The zip file
format shall conform to the Document Container File format as defined in
the ISO/IEC 21320-1 "Document Container File — Part 1: Core" standard
\[[ISO-IEC-21320-1](#CIT_ISO_IEC_21320_1)\]. A CSAR zip file MUST
contain one of the following:

- A
  **TOSCA.meta** metadata file that provides entry information for a
  TOSCA orchestrator processing the CSAR file.
<!----
{"id": "1368", "author": "Calin Curescu", "date": "2019-01-30T15:18:00Z", "comment": "Why keep a mandatory directory for only\n  one file. I think we should allow to have the TOSCA.meta file also in\n  the root of the archive.  \n  Then the processor should do the following:  \n  Look for the TOSCA-Metadata directory. If found, look for the\n  TOSCA.meta inside. If latter not found give an error.  \n  Else look for the TOSCA.meta file in the root of the archive  \n  Look for the a .yml or . yaml file in the root directory", "target": "\n  **TOSCA.meta** metadata file that provides entry information for a\n  TOSCA orchestrator processing the CSAR file."}-->
 The **TOSCA.meta** file may be located either at the
  root of the archive or inside a **TOSCA-Metadata** directory (the
  directory being at the root of the archive). The CSAR may contain only
  one **TOSCA.meta** file.

- a yaml (.yml or .yaml) file at the root of the archive, the yaml file
  being a valid tosca definition template.

The CSAR file MAY contain other directories and files with arbitrary
names and contents.

TOSCA Meta File
---------------

A TOSCA meta file consists of name/value pairs. The name-part of a
name/value pair is followed by a colon, followed by a blank, followed by
the value-part of the name/value pair. The name MUST NOT contain a
colon. Values that represent binary data MUST be base64 encoded. Values
that extend beyond one line can be spread over multiple lines if each
subsequent line starts with at least one space. Such spaces are then
collapsed when the value string is read.

| \<name\>: \<value\> |
|---------------------|

Each name/value pair is in a separate line. A list of related name/value
pairs, i.e. a list of consecutive name/value pairs is called a block.
Blocks are separated by an empty line. The first block, called block_0,
contains metadata about the CSAR itself and is further defined below.
Other blocks may be used to represent custom generic metadata or
metadata pertaining to files in the CSAR. A **TOSCA.meta** file is only
required to include block_0. The structure of block_0 in the TOSCA meta
file is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TOSCA service template
<!----
{"id": "1380\"\ndata-author=\"Matt Rutkowski\" data-date=\"2018-03-06T12:31:00Z\">MUSTFIX:\nbump<br />\n1.2? (independent)<br />\n1.3? (match spec. level)</span>CSAR-Version: digit.digit</p>\n<p>Created-By: string</p>\n<p>Entry-Definitions: string</p>\n<p>Other-Definitions: string</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nhe name/value pairs are as follows:\n\n- **CSAR-Version**: This is the version number of the CSAR\n  specification. It defines the structure of the CSAR and the format of\n  the **TOSCA.meta** file. The value MUST be \u201c2.0\u201d for this version of\n  the CSAR specification.\n\n- **Created-By**: The person or organization that created the CSAR.\n\n- **Entry-Definitions**: This references the TOSCA definitions file that\n  SHOULD be used as entry point for processing the contents of the CSAR\n  (e.g. the main <span class=\"comment-start\" id=\"1381", "author": "Calin Curescu", "date": "2020-06-02T17:15:00Z", "comment": "Tal: this is not\n  necessary a service template may be only used for type definitions or\n  potentially to artifact definitions. This is a terminology problem. To\n  revisit that. Tal suggests that the **Entry-Definitions** should not\n  be required.", "target": "TOSCA service template"}-->
).

- **Other-Definitions**: This references an unambiguous set of files
  containing substitution templates that can be used to implement nodes
  defined in the main template (i.e. the file declared in
  **Entry-Definitions**). Thus, all the service templates defined in
  files listed under the **Other-Definitions** key are to be used only
  as substitution templates, and not as standalone services. If such a
  service template cannot act as a substitution template, it will be
  ignored by the orchestrator. The value of the **Other-Definitions**
  key is a string containing a list of filenames (relative to the root
  of the CSAR archive) delimited by a blank space. If the filenames
  contain blank spaces, the filename should be enclosed by double
  quotation marks (“)

Note that any further TOSCA definitions files required by the
definitions specified by **Entry-Definitions** or **Other-Definitions**
can be found by a TOSCA orchestrator by processing respective
**imports** statements. Note also that artifact files (e.g. scripts,
binaries, configuration files) used by the TOSCA definitions and
included in the CSAR are fully described and referred via relative path
names in artifact definitions in the respective TOSCA definitions files
contained in the CSAR.
<!----
{"id": "1382", "author": "Calin Curescu", "date": "2019-01-30T16:36:00Z", "comment": "MustFix.  \nIn version 1.0 (pre YAML) the subsequent blocks that contained\ndefinitions were used to provide definitions for types imported in the\nservice template, that is these files were parsed instead of taking the\ndefinitions from external repositoris.  \nSince 1.0 yaml, the files are specified explicitly in the imports\nstatements.  \nNevertheless, by allowing the other definition blocks (as per this\nparagraph formulation) we allow also the old style of imports by the\ndefinitions in the other blocks.  \nI think this puts a burden on the implementation of orchestrators and\nquite confusing. So we should deprecate the usage of definitions in the\nother blocks.  \nMoreover, the other blocks can contain other file type decriptions (for\nartifacts) in the other blocks. E.g:  \nName: Plans/AddUser.bpmn  \nContent-Type: application/vnd.oasis.bpmn  \nThese also seem obsolete and useless.  \nI think we should deprecate the other blocks in the TOSCA.meta\nfile", "target": "Note that any further TOSCA definitions files required by the\ndefinitions specified by **Entry-Definitions** or **Other-Definitions**\ncan be found by a TOSCA orchestrator by processing respective\n**imports** statements. Note also that artifact files (e.g. scripts,\nbinaries, configuration files) used by the TOSCA definitions and\nincluded in the CSAR are fully described and referred via relative path\nnames in artifact definitions in the respective TOSCA definitions files\ncontained in the CSAR."}-->


### Custom keynames in the TOSCA.meta file

Users can populate other blocks than block_0 in the TOSCA.meta file with
custom name/value pairs that follow the entry syntax defined above and
have names that are different from the normative keynames (e.g.
CSAR-Version, Created-By, Entry-Definitions, Other-Definitions). These
custom name/value pairs are outside the scope of the TOSCA
specification.Nevertheless, future versions of the TOSCA specification
may add definitions of new keynames to be used in the **TOSCA.meta**
file. In case of a keyname collision (with a custom keyname) the TOSCA
specification definitions take precedence.

To minimize such keyname collisions the specification reserves the use
of keynames starting with TOSCA and tosca. It is recommended as a good
practice to use a specific prefix (e.g. identifying the organization,
scope, etc.) when using custom keynames.

### Example

The following listing represents a valid **TOSCA.meta** file according
to this TOSCA specification.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The
implementations subject to conformance are those introduced in Section
11.3 “Implementations”. They are listed here for
convenience:
<!----
{"id": "1393\"\ndata-author=\"Matt Rutkowski\" data-date=\"2018-03-06T12:31:00Z\">MUSTFIX:\nbump<br />\n1.2? (independent)<br />\n1.3? (match spec. level)</span>CSAR-Version: 2.0</p>\n<p>Created-By: OASIS TOSCA TC</p>\n<p>Entry-Definitions: tosca_elk.yaml</p>\n<p>Other-Definitions: definitions/tosca_moose.yaml\ndefinitions/tosca_deer.yaml</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nThis **TOSCA.meta** file indicates its structure (as well as the overall\nCSAR structure) by means of the **CSAR-Version** keyname with value\n**2.0**. The **Entry-Definitions** keyname points to a TOSCA definitions\nYAML file with the name **tosca_elk.yaml** which is contained in the\nroot of the CSAR file. Additionally, it specifies that substitution\ntemplates can be found in the files **tosca_moose.yaml** and\n**tosca_deer.yaml** found in the directory called **definitions** in the\nroot of the CSAR file.\n\nArchive without TOSCA-Metadata\n------------------------------\n\nIn case the archive doesn\u2019t contains a **TOSCA.meta** file the archive\nis required to contains a single YAML file at the root of the archive\n(other templates may exist in sub-directories).\n\nTOSCA processors should recognize this file as being the CSAR\nEntry-Definitions file. The CSAR-Version is inferred from the\ntosca_definitions_version keyname in the Entry-Definitions file. For\ntosca_definitions_version: tosca_2_0 and onwards, the corresponding\nCSAR-version is 2.0 unless further defined.\n\nNote that in a CSAR without TOSCA-metadata it is not possible to\nunambiguously include definitions for substitution templates as we can\nhave only one service template defined in a yaml file.\n\n### Example\n\nThe following represents a valid TOSCA template file acting as the CSAR\nEntry-Definitions file in an archive without TOSCA-Metadata directory.\n\n<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th><p>tosca_definitions_version: tosca_2_0</p>\n<p>metadata:</p>\n<p>template_name: my_template</p>\n<p>template_author: OASIS TOSCA TC</p>\n<p>template_version: 1.0</p></th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>\n\nSecurity Considerations\n=======================\n\n<span class=\"mark\">(**Note:** OASIS strongly recommends that Technical\nCommittees consider issues that could affect security when implementing\ntheir specification and document them for implementers and adopters. For\nsome purposes, you may find it required, e.g. if you apply for IANA\nregistration.</span>\n\n<span class=\"mark\">While it may not be immediately obvious how your\nspecification might make systems vulnerable to attack, most\nspecifications, because they involve communications between systems,\nmessage formats, or system settings, open potential channels for\nexploit. For example, IETF \\[[RFC3552](#RFC3552)\\] lists \u201ceavesdropping,\nreplay, message insertion, deletion, modification, and\nman-in-the-middle\u201d as well as potential denial of service attacks as\nthreats that must be considered and, if appropriate, addressed in IETF\nRFCs.</span>\n\n<span class=\"mark\">In addition to considering and describing foreseeable\nrisks, this section should include guidance on how implementers and\nadopters can protect against these risks.</span>\n\n<span class=\"mark\">We encourage editors and TC members concerned with\nthis subject to read *Guidelines for Writing RFC Text on Security\nConsiderations,* IETF \\[[RFC3552](#RFC3552)\\], for more\ninformation.)</span>\n\nConformance\n===========\n\n<span class=\"mark\">(**Note**: The [OASIS TC\nProcess](https://www.oasis-open.org/policies-guidelines/tc-process#wpComponentsConfClause)\nrequires that a specification approved by the TC at the Committee\nSpecification Public Review Draft, Committee Specification or OASIS\nStandard level must include a separate section, listing a set of\nnumbered conformance clauses, to which any implementation of the\nspecification must adhere in order to claim conformance to the\nspecification (or any optional portion thereof). This is done by listing\nthe conformance clauses here.</span>\n\n<span class=\"mark\">For the definition of \"conformance clause,\" see\n[OASIS Defined\nTerms](https://www.oasis-open.org/policies-guidelines/oasis-defined-terms-2017-05-26#dConformanceClause).</span>\n\n<span class=\"mark\">See \"Guidelines to Writing Conformance Clauses\":  \n<http://docs.oasis-open.org/templates/TCHandbook/ConformanceGuidelines.html>.</span>\n\n<span class=\"mark\">Remove this note before submitting for\npublication.)</span>\n\nConformance Targets\n-------------------\n\n<span class=\"comment-start\" id=\"2410", "author": "Matt Rutkowski", "date": "2015-12-03T11:41:00Z", "comment": "Fixed typo and section reference.", "target": "The\nimplementations subject to conformance are those introduced in Section\n11.3 \u201cImplementations\u201d. They are listed here for\nconvenience:"}-->


- TOSCA YAML service template

- TOSCA processor

- TOSCA orchestrator (also called orchestration engine)

- TOSCA generator

- TOSCA archive

Conformance Clause 1: TOSCA YAML service template
-------------------------------------------------

A document conforms to this specification as TOSCA YAML service template
if it satisfies all the statements below:

1.  It is valid according to the grammar, rules and requirements defined
    in section 3 “TOSCA definitions in YAML”.

<!-- -->

20. When using functions defined in section 4 “TOSCA functions”, it is
    valid according to the grammar specified for these functions.

21. When using or referring to data types, artifact types, capability
    types, interface types, node types, relationship types, group types,
    policy types defined in section 5 “TOSCA normative type
    definitions”, it is valid according to the definitions given in
    section 5.

Conformance Clause 2: TOSCA processor
-------------------------------------

A processor or program conforms to this specification as TOSCA processor
if it satisfies all the statements below:

1.  It can parse and recognize the elements of any conforming TOSCA YAML
    service template, and generates errors for those documents that fail
    to conform as TOSCA YAML service template while clearly intending
    to.

<!-- -->

22. It implements the requirements and semantics associated with the
    definitions and grammar in section 3 “TOSCA definitions in YAML”,
    including those listed in the “additional requirements” subsections.

23. It resolves the imports, either explicit or implicit, as described
    in section 3 “TOSCA definitions in YAML”.

24. It generates errors as required in error cases described in sections
    3.1 (TOSCA Namespace URI and alias), 3.2 (Parameter and property
    type) and 3.6 (Type-specific definitions).

25. It normalizes string values as described in section 5.4.9.3
    (Additional Requirements)

Conformance Clause 3: TOSCA orchestrator
----------------------------------------

A processor or program conforms to this specification as TOSCA
orchestrator if it satisfies all the statements below:

1.  It is conforming as a TOSCA Processor as defined in conformance
    clause 2: TOSCA Processor.

<!-- -->

26. It can process all types of artifact described in section 5.3
    “Artifact types” according to the rules and grammars in this
    section.

27. It can process TOSCA archives as intended in section 6 “TOSCA Cloud
    Service Archive (CSAR) format” and other related normative sections.

28. It can understand and process the functions defined in section 4
    “TOSCA functions” according to their rules and semantics.

29. It can understand and process the normative type definitions
    according to their semantics and requirements as described in
    section 5 “TOSCA normative type definitions”.

30. It can understand and process the networking types and semantics
    defined in section 7 “TOSCA Networking”.

31. It generates errors as required in error cases described in sections
    2.10 (Using node template substitution for chaining subsystems), 5.4
    (Capabilities Types) and 5.7 (Interface Types).).

Conformance Clause 4: TOSCA generator
-------------------------------------

A processor or program conforms to this specification as TOSCA generator
if it satisfies at least one of the statements below:

1.  When requested to generate a TOSCA service template, it always
    produces a conforming TOSCA service template, as defined in Clause
    1: TOSCA YAML service template,

<!-- -->

32. When requested to generate a TOSCA archive, it always produces a
    conforming TOSCA archive, as defined in Clause 5: TOSCA archive.

Conformance Clause 5: TOSCA archive
-----------------------------------

A package artifact conforms to this specification as TOSCA archive if it
satisfies all the statements below:

1.  It is valid according to the structure and rules defined in section
    6 “TOSCA Cloud Service Archive (CSAR) format”.

Acknowledgments
===============

<span class="mark">(**Note:** A Work Product approved by the TC must
include a list of people who participated in the development of the Work
Product. This is generally done by collecting the list of names in this
appendix. This list shall be initially compiled by the Chair, and any
Member of the TC may add or remove their names from the list by
request.</span>

<span class="mark">Remove this note before submitting for
publication.)</span>

The following individuals have participated in the creation of this
specification and are gratefully acknowledged:

Participants:

Adam Souzis (<adam@souzis.com>)

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

Frank Leymann (<Frank.Leymann@informatik.uni-stuttgart.de>), Univ. of
Stuttgart

Gábor Marton (<gabor.marton@nokia.com>), Nokia

Gerd Breiter (<gbreiter@de.ibm.com>), IBM

Hemal Surti (<hsurti@cisco.com>), Cisco

Ifat Afek (<ifat.afek@alcatel-lucent.com>), Alcatel-Lucent

Idan Moyal, (<idan@gigaspaces.com>), Gigaspaces

Jacques Durand (<jdurand@us.fujitsu.com>), Fujitsu

Jin Qin, (<chin.qinjin@huawei.com>), Huawei

Jeremy Hess, (<jeremy@gigaspaces.com>), Gigaspaces

John Crandall,
([mailto:jcrandal@brocade.com](mailto:jcrandal@brocade.com)), Brocade

Juergen Meynert (<juergen.meynert@ts.fujitsu.com>), Fujitsu

Kapil Thangavelu (<kapil.thangavelu@canonical.com>), Canonical

Karsten Beins (<karsten.beins@ts.fujitsu.com>), Fujitsu

Kevin Wilson (<kevin.l.wilson@hp.com>), HP

Krishna Raman (<kraman@redhat.com>), Red Hat

Luc Boutier (<luc.boutier@fastconnect.fr>), FastConnect

Luca Gioppo, (<luca.gioppo@csi.it>), CSI-Piemonte

Matej Artač, (<matej.artac@xlab.si>), XLAB

Matt Rutkowski (<mrutkows@us.ibm.com>), IBM

Moshe Elisha (<moshe.elisha@alcatel-lucent.com>), Alcatel-Lucent

Nate Finch (<nate.finch@canonical.com>), Canonical

Nikunj Nemani (<nnemani@vmware.com>), Wmware

Peter Bruun (<peter-michael.bruun@hpe.com>), Hewlett Packard Enterprise

Philippe Merle (<philippe.merle@inria.fr>), Inria

Priya TG (<priya.g@netcracker.com)> NetCracker

Richard Probst (<richard.probst@sap.com>), SAP AG

Sahdev Zala (<spzala@us.ibm.com>), IBM

Shitao li (<lishitao@huawei.com>), Huawei

Simeon Monov (<sdmonov@us.ibm.com>), IBM

Sivan Barzily (<sivan@gigaspaces.com>), Gigaspaces

Sridhar Ramaswamy (<sramasw@brocade.com>), Brocade

Stephane Maes (<stephane.maes@hp.com>), HP

Steve Baillargeon (<steve.baillargeon@ericsson.com>), Ericsson

Tal Liron (tliron@redhat.com)

Thinh Nguyenphu (<thinh.nguyenphu@nokia.com>), Nokia

Thomas Spatzier (<thomas.spatzier@de.ibm.com>), IBM

Ton Ngo (<ton@us.ibm.com>), IBM

Travis Tripp (<travis.tripp@hp.com>), HP

Vahid Hashemian (<vahidhashemian@us.ibm.com>), IBM

Wayne Witzel (<wayne.witzel@canonical.com>), Canonical

Yaron Parasol (<yaronpa@gigaspaces.com>), Gigaspaces

Example Title
=============

text

Subsidiary section
------------------

text

### Sub-subsidiary section

Text

### Sub-sub-subsidiary section

text

### Sub-sub-sub-subsidiary section

text

Revision History
================

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 56%" />
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
<td>2019-04-01</td>
<td>Chris Lauwers</td>
<td>Initial WD01, Revision 01 baseline for TOSCA v2.0</td>
</tr>
<tr class="even">
<td>WD01, Rev02</td>
<td>2019-04-22</td>
<td>Chris Lauwers</td>
<td>Split of introductory chapters into the <em>Introduction to TOSCA
Version 2.0</em> document.</td>
</tr>
<tr class="odd">
<td>WD01, Rev03</td>
<td>2019-05-08</td>
<td>Calin Curescu</td>
<td>Incorporate fixes from latest v1.3 specification</td>
</tr>
<tr class="even">
<td>WD01, Rev04</td>
<td>2019-05-10</td>
<td>Chris Lauwers</td>
<td>Fix syntax of schema constraint examples (Sections 5.3.2 and
5.3.4)</td>
</tr>
<tr class="odd">
<td>WD01, Rev05</td>
<td>2019-08-30</td>
<td>Chris Lauwers</td>
<td>Cleanup formatting. No content changes.</td>
</tr>
<tr class="even">
<td>WD01, Rev06</td>
<td>2019-08-30</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Remove 3.6.20.3 since it is no longer relevant.</p></li>
<li><p>Separate out new Operation Assignment section 3.8.3 from the
original Operation Definition section 3.6.17</p></li>
<li><p>Separate out new Notification Assignment section 3.8.4 from the
original Notification Definition section 3.6.19</p></li>
<li><p>Separate out new Interface Assignment section 3.8.5 from the
original Interface Definition section 3.6.20</p></li>
<li><p>Update the Interface Type definitions in section 5.8 to show the
(now mandatory) ‘operations’ keyname.</p></li>
<li><p>Remove erroneous interface definition in tosca.groups.Root type
(section 5.10.1)</p></li>
<li><p>Added ‘description’ keyname to Requirement definition (section
3.7.3)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD01, Rev07</td>
<td>2019-09-08</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Added the “value” keyname to property definition (Section 3.6.10
Property Definition),</p></li>
<li><p>Made the difference between outgoing and incoming parameters in
the parameter definition (Section 3.6.14 Parameter definition)</p></li>
<li><p>Added the “mapping” keyname to the parameter definition, for
mapping the incoming parameter to an attribute (Section 3.6.14 Parameter
definition)</p></li>
<li><p>Changed the wrong usage of “property definitions” and “property
assignments” instead of “parameter definitions” and “parameter
assignments” throughout the document. For example, a larger impact can
be seen in the definition of the get_input function (Section 4.4.1
get_input).</p></li>
<li><p>Changed Section “3.6.16 Operation implementation definition” to
include notification implementation definition (Section 3.6.16 Operation
implementation definition and notification implementation
definition).</p></li>
<li><p>Deleted Section “3.6.18 Notification implementation definition”
since it was redundant and all relevant information has been transferred
to Section “3.6.16 Operation implementation definition and notification
implementation definition”. The “Notification definition” section
becomes the new Section 3.6.18.</p></li>
<li><p>Added operation assignment rules to the operation assignment
section (Section 3.8.3 Operation Assignment).</p></li>
<li><p>Added notification assignment rules to the notification
assignment section (Section 3.8.4 Notification assignment).</p></li>
<li><p>Added interface assignment rules to the interface assignment
section (Section 3.8.5 Interface assignment).</p></li>
<li><p>Changed “interface definitions” with “interface assignments” in
the node template specification, given that we have split interface
assignments from interface definitions (Section 3.8.6 Node
Template)</p></li>
<li><p>Changed “interface definitions” with “interface assignments” in
the relationship template specification, given that we have split
interface assignments from interface definitions (Section 3.8.7
Relationship Template)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD01, Rev08</td>
<td>2019-09-30</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Fix error in TimeInterval example (Section 5.3.7.3.1)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD01, Rev09</td>
<td>2020-02-20</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Move normative type definitions to the “Intro to TOSCA”
document</p></li>
<li><p>Move non-normative type definitions to the “Intro to TOSCA”
document</p></li>
<li><p>Move “CSAR” specification from the “intro to TOSCA” document into
this document</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD01, Rev10</td>
<td>2020-04-15</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Reorganized sections into a new layout (starting with the main
concepts):</p></li>
<li><p>3.5 -&gt; 3.1; 3.10 -&gt; 3.2.1; 3.1 -&gt; 3.2.2.1; 3.2 -&gt;
3.2.2.2; 3.6.8 -&gt; 3.2.3.1; 3.6.6 -&gt; 3.2.3.2; 3.6.1 -&gt; 3.2.4.1;
3.6.2 -&gt; 3.2.4.2; 3.7.1 -&gt; 3.2.5.2; 3.9 -&gt; 3.2.6; 3.7.9 -&gt;
3.3.1; 3.8.6 -&gt; 3.3.2; 3.7.10 -&gt; 3.3.3; 3.8.7 -&gt; 3.3.4; 3.7.7
-&gt; 3.3.5.1; 3.7.2 -&gt; 3.3.5.2; 3.8.1 -&gt; 3.3.5.3; 3.7.8 -&gt;
3.3.5.4; 3.7.3 -&gt; 3.3.5.5; 3.8.2 -&gt; 3.3.5.6; 3.6.5 -&gt; 3.3.5.7;
3.6.4 -&gt; 3.3.5.8; 3.7.5 -&gt; 3.3.6.1; 3.6.19 -&gt; 3.3.6.2; 3.8.5
-&gt; 3.3.6.3; 3.6.17 -&gt; 3.3.6.4; 3.8.3 -&gt; 3.3.6.5; 3.6.18 -&gt;
3.3.6.6; 3.8.4 -&gt; 3.3.6.7; 3.6.16 -&gt; 3.3.6.8; 3.7.4 -&gt; 3.3.7.1;
3.6.7 -&gt; 3.3.7.2; 3.3 -&gt; 3.4.1; 3.7.6 -&gt; 3.4.2; 3.6.9 -&gt;
3.4.3; 3.6.3 -&gt; 3.4.4; 3.6.10 -&gt; 3.4.5; 3.6.11 -&gt; 3.4.6; 3.6.12
-&gt; 3.4.7; 3.6.13 -&gt; 3.4.8; 3.6.14 -&gt; 3.4.9; 3.8.16 -&gt; 3.5.1;
3.8.11 -&gt; 3.5.2; 3.8.12 -&gt; 3.5.3; 3.8.13 -&gt; 3.5.4; 3.8.14 -&gt;
3.5.5; 3.8.15 -&gt; 3.5.6; 3.7.11 -&gt; 3.6.1; 3.8.8 -&gt; 3.6.2; 3.7.12
-&gt; 3.6.3; 3.8.9 -&gt; 3.6.4; 3.6.21 -&gt; 3.6.5; 3.6.20 -&gt; 3.6.6;
3.6.24 -&gt; 3.6.7; 3.6.23 -&gt; 3.6.8; 3.6.22 -&gt; 3.6.9; 3.8.10 -&gt;
3.7.1; 3.6.25 -&gt; 3.7.2; 3.6.26 -&gt; 3.7.3</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD02, Rev01</td>
<td>2020-04-23</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Added Section 3.1.2 Modeling definitions and reuse</p></li>
<li><p>Added Section 3.1.3 Goal of the derivation and refinement
rules</p></li>
<li><p>Added Section 3.2.5 Type definitions</p></li>
<li><p>Added Section 3.2.5.1 General derivation and refinement
rules</p></li>
<li><p>Reworked and simplified Section 3.2.5.2 as describing common
keynames that apply to all TOSCA entity types. Added derivation rules
for the common keynames in TOSCA entity types (Section 3.2.5.2.3
Derivation rules).</p></li>
<li><p>Added derivation rules for the following TOSCA entity types:
node, relationship, capability, interface, and data types in their
specific sections. The new sub-sections are named “Derivation
rules”.</p></li>
<li><p>Added refinement rules for entitiy definitions contained in types
undergoing derivations. Refinement rules for the following entity
definitions: capability, requirement, interface, operation,
notification, schema, property, attribute, and parameter definitions
have been added in their specific sections. The new sub-sections are
named “Refinement rules”.</p></li>
<li><p>Explained that definitions for the properties, attributes and
valid_source_types in a capability definition are refinements of the
definitions in the capability type (Section 3.3.5.2. Capability
definition).</p></li>
<li><p>Changed the occurrences keyname in a capability assignment from a
range of integer to an integer, to correct the wrong specification in
TOSCA v1.3 (Section 3.3.5.3. Capability assignment).</p></li>
<li><p>Added the possibility to have provide a symbolic name of a
Capability definition within a target Node Type that can fulfill the
requirement in the Requirement definition (in addition to the Capability
Type) (Section 3.3.5.5. Requirement definition).</p></li>
<li><p>Added the possibility to provide a node_filter also in the
Requirement definition (this node filter is applied in addition to the
node filter defined in the Requirement assignment) (Section 3.3.5.5.
Requirement definition).</p></li>
<li><p>Explained that the specification supports providing several
requirement assignments with the same symbolic name that represent
subsets of the occurrences specified in the Requirement definition
(Section 3.3.5.6. Requirement assignment).</p></li>
<li><p>Changed the occurrences keyname in a requirement assignment from
a range of integer to an integer, to correct the wrong specification in
TOSCA v1.3 (Section 3.3.5.6. Requirement assignment).</p></li>
<li><p>Explained that property definitions may not be added to data
types derived_from TOSCA primitive types (Section 3.4.2 Data
Type).</p></li>
<li><p>Added the rule for a map key definition that its type must be
originally derived from string. This is due to fact that in many
YAML/TOSCA parsers it is hard to process keys that are not strings, and
the added benefit of non-string keys is minimal (Section 3.4.3 Schema
definition).</p></li>
<li><p>Explained that the default value is irrelevant for properties and
parameters that are not required (i.e. where the keyname required is
“false”) as they will stay undefined (Section 3.4.5 Property definition
and Section 3.4.9 Parameter definition).</p></li>
<li><p>A value definition “fixes” the property, that is it cannot be
further refined (in a type) or even assigned in (in a template) (Section
3.4.5 Property definition and Section 3.4.6 Property
assignment).</p></li>
<li><p>Added metadata keyname to attribute definitions (Section 3.4.7
Attribute definition).</p></li>
<li><p>Explained that parameter can be of two different kinds: outgoing
parameters and incoming parameters, and this depends on the context they
are defined in, and steers if these parameters will have a value
assigned or will have a mapping to an attribute assigned (Section 3.4.9
Parameter definition).</p></li>
<li><p>A value or mapping definition “fixes” the parameter, that is it
cannot be further refined (in a type) or even assigned in (in a
template) (Section 3.4.9 Parameter definition and 3.4.10 Parameter
assignment).</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD02, Rev02</td>
<td>2020-05-07</td>
<td></td>
<td><ul>
<li><p>Added derivation rules for the following TOSCA entity types:
artifact, group, and policy types) in their specific sections; the new
sub-sections are named “Derivation rules”.</p></li>
<li><p>Added refinement rules for Artifact definitions (contained in
node types undergoing derivations). The new sub-section is named
“Refinement rules”.</p></li>
<li><p>Added a single-line grammar for defining a value for a property
to simplify the value definition for a property (Section 3.4.5 Property
definition).</p></li>
<li><p>Added the constraints keyname to attribute definitions (Section
3.4.7 Attribute definition).</p></li>
<li><p>Added a single-line grammar for parameter definitions when only a
parameter to attribute mapping needs to be provided to an incoming
parameter (Section 3.4.9 Parameter definition).</p></li>
<li><p>Added explanation that triggers defined in the policy definition
are applied in addition to the triggers defined in the policy type
(Section 3.6.4 Policy definition).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD02, Rev03</td>
<td></td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Incorporate introductory content from the TOSCA v1.0 document
with the goal of removing references to the XML version of the standard
and making this a stand-alone document.</p></li>
<li><p>Explicitly stated that the default keyname SHALL NOT be defined
for properties and parameters that are not required (i.e. where the
keyname required is “false”) as they will stay undefined (Section 4.4.5
Property definition and Section 4.4.9 Parameter definition).</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD02, Rev04</td>
<td>2020-06-09</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Eliminated some comments that were addressed already.</p></li>
<li><p>Eliminated the namespace_uri that was already deprecated in TOSCA
v1.3</p></li>
<li><p>Eliminated the credential keyname from the repository definition
(Section 4.2.3.2 Repository definition) since it was not very useful in
the context and also to eliminate the dependency on an external type
simple (Credential – in the simple profile)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD02, Rev05</td>
<td>2020-06-18</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Eliminated the schedule keyname in trigger definitions, it was
not relevant and used a complex type from the simple profile (Section
4.6.5 Trigger definition).</p></li>
<li><p>Deleted the operation_host keyword from the operation
implementation definition since it was connected to a hostedOn
relationship type, and this is a type feature and not a grammar feature
(Section 4.3.6.8 Operation and notification implementation
definition).</p></li>
<li><p>Eliminated the HOST from the reserved function keywords since it
was connected to a hostedOn relationship type, and this is a type
feature and not a grammar feature (Section 5 TOSCA functions).</p></li>
<li><p>Eliminated some comments that were addressed already.</p></li>
<li><p>Changed the type of description to string in the keyname tables
throughout the specification.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD02, Rev06</td>
<td>2020-06-20</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Update the TOSCA overview diagram to include workflows and
policies (Section 3.1)</p></li>
<li><p>Update the diagram that explains requirements and capabilities
(Section 3.4)</p></li>
<li><p>Update the diagram that explains substitution (Section
3.5)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD02, Rev07</td>
<td>2020-06-22</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Edit the “TOSCA core concepts” section to reflect current status
of TOSCA (Section 3)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD02, Rev08</td>
<td>2020-06-24</td>
<td>Thinh Nguyenphu</td>
<td><ul>
<li><p>Provide additional detail about the required ZIP format and
standards in the CSAR definition (Section 6.1)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD03, Rev01</td>
<td>2020-07-22</td>
<td>Calin Curescu Chris Lauwers</td>
<td><ul>
<li><p>Remove numerous comments that have been resolved since they were
first introduced.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD03, Rev02</td>
<td>2020-07-26</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Mark keywords as “mandatory” rather than “required” (to avoid
confusion with the “required” keyword in property definitions</p></li>
<li><p>Introduce “conditional” as an alternative to “yes” or “no” in the
“mandatory” columns of the grammar definition.</p></li>
<li><p>Remove “Constraints” columns in grammar definitions.</p></li>
<li><p>Clarify that entry_schema is mandatory for collection
types.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD03, Rev03</td>
<td>2020-07-28</td>
<td>Tal Liron</td>
<td><ul>
<li><p>Introduce clear specification of TOSCA built-in types (Sections
4.4.1, 4.4.2, and 4.4.3)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD03, Rev04</td>
<td>2020-08-03</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Fix typos</p></li>
<li><p>Minor formatting fixes</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD03, Rev05</td>
<td>2020-08-18</td>
<td>Tal Liron Chris Lauwers</td>
<td><ul>
<li><p>Add description of timestamp type</p></li>
<li><p>Move scalar-unit types into the Special Types section
(4.4.2)</p></li>
<li><p>Remove multiples of “bytes per second” from scalar-unit.bitrate
to make all scalar units case insensitive</p></li>
<li><p>Remove references to the <strong>tosca</strong> namespace prefix
from the built-in type definitions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD03, Rev06</td>
<td>2020-08-31</td>
<td>Tal Liron Chris lauwers</td>
<td><ul>
<li><p>Introduce the notion of “profiles”</p></li>
<li><p>Support “import by profile name”</p></li>
<li><p>Simplify “namespaces”</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD03, Rev07</td>
<td>2020-09-06</td>
<td>Chris Lauwers Tal Liron</td>
<td><ul>
<li><p>Remove obsolete prose about namespace URIs (4.2)</p></li>
<li><p>Update the section about “import processing rules”
(4.2.3.1)</p></li>
<li><p>Introduce new prose about support for namespaces
(4.2.3.2)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD03, Rev08</td>
<td>2020-09-07</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Clarify discussion of custom keynames in CSAR (6.2.1)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD03, Rev09</td>
<td>2020-10-26</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Additional discussion of TOSCA Profiles (section 4.2.2)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD03, Rev10</td>
<td>2020-10-27</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Clarified throughout the specification that the key_schema
keyname for maps has the default value as “string”, and that the
entry_schema keyname definition is mandatory for lists and maps
(sections 4.4.5 Schema definition, 4.4.7 Property definition, 4.4.9
Attribute definition, 4.4.11 Parameter definition, 4.4.4. Data
type)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD04, Rev01</td>
<td>2020-11-19</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>New OASIS Logo</p></li>
<li><p>Correct broken cross reference (Section 4.3.5.8)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD04, Rev02</td>
<td>2021-01-25</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Incorporate comments provided as part of external review by Paul
Jordan (BT) and Mike Rehder (Amdocs)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD04, Rev03</td>
<td>2021-05-03</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Introduce new Chapter 4 that describes Operational
Model.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD04, Rev04</td>
<td>2021-06-28</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Slight reorganization of the Operation Model chapter (Chapter
4)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD04, Rev05</td>
<td>2022-02-15</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Modified the capability definition (Section 5.3.5.2 ) and
assignment (Section 5.3.5.3) removing the occurrences keyname We also
added the scope of relationships to the capability assignment (via
directives).</p></li>
<li><p>Modified the requirement definition (Section 5.3.5.5 ) and
assignment (Section 5.3.5.6) replacing the occurrences keyname with the
count_range keyname in the requirements definition, and how the
assignment must respect the definition and how an automated assignment
is assumed to exist if no assignment is specified. The keyname count
replaces the keyname occurrences in the assignment to remove any
confusion between their slightly different semantics. We also added the
scope of relationships to the requirement assignment (via directives).
Finally, we added the optional keyname for a requirement assignment to
designate if the assignment is optional or not.</p></li>
<li><p>We also added the possibility to specify capacity allocation in a
requirement assignment (Section 5.3.5.6) where the target capability
properties can act as capacity.</p></li>
<li><p>Made the relationship definition conditional, it must be present
either in the requirement definition (Section 5.3.5.5 ) or in the
requirement assignment (Section 5.3.5.5 ).</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD04, Rev06</td>
<td>2022-06-08</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Increased the expressivity of accessing properties and attributes
in the representation graph by improving the navigation expression in
the get_property and get_attribute functions. The representation graph
traversal is handled via a new definition (tosca path), that is common
to both and is described in section 6.4.2.2.1 The simplified TOSCA_PATH
definition in BNF format.</p></li>
<li><p>Added multi-step traversal of the representation graph</p></li>
<li><p>Added the backward traversal from capabilities to incoming
relationships</p></li>
<li><p>Added the target capability of a relationship as a possible
traversal</p></li>
<li><p>Added the specification of indexes and allowing traversal of
multi-count requirements</p></li>
<li><p>Examples for get_property have been corrected and
extended.</p></li>
<li><p>Removed the deprecated get_operation_output function</p></li>
<li><p>In relationship types (section 5.3.3) following keynames
changed/added:</p></li>
<li><p>valid_capability_types replaces valid_target_types</p></li>
<li><p>valid_target_node_types - new</p></li>
<li><p>valid_source_node_types - new</p></li>
<li><p>In capability type (section 5.3.5.1) and definition (section
5.3.5.2) following keynames changed/added:</p></li>
<li><p>valid_source_node_types - replaces valid_source_types</p></li>
<li><p>valid_relationship_types - new</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD05, Rev01</td>
<td>2022-06-14</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Fix formatting errors and typos.</p></li>
<li><p>Remove Section 6.1 about reserved function keywords (replaced
with TOSCA Path discussion)</p></li>
<li><p>Remove Section 6.2 about reserved environment variables.</p></li>
<li><p>Rename topology_template keyword to service_template</p></li>
<li><p>Remove reference to TOSCA v1.0 specification (Section
5.2.6.2.8)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD05, Rev02</td>
<td>2022-06-14</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Remove ‘get_nodes_of_type’ function (Section 6.4)</p></li>
<li><p>Remove section about ‘Context-based entity names’ (Section
6.6)</p></li>
<li><p>Remove sections about “Metadata keynames” (Section 5.2.1.1.1,
Section 5.2.1.3.4, Section 5.2.1.3.5, Section 5.2.1.3.6)</p></li>
<li><p>Document new metadata grammar (Section 5.2.1.3.3)</p></li>
<li><p>Document short notation for schema definitions (Section
5.4.5.2)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD05, Rev03</td>
<td>2022-09-28</td>
<td><p>Chris Lauwers</p>
<p>Calin Curescu</p></td>
<td><ul>
<li><p>Change default count range to [0, UNBOUNDED] (Section
5.3.5.5)</p></li>
<li><p>Clarify semantics of profile keynames in imported TOSCA files
(Section 5.2.2.2)</p></li>
<li><p>Add section about function syntax (Section 6.1)</p></li>
<li><p>Add section about defining user-defined custom functions (Section
6.6)</p></li>
<li><p>Update all intrinsic functions with the new dollar sign
syntax.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD05, Rev04</td>
<td>2022-11-21</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Remove Normative Values (Section 5.8). Removal of the Simple
Profile has made this section obsolete.</p></li>
<li><p>Add Condition functions (Section 6.5)</p></li>
<li><p>Update policy trigger syntax to use Boolean expressions.</p></li>
<li><p>Update workflow precondition syntax to use Boolean
expressions</p></li>
<li><p>Move sections about functions and function definitions into the
TOSCA Definitions chapter</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD05, Rev05</td>
<td>2022-11-21</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Introduce new syntax for defining validation clauses on data
types and property definitions.</p></li>
<li><p>Update node filter syntax to use Boolean expressions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD05, Rev06</td>
<td>2022-11-28</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Validation syntax examples.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD05, Rev07</td>
<td>2022-12-14</td>
<td>Calin Curescu</td>
<td><ul>
<li><p>Added the short string-value form for functions without arguments
and changed section Function syntax (Section 5.4.14)
accordingly.</p></li>
<li><p>Added all the existing comparison operators as Boolean functions,
the new Boolean logic functions and the new string, list and map
membership Boolean functions (Section 6.2) and set manipulation (section
6.4) and arithmetic functions (Section 6.5).</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD05, Rev08</td>
<td>2023-01-17</td>
<td><p>Chris Lauwers</p>
<p>Calin Curescu</p></td>
<td><ul>
<li><p>Cleanup for correctness and consistency.</p></li>
<li><p>Additional built-in functions (Section 6)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD05, Rev09</td>
<td>2023-01-18</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Document the ‘value’ function (Section 6.1.5)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>WD06, Rev01</td>
<td>2023-02-19</td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Fix document problems found when publishing CSD05.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>WD06, Rev02</td>
<td></td>
<td>Chris Lauwers</td>
<td><ul>
<li><p>Remove support for the “range” built-in type (Section
5.4.2)</p></li>
</ul></td>
</tr>
</tbody>
</table>
