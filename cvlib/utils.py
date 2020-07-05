import requests
import progressbar as pb 
import os
import pylint

def download_file(url,file_name,dest_dir):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    full_path_to_file=dest_dir+os.path.sep+file_name

    if os.path.exists(dest_dir+os.path.sep+file_name):
        return full_path_to_file
    
    print("downloading the dataset")

    try:
        r=requests.get(url,allow_redirects=True,stream=True)
    except:
        print("could not establish connection")
    
    file_size=int(r.headers['Content-Length'])
    chunk_size=1024
    num_bars=round(file_size/chunk_size)

    bar=pb.ProgressBar(maxval=num_bars).start()
    #pylint: disable=maybe-no-member
    if r.status_code != requests.codes.ok :
        print("error occured while downlading")
        return None
    
    count=0
    with open(full_path_to_file,'wb') as file:
        for chunk in r.iter_content(chunk_size=chunk_size):
            file.write(chunk)
            bar.update(chunk)
            count+=1

    return full_path_to_file

