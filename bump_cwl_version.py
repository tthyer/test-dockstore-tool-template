#! /usr/bin/env python3

import argparse
import yaml

def read_tool(path):
  with open(path) as file:
    tool = yaml.load(file, Loader=yaml.FullLoader)
  return tool


def edit_tool(tool, new_version):
  # this is dependent on cwl syntax -- you'll need to change this
  # if you use the list style for hints, or put your DockerRequirement
  # under 'requirements' instead of 'hints'
  docker_image = tool['hints']['DockerRequirement']['dockerPull']
  parts = docker_image.split(':')
  parts[-1] = new_version
  tool['hints']['DockerRequirement']['dockerPull'] = ':'.join(parts)
  return yaml.dump(tool)


def write_tool(path, output):
  with open(path, mode='w') as file:
    file.write(output)
    file.close()


def parse_args():
  parser = argparse.ArgumentParser(
    description='Change docker image version in cwl tool')
  parser.add_argument(
    'tool_path',
    help='CWL tool file path')
  parser.add_argument(
    'new_version',
    help='New docker version to set in cwl tool')
  args = parser.parse_args()
  return args.tool_path, args.new_version


tool_path, new_version = parse_args()
tool = read_tool(path=tool_path)
output = edit_tool(tool=tool, new_version=new_version)
write_tool(path=tool_path, output=output)