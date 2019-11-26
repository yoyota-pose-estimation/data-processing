from absl import flags, app
from pair_image import s3, job


FLAGS = flags.FLAGS
flags.DEFINE_string("data_path", None, "data path")
flags.mark_flag_as_required("data_path")


def main(argv):
    del argv
    data_path = FLAGS.data_path
    dirs, _ = s3.get_contents(data_path)
    print(dirs)
    for directory in dirs:
        job.create_clone_job(["--data_path={}".format(directory)])


app.run(main)
