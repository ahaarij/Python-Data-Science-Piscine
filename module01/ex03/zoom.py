import matplotlib.pyplot as plt
from load_image import ft_load


def display_img_with_axis(img_array, cmap):
    plt.imshow(img_array, cmap=cmap)
    plt.show()


def zoom(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    zoomed_img = img_array[x_start:x_end, y_start:y_end, 0:1]
    return zoomed_img


def main():
    try:
        original_img = ft_load("animal.jpeg")
        print("The shape of the image is:", original_img.shape)
        print(original_img)

        zoom_img = zoom(original_img)
        print("New shape after slicing:", zoom_img.shape, "or", zoom_img.shape[:2])
        print(zoom_img)

        display_img_with_axis(zoom_img, cmap="gray")

    except AssertionError as e:
        print("Assertion Error:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

