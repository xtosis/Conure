import os
from sweep.sweep import sweep, load_json_data

SIM_NAME = ""

ARTWORKS = ""

SIM_CONFIG = ""
SWEEP = ""

OUTPUT_NAME = ""

GENERATE_LAYOUT = True
GENERATE_SVG = True
RUN_SIM = True
PACK = True

for artwork in os.listdir(ARTWORKS):
    output_dir = ""
    sweep(
        SIM_NAME,
        load_json_data(f'{ARTWORKS}/{artwork}'),
        load_json_data(SWEEP),
        load_json_data(SIM_CONFIG),
        output_dir,
        OUTPUT_NAME,
        GENERATE_LAYOUT,
        GENERATE_SVG,
        RUN_SIM,
        PACK,
        force=False,
        verbose=False,
        log_level=None
    )