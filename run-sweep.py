import os
from sweep.sweep import sweep, load_json_data
from configs.run_sweep import *

for artwork in os.listdir(ARTWORKS):
    sweep(
        SIM_NAME,
        load_json_data(f'{ARTWORKS}/{artwork}'),
        load_json_data(SWEEP),
        SIM_CONFIG,
        f"output/{artwork.replace(".json", "")}",
        None,
        GENERATE_LAYOUT,
        GENERATE_SVG,
        RUN_SIM,
        PACK,
        force=False,
        verbose=False,
        log_level=None
    )