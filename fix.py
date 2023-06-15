#!/usr/bin/env python3

import pathlib, re, io, json

here = pathlib.Path(__file__).parents[0]

source_path = here / "2_0" / "TOSCA-v2.0-generated.md"
target_path = here / "2_0" / "TOSCA-v2.0-processed.md"

comment_re = re.compile(r"<span\s+class=\"comment-start\"\s+id=\"(?P<id>.*?)\"\s+author=\"(?P<author>.*?)\"\s+date=\"(?P<date>.*?)\">(?P<comment>.*?)</span>(?P<target>.*?)<span\s+class=\"comment-end\"\s+id=\".*?\">\s*</span>", re.DOTALL)
snippet_re = re.compile(r"<table>\n<colgroup>\n<col style=\"width: 100%\" />\n</colgroup>\n<thead>\n<tr class=\"header\">\n<th>(?P<snippet>.*?)</th>\n</tr>\n</thead>\n<tbody>\n</tbody>\n</table>", re.DOTALL)
reference_re = re.compile(r"<a\s+href=\"(?P<ref>.*?)\">(?P<target>.*?)</a>", re.DOTALL)


def format_comment(m):
  s = io.StringIO()
  s.write("\n<!----\n")
  json.dump(m.groupdict(), s)
  s.write("-->\n")
  return s.getvalue()


def format_comment_replacement(m):
  return m.group("target") + format_comment(m)


def main():
  with open(source_path) as f:
    source = f.read()

  count = 0
  m = comment_re.search(source)
  while m is not None:
    count += 1
    replacement = format_comment_replacement(m)
    start = m.start()
    end = m.end()
    source = source[0:start] + replacement + source[end:]
    end = start + len(replacement)
    m = comment_re.search(source, end+1)

  with open(target_path, "w") as f:
    f.write(source)

  print(f"comments: {count}")

  # count = 0
  # m = snippet_re.search(source)
  # while m is not None:
  #   count += 1
  #   #print(m.group("snippet"))
  #   m = snippet_re.search(source, m.end()+1)

  # print(f"code snippets: {count}")

  count = 0
  m = reference_re.search(source)
  while m is not None:
    count += 1
    print(m.group("ref"))
    m = reference_re.search(source, m.end()+1)

  print(f"references: {count}")


if __name__=="__main__":
    main()
