for host in 'thumm02' 'thumm03' 'thumm04' 'thumm05';
do
scp client.py 2021214346@$host:mydfs-main/client.py
scp common.py 2021214346@$host:mydfs-main/common.py
scp data_node.py 2021214346@$host:mydfs-main/data_node.py
scp name_node.py 2021214346@$host:mydfs-main/name_node.py
scp name_node.py 2021214346@$host:mydfs-main/wordcount.py
scp util/asset.py 2021214346@$host:mydfs-main/util/asset.py
scp util/job.py 2021214346@$host:mydfs-main/util/job.py
done
