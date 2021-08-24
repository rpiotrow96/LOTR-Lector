import cv2 as cv


class FindSpecialSign:
    sign = None
    sign_replacer = None
    screenshot = None
    threshold = 0.8

    def __init__(self, sign, sign_replacer, screenshot):
        sign = sign[..., :3]
        self.sign = sign
        sign_replacer = sign_replacer[..., :3]
        self.sign_replacer = sign_replacer
        self.screenshot = screenshot

    def find_and_replace(self):
        res = cv.matchTemplate(self.screenshot, self.sign, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val < self.threshold:
            return

        x_offset = max_loc[0]
        y_offset = max_loc[1]
        self.screenshot[y_offset:y_offset + self.sign_replacer.shape[0],
        x_offset:x_offset + self.sign_replacer.shape[1]] = self.sign_replacer

        return self.screenshot

    @staticmethod
    def find_and_replace_all_signs(cropped_img):
        find_special_sign = FindSpecialSign(cv.imread('icon/fate.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/fate_replace.png', cv.IMREAD_UNCHANGED),
                                            cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/success.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/success_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/damage.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/damage_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/fear.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/fear_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/wit.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/wit_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/agility.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/agility_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/wisdom.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/wisdom_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/spirit.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/spirit_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/might.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/might_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/trinket.png', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/trinket_replace.png', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()

        find_special_sign = FindSpecialSign(cv.imread('icon/dist.PNG', cv.IMREAD_UNCHANGED),
                                            cv.imread('icon/dist_replace.PNG', cv.IMREAD_UNCHANGED), cropped_img)
        find_special_sign.find_and_replace()
