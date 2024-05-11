import cv2
from class_definitions import MAPPING_C_TO_A, MAPPING_C_TO_B, PARTSEGMENTATION_CLASSES_C, PARTSEGMENTATION_CLASSES_B, PARTSEGMENTATION_CLASSES_A
from helper import convert_rgb_to_scalar, generate_color_to_id_mapping, print_class_histogram

if __name__ == '__main__':
    example_path = './dataset/0001/clone/00000.png'
    representation = PARTSEGMENTATION_CLASSES_C  # switch here between the representations

    class_to_class_mapping = None
    if representation == PARTSEGMENTATION_CLASSES_B:
        class_to_class_mapping = MAPPING_C_TO_B
    elif representation == PARTSEGMENTATION_CLASSES_A:
        class_to_class_mapping = MAPPING_C_TO_A

    color_id_mapping = generate_color_to_id_mapping(PARTSEGMENTATION_CLASSES_C, class_to_class_mapping)

    segmentation_bgr = cv2.imread(example_path)
    segmentation = convert_rgb_to_scalar(segmentation_bgr, color_id_mapping)

    print_class_histogram(segmentation, representation)
