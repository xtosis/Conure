from sweep.sweep import sweep, load_json_data

SIM_NAME = ""
SIM_CONFIG = ""

ARTWORK = ""
SWEEP = ""

OUTPUT_DIR = ""
OUTPUT_NAME = ""

GENERATE_LAYOUT = True
GENERATE_SVG = True
RUN_SIM = True
PACK = True

sweep(
    SIM_NAME,
    load_json_data(ARTWORK),
    load_json_data(SWEEP),
    SIM_CONFIG,
    OUTPUT_DIR,
    OUTPUT_NAME,
    GENERATE_LAYOUT,
    GENERATE_SVG,
    RUN_SIM,
    PACK,
    force=False,
    verbose=False,
    log_level=None
)