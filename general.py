import os


# Each website you crawl os a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project {}'.format(directory))
        os.mkdir(directory)


# create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# craate a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()