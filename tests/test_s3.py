from pair_image import s3

DATA_PATH = "s3://pi-camera/turtleNeck/2019-11-12/10/00"


def test_get_contents():
    subdirs, files = s3.get_contents(DATA_PATH)
    print(subdirs[:10], files[:10])
