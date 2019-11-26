from os.path import join
import tensorflow as tf


def transform_abs_paths(root_path, paths):
    return [join(root_path, path) for path in paths]


def get_contents(data_path):
    dirname, subdirs, files = next(tf.io.gfile.walk(data_path))
    return (
        transform_abs_paths(dirname, subdirs),
        transform_abs_paths(dirname, files),
    )
