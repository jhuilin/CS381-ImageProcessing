from scipy import misc
from histogram_matching import ExactHistogramMatcher


def histogram_matching():
    target_img = misc.imread('target.jpg')
    reference_img = misc.imread('reference.jpg')

    reference_histogram = ExactHistogramMatcher.get_histogram(reference_img)
    new_target_img = ExactHistogramMatcher.match_image_to_histogram(target_img, reference_histogram)
    misc.imsave('result.jpg', new_target_img)

def main():
    histogram_matching()

if __name__ == "__main__":
    main()
