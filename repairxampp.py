import os, shutil, socket

def caviar():
    dest = "C:/xampp/mysql"
    print("Backing up current data folder...")
    name=socket.gethostname()
    if os.path.exists(dest + "/dataCopy"):
        shutil.rmtree(dest + "/dataCopy")
    shutil.copytree(dest + "/data", dest + "/dataCopy", dirs_exist_ok=True)

    print("Starting repair...")
    xforce = dest + "/data"
    destinator = dest + "/backup"
    builder = ["mysql", "phpmyadmin", "performance_schema", "test", "aria_log.00000001", "aria_log_control", "ib_buffer_pool", "ib_logfile0", "ib_logfile1", "ibtmp1", f"{name}.err", f"{name}.pid", "multi-master.info", "my", "mysql.pid", "mysql_error", "mysql.dmp"]
    skip = ["ibdata1"]

    print("Repair step 1...")
    for i in builder:
        sr = os.path.join(xforce, i)
        if os.path.isdir(sr):
            shutil.rmtree(sr)
        elif os.path.isfile(sr):
            try:
                os.remove(sr)
            except FileNotFoundError:
                pass

    print("Repair step 2...")
    for i in os.listdir(destinator):
        if i not in skip:
            sr = os.path.join(xforce, i)
            ds = os.path.join(destinator, i)
            if os.path.isdir(ds):
                shutil.copytree(ds, sr, dirs_exist_ok=True)
            elif os.path.isfile(ds):
                shutil.copy2(ds, sr)