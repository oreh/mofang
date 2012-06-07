import os
import uuid

def fsplit(f, chunk_size=65536):
    file_size = os.stat(f.name).st_size
    filename = uuid.uuid4().hex
    eof = False
    counter = 0

    while not eof:
        content = f.read(chunk_size)
        if len(content) < chunk_size:
            eof = True

        if len(content) != 0:
            tf = open('/tmp/%s-%d' % (filename, counter), 'wb')
            tf.write(content)
            tf.close()
            counter += 1

    return (filename, counter) 

def fmerge(fname, num_chunk):
    index = 0
    f = open('/tmp/test.pdf', 'wb')
    while index < num_chunk:
        chunk = open('/tmp/%s-%d' % (fname, index), 'rb')
        f.write(chunk.read())
        index += 1
    f.close()

    return ('/tmp/test.pdf')

if __name__ == "__main__":
    f = open('/home/oreh/neo4j-manual-stable.pdf', 'rb')
    filename, counter = fsplit(f)
    print 'filename: %s\nchunks: %d\n' % (filename, counter)
    mfilename = fmerge(filename, counter)
    print 'merged to %s' % mfilename

