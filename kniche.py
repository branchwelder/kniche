from PIL import Image


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def convert_to_bmp(pixels, width, height):
    im = Image.new("1", (width, height))
    px = im.load()
    for ind, pxrow in enumerate(pixels):
        for pixdex, pixel in enumerate(pxrow):
            if pixel == "1":
                pval = 1
            else:
                pval = 0

            px[pixdex, ind] = pval

    return im


if __name__ == "__main__":
    fname = "rule_150_2_80"
    extension = ".txt"
    width = 80

    with open(fname + extension, "r") as f:
        data = f.read()

    binlist = data.split(",")

    pixels = list(divide_chunks(binlist, width))
    im = convert_to_bmp(pixels, width, len(pixels))

    im.save(fname + ".bmp", "BMP")
