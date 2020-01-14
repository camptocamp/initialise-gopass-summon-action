const core = require('@actions/core');
const { spawn } = require('child_process');

try {
  const process = spawn('./install', [], {
    'stdio': ['inherit', 'inherit', 'inherit'],
    'env': {
      LARGE_SECRET_PASSPHRASE: core.getInput('large-secret-passphrase'),
      GITHUB_GOPASS_CI_TOKEN: core.getInput('github-gopass-ci-token'),
      GOPASS_VERSION: core.getInput('gopass_version'),
      SUMMON_VERSION: core.getInput('summon_version'),
      GPG_FINGERPRINT: core.getInput('gpg-fingerprint'),
      GITHUB_REPOSITORY: core.getInput('github-repository')
    }
  });
  process.on('error', (error => {
    console.log('error');
    console.log(error);
    core.setFailed();
  }));
  process.on('exit', (code => {
    if (code != 0) {
      console.log(`exit: code`);
      core.setFailed();
    }
  }));
  process.on('close', (code => {
    if (code != 0) {
      console.log(`close: code`);
      core.setFailed();
    }
  }));
} catch (error) {
  console.log('catch');
  core.setFailed(error.message);
}
