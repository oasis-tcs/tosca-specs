#!/bin/bash


cat > ./examples/TOSCA.meta <<EOF
CSAR-Version: 2.0
Created-By: Ubicity Corp.
Entry-Definitions: s$1.yaml
EOF

ubicity catalog validate examples
