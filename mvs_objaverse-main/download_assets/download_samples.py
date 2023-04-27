# Download specified samples

import multiprocessing
import objaverse

if __name__ == '__main__':
    processes = multiprocessing.cpu_count()

    import random

    random.seed(12)

    object_uids = ['u3WYrMucGzUOhnNukx2EfyQqevA', 'oFfjKlslHqXgtKdKqEtpffmSv6h']

    # the assets are stored in /home/USERNAME/.objaverse
    objects = objaverse.load_objects(
        uids=object_uids,
        download_processes=processes
    )
