import skimage.draw as draw
import numpy as np
from working_space import WorkingSpace
from emiter import EmiterFrame
from sinogram import Sinogram
import filter

class Tomograph:
    scans = []
    angle_step = 1
    angle_count = 180

    def __init__(self, source_img, emiters_count):
        self.working_space = WorkingSpace(source_img)
        self.emiters_frame = EmiterFrame(self.working_space, emiters_count)

    def get_scans(self):
        return self.scans

    def get_sinogram(self):
        self.__scan()
        max = self.sinogram.max()
        self.sinogram = self.sinogram[:, :] * 1 / max
        return self.sinogram

    def get_reconstruct(self):
        self.__reconstruct()
        max = self.reconstruct.max()
        # img = self.reconstruct[:, :] * 1 / max
        x, y = self.working_space.source_x_y()
        h = self.working_space.source_h
        w = self.working_space.source_w
        tmp = self.reconstruct[y:y + h, x:x + w]
        min = np.mean(tmp)
        tmp = tmp - min
        tmp = tmp.clip(0)
        max = tmp.max()
        tmp = tmp * 1/max
        # tmp = tmp/np.linalg.norm(tmp)
        return tmp

    def __scan(self):
        sinogram = Sinogram(self.angle_count, self.emiters_frame.emitersCount)
        img = self.working_space.working_space
        for angle in range(0, self.angle_count, self.angle_step):
            print("scan angle: ", angle)
            emiters = self.emiters_frame.with_angle(angle)
            for emiter_no, emiter in enumerate(emiters):
                xx, yy = draw.line(emiter.s_x, emiter.s_y, emiter.e_x, emiter.e_y)
                test = img[yy, xx]
                sinogram.radon_value(angle, emiter_no, test)
                # self.scans.append(img)
        self.sinogram = sinogram.img

    def __reconstruct(self):
        filtered_sinogram = filter.filter_sinogram(self.sinogram)
        reconstruct = np.zeros(self.working_space.working_space.shape)
        count = np.ones(self.working_space.working_space.shape)
        for angle in range(0, self.angle_count, self.angle_step):
            print("reconstruct angle: ", angle)
            emiters = self.emiters_frame.with_angle(angle)
            for i, e in enumerate(emiters):
                xx, yy = draw.line(e.s_x, e.s_y, e.e_x, e.e_y)
                sinogram_value = filtered_sinogram[i, angle]
                if i == 0:
                    reconstruct[yy, xx] = sinogram_value
                else:
                    reconstruct[yy, xx] = reconstruct[yy, xx] + sinogram_value
                    count[yy, xx] += 1
        t = reconstruct[:, :] / count[:, :]
        self.reconstruct = t


