dfs_replication = 2
dfs_blk_size = 40960000  # * 1024

# NameNode和DataNode数据存放位置
name_node_dir = "./dfs/name"
data_node_dir = "./dfs/data"
checksum_node_dir = "./dfs/checksum"

data_node_port = 14311  # DataNode程序监听端口
name_node_port = 14312  # NameNode监听端口
heartbeat_port = 14313
# scheduler
scheduler_port = 14314
max_load = 1

# job runner
jobrunner_port = 14315
metrics_port = 14316

heartbeat_interval = 30 # second

# 集群中的主机列表
host_list =   ['thumm01', 'thumm02', 'thumm03', 'thumm04', 'thumm05']#, 'thumm03', 'thumm04', 'thumm05'] # ['localhost']
name_node_host = "thumm01"

BUF_SIZE = 40960

main_host = "thumm01"


