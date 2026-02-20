import os
from sweep.sweep import sweep, load_json_data

SIM_NAME = "emx" # fixed cannot chnage

ARTWORKS = "/mnt/storage/batch-sweep/artworks"

SIM_CONFIG = "/mnt/storage/batch-sweep/sim-config.json"
SWEEP = "/mnt/storage/batch-sweep/sweep-config.json"

GENERATE_LAYOUT = True
GENERATE_SVG = True
RUN_SIM = False
PACK = True

for artwork in os.listdir(ARTWORKS):
    output_dir = ""
    sweep(
        SIM_NAME,
        load_json_data(f'{ARTWORKS}/{artwork}'),
        load_json_data(SWEEP),
        load_json_data(SIM_CONFIG),
        "output",
        GENERATE_LAYOUT,
        GENERATE_SVG,
        RUN_SIM,
        PACK,
        force=False,
        verbose=False,
        log_level=None
    )