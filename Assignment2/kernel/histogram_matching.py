import numpy as np
from scipy import signal
import cv2

class ExactHistogramMatcher:
    _kernel1 = np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])
    _kernel2 = 1.0 / 5.0 * np.array([[0, 1, 0],
                                     [1, 1, 1],
                                     [0, 1, 0]])

    _kernel3 = 1.0 / 9.0 * np.array([[1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1]])

    _kernel_mapping = {1: [_kernel1],
                       2: [_kernel1, _kernel2],
                       3: [_kernel1, _kernel2, _kernel3]}

    def get_histogram(image):
        max_grey_value = 256
        dimensions = image.shape[2]
        hist = np.empty((max_grey_value, dimensions))

        for dimension in range(0, dimensions):
            for gray_value in range(0, max_grey_value):
                image_2d = image[:, :, dimension]
                hist[gray_value, dimension] = np.sum(image_2d == gray_value)
        return hist

    def _get_averaged_images(img, kernels):
        return np.array([signal.convolve2d(img, kernel, 'same') for kernel in kernels])

    def _get_average_values_for_every_pixel(img, number_kernels):
        kernels = ExactHistogramMatcher._kernel_mapping[number_kernels]
        averaged_images = ExactHistogramMatcher._get_averaged_images(img, kernels)
        img_size = averaged_images[0].shape[0] * averaged_images[0].shape[1]
        reshaped_averaged_images = averaged_images.reshape((number_kernels, img_size))
        transposed_averaged_images = reshaped_averaged_images.transpose()
        return transposed_averaged_images

    def sort_rows_lexicographically(matrix):

        rotated_matrix = np.rot90(matrix)
        sorted_indices = np.lexsort(rotated_matrix)
        return matrix[sorted_indices]

    def _match_to_histogram(image, reference_histogram, number_kernels):
        img_size = image.shape[0] * image.shape[1]

        merged_images = np.empty((img_size, number_kernels + 2))
        merged_images[:, 0] = image.reshape((img_size,))

        # they haven been sorted lexicographically according their values.
        indices_of_flattened_image = np.arange(img_size).transpose()
        merged_images[:, -1] = indices_of_flattened_image

        # Calculate average images and merged images
        averaged_images = ExactHistogramMatcher._get_average_values_for_every_pixel(image, number_kernels)
        for dimension in range(0, number_kernels):
            merged_images[:, dimension + 1] = averaged_images[:, dimension]

        # Sort the array according the original pixels values and then after
        sorted_merged_images = ExactHistogramMatcher.sort_rows_lexicographically(merged_images)

        # Assign gray values according the distribution of the reference histogram
        index_start = 0
        for gray_value in range(0, len(reference_histogram)):
            index_end = int(index_start + reference_histogram[gray_value])
            sorted_merged_images[index_start:index_end, 0] = gray_value
            index_start = index_end

        # Sort back ordered by the flattened image index. The last column represents the index
        sorted_merged_images = sorted_merged_images[sorted_merged_images[:, -1].argsort()]
        new_target_img = sorted_merged_images[:, 0].reshape(image.shape)

        return new_target_img

    def match_image_to_histogram(image, reference_histogram, number_kernels=3):
        if len(image.shape) == 3:
            output = np.empty(image.shape)
            dimensions = image.shape[2]

            for dimension in range(0, dimensions):
                output[:, :, dimension] = ExactHistogramMatcher._match_to_histogram(image[:, :, dimension],
                                                                                    reference_histogram[:, dimension],
                                                                                    number_kernels)
        return output
