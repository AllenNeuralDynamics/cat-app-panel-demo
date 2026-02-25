# cat-app-panel-demo

A skeleton capsule with an example of a `pydantic-settings` class for parsing arguments from multiple sources.

## Create an app panel from the arg parser
- enter a terminal cloud workstation and run the following:
```
pip install auto-app-panel && auto-app-panel code/run_capsule.pydantic
```
- an `app-panel.json` will be created in the `.codeocean` folder
- exit the cloud workstation and check the `App Builder` tab

## Notes 
- app panels can also be created automatically from `argparse.ArgumnetParser` classes, **provided that they are defined at the top level of a .py file** (i.e. not inside a function)