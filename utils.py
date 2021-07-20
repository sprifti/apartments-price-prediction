from model_utils import Choices

ZONES = Choices(
    (1, "unaza_e_re", "Unaza e Re"),
    (2, "fresku", "Fresku")
)

SCALER = Choices(
    (1, "unaza_e_re_scaler.sav"),
    (2, "fresku_scaler.sav")
)

MODEL = Choices(
    (1, "unaza_e_re.sav"),
    (2, "fresku.sav")
)
