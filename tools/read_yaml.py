import os
import yaml


class ReadYaml:
    def __init__(self, filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    # 外侧 run_suite使用
    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

# 右键 调试使用
def read_yaml1():
    with open("../data/login.yaml", "r", encoding="utf-8") as f:
        return yaml.load(f)

if __name__ == '__main__':
    arrs = []
    for data in read_yaml1().values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("verify_code"),
                     data.get("expect_info"),
                     data.get("expect_msg")))
    print(arrs)