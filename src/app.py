import os
from absl import flags, app

FLAGS = flags.FLAGS
flags.DEFINE_integer("test", 32, "test")


def main(argv):
    del argv
    print("hello")
    with open("/template/job-template.yaml") as f:
        t = f.read()
        print(t)


if __name__ == "__main__":
    app.run(main)
