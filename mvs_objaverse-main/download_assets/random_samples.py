import multiprocessing
import objaverse
import random

if __name__ == '__main__':
    processes = multiprocessing.cpu_count()



    random.seed(12)

    uids = objaverse.load_uids()
    random_object_uids = random.sample(uids, 10)

    # the assets are stored in /home/USERNAME/.objaverse
    objects = objaverse.load_objects(
        uids=random_object_uids,
        download_processes=processes
    )
