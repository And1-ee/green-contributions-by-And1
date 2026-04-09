import os
import random
import datetime

# ========== 这里改成你的仓库路径 ==========
REPO_PATH = r"/Users/xxx/Documents/github-auto-green"
FILE_NAME = "daily_record.txt"

def make_commit():
    os.chdir(REPO_PATH)
    
    # 写入当日时间+随机数字，模拟真实修改
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rand_num = random.randint(100, 999)
    content = f"{today} - study record: {rand_num}\n"
    
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(content)

    # git 提交命令
    os.system("git add .")
    os.system(f'git commit -m "auto commit: {today}"')
    os.system("git push origin main")

if __name__ == "__main__":
    make_commit()
