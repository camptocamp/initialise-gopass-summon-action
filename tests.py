#!/usr/bin/env python3

import os
import subprocess

import yaml


def main():
    with open("action.yml", encoding="utf-8") as action_file:
        action = yaml.load(action_file, Loader=yaml.SafeLoader)
    subprocess.run(
        ["./install"],
        env={
            "PATH": os.environ["PATH"],
            "HOME": os.environ["HOME"],
            "GITHUB_ENV": os.environ["GITHUB_ENV"],
            "PATTERNS": os.environ["PATTERNS"],
            "CI_GPG_PRIVATE_KEY": os.environ["CI_GPG_PRIVATE_KEY"],
            "GITHUB_GOPASS_CI_TOKEN": os.environ["GOPASS_CI_GITHUB_TOKEN"],
            "GOPASS_VERSION": action["inputs"]["gopass_version"]["default"].lstrip("v"),
            "SUMMON_VERSION": action["inputs"]["summon_version"]["default"].lstrip("v"),
            "GPG_FINGERPRINT": action["inputs"]["gpg-fingerprint"]["default"],
            "GITHUB_REPOSITORY": action["inputs"]["github-repository"]["default"],
        },
    )


if __name__ == "__main__":
    main()
