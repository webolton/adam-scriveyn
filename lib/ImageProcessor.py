# Divide MS images into single pages; name images
import imageio

def split_and_rename_image(img_path, output_path, ms_siglum):
    """
    Split and rename images
    """

    verso_no = 2
    recto_no = 3

    # Load the image
    img = imageio.imread(img_path)
    height, width, _ = img.shape

    # Cut the image in half
    width_cutoff = width // 2
    side1 = img[:, :width_cutoff, :]
    side2 = img[:, width_cutoff:, :]

    # Save the two halves
    imageio.imwrite(f"{output_path}/{ms_siglum}_{verso_no}v.jpg", side1)
    imageio.imwrite(f"{output_path}/{ms_siglum}_{recto_no}r.jpg", side2)

    return(height, width)

if __name__ == '__main__':
    main()
