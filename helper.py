from typing import Dict
import numpy as np

from class_definitions import CLASS_COLOR_MAPPING


def convert_rgb_to_scalar(segmentation_bgr: np.ndarray, color_id_mapping: Dict) -> np.ndarray:
    segmentation_scalar = np.zeros((segmentation_bgr.shape[:-1] + (1,)), dtype=np.uint8)

    for color, id in color_id_mapping.items():
        copymask = np.expand_dims(np.all(np.equal(np.flip(color, axis=-1), segmentation_bgr), axis=-1), axis=-1)
        segmentation_scalar[copymask] = id

    return segmentation_scalar


def generate_color_to_id_mapping(id_class_mapping: Dict, class_to_class_mapping: Dict = None, colors: Dict=CLASS_COLOR_MAPPING) -> Dict:
    color_id_mapping = {}
    for class_id, class_name in id_class_mapping.items():
        assert class_name in colors.keys(), f"Class {class_name} not found in class-to-color mapping."
        if class_to_class_mapping is not None:
            class_id = class_to_class_mapping[class_id]
        color_id_mapping[colors[class_name]] = class_id
    return color_id_mapping


def print_class_histogram(segmentation: np.ndarray, class_decoding: Dict) -> None:
    print("== Class histogram == ")
    for class_id, class_name in class_decoding.items():
        print(f"{class_name}: {np.sum(segmentation == class_id)}")