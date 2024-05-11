# There are three partsegmentation representations: C (29 classes), B (9 classes), A (4 classes)
# The paper from 2018 refers to them as full (C), fine (B) and coarse (A).


# Other Acrynoms:
# F: Front, R: Rear, FL: Front Left, FR: Front Right, RL: Rear Left, RR: Rear Right, CL: C-Pillar-Left, CR: C-Pillar-Righ

PARTSEGMENTATION_CLASSES_C = {
    0: "unlabeled",
    1: "lights_FL",
    2: "lights_FR",
    3: "lights_RL",
    4: "lights_RR",
    5: "wheels_FL",
    6: "wheels_FR",
    7: "wheels_RL",
    8: "wheels_RR",
    9: "apron_F",
    10: "apron_R",
    11: "doors_FL",
    12: "doors_FR",
    13: "doors_RL",
    14: "doors_RR",
    15: "side_L",
    16: "side_R",
    17: "windshield_F",
    18: "windshield_R",
    19: "glass_FL",
    20: "glass_FR",
    21: "glass_RL",
    22: "glass_RR",
    23: "glass_CL",
    24: "glass_CR",
    25: "roof",
    26: "trunk",
    27: "hood",
    28: "mirror_L",
    29: "mirror_R"
}

PARTSEGMENTATION_CLASSES_B = {
    0: "unlabeled",
    1: "lights",
    2: "wheels",
    3: "apron",
    4: "doors",
    5: "side",
    6: "windshield",
    7: "roof",
    8: "trunk",
    9: "hood",

}

PARTSEGMENTATION_CLASSES_A = {
    0: "unlabeled",
    1: "lights",
    2: "wheels",
    3: "body",
    4: "glass"
}

MAPPING_C_TO_A = {
    0: 0,  # "unlabeled"
    1: 1,  # "lights_FL",
    2: 1,  # "lights_FR",
    3: 1,  # "lights_RL",
    4: 1,  # "lights_RR",
    5: 2,  # "wheels_FL",
    6: 2,  # "wheels_FR",
    7: 2,  # "wheels_RL",
    8: 2,  # "wheels_RR",
    9: 3,  # "apron_F",
    10: 3,  # "apron_R",
    11: 3,  # "doors_FL",
    12: 3,  # "doors_FR",
    13: 3,  # "doors_RL",
    14: 3,  # "doors_RR",
    15: 3,  # "side_L",
    16: 3,  # "side_R",
    17: 4,  # "windshield_F",
    18: 4,  # "windshield_R",
    19: 4,  # "glass_FL",
    20: 4,  # "glass_FR",
    21: 4,  # "glass_RL",
    22: 4,  # "glass_RR",
    23: 4,  # "glass_CL",
    24: 4,  # "glass_CR",
    25: 3,  # "roof",
    26: 3,  # "trunk",
    27: 3,  # "hood",
    28: 3,  # "mirror_L",
    29: 3,  # "mirror_R"
}

MAPPING_C_TO_B = {
    0: 0,  # "unlabeled",
    1: 1,  # "lights_FL",
    2: 1,  # "lights_FR",
    3: 1,  # "lights_RL",
    4: 1,  # "lights_RR",
    5: 2,  # "wheels_FL",
    6: 2,  # "wheels_FR",
    7: 2,  # "wheels_RL",
    8: 2,  # "wheels_RR",
    9: 3,  # "apron_F",
    10: 3,  # "apron_R",
    11: 4,  # "doors_FL",
    12: 4,  # "doors_FR",
    13: 4,  # "doors_RL",
    14: 4,  # "doors_RR",
    15: 5,  # "side_L",
    16: 5,  # "side_R",
    17: 6,  # "windshield_F",
    18: 6,  # "windshield_R",
    19: 4,  # "glass_FL",
    20: 4,  # "glass_FR",
    21: 4,  # "glass_RL",
    22: 4,  # "glass_RR",
    23: 4,  # "glass_CL",
    24: 4,  # "glass_CR",
    25: 7,  # "roof",
    26: 8,  # "trunk",
    27: 9,  # "hood",
    28: 5,  # "mirror_L",
    29: 5,  # "mirror_R"
}

CLASS_COLOR_MAPPING = {
    "unlabeled": (0, 0, 0),
    "lights": (255, 160, 122),
    "wheels": (10, 10, 10),
    "body": (255, 10, 10),
    "glass": (0, 0, 238),
    "apron": (255, 10, 10),
    "doors": (255, 110, 180),
    "side": (210, 105, 30),
    "windshield": (139, 35, 35),
    "roof": (0, 139, 0),
    "trunk": (0, 238, 0),
    "hood": (0, 100, 0),
    "lights_FL": (255, 160, 122),
    "lights_FR": (255, 127, 0),
    "lights_RL": (255, 236, 139),
    "lights_RR": (255, 215, 0),
    "wheels_FL": (120, 120, 120),
    "wheels_FR": (10, 10, 10),
    "wheels_RL": (248, 248, 255),
    "wheels_RR": (205, 201, 201),
    "apron_F": (255, 0, 0),
    "apron_R": (208, 32, 144),
    "doors_FL": (255, 110, 180),
    "doors_FR": (255, 20, 147),
    "doors_RL": (224, 102, 255),
    "doors_RR": (153, 50, 204),
    "side_L": (210, 105, 0),
    "side_R": (139, 69, 19),
    "windshield_F": (0, 0, 238),
    "windshield_R": (139, 35, 35),
    "glass_FL": (135, 206, 250),
    "glass_FR": (28, 134, 238),
    "glass_RL": (39, 64, 139),
    "glass_RR": (0, 0, 139),
    "glass_CL": (0, 205, 205),
    "glass_CR": (0, 139, 139),
    "mirror": (200, 83, 86),
    "mirror_L": (200, 83, 86),
    "mirror_R": (157, 0, 4)
}