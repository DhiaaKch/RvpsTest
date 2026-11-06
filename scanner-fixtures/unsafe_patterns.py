"""Static-only examples for scanner validation; do not call these functions."""

import subprocess

import yaml


def dynamic_eval_fixture(expression: str) -> object:
    return eval(expression)


def dynamic_exec_fixture(source: str) -> None:
    exec(source)


def shell_subprocess_fixture(command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, shell=True, check=False, text=True)


def yaml_load_fixture(document: str) -> object:
    return yaml.load(document)
