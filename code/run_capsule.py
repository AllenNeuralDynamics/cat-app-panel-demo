from __future__ import annotations # for use of "|" in Python 3.9. eval-type-backport also required for use with pydantic

import os
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, CliSettingsSource
from pydantic_settings.sources import JsonConfigSettingsSource

class Params(BaseSettings):
    skip_existing: bool = Field(default=True, exclude=True)
    test: bool = Field(default=False, exclude=True)
    logging_level: str | int = Field(default='INFO', exclude=True)
    use_process_pool: bool = Field(default=True, exclude=True)
    max_workers: int | None = Field(default=int(os.environ['CO_CPUS']), exclude=True)
    # `exclude=True` excludes a parameter from the json when dumping the settings to json
    # (typically used for parameters that affect *how* a capsule runs rather than *what* the capsule actually does)

    baseline_subtraction: bool = False
    min_n_units: int = 20
    label_to_decode: str = 'rewarded_modality'
    sliding_window_size: float | None = None
    # constrain the acceptable values of a string to a set of options:
    input_data_type: Literal['spikes', 'facemap', 'LP'] = 'spikes'

    # this settings class can parse inputs from multiple sources, including
    # command line arguments (which is how app-panel parameters are passed to python in code ocean)
    # as well as .env and .json files 
    # - we can control which sources are used, and assign a priority to each by customizing the following:
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        *args,
        **kwargs,
    ):
        # see https://docs.pydantic.dev/latest/concepts/pydantic_settings/#changing-priority
        #
        # the order of the variables below is what defines the priority:
        # - first source is highest priority
        # - for each field in the class, the first source that contains a value will be used
        # - if no sources contain a value for a field, the default is used
        return (
            init_settings,
            JsonConfigSettingsSource(settings_cls, json_file='parameters.json'),
            CliSettingsSource(settings_cls, cli_parse_args=True),
        )
        

def main():
    params = Params()
    print(params)
    print(repr(params))
    print(params.model_dump_json(indent=4))
    
    # use properties as needed:
    print(f"Launching capsule with {params.min_n_units=}")

if __name__ == "__main__": 
    main()