arguments:
- $(inputs.message)
baseCommand:
- echo
- -n
class: CommandLineTool
cwlVersion: v1.0
hints:
  DockerRequirement:
    dockerPull: tessthyer/test-dockstore-tool-template:1.0.4
inputs:
  message:
    type: string
outputs:
  out:
    outputBinding:
      glob: out.txt
      loadContents: true
      outputEval: $(self[0].contents)
    type: string
stdout: out.txt
