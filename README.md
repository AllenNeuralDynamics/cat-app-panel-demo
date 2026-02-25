# cat-app-panel-demo

A skeleton capsule with an example of a `pydantic-settings` class for parsing arguments from multiple sources.

## Create an app panel from the arg parser
- enter a terminal cloud workstation and run the following:
    ```
    pip install auto-app-panel && auto-app-panel code/run_capsule.pydantic
    ```
- an `app-panel.json` will be created in the `.codeocean/` folder
- exit the cloud workstation and check the `App Builder` tab

## Notes 
- app panels can also be created automatically from `argparse.ArgumnetParser` classes, **provided that they are defined at the top level of a .py file** (i.e. not inside a function)
- if an `app-panel.json` already exists, only new fields will be added to it: the alternative is to write a completely new file with `--strategy overwrite`
- any time an existing `app-panel.json` is modified, a timestamped backup of the existing version is created in `.codeocean/` (which should not interfere with the behavior of the capsule)
- source code: [https://github.com/AllenNeuralDynamics/auto-app-panel](https://github.com/AllenNeuralDynamics/auto-app-panel)

```
 Usage: auto-app-panel [OPTIONS] SOURCE [OUTPUT]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    source      PATH      Path to Python file containing argument parsing class [required]                                                                                          │
│      output      [OUTPUT]  Path where App Panel JSON will be written [default: /root/capsule/.codeocean/app-panel.json]                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --strategy                                [overwrite|preserve]  Strategy for merging with existing app-panel.json: 'overwrite' updates fields, 'preserve' keeps existing values      │
│                                                                 [default: preserve]                                                                                                  │
│ --no-backup             --no-no-backup                          Skip creating backup of existing app-panel.json [default: no-no-backup]                                              │
│ --install-completion                                            Install completion for the current shell.                                                                            │
│ --show-completion                                               Show completion for the current shell, to copy it or customize the installation.                                     │
│ --help                                                          Show this message and exit.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```