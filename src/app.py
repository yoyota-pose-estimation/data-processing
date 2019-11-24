import os
from time import sleep
from absl import flags, app
import job


FLAGS = flags.FLAGS
flags.DEFINE_integer("test", 32, "test")


def main(argv):
    del argv
    job.create_job()


if __name__ == "__main__":
    app.run(main)
