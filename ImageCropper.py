import cv2 as cv
from FindSpecialSign import FindSpecialSign


class ImageCropper:
    border = None
    threshold = 0.9
    debug = False

    def __init__(self):
        self.border = cv.imread('border.PNG', cv.IMREAD_UNCHANGED)

    def find_image(self, haystack_img):
        result_bottom = cv.matchTemplate(haystack_img, self.border, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result_bottom)
        if max_val > self.threshold:
            return True, max_loc
        return False, None

    def crop_image(self, haystack_img, max_loc):
        needle_w = self.border.shape[1]
        needle_h = self.border.shape[0]

        # top left always at 0,0
        top_left = (0, 0)
        bottom_right = (max_loc[0] + needle_w, max_loc[1] + needle_h)

        cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        margin = 20

        x = top_left[0] + margin
        y = top_left[1] + margin
        h = bottom_right[1] - (top_left[1] + 2 * margin)
        w = bottom_right[0] - (top_left[0] + 2 * margin)

        cropped_img = haystack_img[y:y + h, x:x + w]

        if cropped_img.size == 0:
            cropped_img = None
            return haystack_img, cropped_img

        FindSpecialSign.find_and_replace_all_signs(cropped_img)

        return haystack_img, cropped_img
