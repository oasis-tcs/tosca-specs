#!/bin/bash
set -e

HERE=$(dirname "$(readlink --canonicalize "$BASH_SOURCE")")

function pandoc () {
	docker run --rm --volume "$HERE:/data" --user $(id -u):$(id -g) pandoc/latex "$@"
}

pandoc TOSCA-v2.0-wd06-rev02-comments-only.docx -f docx -t gfm --track-changes=all --markdown-headings=setext > 2_0/TOSCA-v2.0-generated.md
