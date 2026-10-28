# Little Signals: Python + uv starter

A small interactive Python app for SD5913 teams. It opens a window; click to
place a signal, and press Escape or close the window to quit. Use **Use this
template → Create a new repository** on GitHub to make your team's copy, then
change the interaction into an app, game or creative tool of your own.

## Run the source

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run
these commands from the repository root:

```bash
uv run --locked python main.py
uv run --locked python -m unittest discover -s tests
```

The first command installs Python 3.13 and the locked dependencies if necessary,
then starts the app. You need a graphical desktop for the window. The tests
check small interaction functions without a window. To check that one frame
can be drawn on a headless runner:

```bash
uv run --locked python main.py --smoke-test
```

`pyproject.toml` declares dependencies, `.python-version` selects Python, and
`uv.lock` records versions for teammates and CI. To add a dependency, use
`uv add PACKAGE`, run the tests and commit both the project file and lockfile.
For a first team task, change the signal colour or counter, run the app and
ask someone else to review your pull request.

## Codex cloud environment

In Codex, choose **Work in → Cloud → Select environment → Create environment**,
connect GitHub and select your team's repository. Ask Codex to install uv if it
is missing and run `.codex/setup.sh`; review setup and test results, save and
**Publish**. Start a task asking for one small change and its checks, then review
the diff and test the interaction. A headless smoke test does not replace
trying the visible window. See [Codex cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments).

## Build a downloadable app

`uv` manages Python and dependencies; it does not by itself create a standalone
application. This starter uses [PyInstaller](https://pyinstaller.org/en/stable/)
to bundle the app and its dependencies. A bundle is built separately on each
operating system. The GitHub Actions matrix builds and smoke-tests:

| Build | Download | Run after extracting |
| --- | --- | --- |
| Linux x64, built on Ubuntu 26.04 | `little-signals-linux-x64.tar.gz` | `LittleSignals/LittleSignals` |
| Windows x64 | `little-signals-windows-x64.zip` | `LittleSignals/LittleSignals.exe` |
| macOS Apple Silicon | `little-signals-macos-arm64.tar.gz` | Run `LittleSignals/LittleSignals` from Terminal |

Keep the **whole extracted folder** together: PyInstaller's executable uses
its bundled supporting files. A user does not need Python or uv to run it.
These are unsigned test builds, not app-store packages; operating systems can
warn about untrusted downloads. The Linux build may require a sufficiently
recent compatible Linux distribution. An Intel Mac, Android, iOS or browser
build needs a different build target or toolchain; it is not included here.

To build on your own computer for that same operating system:

```bash
uv sync --locked --group build
uv run --locked --group build python -m PyInstaller --noconfirm --clean --onedir --name LittleSignals main.py
```

The resulting folder is `dist/LittleSignals/`. If you add images, fonts, model
files or other assets, configure PyInstaller to include them and test the
bundled app on the target platform. A passing build is not a usability test.

## Publish a versioned release

For ordinary pushes and pull requests, Actions runs checks and uploads platform
bundles as workflow artifacts. Run **Check and build Python app** manually to
also get a `release-preview` artifact without publishing a release.

When the team is ready to publish, push a version tag from an up-to-date main:

```bash
git switch main
git pull origin main
git tag v1.0.0
git push origin v1.0.0
```

Use `vMAJOR.MINOR.PATCH`. Once all three builds pass, Actions creates a GitHub
Release and attaches the three platform archives. Keep Actions enabled and allow
its `GITHUB_TOKEN` contents-write permission. A tag in a public repository
creates a public release; do not push one until you are ready to share it.

## Work together

Make a feature branch, make a focused change, commit and push it, then open a
pull request. Explain how a teammate can run and test it. The README should
continue to describe what your own project does, its dependencies, how to run
it and any limitations. Credit assets and tools. Keep passwords and API tokens
out of source code, commits, prompts, logs and packaged applications.
