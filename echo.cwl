#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
inputs:
  message:
    type: string
outputs:
  out:
    type: string
    outputBinding:
      glob: out.txt
      loadContents: true
      outputEval: $(self[0].contents)
baseCommand: [echo, -n]
arguments: [ $(inputs.message) ]
stdout: out.txt
hints:
  DockerRequirement:
    dockerPull: tessthyer/test-dockstore-tool-template:alpha
