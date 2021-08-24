from ImageReader import ImageReader
from ImageCropper import ImageCropper
from WindowCapture import WindowCapture
import cv2 as cv
import time


class AlgorithmRunner:

    @staticmethod
    def run():
        debug = False
        window_capture = WindowCapture('Journeys in Middle-Earth')

        time_spend = ''
        text_read = False

        while True:
            loop_time = time.time()
            screenshot = window_capture.get_screenshot()

            image_cropper = ImageCropper()
            found_img, max_loc = image_cropper.find_image(screenshot)

            if debug:
                cv.imshow('Journeys in Middle-Earth better', screenshot)

            if found_img is False:
                text_read = False

            if found_img and text_read is False:
                # wait until the whole border appears
                time.sleep(0.2)
                screenshot = window_capture.get_screenshot()

                screenshot, crop_img = image_cropper.crop_image(screenshot, max_loc)

                if debug:
                    crop_time = time.time()
                    print('crop_time {}'.format(crop_time - loop_time))
                    cv.imwrite('result.jpg', crop_img)

                image_reader = ImageReader(crop_img)
                text = image_reader.read_from_img()

                if debug:
                    read_time = time.time()
                    print('read_time {}'.format(read_time - crop_time))

                if len(text) < 5:
                    continue
                image_reader.read_sentence_by_sentence()

                if debug:
                    voice_time = time.time()
                    print('voice_time {}'.format(voice_time - read_time))
                    time_spend = 'Time {}'.format(time.time() - loop_time)
                text_read = True

            if debug:
                fps = 'FPS {}'.format(round(1 / (time.time() - loop_time), 2))
                loop_time = time.time()
                cv.putText(screenshot, fps, (1100, 590), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv.putText(screenshot, time_spend, (1050, 550), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv.imshow('Journeys in Middle-Earth better', screenshot)

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
