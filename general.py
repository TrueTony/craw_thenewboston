import os


# Each website you crawl os a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project {}'.format(directory))
        os.mkdir(directory)