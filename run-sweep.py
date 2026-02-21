import os
from sweep.sweep import sweep, load_json_data

# --- Main Input ------------
JOB_NAME = "01-sweep"
# ---------------------------

SIM_NAME = "emx" # fixed cannot change
GENERATE_LAYOUT = True
GENERATE_SVG = True
RUN_SIM = True
PACK = True

_JOB_PATH = "/mnt/storage/shared/jobs/" + JOB_NAME
_CONFIGS = _JOB_PATH + "/configs/"
_ARTWORKS = _CONFIGS + "artworks"

for artwork in os.listdir(_ARTWORKS):
    sweep(
        SIM_NAME,
        load_json_data(f'{_ARTWORKS}/{artwork}'),
        load_json_data(_CONFIGS + "sweep.json"),
        _CONFIGS + "sim.json",
        f"{_JOB_PATH}/output/{artwork.replace(".json", "")}",
        None,
        GENERATE_LAYOUT,
        GENERATE_SVG,
        RUN_SIM,
        PACK,
        force=False,
        verbose=False,
        log_level=None
    )